# -*- coding: utf-8 -*-

from kitaev_data_manager import KitaevDataManager
import numpy as np
import time
from pfapack import pfaffian
from scipy.linalg import solve
from scipy.linalg import pinv
import gc

def build_U0_prime_matrix(U0, N):
    I_N = np.eye(N, dtype=complex)
    U0_prime = np.block([
        [I_N, I_N],
        [-1j*I_N, 1j*I_N]
    ]) @ U0
    U0_prime_11 = U0_prime[:N, :N]
    U0_prime_12 = U0_prime[:N, N:]
    U0_prime_21 = U0_prime[N:, :N]
    U0_prime_22 = U0_prime[N:, N:]
    del U0_prime
    gc.collect()
    return U0_prime_11, U0_prime_12, U0_prime_21, U0_prime_22

def build_T_1_matrix(N1, N2):
    single_block = np.eye(N1, k=-1)
    single_block[0, N1-1] = -1
    T_1 = np.kron(np.eye(N2), single_block)
    del single_block
    gc.collect()
    return T_1

def build_T_2_matrix(N1, N2):
    single_block = np.eye(N2, k=-1)
    single_block[0, N2-1] = -1
    T_2 = np.kron(single_block, np.eye(N1))
    del single_block
    gc.collect()
    return T_2

def build_T_matrix(U0, U0_prime_11, U0_prime_12, U0_prime_21, U0_prime_22, 
                   U_1, U_2, i, j, N1, N2, bc1, bc2, Kx, Ky, Kz, kappa):
    start_time = time.time()
    N = N1 * N2
    
    # dagger
    U0_dagger = U0.T.conj()
    
    # U_tilde
    U_tilde_1 = U0_dagger @ U_1
    U_tilde_2 = U0_dagger @ U_2

    W_tilde_1 = U_tilde_1[:N, :N]
    W_tilde_2 = U_tilde_2[:N, :N]
    V_tilde_1 = U_tilde_1[N:, :N]
    V_tilde_2 = U_tilde_2[N:, :N]

    # F_tilde
    F_tilde_1 = V_tilde_1.conj() @ np.linalg.inv(W_tilde_1.conj())
    pf_check_1 = np.max(np.abs(F_tilde_1 + F_tilde_1.T))
    F_tilde_1 = (F_tilde_1 - F_tilde_1.T) / 2

    F_tilde_2 = V_tilde_2.conj() @ np.linalg.inv(W_tilde_2.conj())
    pf_check_2 = np.max(np.abs(F_tilde_2 + F_tilde_2.T))
    F_tilde_2 = (F_tilde_2 - F_tilde_2.T) / 2

    # normalization
    N_1_tilde = np.sqrt(np.abs(np.linalg.det(W_tilde_1)))
    N_2_tilde = np.sqrt(np.abs(np.linalg.det(W_tilde_2)))

    # M matrix
    M = np.block([
        [F_tilde_2, -np.eye(N)],
        [np.eye(N), -F_tilde_1.conj()]
    ])

    # overlap
    overlap = N_1_tilde * N_2_tilde * (-1)**(N*(N+1)/2) * pfaffian.pfaffian(M)

    # middle_matrix
    middle_matrix = -np.linalg.inv(M) + np.block([
        [np.zeros((N,N)), np.eye(N)],
        [np.zeros((N,N)), np.zeros((N,N))]
    ])

    # correlations
    left_WV = np.hstack([V_tilde_1.T.conj(), W_tilde_1.T.conj()])
    right_WV = np.vstack([W_tilde_2, V_tilde_2])

    cor_alpha_1_alpha_2_dag = left_WV @ middle_matrix @ right_WV

    cor_alpha_1_c_i_A = left_WV @ middle_matrix @ np.vstack([U0_prime_11[i, :].conj().reshape(-1,1),
                                                             U0_prime_12[i, :].conj().reshape(-1,1)])
    cor_alpha_1_c_j_B = left_WV @ middle_matrix @ np.vstack([U0_prime_21[j, :].conj().reshape(-1,1),
                                                             U0_prime_22[j, :].conj().reshape(-1,1)])
    cor_c_i_A_alpha_2_dag = np.hstack([U0_prime_12[i,:].reshape(1,-1), U0_prime_11[i,:].reshape(1,-1)]) @ middle_matrix @ right_WV
    cor_c_j_B_alpha_2_dag = np.hstack([U0_prime_22[j,:].reshape(1,-1), U0_prime_21[j,:].reshape(1,-1)]) @ middle_matrix @ right_WV
    cor_c_i_A_c_j_B = np.hstack([U0_prime_12[i,:].reshape(1,-1), U0_prime_11[i,:].reshape(1,-1)]) @ middle_matrix @ np.vstack([
        U0_prime_21[j, :].conj().reshape(-1,1),
        U0_prime_22[j, :].conj().reshape(-1,1)
    ])
    cor_alpha_1_c_i_A_c_j_B_alpha_2_dag = cor_alpha_1_c_i_A @ cor_c_j_B_alpha_2_dag - cor_alpha_1_c_j_B @ cor_c_i_A_alpha_2_dag + \
        cor_alpha_1_alpha_2_dag * cor_c_i_A_c_j_B[0,0]

    # final T
    T = overlap * (1j * cor_alpha_1_alpha_2_dag - cor_alpha_1_c_i_A_c_j_B_alpha_2_dag)

    end_time = time.time()
    print(f"T_matrix计算耗时: {end_time-start_time:.6f} 秒")

    # 释放大矩阵
    del U0_dagger, U_tilde_1, U_tilde_2, W_tilde_1, W_tilde_2, V_tilde_1, V_tilde_2
    del F_tilde_1, F_tilde_2, N_1_tilde, N_2_tilde, M, middle_matrix
    del left_WV, right_WV
    del cor_alpha_1_alpha_2_dag, cor_alpha_1_c_i_A, cor_alpha_1_c_j_B
    del cor_c_i_A_alpha_2_dag, cor_c_j_B_alpha_2_dag, cor_c_i_A_c_j_B, cor_alpha_1_c_i_A_c_j_B_alpha_2_dag
    gc.collect()

    return T, pf_check_1, pf_check_2

# ------------------------ 主程序 ------------------------
manager = KitaevDataManager()
N1, N2, bc1, bc2 = 20, 20, -1, -1
N = N1 * N2
n1, n2 = N1//2, N2//2
pf_check_list = []

for Kx, Ky, Kz in [(1,1,1), (-1,-1,-1)]:
    for kappa in np.linspace(0, 0.5, 6):
        params = {'Kx':Kx, 'Ky':Ky, 'Kz':Kz, 'kappa':kappa}

        # 加载初始U0
        W_u_0 = manager.load_data('W_u_0', N1, N2, bc1, bc2, **params)
        V_u_0 = manager.load_data('V_u_0', N1, N2, bc1, bc2, **params)
        U0 = np.block([[W_u_0, V_u_0.conj()], [V_u_0, W_u_0.conj()]])
        del W_u_0, V_u_0
        gc.collect()

        U0_prime_11, U0_prime_12, U0_prime_21, U0_prime_22 = build_U0_prime_matrix(U0, N)

        # 构造U_A
        U_A_list = [None]
        for i in [1,2,3]:
            W_A = manager.load_data(f'W_u_{i}', N1, N2, bc1, bc2, **params)
            V_A = manager.load_data(f'V_u_{i}', N1, N2, bc1, bc2, **params)
            U_A = np.block([[W_A, V_A.conj()], [V_A, W_A.conj()]])
            U_A_list.append(U_A)
            del W_A, V_A
            gc.collect()

        # 构造T_1, T_2
        T_1 = build_T_1_matrix(N1, N2)
        T_2 = build_T_2_matrix(N1, N2)

        # 构造U_B
        U_B_list = [None]
        U_B_list.append(np.kron(np.eye(2), T_2) @ U_A_list[1])
        U_B_list.append(np.kron(np.eye(2), T_2) @ np.kron(np.eye(2), T_1.T) @ U_A_list[2])
        U_B_list.append(U_A_list[3])
        gc.collect()

        # 计算T矩阵
        T_pairs = [
            (('A',1,2),'T_A_xy'), (('A',2,3),'T_A_yz'), (('A',3,1),'T_A_zx'),
            (('B',1,2),'T_B_xy'), (('B',2,3),'T_B_yz'), (('B',3,1),'T_B_zx')
        ]
        for (label,u1_idx,u2_idx), name in T_pairs:
            if 'xy' in name:
                j = N1*((n2+1)%N2)+n1
            elif 'yz' in name:
                j = N1*n2+n1 if label=='A' else N1*((n2+1)%N2)+n1
            else: # zx
                j = N1*n2+n1 if label=='A' else N1*((n2+1)%N2)+(n1-1+N1)%N1
            i = N1*n2+n1

            U1 = U_A_list[u1_idx] if label=='A' else U_B_list[u1_idx]
            U2 = U_A_list[u2_idx] if label=='A' else U_B_list[u2_idx]

            T_matrix, pf1, pf2 = build_T_matrix(
                U0, U0_prime_11, U0_prime_12, U0_prime_21, U0_prime_22,
                U1, U2, i, j, N1, N2, bc1, bc2, Kx, Ky, Kz, kappa
            )

            manager.save_data(name, T_matrix, N1, N2, bc1, bc2, **params)
            pf_check_list.extend([pf1, pf2])

            del T_matrix, U1, U2
            gc.collect()

        # 循环结束，释放U0和U_A/U_B
        del U0, U0_prime_11, U0_prime_12, U0_prime_21, U0_prime_22
        del U_A_list, U_B_list, T_1, T_2
        gc.collect()

print("all done")
print(f"final pf check:{max(pf_check_list)}")