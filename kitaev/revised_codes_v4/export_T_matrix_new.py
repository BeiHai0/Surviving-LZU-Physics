# -*- coding: utf-8 -*-

from kitaev_data_manager import KitaevDataManager
import numpy as np
import cupy as cp
import time
from pfapack import pfaffian
from scipy.linalg import solve
from scipy.linalg import pinv


def gpu_clear():
    cp.get_default_memory_pool().free_all_blocks()
    cp.get_default_pinned_memory_pool().free_all_blocks()


def build_U0_prime_matrix(U0, N):
    U0 = cp.asarray(U0)
    I_N = cp.eye(N, dtype=complex)

    U0_prime = cp.vstack([
        cp.hstack([I_N, I_N]),
        cp.hstack([-1j*I_N, 1j*I_N])
    ]) @ U0

    U0_prime_11 = U0_prime[:N, :N]
    U0_prime_12 = U0_prime[:N, N:]
    U0_prime_21 = U0_prime[N:, :N]
    U0_prime_22 = U0_prime[N:, N:]

    del U0_prime
    gpu_clear()

    return U0_prime_11, U0_prime_12, U0_prime_21, U0_prime_22


def build_T_1_matrix(N1, N2):

    single_block = cp.eye(N1, k=-1)
    single_block[0, N1-1] = -1

    T_1 = cp.kron(cp.eye(N2), single_block)

    return T_1


def build_T_2_matrix(N1, N2):

    single_block = cp.eye(N2, k=-1)
    single_block[0, N2-1] = -1

    T_2 = cp.kron(single_block, cp.eye(N1))

    return T_2


def build_T_matrix(U0, U0_prime_11, U0_prime_12, U0_prime_21, U0_prime_22,
                   U_1, U_2, i, j, N1, N2, bc1, bc2, Kx, Ky, Kz, kappa):

    start_time = time.time()

    N = N1 * N2

    U0 = cp.asarray(U0)
    U_1 = cp.asarray(U_1)
    U_2 = cp.asarray(U_2)

    U0_dagger = U0.T.conj()

    U_tilde_1 = U0_dagger @ U_1
    U_tilde_2 = U0_dagger @ U_2

    del U0_dagger
    gpu_clear()

    W_tilde_1 = U_tilde_1[:N, :N]
    W_tilde_2 = U_tilde_2[:N, :N]

    V_tilde_1 = U_tilde_1[N:, :N]
    V_tilde_2 = U_tilde_2[N:, :N]

    del U_tilde_1
    del U_tilde_2
    gpu_clear()

    F_tilde_1 = V_tilde_1.conj() @ cp.linalg.inv(W_tilde_1.conj())

    pf_check_1 = cp.max(cp.abs(F_tilde_1 + F_tilde_1.T)).get()

    F_tilde_1 = (F_tilde_1 - F_tilde_1.T) / 2

    print(f"pf_check_1:{pf_check_1}")

    F_tilde_2 = V_tilde_2.conj() @ cp.linalg.inv(W_tilde_2.conj())

    pf_check_2 = cp.max(cp.abs(F_tilde_2 + F_tilde_2.T)).get()

    F_tilde_2 = (F_tilde_2 - F_tilde_2.T) / 2

    print(f"pf_check_2:{pf_check_2}")

    N_1_tilde = cp.sqrt(cp.abs(cp.linalg.det(W_tilde_1)))
    N_2_tilde = cp.sqrt(cp.abs(cp.linalg.det(W_tilde_2)))

    M = cp.vstack([
        cp.hstack([F_tilde_2, -cp.eye(N)]),
        cp.hstack([cp.eye(N), -F_tilde_1.conj()])
    ])

    overlap = N_1_tilde * N_2_tilde * (-1)**(N*(N+1)/2) * pfaffian.pfaffian(cp.asnumpy(M))

    print(f"overlap:{overlap}")

    middle_matrix = -cp.linalg.inv(M) + cp.vstack([
        cp.hstack([cp.zeros((N, N)), cp.eye(N)]),
        cp.hstack([cp.zeros((N, N)), cp.zeros((N, N))])
    ])

    del M
    gpu_clear()

    left_WV = cp.hstack([V_tilde_1.T.conj(), W_tilde_1.T.conj()])
    right_WV = cp.vstack([W_tilde_2, V_tilde_2])

    del V_tilde_1
    del V_tilde_2
    del W_tilde_1
    del W_tilde_2
    gpu_clear()

    cor_alpha_1_alpha_2_dag = left_WV @ middle_matrix @ right_WV

    cor_alpha_1_c_i_A = left_WV @ middle_matrix @ cp.vstack([
        U0_prime_11[i, :].conj().reshape(-1, 1),
        U0_prime_12[i, :].conj().reshape(-1, 1)
    ])

    cor_alpha_1_c_j_B = left_WV @ middle_matrix @ cp.vstack([
        U0_prime_21[j, :].conj().reshape(-1, 1),
        U0_prime_22[j, :].conj().reshape(-1, 1)
    ])

    cor_c_i_A_alpha_2_dag = cp.hstack([
        U0_prime_12[i,:].reshape(1,-1),
        U0_prime_11[i,:].reshape(1,-1)
    ]) @ middle_matrix @ right_WV

    cor_c_j_B_alpha_2_dag = cp.hstack([
        U0_prime_22[j,:].reshape(1,-1),
        U0_prime_21[j,:].reshape(1,-1)
    ]) @ middle_matrix @ right_WV

    cor_c_i_A_c_j_B = cp.hstack([
        U0_prime_12[i,:].reshape(1,-1),
        U0_prime_11[i,:].reshape(1,-1)
    ]) @ middle_matrix @ cp.vstack([
        U0_prime_21[j, :].conj().reshape(-1, 1),
        U0_prime_22[j, :].conj().reshape(-1, 1)
    ])

    cor_alpha_1_c_i_A_c_j_B_alpha_2_dag = (
        cor_alpha_1_c_i_A @ cor_c_j_B_alpha_2_dag
        - cor_alpha_1_c_j_B @ cor_c_i_A_alpha_2_dag
        + cor_alpha_1_alpha_2_dag * cor_c_i_A_c_j_B[0, 0]
    )

    T = overlap * (1j * cor_alpha_1_alpha_2_dag - cor_alpha_1_c_i_A_c_j_B_alpha_2_dag)

    del middle_matrix
    del left_WV
    del right_WV
    gpu_clear()

    end_time = time.time()

    print(f"T_matrix计算耗时: {end_time - start_time:.6f} 秒")

    return cp.asnumpy(T), pf_check_1, pf_check_2


manager = KitaevDataManager()

N1, N2, bc1, bc2 = 50, 50, -1, -1

N = N1 * N2

n1, n2 = N1//2, N2//2

pf_check_list = []


for Kx, Ky, Kz in [(-1, -1, -1)]:

    for kappa in np.linspace(0, 0.5, 6):

        U_A_list = [None,]
        U_B_list = [None,]

        params = {'Kx':Kx, 'Ky':Ky, 'Kz':Kz, 'kappa':kappa}

        W_u_0 = cp.asarray(manager.load_data('W_u_0', N1, N2, bc1, bc2, **params))
        V_u_0 = cp.asarray(manager.load_data('V_u_0', N1, N2, bc1, bc2, **params))

        U0 = cp.vstack([
            cp.hstack([W_u_0, V_u_0.conj()]),
            cp.hstack([V_u_0, W_u_0.conj()])
        ])

        del W_u_0
        del V_u_0
        gpu_clear()

        U0_prime_11, U0_prime_12, U0_prime_21, U0_prime_22 = build_U0_prime_matrix(U0, N)

        for i in [1, 2, 3]:

            W_A = cp.asarray(manager.load_data(f'W_u_{i}', N1, N2, bc1, bc2, **params))
            V_A = cp.asarray(manager.load_data(f'V_u_{i}', N1, N2, bc1, bc2, **params))

            U_A = cp.vstack([
                cp.hstack([W_A, V_A.conj()]),
                cp.hstack([V_A, W_A.conj()])
            ])

            del W_A
            del V_A
            gpu_clear()

            U_A_list.append(U_A)

        T_1 = build_T_1_matrix(N1, N2)
        T_2 = build_T_2_matrix(N1, N2)

        U_B_1 = cp.kron(cp.eye(2), T_2) @ U_A_list[1]
        U_B_list.append(U_B_1)

        U_B_2 = cp.kron(cp.eye(2), T_2) @ cp.kron(cp.eye(2), T_1.T) @ U_A_list[2]
        U_B_list.append(U_B_2)

        U_B_3 = U_A_list[3]
        U_B_list.append(U_B_3)

        i = N1 * n2 + n1
        j = N1 * ((n2+1) % N2) + n1

        T_A_xy, pf_check_1, pf_check_2 = build_T_matrix(
            U0, U0_prime_11, U0_prime_12, U0_prime_21, U0_prime_22,
            U_A_list[1], U_A_list[2],
            i, j, N1, N2, bc1, bc2, Kx, Ky, Kz, kappa
        )

        manager.save_data('T_A_xy', T_A_xy, N1, N2, bc1, bc2, **params)

        pf_check_list.extend([pf_check_1, pf_check_2])

        gpu_clear()


print("all done")

print(f"final pf check:{max(pf_check_list)}")