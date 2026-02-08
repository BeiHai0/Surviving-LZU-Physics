# -*- coding: utf-8 -*-
import numpy as np
from kitaev_data_exporter import KitaevDataExporter
from scipy.linalg import block_diag

# --- 基础索引转换函数 ---
def one_idx_to_two_idx(N1, N2, i):
    return i % N1, i // N1

def two_idx_to_one_idx(N1, N2, n1, n2):
    return n1 + n2 * N1

# --- 核心矩阵构造函数 ---
def build_Mkappa_matrices(u, N1, N2, bc1, bc2):
    """
    一次性计算 MkappaA 和 MkappaB，减少索引转换的重复开销
    """
    N = N1 * N2
    MkappaA = np.zeros((N, N))
    MkappaB = np.zeros((N, N))
    
    # 定义对应 a1, a2 方向的位移向量
    delta_pairs = [
        ((1, 0), (0, 1)), # (a1, a2)
        ((0, 1), (0, 0)), # (a2, 0)
        ((0, 0), (1, 0))  # (0, a1)
    ]
    
    for i in range(N):
        n1_i, n2_i = one_idx_to_two_idx(N1, N2, i)
        
        for delta1, delta2 in delta_pairs:
            # --- MkappaA 逻辑 ---
            r_minus_n1 = (n1_i - delta1[0] + N1) % N1
            r_minus_n2 = (n2_i - delta1[1] + N2) % N2
            r_m_idx = two_idx_to_one_idx(N1, N2, r_minus_n1, r_minus_n2)
            
            j_a_n1 = (n1_i - delta1[0] + delta2[0] + N1) % N1
            j_a_n2 = (n2_i - delta1[1] + delta2[1] + N2) % N2
            j_a = two_idx_to_one_idx(N1, N2, j_a_n1, j_a_n2)
            
            MkappaA[i, j_a] += u[r_m_idx, i] * u[r_m_idx, j_a]
            
            # --- MkappaB 逻辑 ---
            r_plus_n1 = (n1_i + delta1[0] + N1) % N1
            r_plus_n2 = (n2_i + delta1[1] + N2) % N2
            r_p_idx = two_idx_to_one_idx(N1, N2, r_plus_n1, r_plus_n2)
            
            j_b_n1 = (n1_i + delta1[0] - delta2[0] + N1) % N1
            j_b_n2 = (n2_i + delta1[1] - delta2[1] + N2) % N2
            j_b = two_idx_to_one_idx(N1, N2, j_b_n1, j_b_n2)
            
            MkappaB[i, j_b] += u[i, r_p_idx] * u[j_b, r_p_idx]
            
    # 构造最终的反对称块对角矩阵
    # 物理上对应 i*kappa*(c_i*c_j)，因此需要满足反对称性 A - A.T
    MkappaAB = block_diag(MkappaB - MkappaB.T, MkappaA - MkappaA.T)
    return MkappaAB

# --- 批量处理逻辑 ---
manager = KitaevDataExporter()
params = {'N1': 10, 'N2': 10, 'bc1': -1, 'bc2': -1}

# 定义所有需要处理的构型
cases = ['std', 'vison_pair_x', 'vison_pair_y', 'vison_pair_z']

for case in cases:
    input_label = f'u_{case}'
    output_label = f'MkappaAB_{case}'
    
    try:
        # 读取
        u_matrix = manager.load_sparse_matrix_grid(input_label, **params)
        print(f"成功读取 {input_label}")
        
        # 计算
        MkappaAB = build_Mkappa_matrices(u_matrix, **params)
        
        # 保存
        manager.save_sparse_matrix_grid(MkappaAB, output_label, **params)
        print(f"  已生成并保存: {output_label}，矩阵大小: {MkappaAB.shape}")
        
    except FileNotFoundError:
        print(f"跳过: 未找到文件 {input_label}")
    except Exception as e:
        print(f"处理 {case} 时出错: {e}")

print("所有任务处理完成。")

