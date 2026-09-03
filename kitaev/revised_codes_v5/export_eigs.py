# -*- coding: utf-8 -*-
from kitaev_data_manager import KitaevDataManager
from scipy import sparse
import numpy as np
import time
import gc

# ===================== 工具函数 =====================
def one_idx_to_two_idx(N1, N2, i):
    return i % N1, i // N1

def two_idx_to_one_idx(N1, N2, n1, n2):
    return n1 + n2 * N1

# ===================== 构建 u 矩阵（优化向量化） =====================
def build_standard_zero_flux_u_matrix(N1, N2, bc1, bc2):
    """完全向量化构建零通量 u 矩阵，避免 Python 循环和 lil_matrix"""
    N = N1 * N2
    rows = []   # 行索引
    cols = []   # 列索引
    data = []   # 数值

    for n2 in range(N2):
        for n1 in range(N1):
            i = n1 + n2 * N1            # 元胞 (n1, n2) 的 A 子格

            # x‑bond: 同一元胞内 A→B，始终为 +1
            rows.append(i)
            cols.append(i)
            data.append(1)

            # y‑bond: A 在 (n1, n2) 连接 B 在 (n1+1, n2)
            jy = ((n1 + 1) % N1) + n2 * N1
            rows.append(i)
            cols.append(jy)
            data.append(bc1 if n1 == N1 - 1 else 1)

            # z‑bond: A 在 (n1, n2) 连接 B 在 (n1, n2+1)
            jz = n1 + ((n2 + 1) % N2) * N1
            rows.append(i)
            cols.append(jz)
            data.append(bc2 if n2 == N2 - 1 else 1)

    u = sparse.coo_matrix((data, (rows, cols)), shape=(N, N)).tocsr()
    return u

def build_vison_pair_added_u_matrix(u_std, n1, n2, bond, N1, N2, bc1, bc2):
    """在指定键上翻转 u 的符号（产生一对 vison）"""
    u = u_std.tolil()          # lil 格式修改单元素最高效
    i = n1 + n2 * N1
    if bond == 1:      # x-bond
        j = n1 + n2 * N1
    elif bond == 2:    # y-bond
        j = ((n1 + 1) % N1) + n2 * N1
    elif bond == 3:    # z-bond
        j = n1 + ((n2 + 1) % N2) * N1
    else:
        raise ValueError("bond must be 1 (x), 2 (y) or 3 (z)")

    u[i, j] = -u[i, j]
    return u.tocsr()

# ===================== 构建 M_Ka 矩阵（向量化） =====================
def build_M_Ka0_matrix(u, N1, N2, bc1, bc2):
    """M_Ka0 直接从 u 的对角线构建，原实现已高效"""
    return sparse.diags(u.diagonal()).tocsr()

def build_M_Ka1_matrix(u, N1, N2, bc1, bc2):
    """
    M_Ka1 抽取 u 中对应于 x 方向键的元素。
    优化：一次性取出所有需要的行列索引和数据，用 COO 直接构造。
    """
    N = N1 * N2
    rows = np.arange(N)
    cols = ((rows % N1 + 1) % N1) + (rows // N1) * N1   # (n1+1)%N1 的向量化
    # u 已经是 CSR 格式，用花式索引一次性提取所有值
    vals = u[rows, cols].A1          # .A1 转换为 1D 数组
    M_Ka1 = sparse.csr_matrix((vals, (rows, cols)), shape=(N, N))
    return M_Ka1

def build_M_Ka2_matrix(u, N1, N2, bc1, bc2):
    """M_Ka2 抽取 u 中对应于 z 方向键的元素，同样向量化"""
    N = N1 * N2
    rows = np.arange(N)
    cols = (rows % N1) + ((rows // N1 + 1) % N2) * N1   # (n2+1)%N2 的向量化
    vals = u[rows, cols].A1
    M_Ka2 = sparse.csr_matrix((vals, (rows, cols)), shape=(N, N))
    return M_Ka2

# ===================== 构建 M_kappa 矩阵 =====================
def build_M_kappaA_matrix(M_Ka0, M_Ka1, M_Ka2):
    pairs = [(M_Ka1, M_Ka2), (M_Ka2, M_Ka0), (M_Ka0, M_Ka1)]
    M = sparse.csr_matrix(M_Ka0.shape)
    for M1, M2 in pairs:
        M += M1 @ M2.T
    return M.tocsr()

def build_M_kappaB_matrix(M_Ka0, M_Ka1, M_Ka2):
    pairs = [(M_Ka1, M_Ka2), (M_Ka2, M_Ka0), (M_Ka0, M_Ka1)]
    M = sparse.csr_matrix(M_Ka0.shape)
    for M1, M2 in pairs:
        M += M1.T @ M2
    return M.tocsr()

def build_M_kappaAB_matrix(M_kappaA, M_kappaB):
    N = M_kappaA.shape[0]
    zero = sparse.csr_matrix((N, N))
    M_kappaAB = sparse.bmat([
        [M_kappaA - M_kappaA.T, zero],
        [zero, M_kappaB - M_kappaB.T],
    ])
    return M_kappaAB.tocsr()

# ===================== 体系哈密顿量 =====================
def build_H_K_plus_H_kappa_c_matrix(M_Ka0, M_Ka1, M_Ka2, M_kappaAB, Kx, Ky, Kz, kappa):
    M_K = Kx * M_Ka0 + Ky * M_Ka1 + Kz * M_Ka2
    H_K_c = sparse.bmat([[None, M_K], [-M_K.T, None]])
    H = H_K_c + kappa * M_kappaAB
    return H.tocsr()



def get_transformation_matrices(N):
    """
    缓存从 c 基到 a 基的变换矩阵及其共轭转置。
    由于 T 只与 N 有关，相同尺寸的系统可复用。
    """
    I = sparse.eye(N, dtype=np.complex128)
    T_ca = sparse.bmat([[I, I], [-1j*I, 1j*I]])
    T_ca_dag = T_ca.conj().T
    return T_ca, T_ca_dag

def build_Ha_from_Hc(Hc, T_ca_dag, T_ca):
    """利用缓存的变换矩阵，避免每次新建大矩阵"""
    Ha = 1j * (T_ca_dag @ Hc @ T_ca)
    return Ha

# ===================== 对角化 =====================
def diagonalize_BdG_matrix(H_BdG_sparse):
    total_dim = H_BdG_sparse.shape[0]
    N = total_dim // 2
    H_dense = H_BdG_sparse.toarray()
    eigvals, eigvecs = np.linalg.eigh(H_dense)
    del H_dense
    eigvals_pos = eigvals[N:]
    eigvecs_pos = eigvecs[:, N:]
    del eigvals, eigvecs
    W = eigvecs_pos[:N, :]
    V = eigvecs_pos[N:, :]
    print("对角化完成！")
    return eigvals_pos, W, V

# ===================== 主程序（重构循环，消除重复计算） =====================
if __name__ == "__main__":
    manager = KitaevDataManager()
    N1, N2, bc1, bc2 = 30, 30, -1, -1
    n1, n2 = N1 // 2, N2 // 2

    # 准备 4 种 u 位形：零通量 + 三对 vison 对
    u_std = build_standard_zero_flux_u_matrix(N1, N2, bc1, bc2)
    u_vison_x = build_vison_pair_added_u_matrix(u_std, n1, n2, 1, N1, N2, bc1, bc2)
    u_vison_y = build_vison_pair_added_u_matrix(u_std, n1, n2, 2, N1, N2, bc1, bc2)
    u_vison_z = build_vison_pair_added_u_matrix(u_std, n1, n2, 3, N1, N2, bc1, bc2)
    u_list = [u_std, u_vison_x, u_vison_y, u_vison_z]

    # 基变换矩阵与 u 无关，只依赖尺寸 N1,N2，提前算好
    N = N1 * N2
    T_ca, T_ca_dag = get_transformation_matrices(N)

    for i, u in enumerate(u_list):
        # ---------- 与 K, kappa 无关的矩阵只计算一次 ----------
        M_Ka0 = build_M_Ka0_matrix(u, N1, N2, bc1, bc2)
        M_Ka1 = build_M_Ka1_matrix(u, N1, N2, bc1, bc2)
        M_Ka2 = build_M_Ka2_matrix(u, N1, N2, bc1, bc2)
        M_kappaA = build_M_kappaA_matrix(M_Ka0, M_Ka1, M_Ka2)
        M_kappaB = build_M_kappaB_matrix(M_Ka0, M_Ka1, M_Ka2)
        M_kappaAB = build_M_kappaAB_matrix(M_kappaA, M_kappaB)

        for Kx, Ky, Kz in [(1, 1, 1), (-1, -1, -1)]:
            for kappa in np.linspace(0, 0.1, 6):
                params = {'Kx': Kx, 'Ky': Ky, 'Kz': Kz, 'kappa': kappa}
                print(params)

                # 直接用已有的矩阵组合 H_c 和 H_a
                Hc = build_H_K_plus_H_kappa_c_matrix(
                    M_Ka0, M_Ka1, M_Ka2, M_kappaAB, Kx, Ky, Kz, kappa
                )
                Ha = build_Ha_from_Hc(Hc, T_ca_dag, T_ca)

                start = time.time()
                pos_ev, W, V = diagonalize_BdG_matrix(Ha)
                print(f"对角化耗时: {time.time() - start:.6f} 秒")

                GS = -np.sum(pos_ev) / 2
                print(f"GS_energy: {GS}")
                print(f"前10个正本征值 u_{i}:\n{pos_ev[:10]}")

                manager.save_data(f'positive_eigvals_u_{i}', pos_ev,
                                  N1, N2, bc1, bc2, **params)
                manager.save_data(f'W_u_{i}', W, N1, N2, bc1, bc2, **params)
                manager.save_data(f'V_u_{i}', V, N1, N2, bc1, bc2, **params)

                del Hc, Ha
                gc.collect()

        # 当前 u 位形结束，释放相应的大型矩阵
        del M_Ka0, M_Ka1, M_Ka2, M_kappaA, M_kappaB, M_kappaAB
        gc.collect()

    print("all done")