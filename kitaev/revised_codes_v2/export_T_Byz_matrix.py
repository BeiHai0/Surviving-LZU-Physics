# -*- coding: utf-8 -*-
from kitaev_data_manager import KitaevDataManager
import numpy as np
import matplotlib.pyplot as plt
from pfapack import pfaffian
from datetime import datetime

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
    return U0_prime_11, U0_prime_12, U0_prime_21, U0_prime_22

def build_T_1_matrix(N1, N2):
    single_block = np.eye(N1, k=-1)
    single_block[0, N1-1] = -1
    T_1 = np.kron(np.eye(N2), single_block)
    return T_1

def build_T_2_matrix(N1, N2):
    single_block = np.eye(N2, k=-1)
    single_block[0, N2-1] = -1
    T_2 = np.kron(single_block, np.eye(N1))
    return T_2

manager = KitaevDataManager() # 不传参，默认 root 为 kitaev_data
N1, N2, bc1, bc2 = 10, 10, -1, -1
N = N1 * N2
params = {'Kx': 1, 'Ky': 1, 'Kz': 1, 'kappa': 0.0}

T_1 = build_T_1_matrix(N1, N2)
T_2 = build_T_2_matrix(N1, N2)

eigvals_positive_std = manager.load_data('eigvals_positive_std', N1, N2, bc1, bc2, **params)
W_std = manager.load_data('W_std', N1, N2, bc1, bc2, **params)
V_std = manager.load_data('V_std', N1, N2, bc1, bc2, **params)
U0 = np.block([[W_std, V_std.conj()], [V_std, W_std.conj()]])
U0_prime_11, U0_prime_12, U0_prime_21, U0_prime_22 = build_U0_prime_matrix(U0, N)
U0_dagger = U0.T.conj()
# 
eigvals_positive_1 = manager.load_data('eigvals_positive_vison_pair_y', N1, N2, bc1, bc2, **params)
W_1 = manager.load_data('W_vison_pair_y', N1, N2, bc1, bc2, **params)
V_1 = manager.load_data('V_vison_pair_y', N1, N2, bc1, bc2, **params)
U_1 = np.block([[W_1, V_1.conj()], [V_1, W_1.conj()]])
U_1 = np.kron(np.eye(2), T_2) @ np.kron(np.eye(2), T_1.T) @ U_1

eigvals_positive_2 = manager.load_data('eigvals_positive_vison_pair_z', N1, N2, bc1, bc2, **params)
W_2 = manager.load_data('W_vison_pair_z', N1, N2, bc1, bc2, **params)
V_2 = manager.load_data('V_vison_pair_z', N1, N2, bc1, bc2, **params)
U_2 = np.block([[W_2, V_2.conj()], [V_2, W_2.conj()]])

U_tilde_1 = U0_dagger @ U_1
U_tilde_2 = U0_dagger @ U_2

W_tilde_1 = U_tilde_1[:N, :N]
W_tilde_2 = U_tilde_2[:N, :N]

V_tilde_1 = U_tilde_1[N:, :N]
V_tilde_2 = U_tilde_2[N:, :N]

F_tilde_1 = V_tilde_1.conj() @ np.linalg.inv(W_tilde_1.conj())
F_tilde_2 = V_tilde_2.conj() @ np.linalg.inv(W_tilde_2.conj())

N_1_tilde = np.sqrt(np.abs(np.linalg.det(W_tilde_1)))
N_2_tilde = np.sqrt(np.abs(np.linalg.det(W_tilde_2)))

M = np.block([
                [F_tilde_2, -np.eye(N)],
                [np.eye(N), -F_tilde_1.conj()]
            ])

overlap = N_1_tilde * N_2_tilde * (-1)**(N*(N+1)/2) * pfaffian.pfaffian(M)
print(overlap)

n1 = N1 // 2
n2 = N2 // 2
# 
i = N1 * ((n2+1) % N2) + n1
j = N1 * ((n2+1) % N2) + n1

middle_matrix = -np.linalg.inv(M) + np.block([ [np.zeros((N, N)), np.eye(N)], [np.zeros((N, N)), np.zeros((N, N))] ])
left_WV = np.hstack([V_tilde_1.T.conj(), W_tilde_1.T.conj()])
right_WV = np.vstack([W_tilde_2, V_tilde_2])
cor_alpha_1_alpha_2_dag = left_WV @ middle_matrix @ right_WV
cor_alpha_1_c_i_A = left_WV @ middle_matrix @ np.vstack([U0_prime_11[i, :].conj().reshape(-1, 1) ,U0_prime_12[i, :].conj().reshape(-1, 1)])
cor_alpha_1_c_j_B = left_WV @ middle_matrix @ np.vstack([U0_prime_21[j, :].conj().reshape(-1, 1) ,U0_prime_22[j, :].conj().reshape(-1, 1)])
cor_c_i_A_alpha_2_dag = np.hstack([U0_prime_12[i,:].reshape(1,-1), U0_prime_11[i,:].reshape(1,-1) ]) @ middle_matrix @ right_WV
cor_c_j_B_alpha_2_dag = np.hstack([U0_prime_22[j,:].reshape(1,-1), U0_prime_21[j,:].reshape(1,-1) ]) @ middle_matrix @ right_WV
cor_c_i_A_c_j_B = np.hstack([U0_prime_12[i,:].reshape(1,-1), U0_prime_11[i,:].reshape(1,-1) ]) @ middle_matrix @ np.vstack(
                [U0_prime_21[j, :].conj().reshape(-1, 1) ,U0_prime_22[j, :].conj().reshape(-1, 1)]
            ) # 还是个1\times 1二维数组
cor_alpha_1_c_i_A_c_j_B_alpha_2_dag = cor_alpha_1_c_i_A @ cor_c_j_B_alpha_2_dag - cor_alpha_1_c_j_B @ cor_c_i_A_alpha_2_dag + \
            cor_alpha_1_alpha_2_dag * cor_c_i_A_c_j_B[0, 0]
# 
T_Byz = overlap * (1j * cor_alpha_1_alpha_2_dag - cor_alpha_1_c_i_A_c_j_B_alpha_2_dag)

manager.save_data('T_Byz', T_Byz, N1, N2, bc1, bc2, **params)
print('done!')
