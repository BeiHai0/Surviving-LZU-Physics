# -*- coding: utf-8 -*-
from kitaev_data_manager import KitaevDataManager
import numpy as np
import time
from pfapack import pfaffian
from scipy.linalg import solve
from scipy.linalg import pinv

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

def build_T_matrix(U0, U0_prime_11, U0_prime_12, U0_prime_21, U0_prime_22, U_1, U_2, i, j, N1, N2, bc1, bc2, Kx, Ky, Kz, kappa):
    start_time = time.time()
    N = N1 * N2
    
    #U_1 = np.block([[W_1, V_1.conj()], [V_1, W_1.conj()]])
    #U_2 = np.block([[W_2, V_2.conj()], [V_2, W_2.conj()]])
    
    U0_dagger = U0.T.conj()
    # print(U0_dagger)
    U_tilde_1 = U0_dagger @ U_1
    U_tilde_2 = U0_dagger @ U_2

    W_tilde_1 = U_tilde_1[:N, :N]
    #print(W_tilde_1)
    W_tilde_2 = U_tilde_2[:N, :N]

    V_tilde_1 = U_tilde_1[N:, :N]
    V_tilde_2 = U_tilde_2[N:, :N]

        
    F_tilde_1 = V_tilde_1.conj() @ np.linalg.inv(W_tilde_1.conj())
    # print(F_tilde_1 + F_tilde_1.T)
    print(np.max(np.abs(F_tilde_1 + F_tilde_1.T)))
    F_tilde_2 = V_tilde_2.conj() @ np.linalg.inv(W_tilde_2.conj())
    print(np.max(np.abs(F_tilde_2 + F_tilde_2.T)))
    #print(F_tilde_2 + F_tilde_2.T)

    N_1_tilde = np.sqrt(np.abs(np.linalg.det(W_tilde_1)))
    print(f"N_1_tilde:{N_1_tilde}")
    N_2_tilde = np.sqrt(np.abs(np.linalg.det(W_tilde_2)))
    

    M = np.block([
                    [F_tilde_2, -np.eye(N)],
                    [np.eye(N), -F_tilde_1.conj()]
                ])
    # M = (M - M.T) / 2 # 有一些误差会让 pf M 无法计算
    
    #print(f"当前参数: {params}")
    overlap = N_1_tilde * N_2_tilde * (-1)**(N*(N+1)/2) * pfaffian.pfaffian(M)
    print(overlap)
    
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
    T = overlap * (1j * cor_alpha_1_alpha_2_dag - cor_alpha_1_c_i_A_c_j_B_alpha_2_dag)
    end_time = time.time() 
    print(f"T_matrix计算耗时: {end_time - start_time:.6f} 秒")
    return T
    
manager = KitaevDataManager() # 不传参，默认 root 为 kitaev_data
N1, N2, bc1, bc2 = 30, 30, -1, -1
N = N1 * N2
n1, n2 = N1//2, N2//2

for Kx, Ky, Kz in [(1, 1, 1), (-1, -1, -1)]:
    for kappa in np.linspace(0, 0.5, 6):
        U_A_list = [None,]
        U_B_list = [None,]
        params = {'Kx':Kx, 'Ky':Ky, 'Kz':Kz, 'kappa':kappa}
        
        W_u_0 = manager.load_data('W_u_0', N1, N2, bc1, bc2, **params)
        V_u_0 = manager.load_data('V_u_0', N1, N2, bc1, bc2, **params)
        U0 = np.block([[W_u_0, V_u_0.conj()], [V_u_0, W_u_0.conj()]])
        U0_prime_11, U0_prime_12, U0_prime_21, U0_prime_22 = build_U0_prime_matrix(U0, N)
        
        for i in [1, 2, 3]:
            W_A = manager.load_data(f'W_u_{i}', N1, N2, bc1, bc2, **params)
            V_A = manager.load_data(f'V_u_{i}', N1, N2, bc1, bc2, **params)
            U_A = np.block([[W_A, V_A.conj()], [V_A, W_A.conj()]])
            #print(U_A @ U_A.conj().T)
            U_A_list.append(U_A)
            
        # 利用平移对称性构造下三角的本征向量
        T_1 = build_T_1_matrix(N1, N2)
        T_2 = build_T_2_matrix(N1, N2)
        
        U_B_1 = np.kron(np.eye(2), T_2) @ U_A_list[1]
        U_B_list.append(U_B_1)
        
        U_B_2 = np.kron(np.eye(2), T_2) @ np.kron(np.eye(2), T_1.T) @ U_A_list[2]
        U_B_list.append(U_B_2)
        
        U_B_3 = U_A_list[3]
        U_B_list.append(U_B_3)
        
        # T_A_xy
        i = N1 * n2 + n1
        j = N1 * ((n2+1) % N2) + n1
        T_A_xy = build_T_matrix(U0, U0_prime_11, U0_prime_12, U0_prime_21, U0_prime_22, U_A_list[1], U_A_list[2], i, j, N1, N2, bc1, bc2, Kx, Ky, Kz, kappa)
        manager.save_data('T_A_xy', T_A_xy, N1, N2, bc1, bc2, **params) 
        # T_A_yz
        i = N1 * n2 + n1
        j = N1 * n2 + n1
        T_A_yz = build_T_matrix(U0, U0_prime_11, U0_prime_12, U0_prime_21, U0_prime_22, U_A_list[2], U_A_list[3], i, j, N1, N2, bc1, bc2, Kx, Ky, Kz, kappa)
        manager.save_data('T_A_yz', T_A_yz, N1, N2, bc1, bc2, **params)       
        # T_A_zx
        i = N1 * n2 + n1
        j = N1 * n2 + (n1 + 1) % N1
        T_A_zx = build_T_matrix(U0, U0_prime_11, U0_prime_12, U0_prime_21, U0_prime_22, U_A_list[3], U_A_list[1], i, j, N1, N2, bc1, bc2, Kx, Ky, Kz, kappa)
        manager.save_data('T_A_zx', T_A_zx, N1, N2, bc1, bc2, **params)         
        # T_B_xy
        i = N1 * n2 + n1
        j = N1 * ((n2+1) % N2) + n1
        T_B_xy = build_T_matrix(U0, U0_prime_11, U0_prime_12, U0_prime_21, U0_prime_22, U_B_list[1], U_B_list[2], i, j, N1, N2, bc1, bc2, Kx, Ky, Kz, kappa)
        manager.save_data('T_B_xy', T_B_xy, N1, N2, bc1, bc2, **params) 
        # T_B_yz
        i = N1 * ((n2+1) % N2) + n1
        j = N1 * ((n2+1) % N2) + n1
        T_B_yz = build_T_matrix(U0, U0_prime_11, U0_prime_12, U0_prime_21, U0_prime_22, U_B_list[2], U_B_list[3], i, j, N1, N2, bc1, bc2, Kx, Ky, Kz, kappa)
        manager.save_data('T_B_yz', T_B_yz, N1, N2, bc1, bc2, **params) 
        # T_B_zx
        i = N1 * ((n2+1) % N2) + (n1-1+N1) % N1
        j = N1 * ((n2+1) % N2) + n1
        T_B_zx = build_T_matrix(U0, U0_prime_11, U0_prime_12, U0_prime_21, U0_prime_22, U_B_list[3], U_B_list[1], i, j, N1, N2, bc1, bc2, Kx, Ky, Kz, kappa)
        manager.save_data('T_B_zx', T_B_zx, N1, N2, bc1, bc2, **params) 
        

print("all done")

