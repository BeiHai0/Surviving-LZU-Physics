# -*- coding: utf-8 -*-

import numpy as np
from kitaev_data_exporter import KitaevDataExporter

def build_vison_pair_added_u_matrix(u_std, n1, n2, bond, N1, N2, bc1, bc2):
    u_vison_pair = u_std.copy()
    def index(n1, n2):
        return n1 + n2*N1
    i = index(n1, n2)
    if bond == 1: # x-bond
        j = index(n1, n2)
    elif bond == 2: # y-bond
        j = index((n1+1)%N1, n2)
    elif bond == 3: # z-bond
        j = index(n1, (n2+1)%N2)
    
    u_vison_pair[i, j] = -u_vison_pair[i, j]
    
    return u_vison_pair
    

manager = KitaevDataExporter()
params = {'N1':60, 'N2': 60, 'bc1': -1, 'bc2': -1}

try:
    u_std = manager.load_sparse_matrix_grid('u_std', **params)
    print('成功读取矩阵!')
    print(u_std)
except FileNotFoundError as e:
    print(f"读取失败:{e}")
    
n1 = params['N1'] // 2
n2 = params['N2'] // 2
u_vison_pair_x = build_vison_pair_added_u_matrix(u_std, n1, n2, bond=1, **params)
u_vison_pair_y = build_vison_pair_added_u_matrix(u_std, n1, n2, bond=2, **params) 
u_vison_pair_z = build_vison_pair_added_u_matrix(u_std, n1, n2, bond=3, **params)   
    
manager.save_sparse_matrix_grid(u_vison_pair_x, 'u_vison_pair_x', **params)
manager.save_sparse_matrix_grid(u_vison_pair_y, 'u_vison_pair_y', **params)
manager.save_sparse_matrix_grid(u_vison_pair_z, 'u_vison_pair_z', **params)


    