# -*- coding: utf-8 -*-

import numpy as np
from kitaev_data_exporter import KitaevDataExporter

def one_idx_to_two_idx(N1, N2, i):
    n1 = i%N1
    n2 = i//N1
    return n1, n2    

def two_idx_to_one_idx(N1, N2, n1, n2):
    return n1+n2*N1

def build_MKx_matrix(u, N1, N2, bc1, bc2): # 关键字参数要放最后
    N = N1*N2
    MKx = np.zeros((N, N))
    u_diag = np.diagonal(u)
    MKx[np.diag_indices_from(MKx)] = u_diag
    return MKx

def build_MKy_matrix(u, N1, N2, bc1, bc2):
    N = N1*N2
    MKy = np.zeros((N, N))
    for i in range(N):
        n1_i, n2_i = one_idx_to_two_idx(N1, N2, i)
        n1_j = (n1_i+1)%N1
        n2_j = n2_i
        j = two_idx_to_one_idx(N1, N2, n1_j, n2_j)
        
        MKy[i, j] = u[i, j]
    
    return MKy

def build_MKz_matrix(u, N1, N2, bc1, bc2):
    N = N1*N2
    MKz = np.zeros((N, N))
    for i in range(N):
        n1_i, n2_i = one_idx_to_two_idx(N1, N2, i)
        n1_j = n1_i
        n2_j = (n2_i+1)%N2
        j = two_idx_to_one_idx(N1, N2, n1_j, n2_j)
        
        MKz[i, j] = u[i, j]
    
    return MKz

manager = KitaevDataExporter()
params = {'N1': 30, 'N2': 30, 'bc1': -1, 'bc2': -1}

try:
    u_std = manager.load_sparse_matrix_grid('u_std', **params)
    print('成功读取矩阵!')
    # print(u_std)
except FileNotFoundError as e:
    print(f"读取失败:{e}")

MKx_std = build_MKx_matrix(u_std, **params)
MKy_std = build_MKy_matrix(u_std, **params)
MKz_std = build_MKz_matrix(u_std, **params)

manager.save_sparse_matrix_grid(MKx_std, 'MKx_std', **params)
manager.save_sparse_matrix_grid(MKy_std, 'MKy_std', **params)
manager.save_sparse_matrix_grid(MKz_std, 'MKz_std', **params)

print(MKx_std)
print(MKy_std)
print(MKz_std)



