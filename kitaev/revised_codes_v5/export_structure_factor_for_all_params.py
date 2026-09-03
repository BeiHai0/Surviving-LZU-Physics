# -*- coding: utf-8 -*-
from kitaev_data_manager import KitaevDataManager
import numpy as np
import scipy.linalg as la

def k_path(points, total_interval_number):
    points = np.array(points)
    diffs = np.diff(points, axis=0)
    seg_lengths = np.linalg.norm(diffs, axis=1)
    total_length = np.sum(seg_lengths)
    target_step = total_length / (total_interval_number)
    k_list = []
    k_dist = []
    node_indices = []
    current_cumulative_dist = 0.0
    for i in range(len(diffs)):
        node_indices.append(len(k_list))
        n_seg_intervals = max(1, int(round(seg_lengths[i] / target_step)))
        seg = np.linspace(points[i], points[i+1], n_seg_intervals, endpoint=False)
        dists = np.linspace(current_cumulative_dist, 
                            current_cumulative_dist + seg_lengths[i], 
                            n_seg_intervals, endpoint=False)
        k_list.extend(seg)
        k_dist.extend(dists)
        current_cumulative_dist += seg_lengths[i]
    node_indices.append(len(k_list))
    k_list.append(points[-1])
    k_dist.append(current_cumulative_dist)
    return np.array(k_list), np.array(k_dist), node_indices

def fold_to_1BZ(q, b1, b2):
    B = np.column_stack((b1, b2))
    coeff = np.linalg.solve(B, q)
    coeff_fold = coeff - np.round(coeff)
    q_fold = B @ coeff_fold
    return q_fold

# 这里只计算权重因子

def main():
    # 参数
    manager = KitaevDataManager()
    N1, N2, bc1, bc2 = 20, 20, -1, -1
    N = N1 * N2

    # 实空间基矢
    a1 = np.array([1.0, 0.0])
    a2 = np.array([0.5, np.sqrt(3)/2])

    # 倒空间基矢
    b1 = 2*np.pi * np.array([1, -1/np.sqrt(3)])
    b2 = 2*np.pi * np.array([0,  2/np.sqrt(3)])
    
    delta_x = np.array([-0.5, -0.5/np.sqrt(3)])
    delta_y = np.array([0.5, -0.5/np.sqrt(3)])
    delta_z = np.array([0, 1/np.sqrt(3)])
    delta_list = [None, delta_x, delta_y, delta_z]
    
    # 动量空间高对称点
    Gamma  = np.array([0.0, 0.0])
    K = (2*b1 + b2) / 3
    M_prime = b1 + b2/2
    Gamma_prime = b1 + b2
    K_prime = 2*np.pi * np.array([1.0/3, 1.0/np.sqrt(3)])
    M = b2/2
    
    # 预计算
    points = [Gamma, K, M_prime, Gamma_prime, K_prime, M, Gamma]
    q_interval_number = 20
    q_list, q_dist, node_idx = k_path(points, q_interval_number)
    
    q_fold_list = np.array([fold_to_1BZ(q, b1, b2) for q in q_list])
    
    phase_xy_list = np.exp(-1j * (q_fold_list @ a1))
    phase_yz_list = np.exp(1j * (q_fold_list @ (a1 - a2)))
    phase_zx_list = np.exp(1j * (q_fold_list @ a2))
    
    K_list = [(1, 1, 1), (-1, -1, -1)]
    kappa_list = [0.0, 0.02, 0.04, 0.06]
    
    for Kx, Ky, Kz in K_list:
        
        for kappa in kappa_list:
            
            params = {'Kx':Kx, 'Ky':Ky, 'Kz':Kz, 'kappa':kappa}
            
            T_dict = {}
            params_0 = {'Kx':Kx, 'Ky':Ky, 'Kz':Kz, 'kappa':kappa}
            keys_to_load = ['T_A_1_2', 'T_B_1_2', 'T_A_2_3', 'T_B_2_3', 'T_A_3_1', 'T_B_3_1']
            
            for key in keys_to_load:
                
                T_dict[key] = manager.load_data(key, N1, N2, bc1, bc2, **params_0)
                
            positive_eigvals_list = []
            GS_energy_list = []
                
            for bond in [0, 1, 2, 3]:
                
                params_1 = {'bond': bond, 'Kx':Kx, 'Ky':Ky, 'Kz':Kz, 'kappa':kappa}
                
                positive_eigvals = manager.load_data(f'positive_eigvals_u', N1, N2, bc1, bc2, **params_1)
                positive_eigvals_list.append(positive_eigvals)
                
                GS_energy = -0.5*np.sum(positive_eigvals)
                GS_energy_list.append(GS_energy)
                
            diag_1 = GS_energy_list[1] - GS_energy_list[0] + positive_eigvals_list[1]
            diag_2 = GS_energy_list[2] - GS_energy_list[0] + positive_eigvals_list[2]
            diag_3 = GS_energy_list[3] - GS_energy_list[0] + positive_eigvals_list[3]
            
            p_A_list = [None,]
            p_B_list = [None,]
            
            keys_to_load_A = [f'sigma_A_d_dag_GS_exp_bond_{1}', f'sigma_A_d_dag_GS_exp_bond_{2}', f'sigma_A_d_dag_GS_exp_bond_{3}']
            keys_to_load_B = [f'sigma_B_d_dag_GS_exp_bond_{1}', f'sigma_B_d_dag_GS_exp_bond_{2}', f'sigma_B_d_dag_GS_exp_bond_{3}']
            
            for key_A in keys_to_load_A:
                p_A = manager.load_data(key_A, N1, N2, bc1, bc2, **params)
                p_A_list.append(p_A)
                
            for key_B in keys_to_load_B:
                p_B = manager.load_data(key_B, N1, N2, bc1, bc2, **params)
                p_B_list.append(p_B)
            
            h_c = manager.load_data('h_c', N1, N2, bc1, bc2, **params)
            step = 0.1
            h_list = [(h, h, h) for h in np.arange(0.0, h_c, step)]
            h_list.append((h_c, h_c, h_c))
            
            for hx, hy, hz in h_list:
                params_2 = {'Kx': Kx, 'Ky': Ky, 'Kz': Kz, 'kappa': kappa, 'hx': hx, 'hy': hy, 'hz': hz}
                print(params_2, flush=True)
                tol = 1e-6
                eigvals_all = np.zeros((len(q_list), 3*N), dtype=float) # 用来装所有 q 点对角化矩阵得到的所有本征值
                weights_all = np.zeros((len(q_list), 3*N), dtype=float)
                
                A_xy_h = hz * T_dict['T_A_1_2']; B_xy_h = hz * T_dict['T_B_1_2']
                A_yz_h = hx * T_dict['T_A_2_3']; B_yz_h = hx * T_dict['T_B_2_3']
                A_zx_h = hy * T_dict['T_A_3_1']; B_zx_h = hy * T_dict['T_B_3_1']
                
                if np.abs(hx) < tol: # h=0 的情况 H_k 已经对角，对角元就是本征值
                    
                    eigvals = np.concatenate([diag_1, diag_2, diag_3])
                    eigvals_all[:] = eigvals
                    
                    for q_idx, q in enumerate(q_list):

                        form_factor_list = [None, ]
                    
                        for mu in [1,2,3]:
                    
                            form_factor = (p_A_list[mu] + np.exp(-1j * np.dot(q, delta_list[mu])) * p_B_list[mu])
                    
                            form_factor_list.append(form_factor)
                    
                        weights = np.concatenate([np.abs(form_factor_list[1])**2, np.abs(form_factor_list[2])**2, np.abs(form_factor_list[3])**2])
                        weights_all[q_idx] = np.real(weights) # 为了画图，保险起见强制转化为实数
                    
                else:
          
                    for q_idx, q in enumerate(q_list):
                        
                        H_k = np.zeros((3*N, 3*N), dtype=complex)
                        
                        # 对角块填充
                        
                        H_k[np.arange(N), np.arange(N)] = diag_1 
                        H_k[np.arange(N, 2*N), np.arange(N, 2*N)] = diag_2
                        H_k[np.arange(2*N, 3*N), np.arange(2*N, 3*N)] = diag_3
                        
                        phase_xy = phase_xy_list[q_idx]
                        phase_yz = phase_yz_list[q_idx]
                        phase_zx = phase_zx_list[q_idx]
                        
                        # 非对角块填充
                        
                        H12 = A_xy_h + phase_xy * B_xy_h
                        H_k[0:N, N:2*N] = H12
                        H_k[N:2*N, 0:N] = H12.T.conj()
                        
                        H23 = A_yz_h + phase_yz * B_yz_h
                        H_k[N:2*N, 2*N:3*N] = H23
                        H_k[2*N:3*N, N:2*N] = H23.T.conj()
                        
                        H31 = A_zx_h + phase_zx * B_zx_h
                        H_k[2*N:3*N, 0:N] = H31
                        H_k[0:N, 2*N:3*N] = H31.T.conj()
                        
                        # overwrite_a = True 表示 H_k 会被覆盖（节省内存）
                        eigvals, eigvecs = la.eigh(H_k, overwrite_a=True, check_finite=False, driver='evd')
                        eigvals_all[q_idx] = eigvals
                        # 矩阵太多太大了，没法全部保存，这里只存本征值和权重
                        
                        eigvecs_reshape = eigvecs.reshape(3, N, 3*N)
                        
                        form_factor_list = [None, ]
                        
                        for mu in [1, 2, 3]:
                            
                            form_factor = p_A_list[mu] + np.exp(-1j * np.dot(q, delta_list[mu])) * p_B_list[mu]
                            form_factor_list.append(form_factor)
                            
                        weights = np.zeros(3*N, dtype=float)

                        for mu in [1,2,3]:
                        
                            form_factor = form_factor_list[mu] # form_factor.shape == (N,)
                        
                            phi_block = eigvecs_reshape[mu-1] # phi_block.shape == (N, 3*N)
                        
                            amp = form_factor @ phi_block # amp.shape == (3*N,)
                        
                            weights += np.abs(amp)**2 # weights.shape == (3*N,)
                        
                        weights_all[q_idx] = np.real(weights) 
                            
                # 保存下面这两个，就算 eta 取别的数值也能画结构因子图
                manager.save_data(f'eigvals_q_interval_number_{q_interval_number}', eigvals_all, N1, N2, bc1, bc2, **params_2)
                manager.save_data(f'weights_q_interval_number_{q_interval_number}', weights_all, N1, N2, bc1, bc2, **params_2)
                               
                manager.save_data(f'q_list_q_interval_number_{q_interval_number}', q_list, N1, N2, bc1, bc2, **params_2)
                manager.save_data(f'node_idx_q_interval_number_{q_interval_number}', node_idx, N1, N2, bc1, bc2, **params_2)
    
    
    

if __name__ == "__main__":
    main()