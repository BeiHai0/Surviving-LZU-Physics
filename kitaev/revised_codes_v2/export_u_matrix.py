# -*- coding: utf-8 -*-
from kitaev_data_manager import KitaevDataManager
from scipy import sparse

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

manager = KitaevDataManager() # 不传参，默认 root 为 kitaev_data
N1, N2, bc1, bc2 = 10, 10, -1, -1
n1, n2 = N1//2, N2//2
params = {'n1': n1, 'n2': n2}

u_std = build_standard_zero_flux_u_matrix(N1, N2, bc1, bc2)
u_vison_pair_x = build_vison_pair_added_u_matrix(u_std, n1, n2, 1, N1, N2, bc1, bc2)
u_vison_pair_y = build_vison_pair_added_u_matrix(u_std, n1, n2, 2, N1, N2, bc1, bc2)
u_vison_pair_z = build_vison_pair_added_u_matrix(u_std, n1, n2, 3, N1, N2, bc1, bc2)

manager.save_data("u_std", u_std, N1, N2, bc1, bc2)
manager.save_data("u_vison_pair_x", u_vison_pair_x, N1, N2, bc1, bc2, **params)
manager.save_data("u_vison_pair_y", u_vison_pair_y, N1, N2, bc1, bc2, **params)
manager.save_data("u_vison_pair_z", u_vison_pair_z, N1, N2, bc1, bc2, **params)
