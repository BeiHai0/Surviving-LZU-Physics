# -*- coding: utf-8 -*-

import numpy as np
from kitaev_data_exporter import KitaevDataExporter
from scipy.linalg import block_diag

def one_idx_to_two_idx(N1, N2, i):
    n1 = i%N1
    n2 = i//N1
    return n1, n2    

def two_idx_to_one_idx(N1, N2, n1, n2):
    return n1+n2*N1

def build_MkappaA_matrix(u, N1, N2, bc1, bc2):
    N = N1*N2
    MkappaA = np.zeros((N, N))
    delta_pairs = [
        ((1, 0), (0, 1)), # (a1, a2)
        ((0, 1), (0, 0)), # (a2, 0)
        ((0, 0), (1, 0))  # (0, a1)
    ]
    
    for i in range(N):
        n1_i, n2_i = one_idx_to_two_idx(N1, N2, i)
        
        for delta1, delta2 in delta_pairs:
            r_i_minus_delta1_n1 = (n1_i - delta1[0] + N1) % N1
            r_i_minus_delta1_n2 = (n2_i - delta1[1] + N2) % N2
            r_i_minus_delta1_one_idx = two_idx_to_one_idx(N1, N2, r_i_minus_delta1_n1, r_i_minus_delta1_n2)
            
            n1_j = (n1_i - delta1[0] + delta2[0] + N1) % N1
            n2_j = (n2_i - delta1[1] + delta2[1] + N2) % N2
            j = two_idx_to_one_idx(N1, N2, n1_j, n2_j)
            MkappaA[i, j] += u[r_i_minus_delta1_one_idx, i] * u[r_i_minus_delta1_one_idx, j]
            
    return MkappaA

def build_MkappaB_matrix(u, N1, N2, bc1, bc2):
    N = N1*N2
    MkappaB = np.zeros((N, N))
    delta_pairs = [
        ((1, 0), (0, 1)), # (a1, a2)
        ((0, 1), (0, 0)), # (a2, 0)
        ((0, 0), (1, 0))  # (0, a1)
    ]
    
    for i in range(N):
        n1_i, n2_i = one_idx_to_two_idx(N1, N2, i)
        
        for delta1, delta2 in delta_pairs:
            r_i_plus_delta1_n1 = (n1_i + delta1[0] + N1) % N1
            r_i_plus_delta1_n2 = (n2_i + delta1[1] + N2) % N2
            r_i_plus_delta1_one_idx = two_idx_to_one_idx(N1, N2, r_i_plus_delta1_n1, r_i_plus_delta1_n2)
            
            n1_j = (n1_i + delta1[0] - delta2[0] + N1) % N1
            n2_j = (n2_i + delta1[1] - delta2[1] + N2) % N2
            j = two_idx_to_one_idx(N1, N2, n1_j, n2_j)
            MkappaB[i, j] += u[i, r_i_plus_delta1_one_idx] * u[j, r_i_plus_delta1_one_idx]
            
    return MkappaB

def build_MkappaAB_matrix(MkappaA, MkappaB):
    MkappaAB = block_diag(MkappaB - MkappaB.T, MkappaA-MkappaA.T)
    return MkappaAB

manager = KitaevDataExporter()
params = {'N1': 40, 'N2': 40, 'bc1': -1, 'bc2': -1}

try:
    u_std = manager.load_sparse_matrix_grid('u_std', **params)
    print('成功读取矩阵!')
    # print(u_std)
except FileNotFoundError as e:
    print(f"读取失败:{e}")
    
MkappaA_std = build_MkappaA_matrix(u_std, **params)
MkappaB_std = build_MkappaB_matrix(u_std, **params)
MkappaAB_std = build_MkappaAB_matrix(MkappaA_std, MkappaB_std)

manager.save_sparse_matrix_grid(MkappaAB_std, 'MkappaAB_std', **params)
print(MkappaAB_std)

