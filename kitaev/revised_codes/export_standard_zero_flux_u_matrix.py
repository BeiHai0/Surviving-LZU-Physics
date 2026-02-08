# -*- coding: utf-8 -*-

import numpy as np
from kitaev_data_exporter import KitaevDataExporter

def build_standard_zero_flux_u_matrix(N1, N2, bc1, bc2):
    def index(n1, n2):
        return n1 + n2*N1
        
    N = N1*N2
    u = np.zeros((N, N))
    for n2 in range(N2):
        for n1 in range(N1):
            i = index(n1, n2) # (n1 ,n2 ) A 所处元胞 (n1, n2) 的单指标
            
            jx = index(n1, n2) # (n1, n2) B 所处元胞 (n1 ,n2) 的单指标
            u[i, jx] = 1 # x-bond 不会跨边界, standard情况下内部的 u 都为 +1
            
            jy = index((n1+1)%N1, n2) # (n1+1, n2) B 所处元胞的单指标, 但要考虑周期性边界条件; i,A 与 jy,B 通过 y-bond 相连
            if n1 == N1-1:
                u[i, jy] = bc1
            else:
                u[i, jy] = 1
                
            jz = index(n1, (n2+1)%N2) # (n1, n2+1) B 所处元胞的单指标, 但要考虑周期性边界条件; i,A 与 jz,B 通过 z-bond 相连
            if n2 == N2-1:
                u[i, jz] = bc2
            else:
                u[i, jz] = 1
    return u
    
params_export = {'N1': 40, 'N2': 40, 'bc1': -1, 'bc2': -1}
manager = KitaevDataExporter() # 不传参，默认 root 为 kitaev_data
u_std = build_standard_zero_flux_u_matrix(**params_export)
print(u_std)
manager.save_sparse_matrix_grid(u_std, 'u_std', **params_export)

### 读取
params_load = {'N1': 60, 'N2': 60, 'bc1': -1, 'bc2': -1}
try:
    u_std_loaded = manager.load_sparse_matrix_grid('u_std', **params_load)
    print('成功读取矩阵!')
    print(u_std_loaded)
except FileNotFoundError as e:
    print(f"读取失败:{e}")
