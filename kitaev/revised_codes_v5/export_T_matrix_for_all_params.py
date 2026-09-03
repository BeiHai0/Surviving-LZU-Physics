# -*- coding: utf-8 -*-
from kitaev_data_manager import KitaevDataManager
from scipy import sparse
import numpy as np
from pfapack import pfaffian
import time
import gc


# 注意，与论文中不同的是，这里的跃迁矩阵没有把磁场算进来，所有这里的 T 矩阵乘上磁场某一分量才是论文中的 T 矩阵

def build_T_minus_a1_matrix(N1, N2):
    N = N1*N2
    single_block = np.eye(N1, k=1) # k=1 代表上对角线全 +1
    single_block[N1-1, 0] = -1
    T_minus_a1_matrix = np.kron(np.eye(N2), single_block)
    return T_minus_a1_matrix

def build_T_minus_a2_matrix(N1, N2):
    single_block = np.eye(N2, k=1)  
    single_block[N2-1, 0] = -1
    T_minus_a2_matrix = np.kron(single_block, np.eye(N1))
    return T_minus_a2_matrix

# 主函数
def main():
    manager = KitaevDataManager()
    N1, N2, bc1, bc2 = 20, 20, -1, -1
    N = N1 * N2
    n1, n2 = N1//2, N2//2
    
    T_minus_a1_matrix = build_T_minus_a1_matrix(N1, N2)
    T_minus_a2_matrix = build_T_minus_a2_matrix(N1, N2)
    T_trans_matrix_list = [None, np.eye(N), T_minus_a1_matrix, T_minus_a2_matrix]
    
    I_N = np.eye(N)
    
    for Kx, Ky, Kz in [(1,1,1), (-1,-1,-1)]:
        for kappa in [0.0, 0.02, 0.04, 0.06]:
            params_0 = {'bond':0 ,'Kx': Kx, 'Ky': Ky, 'Kz': Kz, 'kappa': kappa} # zero flux
            W_0 = manager.load_data('W_u', N1, N2, bc1, bc2, **params_0)
            V_0 = manager.load_data('V_u', N1, N2, bc1, bc2, **params_0)
            
            S_A = W_0.T.conj() + V_0.T.conj()
            S_B = 1j*(W_0.T.conj() - V_0.T.conj()) 
            for bond_1, bond_2 in [(1, 2), (2, 3), (3, 1)]: # 1, 2 代表两种 u 构型
                params_1 = {'bond':bond_1 ,'Kx': Kx, 'Ky': Ky, 'Kz': Kz, 'kappa': kappa}
                params_2 = {'bond':bond_2 ,'Kx': Kx, 'Ky': Ky, 'Kz': Kz, 'kappa': kappa}
                print(params_1)
                print(params_2)
                W_A_1 = manager.load_data('W_u', N1, N2, bc1, bc2, **params_1)
                V_A_1 = manager.load_data('V_u', N1, N2, bc1, bc2, **params_1)
                W_A_2 = manager.load_data('W_u', N1, N2, bc1, bc2, **params_2)
                V_A_2 = manager.load_data('V_u', N1, N2, bc1, bc2, **params_2)
                
                bond_3 = 6 - bond_1 - bond_2 # (123) 中初 bond_1, bond_2 剩下的那条 bond
                for T_type in ['A', 'B']:
                    total_start_time = time.time()
                    if T_type == 'A':
                        W_1 = W_A_1
                        V_1 = V_A_1
                        W_2 = W_A_2
                        V_2 = V_A_2
                        
                        if bond_3 == 1: # T_A_23, 也即 T_A_yz, (mu, nu) = (y, z), lambda = x, tau_lambda = 0, R---i, R+tau_lambda---j
                            i = n1 + n2*N1 # (n1, n2)
                            j = n1 + n2*N1 # (n1, n2)
                        elif bond_3 == 2: # T_A_31, 也即 T_A_zx, (mu, nu) = (z, x), lambda = y, tau_lambda = a1, R---i, R+tau_lambda---j
                            i = n1 + n2*N1 # (n1, n2)
                            j = n1+1 + n2*N1 # (n1+1, n2)
                        elif bond_3 == 3: # T_A_12, 也即 T_A_xy, (mu, nu) = (x, y), lambda = z, tau_lambda = a2, R---i, R+tau_lambda---j
                            i = n1 + n2*N1 # (n1, n2)
                            j = n1 + (n2+1)*N1 # (n1, n2+1)

                    elif T_type == 'B':
                        W_1 = T_trans_matrix_list[bond_1] @ W_A_1
                        V_1 = T_trans_matrix_list[bond_1] @ V_A_1
                        W_2 = T_trans_matrix_list[bond_2] @ W_A_2
                        V_2 = T_trans_matrix_list[bond_2] @ V_A_2
                        
                        if bond_3 == 1: # T_B_23, 也即 T_B_yz, (mu, nu) = (y, z), lambda = x, tau_lambda = 0, R-tau_lambda---i, R---j
                            i = n1 + n2*N1 # (n1, n2)
                            j = n1 + n2*N1 # (n1, n2)
                        elif bond_3 == 2: # T_A_31, 也即 T_A_zx, (mu, nu) = (z, x), lambda = y, tau_lambda = a1, R-tau_lambda---i, R---j
                            i = (n1-1) + n2*N1 # (n1-1, n2)
                            j = n1 + n2*N1 # (n1, n2)
                        elif bond_3 == 3: # T_A_12, 也即 T_A_xy, (mu, nu) = (x, y), lambda = z, tau_lambda = a2, R-tau_lambda---i, R---j
                            i = n1 + (n2-1)*N1 # (n1, n2-1)
                            j = n1 + n2*N1 # (n1, n2)
                    
                    # alpha(1) 与 alpha(0) 转换矩阵
                    W_tilde_1 = W_0.T.conj() @ W_1 + V_0.T.conj() @ V_1
                    V_tilde_1 = V_0.T @ W_1 + W_0.T @ V_1
                    # alpha(2) 与 alpha(0) 转换矩阵
                    W_tilde_2 = W_0.T.conj() @ W_2 + V_0.T.conj() @ V_2
                    V_tilde_2 = V_0.T @ W_2 + W_0.T @ V_2
                    
                    # 知道了转换矩阵就可得到 BCS 态系数矩阵 Z, Z = V^* (W^*)^{-1}
                    Z_tilde_1 = np.linalg.solve(W_tilde_1.T, V_tilde_1.T).T.conj()
                    Z_tilde_2 = np.linalg.solve(W_tilde_2.T, V_tilde_2.T).T.conj()
                    # 理论上 Z 是反对称的，这里检查数值上是否反对称
                    err_1 = np.linalg.norm(Z_tilde_1 + Z_tilde_1.T)
                    err_2 = np.linalg.norm(Z_tilde_2 + Z_tilde_2.T)
                    print(f'norm of Z_tilde_1 + Z_tilde_1.T:{err_1}')
                    print(f'norm of Z_tilde_2 + Z_tilde_2.T:{err_2}')
                    # 手动反对称化，减小数值误差
                    Z_tilde_1 = 0.5*(Z_tilde_1 - Z_tilde_1.T)
                    Z_tilde_2 = 0.5*(Z_tilde_2 - Z_tilde_2.T)
                    
                    M = np.block([
                        [-Z_tilde_1.conj(), I_N],
                        [-I_N, Z_tilde_2]
                        ])
                    
                    # pfaffian 计算，耗时较长
                    start_time = time.time()
                    pf_M = pfaffian.pfaffian(M)
                    end_time = time.time()
                    print(f"pfaffian 计算耗时：{end_time-start_time:.4f}")
                    
                    # BCS 态归一化系数
                    cal_N_1 = np.sqrt(np.abs(np.linalg.det(W_tilde_1)))
                    cal_N_2 = np.sqrt(np.abs(np.linalg.det(W_tilde_2)))
                    
                    # 两个 BCS 态的 overlap
                    overlap = (-1)**(N*(N-1)//2) * cal_N_1 * cal_N_2 * pf_M 
                    print(f"overlap:{overlap}")
                    
                    # 两点关联函数矩阵
                    zeros_N = np.zeros((N, N))
                    middle_matrix = -np.linalg.solve(M, np.block([
                        [zeros_N, np.eye(N)],
                        [np.eye(N), zeros_N]
                        ])) + np.block([[zeros_N, zeros_N], [zeros_N, np.eye(N)]])
                    
                    cor_c_A_c_B_T = np.hstack([S_A.T.conj(), S_A.T]) @ middle_matrix @ np.vstack([S_B, S_B.conj()])
                    cor_alpha_1_alpha_dag_2 = np.hstack([W_tilde_1.T.conj(), V_tilde_1.T.conj()]) @ middle_matrix @ np.vstack([W_tilde_2, V_tilde_2])
                    cor_alpha_1_c_A_T = np.hstack([W_tilde_1.T.conj(), V_tilde_1.T.conj()]) @ middle_matrix @ np.vstack([S_A, S_A.conj()])
                    cor_c_B_alpha_dag_2 = np.hstack([S_B.T.conj(), S_B.T]) @ middle_matrix @ np.vstack([W_tilde_2, V_tilde_2])
                    cor_alpha_1_c_B_T = np.hstack([W_tilde_1.T.conj(), V_tilde_1.T.conj()]) @ middle_matrix @ np.vstack([S_B, S_B.conj()])
                    cor_c_A_alpha_dag_2 = np.hstack([S_A.T.conj(), S_A.T]) @ middle_matrix @ np.vstack([W_tilde_2, V_tilde_2])
                    
                    T_matrix = overlap*( (1j-cor_c_A_c_B_T[i, j])*cor_alpha_1_alpha_dag_2 
                    - np.outer(cor_alpha_1_c_A_T[:,i], cor_c_B_alpha_dag_2[j,:]) + np.outer(cor_alpha_1_c_B_T[:,j], cor_c_A_alpha_dag_2[i,:]) )
                    
                    params_to_save = {'Kx': Kx, 'Ky': Ky, 'Kz': Kz, 'kappa': kappa}
                    manager.save_data(f'T_{T_type}_{bond_1}_{bond_2}', T_matrix, N1, N2, bc1, bc2, **params_to_save)
                    
                    total_end_time = time.time()
                    print(f"这组参数计算总耗时：{total_end_time-total_start_time:.4f}")
if __name__ == "__main__":
    main()

