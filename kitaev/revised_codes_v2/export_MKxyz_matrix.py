# -*- coding: utf-8 -*-
from kitaev_data_manager import KitaevDataManager
from scipy import sparse

def one_idx_to_two_idx(N1, N2, i):
    n1 = i % N1
    n2 = i // N1
    return n1, n2    

def two_idx_to_one_idx(N1, N2, n1, n2):
    return n1 + n2 * N1

def build_MKx_matrix(u, N1, N2, bc1, bc2):
    # u 是稀疏矩阵，使用其自带的 .diagonal() 方法
    u_diag = u.diagonal()
    # 直接用对角数组构造稀疏对角阵，效率最高
    MKx = sparse.diags(u_diag).tocsr()
    return MKx

def build_MKy_matrix(u, N1, N2, bc1, bc2):
    N = N1 * N2
    # 使用 lil_matrix 方便逐点赋值，最后转为 csr
    MKy = sparse.lil_matrix((N, N))
    for i in range(N):
        n1_i, n2_i = one_idx_to_two_idx(N1, N2, i)
        n1_j = (n1_i + 1) % N1
        n2_j = n2_i
        j = two_idx_to_one_idx(N1, N2, n1_j, n2_j)
        
        # 稀疏矩阵索引获取值需要注意性能，但在 N=100 左右没问题
        MKy[i, j] = u[i, j]
    
    return MKy.tocsr()

def build_MKz_matrix(u, N1, N2, bc1, bc2):
    N = N1 * N2
    MKz = sparse.lil_matrix((N, N))
    for i in range(N):
        n1_i, n2_i = one_idx_to_two_idx(N1, N2, i)
        n1_j = n1_i
        n2_j = (n2_i + 1) % N2
        j = two_idx_to_one_idx(N1, N2, n1_j, n2_j)
        
        MKz[i, j] = u[i, j]
    
    return MKz.tocsr()

manager = KitaevDataManager() # 不传参，默认 root 为 kitaev_data
N1, N2, bc1, bc2 = 10, 10, -1, -1

case_list = ['std', 'vison_pair_x', 'vison_pair_y', 'vison_pair_z']
for case in case_list:
    input_name = f'u_{case}'
    u = manager.load_data(input_name, N1, N2, bc1, bc2)
    print(f'成功读取 {input_name}!')
    
    MK_functions = {
        'MKx': build_MKx_matrix,
        'MKy': build_MKy_matrix,
        'MKz': build_MKz_matrix
    }
    
    for MK_type, func in MK_functions.items():
        output_name = f'{MK_type}_{case}'
        MK_res = func(u, N1, N2, bc1, bc2)
        manager.save_data(output_name, MK_res, N1, N2, bc1, bc2)
        print(f'  已生成并保存: {output_name}')
        
        