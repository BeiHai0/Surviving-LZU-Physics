# -*- coding: utf-8 -*-
from kitaev_data_manager import KitaevDataManager
from scipy import sparse

def build_M_kappaA_matrix(M_Ka0, M_Ka1, M_Ka2):
    pairs = [
        (M_Ka1, M_Ka2),
        (M_Ka2, M_Ka0),
        (M_Ka0, M_Ka1),
    ]
    
    M_kappaA = sparse.csr_matrix(M_Ka0.shape)
    
    for M1, M2 in pairs:
        M_kappaA += M1 @ M2.T
        
    return M_kappaA.tocsr()
    
def build_M_kappaB_matrix(M_Ka0, M_Ka1, M_Ka2):
    pairs = [
        (M_Ka1, M_Ka2),
        (M_Ka2, M_Ka0),
        (M_Ka0, M_Ka1),
    ]
    
    M_kappaB = sparse.csr_matrix(M_Ka0.shape)
    
    for M1, M2 in pairs:
        M_kappaB += M1.T @ M2
        
    return M_kappaB.tocsr()

def build_M_kappaAB_matrix(M_kappaA, M_kappaB):
    N = M_kappaA.shape[0]
    zero = sparse.csr_matrix((N, N))
    M_kappaAB = sparse.bmat([
        [M_kappaA - M_kappaA.T, zero],
        [zero, M_kappaB - M_kappaB.T],
    ])
    return M_kappaAB.tocsr()

manager = KitaevDataManager() # 不传参，默认 root 为 kitaev_data
N1, N2, bc1, bc2 = 10, 10, -1, -1

u_case_list = ['std', 'vison_pair_x', 'vison_pair_y', 'vison_pair_z']
M_K_case_list = ['Ka0', 'Ka1', 'Ka2']

for u_case in u_case_list:
    M_K_list = []
    for M_K_case in M_K_case_list:
        input_name = f'M_{M_K_case}_{u_case}'
        tmp = manager.load_data(input_name, N1, N2, bc1, bc2)
        if tmp is None:
            raise ValueError(f"{input_name} 读取失败")
        print(f'成功读取 {input_name}!')
        M_K_list.append(tmp)
        
    M_kappaA = build_M_kappaA_matrix(M_K_list[0], M_K_list[1], M_K_list[2])
    M_kappaB = build_M_kappaB_matrix(M_K_list[0], M_K_list[1], M_K_list[2])
    M_kappaAB = build_M_kappaAB_matrix(M_kappaA, M_kappaB)
    
    output_name = f'M_kappaAB_{u_case}'
    manager.save_data(output_name, M_kappaAB, N1, N2, bc1, bc2)
    print(f'  已生成并保存: {output_name}')
