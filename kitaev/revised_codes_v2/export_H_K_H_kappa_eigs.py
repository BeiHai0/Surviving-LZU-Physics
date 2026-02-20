# -*- coding: utf-8 -*-
from kitaev_data_manager import KitaevDataManager
import numpy as np
from scipy import sparse
import scipy.linalg as la
import matplotlib.pyplot as plt
import time

def build_H_K_plus_H_kappa_c_matrix(M_Ka0, M_Ka1, M_Ka2, M_kappaAB, Kx, Ky, Kz, kappa):
    M_K = Kx*M_Ka0 + Ky*M_Ka1 + Kz*M_Ka2
    H_K_c_matrix = sparse.bmat([
        [None,  M_K],
        [-M_K.T, None]
    ])
    Hkappa_c_matrix = kappa * M_kappaAB
    HK_plus_Hkappa_c_matrix = H_K_c_matrix + Hkappa_c_matrix
    return HK_plus_Hkappa_c_matrix.tocsr()

def build_Ha_from_Hc(Hc):
    total_dim = Hc.shape[0]
    N = total_dim // 2
    I = sparse.eye(N)
    T_ca = sparse.bmat([
        [I, I],
        [-1j*I, 1j*I]
    ])
    T_ca_dag = T_ca.conj().T
    Ha = 1j * (T_ca_dag @ Hc @ T_ca)
    return Ha

def diagonalize_BdG_matrix(H_BdG_sparse):
    total_dim = H_BdG_sparse.shape[0]
    N = total_dim // 2
    H_BdG_dense = H_BdG_sparse.toarray()
    eigvals, eigvecs = np.linalg.eigh(H_BdG_dense)
    eigvals_positive = eigvals[N:]
    eigvecs_positive = eigvecs[:, N:]
    W = eigvecs_positive[:N, :]
    V = eigvecs_positive[N:, :]
    print("对角化完成！")
    return eigvals_positive, W, V

manager = KitaevDataManager() # 不传参，默认 root 为 kitaev_data
N1, N2, bc1, bc2 = 10, 10, -1, -1
params = {'Kx': 1, 'Ky': 1, 'Kz': 1, 'kappa': 0.0}

u_case_list = ['std', 'vison_pair_x', 'vison_pair_y', 'vison_pair_z']

for u_case in u_case_list:
    try:
        M_kappaAB = manager.load_data(f'M_kappaAB_{u_case}', N1, N2, bc1, bc2)
        M_Ka0 = manager.load_data(f'M_Ka0_{u_case}', N1, N2, bc1, bc2)
        M_Ka1 = manager.load_data(f'M_Ka1_{u_case}', N1, N2, bc1, bc2)
        M_Ka2 = manager.load_data(f'M_Ka2_{u_case}', N1, N2, bc1, bc2)
        print('成功读取矩阵!')
    except FileNotFoundError as e:
        print(f"读取失败:{e}")
        
    H_K_plus_H_kappa_c_matrix = build_H_K_plus_H_kappa_c_matrix(M_Ka0, M_Ka1, M_Ka2, M_kappaAB, **params)
    H_K_plus_H_kappa_a_matrix = build_Ha_from_Hc(H_K_plus_H_kappa_c_matrix)
    start_time = time.time()
    eigvals_positive, W, V = diagonalize_BdG_matrix(H_K_plus_H_kappa_a_matrix)
    end_time = time.time()
    print(f"执行耗时: {end_time - start_time:.6f} 秒")

    GS_energy = -np.sum(eigvals_positive) / 2
    print(f"GS_energy:{GS_energy}")
    
    manager.save_data(f'eigvals_positive_{u_case}', eigvals_positive, N1, N2, bc1, bc2, **params)
    manager.save_data(f'W_{u_case}', W, N1, N2, bc1, bc2, **params)
    manager.save_data(f'V_{u_case}', V, N1, N2, bc1, bc2, **params)
        
