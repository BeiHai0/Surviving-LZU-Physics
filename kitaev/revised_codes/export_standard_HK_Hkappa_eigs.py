# -*- coding: utf-8 -*-

import numpy as np
from kitaev_data_exporter import KitaevDataExporter
from scipy import sparse
import scipy.linalg as la
import matplotlib.pyplot as plt
import time

def build_HK_plus_Hkappa_c_matrix(MKx, MKy, MKz, MkappaAB, Kx, Ky, Kz, kappa):
    MK = Kx*MKx + Ky*MKy + Kz*MKz
    HK_c_matrix = sparse.bmat([
        [None,  MK],
        [-MK.T, None]
    ])
    Hkappa_c_matrix = kappa * MkappaAB
    HK_plus_Hkappa_c_matrix = HK_c_matrix + Hkappa_c_matrix
    return HK_plus_Hkappa_c_matrix

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
    
def diagonalize_BdG_matrix(H_BdG):
    total_dim = H_BdG.shape[0]
    N = total_dim // 2
    eigvals, eigvecs = la.eigh(H_BdG)
    eigvals_positive = eigvals[N:]
    eigvecs_positive = eigvecs[:, N:]
    W = eigvecs_positive[:N, :]
    V = eigvecs_positive[N:, :]
    print("对角化完成！")
    return eigvals_positive, W, V

manager = KitaevDataExporter()
params1 = {'N1': 60, 'N2': 60, 'bc1': -1, 'bc2': -1}
params2 = {'Kx': 1, 'Ky': 1, 'Kz': 1, 'kappa': 0.03}
params_grid_kappa = {**params1, 'kappa': params2['kappa']}
print("开始")

try:
    MKx_std = manager.load_sparse_matrix_grid('MKx_std', **params1)
    MKy_std = manager.load_sparse_matrix_grid('MKy_std', **params1)
    MKz_std = manager.load_sparse_matrix_grid('MKz_std', **params1)
    MkappaAB_std = manager.load_sparse_matrix_grid('MKappaAB_std', **params1)
    print('成功读取矩阵!')
except FileNotFoundError as e:
    print(f"读取失败:{e}")

HK_plus_Hkappa_c_matrix_std = build_HK_plus_Hkappa_c_matrix(MKx_std, MKy_std, MKz_std, MkappaAB_std, **params2)
HK_plus_Hkappa_a_matrix_std = build_Ha_from_Hc(HK_plus_Hkappa_c_matrix_std)

start_time = time.time()
eigvals_positive_std, W_std, V_std = diagonalize_BdG_matrix(HK_plus_Hkappa_a_matrix_std)
end_time = time.time()

print(f"执行耗时: {end_time - start_time:.6f} 秒")

GS_energy_std = -np.sum(eigvals_positive_std) / 2
print(f"GS_energy:{GS_energy_std}")

manager.save_nonsparse_matrix_grid_kappa(W_std, 'W_std', **params_grid_kappa)
manager.save_nonsparse_matrix_grid_kappa(V_std, 'V_std', **params_grid_kappa)
manager.save_nonsparse_matrix_grid_kappa(eigvals_positive_std, 'eigvals_positive_std', **params_grid_kappa)
print("all done")

data_masked = np.where(HK_plus_Hkappa_a_matrix_std == 0, np.nan, HK_plus_Hkappa_a_matrix_std)

plt.imshow(data_masked, cmap='viridis', interpolation='nearest')
plt.colorbar(label='Value')
plt.title("Non-zero Elements with Intensity")
plt.show()
