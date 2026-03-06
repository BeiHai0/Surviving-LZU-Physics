# -*- coding: utf-8 -*-
from kitaev_data_manager import KitaevDataManager
from scipy import sparse
import numpy as np
import time
import gc

def build_standard_zero_flux_u_matrix(N1, N2, bc1, bc2):
    def index(n1, n2):
        return n1 + n2*N1
        
    N = N1*N2
    u = sparse.lil_matrix((N, N)) # 稀疏且便于填充的全零矩阵
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
    u = u.tocsr()
    return u

def build_vison_pair_added_u_matrix(u_std, n1, n2, bond, N1, N2, bc1, bc2):
    u_vison_pair = u_std.tolil()
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
    
    return u_vison_pair.tocsr()

def one_idx_to_two_idx(N1, N2, i):
    n1 = i % N1
    n2 = i // N1
    return n1, n2    

def two_idx_to_one_idx(N1, N2, n1, n2):
    return n1 + n2 * N1

def build_M_Ka0_matrix(u, N1, N2, bc1, bc2):
    # u 是稀疏矩阵，使用其自带的 .diagonal() 方法
    u_diag = u.diagonal()
    # 直接用对角数组构造稀疏对角阵，效率最高
    M_Ka0 = sparse.diags(u_diag).tocsr()
    return M_Ka0

def build_M_Ka1_matrix(u, N1, N2, bc1, bc2):
    N = N1 * N2
    # 使用 lil_matrix 方便逐点赋值，最后转为 csr
    M_Ka1 = sparse.lil_matrix((N, N))
    for i in range(N):
        i_n1, i_n2 = one_idx_to_two_idx(N1, N2, i)
        j_n1 = (i_n1 + 1) % N1
        j_n2 = i_n2
        j = two_idx_to_one_idx(N1, N2, j_n1, j_n2)
        
        # 稀疏矩阵索引获取值需要注意性能，但在 N=100 左右没问题
        M_Ka1[i, j] = u[i, j]
    
    return M_Ka1.tocsr()

def build_M_Ka2_matrix(u, N1, N2, bc1, bc2):
    N = N1 * N2
    M_Ka2 = sparse.lil_matrix((N, N))
    for i in range(N):
        i_n1, i_n2 = one_idx_to_two_idx(N1, N2, i)
        j_n1 = i_n1
        j_n2 = (i_n2 + 1) % N2
        j = two_idx_to_one_idx(N1, N2, j_n1, j_n2)
        
        M_Ka2[i, j] = u[i, j]
    
    return M_Ka2.tocsr()

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
    I = sparse.eye(N, dtype=np.complex128)
    T_ca = sparse.bmat([
        [I, I],
        [-1j*I, 1j*I]
    ])
    # print(T_ca)
    T_ca_dag = T_ca.conj().T
    Ha = 1j * (T_ca_dag @ Hc @ T_ca)
    # Ha = 0.5 * (Ha + Ha.conj().T)
    return Ha

def diagonalize_BdG_matrix(H_BdG_sparse):
    total_dim = H_BdG_sparse.shape[0]
    N = total_dim // 2
    H_BdG_dense = H_BdG_sparse.toarray()
    eigvals, eigvecs = np.linalg.eigh(H_BdG_dense)
    del H_BdG_dense
    eigvals_positive = eigvals[N:]
    # print(eigvals)
    eigvecs_positive = eigvecs[:, N:]
    del eigvals, eigvecs
    W = eigvecs_positive[:N, :]
    V = eigvecs_positive[N:, :]
    # print(W)
    
    print("对角化完成！")
    # U = np.block([[W, V.conj()], [V, W.conj()]])
    # error = np.linalg.norm(U @ U.conj().T - np.eye(2*N))
    # print(f"酉矩阵误差: {error}")
    return eigvals_positive, W, V

manager = KitaevDataManager() # 不传参，默认 root 为 kitaev_data
N1, N2, bc1, bc2 = 20, 20, -1, -1
n1, n2 = N1//2, N2//2

u_std = build_standard_zero_flux_u_matrix(N1, N2, bc1, bc2)
u_vison_pair_x = build_vison_pair_added_u_matrix(u_std, n1, n2, 1, N1, N2, bc1, bc2)
u_vison_pair_y = build_vison_pair_added_u_matrix(u_std, n1, n2, 2, N1, N2, bc1, bc2)
u_vison_pair_z = build_vison_pair_added_u_matrix(u_std, n1, n2, 3, N1, N2, bc1, bc2)

u_list = [u_std, u_vison_pair_x, u_vison_pair_y, u_vison_pair_z]

for i in [0, 1, 2, 3]:
    for Kx, Ky, Kz in [(1, 1, 1), (-1, -1, -1)]:
        for kappa in np.linspace(0, 0, 1):
            u = u_list[i]
            M_Ka0 = build_M_Ka0_matrix(u, N1, N2, bc1, bc2)
            M_Ka1 = build_M_Ka1_matrix(u, N1, N2, bc1, bc2)
            M_Ka2 = build_M_Ka2_matrix(u, N1, N2, bc1, bc2)
            M_kappaA = build_M_kappaA_matrix(M_Ka0, M_Ka1, M_Ka2)
            M_kappaB = build_M_kappaB_matrix(M_Ka0, M_Ka1, M_Ka2)
            M_kappaAB = build_M_kappaAB_matrix(M_kappaA, M_kappaB)        
            
            params = {'Kx': Kx, 'Ky': Ky, 'Kz': Kz, 'kappa': kappa}
            print(params)
            
            H_K_plus_H_kappa_c_matrix = build_H_K_plus_H_kappa_c_matrix(M_Ka0, M_Ka1, M_Ka2, M_kappaAB, **params)
            H_K_plus_H_kappa_a_matrix = build_Ha_from_Hc(H_K_plus_H_kappa_c_matrix)
            # print(H_K_plus_H_kappa_a_matrix)
            start_time = time.time()
            positive_eigvals, W, V = diagonalize_BdG_matrix(H_K_plus_H_kappa_a_matrix)
            end_time = time.time()
            print(f"对角化执行耗时: {end_time - start_time:.6f} 秒")
            
            GS_energy = -np.sum(positive_eigvals) / 2
            print(f"GS_energy:{GS_energy}")       
            print(f"positive_eigvals_u_{i}\n{positive_eigvals[:10]}")
            manager.save_data(f'positive_eigvals_u_{i}', positive_eigvals, N1, N2, bc1, bc2, **params)
            manager.save_data(f'W_u_{i}', W, N1, N2, bc1, bc2, **params)
            manager.save_data(f'V_u_{i}', V, N1, N2, bc1, bc2, **params)
            
            del M_Ka0, M_Ka1, M_Ka2, M_kappaA, M_kappaB, M_kappaAB
            del H_K_plus_H_kappa_c_matrix, H_K_plus_H_kappa_a_matrix
            gc.collect()            
            
print("all done")   