# -*- coding: utf-8 -*-
from kitaev_data_manager import KitaevDataManager
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la
from pfapack import pfaffian

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

# 参数
manager = KitaevDataManager()
N1, N2, bc1, bc2 = 20, 20, -1, -1
N = N1 * N2
n1, n2 = N1//2, N2//2

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

points = [Gamma, K, M_prime, Gamma_prime, K_prime, M, Gamma]
q_interval_number = 50
q_list, q_dist, node_idx = k_path(points, q_interval_number)

H_k = np.zeros((3*N, 3*N), dtype=complex)

for Kx, Ky, Kz in [(1, 1, 1)]:
    for kappa in np.linspace(0, 0.02, 2):
        T_dict = {}
        params = {'Kx':Kx, 'Ky':Ky, 'Kz':Kz, 'kappa':kappa}
        # 导入 T 矩阵
        keys_to_load = ['T_A_xy', 'T_B_xy', 'T_A_yz', 'T_B_yz', 'T_A_zx', 'T_B_zx']
        for key in keys_to_load:
            T_dict[key] = manager.load_data(key, N1, N2, bc1, bc2, **params)
            #print(T_dict[key])
            
        pos_list = [manager.load_data(f'positive_eigvals_u_{i}', N1, N2, bc1, bc2, **params) for i in range(4)]
        gs_list = [-np.sum(p)/2 for p in pos_list]
        diag_vals = [np.array(gs_list[i] - gs_list[0] + pos_list[i], dtype=complex) for i in [1,2,3]]
        #print(pos_list)
        #print(diag_vals)

        H_k.fill(0)      
        H_k[np.arange(N), np.arange(N)] = diag_vals[0] # 对角块填充
        H_k[np.arange(N, 2*N), np.arange(N, 2*N)] = diag_vals[1]
        H_k[np.arange(2*N, 3*N), np.arange(2*N, 3*N)] = diag_vals[2]
        
        # p_A_mu & p_B_mu
        p_A_list = [None,]
        p_B_list = [None,]
        
        keys_to_load_A = [f'sigma_A_d_dag_GS_exp_bond_{1}', f'sigma_A_d_dag_GS_exp_bond_{2}', f'sigma_A_d_dag_GS_exp_bond_{3}']
        for key_A in keys_to_load_A:
            p_A_mu = manager.load_data(key_A, N1, N2, bc1, bc2, **params)
            p_A_list.append(p_A_mu)
        
        keys_to_load_B = [f'sigma_B_d_dag_GS_exp_bond_{1}', f'sigma_B_d_dag_GS_exp_bond_{2}', f'sigma_B_d_dag_GS_exp_bond_{3}']
        for key_B in keys_to_load_B:
            p_B_mu = manager.load_data(key_B, N1, N2, bc1, bc2, **params)
            p_B_list.append(p_B_mu)
        
        #print(p_A_list)
        #print(p_B_list)
        
        for hx, hy, hz in [(v,v,v) for v in np.linspace(0, 0.3, 4)]:
            params2 = {'Kx': Kx, 'Ky': Ky, 'Kz': Kz, 'kappa': kappa, 'hx': hx, 'hy': hy, 'hz': hz}
            A_xy_h = hz * T_dict['T_A_xy']; B_xy_h = hz * T_dict['T_B_xy']
            A_yz_h = hx * T_dict['T_A_yz']; B_yz_h = hx * T_dict['T_B_yz']
            A_zx_h = hy * T_dict['T_A_zx']; B_zx_h = hy * T_dict['T_B_zx']
            
            omega = np.linspace(0, 5, 501)
            S = np.zeros((len(q_list), len(omega)), dtype=complex)
            
            for q_idx, q in enumerate(q_list):
                q_in_1BZ = fold_to_1BZ(q, b1, b2)
                
                phase_xy = np.array(np.exp(-1j * np.dot(q_in_1BZ, a1)), dtype=complex)
                phase_yz = np.array(np.exp(1j * np.dot(q_in_1BZ, a1 - a2)), dtype=complex)
                phase_zx = np.array(np.exp(1j * np.dot(q_in_1BZ, a2)), dtype=complex)
                
                H12 = A_xy_h + phase_xy * B_xy_h
                H_k[0:N, N:2*N] = H12
                H_k[N:2*N, 0:N] = H12.T.conj()
                
                H23 = A_yz_h + phase_yz * B_yz_h
                H_k[N:2*N, 2*N:3*N] = H23
                H_k[2*N:3*N, N:2*N] = H23.T.conj()
                
                H31 = A_zx_h + phase_zx * B_zx_h
                H_k[2*N:3*N, 0:N] = H31
                H_k[0:N, 2*N:3*N] = H31.T.conj()
                
                eigvals, eigvecs = la.eigh(H_k)
                #print(eigvals)
                
                
                eta = 0.04
                
                
                for i in np.arange(3*N):
                    eps = eigvals[i]
                    phi = eigvecs[:,i]
                    total_weight = 0.0
                    
                    for mu in [1,2,3]:
                        if mu == 1:
                            phi_mu = phi[0:N]
                        elif mu == 2:
                            phi_mu = phi[N:2*N]
                        else:
                            phi_mu = phi[2*N:3*N]                            
                
                        form_factor = p_A_list[mu] + np.exp(-1j * np.dot(q, delta_list[mu])) * p_B_list[mu]
                        #print(form_factor)
                        #print(form_factor.shape)
                        amp = (form_factor @ phi_mu)[0]
                        #print(amp)
                        total_weight += np.abs(amp)**2
                    
                    S[q_idx] += total_weight * (eta)/((omega - eps)**2 + eta**2)
            S = np.real(S)
            manager.save_data('S', S, N1, N2, bc1, bc2, **params2)
            manager.save_data('q_list', q_list, N1, N2, bc1, bc2, **params2)
            manager.save_data('omega', omega, N1, N2, bc1, bc2, **params2)
            manager.save_data('node_idx', node_idx, N1, N2, bc1, bc2, **params2)
            
            # plt.figure(figsize=(6,5))
            # plt.imshow(S.T,aspect='auto',origin='lower',extent=[0, len(q_list), omega[0], omega[-1]])
            # plt.colorbar(label='S(ω,q)')
            # ax = plt.gca()

            # ax.yaxis.set_major_locator(MultipleLocator(1))   # 主刻度间隔
            # ax.yaxis.set_minor_locator(MultipleLocator(0.1))   # 次刻度更细
            
            # ax.tick_params(axis='y', which='major', length=6)
            # ax.tick_params(axis='y', which='minor', length=3)
            # plt.ylabel('ω')
            # plt.xlabel('k-path')
            # plt.xticks(node_idx, ['Γ','K',"M'","Γ'","K'","M",'Γ'])
            # plt.title(f"K=({Kx},{Ky},{Kz}), κ={kappa:.3f}, h={hx:.3f}")
            # plt.tight_layout()
            # plt.show()
                
        
            
            














