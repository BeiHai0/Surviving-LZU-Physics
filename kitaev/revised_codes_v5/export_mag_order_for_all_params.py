# -*- coding: utf-8 -*-
from kitaev_data_manager import KitaevDataManager
import numpy as np
import time
from pfapack import pfaffian

# 主函数

def main():
    
    manager = KitaevDataManager()
    N1, N2, bc1, bc2 = 20, 20, -1, -1
    N = N1 * N2
    n1, n2 = N1//2, N2//2
    
    a1 = np.array([1.0, 0.0])
    a2 = np.array([0.5, np.sqrt(3)/2])
    
    Gamma = np.array([0.0, 0.0])
    K = np.array([4*np.pi/3, 0.0])
    
    tau_x, tau_y, tau_z = np.array([0.0, 0.0]), a1, a2
    tau_list = [None, tau_x, tau_y, tau_z]
    
    K_list = [(1, 1, 1), (-1, -1 , -1)]
    kappa_list = [0.0, 0.02, 0.04, 0.06]
    
    zeros_N = np.zeros((N, N), dtype=complex)
    I_N = np.eye(N, dtype=complex)
    
    for Kx, Ky, Kz in K_list:
        
        for kappa in kappa_list:
            
            start_time = time.time()
            
            sigma_A_d_dag_GS_exp_list = [np.array([0]), ] # 0 数组用来占位，没实际意义
            sigma_B_d_dag_GS_exp_list = [np.array([0]), ]
            sigma_A_beta_k_1_dag_GS_exp_list = [0, ] # 数字 0 用来占位，没实际意义
            sigma_B_beta_k_1_dag_GS_exp_list = [0, ]
            
            params_0 = {'bond': 0, 'Kx': Kx, 'Ky': Ky, 'Kz': Kz, 'kappa': kappa}
            W_0 = manager.load_data('W_u', N1, N2, bc1, bc2, **params_0)
            V_0 = manager.load_data('V_u', N1, N2, bc1, bc2, **params_0)
            
            S_A = W_0.T.conj() + V_0.T.conj()
            S_B = 1j*(W_0.T.conj() - V_0.T.conj()) 
            
            params_1 = {'Kx': Kx, 'Ky': Ky, 'Kz': Kz, 'kappa': kappa}
            phi = manager.load_data("critical_eigvec", N1, N2, bc1, bc2, **params_1)
            phi_x = phi[0:N]
            phi_y = phi[N:2*N]
            phi_z = phi[2*N:3*N]
            phi_list = [None, phi_x, phi_y, phi_z]
            
            for bond in [1, 2, 3]:
                
                params_2 = {'bond': bond, 'Kx': Kx, 'Ky': Ky, 'Kz': Kz, 'kappa': kappa}
                print(params_2)
                W_2 = manager.load_data('W_u', N1, N2, bc1, bc2, **params_2)
                V_2 = manager.load_data('V_u', N1, N2, bc1, bc2, **params_2)
                
                W_tilde_2 = W_0.T.conj() @ W_2 + V_0.T.conj() @ V_2
                V_tilde_2 = V_0.T @ W_2 + W_0.T @ V_2
                Z_tilde_2 = np.linalg.solve(W_tilde_2.T, V_tilde_2.T).T.conj()
                Z_tilde_2 = 0.5*(Z_tilde_2-Z_tilde_2.T)
                
                sign, logdet = np.linalg.slogdet(W_tilde_2)
                N_tilde_2 = np.exp(0.5 * logdet)
                
                M = np.block([
                    [zeros_N, I_N],
                    [-I_N, Z_tilde_2]
                    ])
                
                overlap = (-1)**(N*(N-1)/2) * N_tilde_2 * pfaffian.pfaffian(M)
                
                M_inv = np.block([
                    [Z_tilde_2, -I_N],
                    [I_N, zeros_N]
                    ])
                
                middle_matrix = - M_inv @ np.block([
                    [zeros_N, I_N],
                    [I_N, zeros_N]
                    ]) + np.block([
                        [zeros_N, zeros_N],
                        [zeros_N, I_N]
                        ])
                
                # 两点关联函数矩阵
                        
                cor_c_A_alpha_dag_2 = np.hstack([S_A.T.conj(), S_A.T]) @ middle_matrix @ np.vstack([W_tilde_2, V_tilde_2])
                cor_c_B_alpha_dag_2 = np.hstack([S_B.T.conj(), S_B.T]) @ middle_matrix @ np.vstack([W_tilde_2, V_tilde_2])
                
                if Kx == 1:
                    k = Gamma
                elif Kx == -1:
                    k = K
                
                R = n1 * a1 + n2 * a2
                
                # A 子格 R 矢量 -- i 
                
                i = n1 + N1 * n2
                
                cor_c_i_A_alpha_dag_2 = cor_c_A_alpha_dag_2[i, :]
                sigma_A_d_dag_GS_exp = -1j * overlap * cor_c_i_A_alpha_dag_2 
                manager.save_data('sigma_A_d_dag_GS_exp', sigma_A_d_dag_GS_exp, N1, N2, bc1, bc2, **params_2)
                sigma_A_d_dag_GS_exp_list.append(sigma_A_d_dag_GS_exp)
                                
                sigma_A_beta_k_1_dag_GS_exp = 1.0 / np.sqrt(N) * np.exp(1j * np.dot(k, R)) * sigma_A_d_dag_GS_exp @ phi_list[bond] 
                sigma_A_beta_k_1_dag_GS_exp_list.append(sigma_A_beta_k_1_dag_GS_exp)
                manager.save_data('sigma_A_beta_k_1_dag_GS_exp', sigma_A_beta_k_1_dag_GS_exp, N1, N2, bc1, bc2, **params_2)
                
                # B 子格 R+tau_mu矢量 -- j
                
                if bond == 1:
                    j = i
                elif bond == 2:
                    j = i + 1
                elif bond == 3:
                    j = i + N1
                
                cor_c_j_B_alpha_dag_2 = cor_c_B_alpha_dag_2[j, :]
                sigma_B_d_dag_GS_exp = - overlap * cor_c_j_B_alpha_dag_2
                #print(sigma_B_d_dag_GS_exp.shape)
                manager.save_data('sigma_B_d_dag_GS_exp', sigma_B_d_dag_GS_exp, N1, N2, bc1, bc2, **params_2)
                sigma_B_d_dag_GS_exp_list.append(sigma_B_d_dag_GS_exp)
                
                sigma_B_beta_k_1_dag_GS_exp = 1.0 / np.sqrt(N) * np.exp(1j * np.dot(k, R)) * sigma_B_d_dag_GS_exp @ phi_list[bond] 
                sigma_B_beta_k_1_dag_GS_exp_list.append(sigma_B_beta_k_1_dag_GS_exp)
                manager.save_data('sigma_B_beta_k_1_dag_GS_exp', sigma_B_beta_k_1_dag_GS_exp, N1, N2, bc1, bc2, **params_2)
            
            print(f"sigma_A_beta_k_1_dag_GS_exp_list:{sigma_A_beta_k_1_dag_GS_exp_list}")
            print(f"sigma_B_beta_k_1_dag_GS_exp_list:{sigma_B_beta_k_1_dag_GS_exp_list}")
            
            end_time = time.time()
            print(params_1)
            print(f"计算用时:{end_time-start_time}")
    

if __name__ == "__main__":
    main()