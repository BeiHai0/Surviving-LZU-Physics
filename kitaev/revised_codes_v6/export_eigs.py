# -*- coding: utf-8 -*-
from kitaev_data_manager import KitaevDataManager
from scipy import sparse
import numpy as np
import time
import gc
import scipy.linalg as la
import argparse

def one_idx_to_two_idx(N1, N2, i):
    return i % N1, i // N1

def two_idx_to_one_idx(N1, N2, n1, n2):
    return n1 + n2 * N1

# 构建 u 矩阵
# u[i ,j] 代表 (i, A) 格点与 (j, B) 格点的 u_{i,A;j,B}；其中 i,j 都是原胞单指标 
# bond==0 代表标准零磁通构型 u_0，也即内部的 u 全为 +1，跨边界的 u 依赖于边界条件
# bond==1 代表在 u_0 构型基础上，中间 (n1,n2,x) 的 u 为 -1 
def build_u_matrix(N1, N2, bc1, bc2, bond):
    N = N1 * N2
    rows = []   # 行索引
    cols = []   # 列索引
    data = []   # 数值
    
    # 构造 u_0
    for n2 in range(N2):
        for n1 in range(N1):
            i = n1 + n2 * N1            # 元胞 (n1, n2) 的 A 子格

            # x‑bond: 同一元胞内 A→B，始终为 +1
            rows.append(i)
            cols.append(i)
            data.append(1)

            # y‑bond: A 在 (n1, n2) 连接 B 在 (n1+1, n2)，有可能跨边界
            jy = ((n1 + 1) % N1) + n2 * N1
            rows.append(i)
            cols.append(jy)
            data.append(bc1 if n1 == N1 - 1 else 1)

            # z‑bond: A 在 (n1, n2) 连接 B 在 (n1, n2+1)，有可能跨边界
            jz = n1 + ((n2 + 1) % N2) * N1
            rows.append(i)
            cols.append(jz)
            data.append(bc2 if n2 == N2 - 1 else 1)
    
    u = sparse.coo_matrix((data, (rows, cols)), shape=(N, N))
    u = u.tolil()
    
    # 若 bond 不为 0，还要翻转中间的一个 u
    n1, n2 = N1//2, N2//2 
    i = n1 + n2 * N1 
    
    if bond == 1:
        j = i
        u[i, j] = -1
    elif bond == 2:
        j = n1+1 + n2*N1 
        u[i, j] = -1
    elif bond == 3:
        j = n1 + (n2+1)*N1
        u[i, j] = -1
    
    return u.tocsr()

def build_M_K_x_matrix(u, N1, N2, bc1, bc2):
    # tau_x = 0 = (0, 0)
    return sparse.diags(u.diagonal()).tocsr()

def build_M_K_y_matrix(u, N1, N2, bc1, bc2):
    # tau_y = a_1 = (1, 0)
    N = N1*N2
    M_K_y = sparse.lil_matrix((N, N))
    tau_y = np.array([1, 0])
    
    for i in range(N):
        R_i = np.array([i % N1, i // N1])
        R_j = (R_i + tau_y) % np.array([N1, N2])
        j = R_j[0] + N1 * R_j[1]
        M_K_y[i, j] = u[i, j]
    
    return M_K_y.tocsr()

def build_M_K_z_matrix(u, N1, N2, bc1, bc2):
    # tau_z = a_2 = (0, 1)
    N = N1*N2
    M_K_z = sparse.lil_matrix((N, N))
    tau_z = np.array([0, 1])
    
    for i in range(N):
        R_i = np.array([i % N1, i // N1])
        R_j = (R_i + tau_z) % np.array([N1, N2])
        j = R_j[0] + N1 * R_j[1]
        M_K_z[i, j] = u[i, j]
    
    return M_K_z.tocsr()


## 注意，M_kappa 矩阵可以用 M_K 矩阵表达

# H_kappa 中 两个 A 子格 c-Majorana 耦合的系数矩阵
def build_M_kappa_A_matrix(M_K_x, M_K_y, M_K_z):
    M_kappa_A = M_K_x @ M_K_y.T + M_K_y @ M_K_z.T + M_K_z @ M_K_x.T
    return M_kappa_A

# H_kappa 中 两个 B 子格 c-Majorana 耦合的系数矩阵
def build_M_kappa_B_matrix(M_K_x, M_K_y, M_K_z):
    M_kappa_B = M_K_x.T @ M_K_y + M_K_y.T @ M_K_z + M_K_z.T @ M_K_x
    return M_kappa_B

def build_M_kappa_AB_matrix(M_kappa_A, M_kappa_B):
    M_kappa_AB = sparse.bmat([
        [M_kappa_A - M_kappa_A.T, None],
        [None, M_kappa_B- M_kappa_B.T],
    ])
    return M_kappa_AB

def build_H_K_plus_H_kappa_c_matrix(M_K_x, M_K_y, M_K_z, M_kappa_AB, Kx, Ky, Kz, kappa):
    M_K = Kx * M_K_x + Ky * M_K_y + Kz * M_K_z
    H_K_c = sparse.bmat([[None, M_K], [-M_K.T, None]])
    H_kappa_c = kappa * M_kappa_AB
    H_c = H_K_c + H_kappa_c
    return H_c.tocsr()

def build_H_a_from_H_c(H_c):
    N = H_c.shape[0] // 2
    I_N = sparse.eye(N, dtype=complex)
    T_ca = sparse.bmat([
        [I_N, I_N],
        [-1j*I_N, 1j*I_N]
    ])
    T_ca_dag = T_ca.T.conj()
    H_a = 1j * (T_ca_dag @ H_c @ T_ca)
    return H_a.toarray()


# 主函数
# 提交给 cluster, 每个 python 文件算一组特定参数 bond, K, kappa, 参数从命令行接收
def main():
    manager = KitaevDataManager()
    N1, N2, bc1, bc2 = 60, 60, -1, -1
    N = N1 * N2
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--bond", type=int, required=True)
    parser.add_argument("--Kx", type=int, required=True)
    parser.add_argument("--Ky", type=int, required=True)
    parser.add_argument("--Kz", type=int, required=True)
    parser.add_argument("--kappa", type=float, required=True)
    args = parser.parse_args()
    
    bond = args.bond
    Kx, Ky, Kz = args.Kx, args.Ky, args.Kz
    kappa = args.kappa
    
    params = {'bond':bond ,'Kx': Kx, 'Ky': Ky, 'Kz': Kz, 'kappa': kappa}
    print(params)
    
    u = build_u_matrix(N1, N2, bc1, bc2, bond)
    M_K_x = build_M_K_x_matrix(u, N1, N2, bc1, bc2)
    M_K_y = build_M_K_y_matrix(u, N1, N2, bc1, bc2)
    M_K_z = build_M_K_z_matrix(u, N1, N2, bc1, bc2)
    M_kappa_A = build_M_kappa_A_matrix(M_K_x, M_K_y, M_K_z)
    M_kappa_B = build_M_kappa_B_matrix(M_K_x, M_K_y, M_K_z)
    M_kappa_AB = build_M_kappa_AB_matrix(M_kappa_A, M_kappa_B)
                
    H_c = build_H_K_plus_H_kappa_c_matrix(M_K_x, M_K_y, M_K_z, M_kappa_AB, Kx, Ky, Kz, kappa)
    H_a = build_H_a_from_H_c(H_c)
    
    start_time = time.time()
    #eigvals, eigvecs = la.eigh(H_a)
    eigvals, eigvecs = np.linalg.eigh(H_a)
    #print(eigvals)
    end_time = time.time()
    print(f"对角化耗时:{end_time-start_time:.4f}")
    
    positive_eigvals = eigvals[N:]
    W = eigvecs[:N, N:]
    V = eigvecs[N:, N:]
    
    GS_energy = -np.sum(positive_eigvals) / 2
    print(f"GS_energy: {GS_energy}")
    manager.save_data('positive_eigvals_u', positive_eigvals, N1, N2, bc1, bc2, **params)
    manager.save_data('W_u', W, N1, N2, bc1, bc2, **params)
    manager.save_data('V_u', V, N1, N2, bc1, bc2, **params)
    

if __name__ == "__main__":
    main()


