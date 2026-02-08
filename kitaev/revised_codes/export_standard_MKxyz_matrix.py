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
params = {'N1': 40, 'N2': 40, 'bc1': -1, 'bc2': -1}

case_list = ['std', 'vison_pair_x', 'vison_pair_y', 'vison_pair_z']

for case in case_list:
    input_name = f'u_{case}'
    try:
        # 1. 动态加载矩阵
        u_matrix = manager.load_sparse_matrix_grid(input_name, **params)
        print(f'成功读取 {input_name}!')
        
        # 2. 构造三种 MK 矩阵并存入字典或直接操作
        # 这里用字典存储可以方便后续调用，例如 result_matrices['MKx_std']
        mk_functions = {
            'MKx': build_MKx_matrix,
            'MKy': build_MKy_matrix,
            'MKz': build_MKz_matrix
        }
        
        for mk_type, func in mk_functions.items():
            output_name = f'{mk_type}_{case}'
            # 执行构造
            mk_res = func(u_matrix, **params)
            # 保存结果
            manager.save_sparse_matrix_grid(mk_res, output_name, **params)
            print(f'  已生成并保存: {output_name}')
            
    except FileNotFoundError:
        print(f"读取失败: 未找到文件 {input_name}")
    except Exception as e:
        print(f"处理 {case} 时发生错误: {e}")
