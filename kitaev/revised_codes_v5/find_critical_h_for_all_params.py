# -*- coding: utf-8 -*-
from kitaev_data_manager import KitaevDataManager
import numpy as np
import scipy.linalg as la
import time
import gc

def build_H_k(hx, hy, hz, N, Ex_val, Ey_val, Ez_val, XY_base, YZ_base, ZX_base): # base 不含磁场
    H = np.zeros((3*N, 3*N), dtype=complex)
    # 对角块
    H[range(N), range(N)] = Ex_val
    H[range(N, 2*N), range(N, 2*N)] = Ey_val
    H[range(2*N, 3*N), range(2*N, 3*N)] = Ez_val
    # 非对角块
    H[:N, N:2*N] = hz * XY_base
    H[N:2*N, :N] = hz * XY_base.T.conj()
    H[N:2*N, 2*N:3*N] = hx * YZ_base
    H[2*N:3*N, N:2*N] = hx * YZ_base.T.conj()
    H[2*N:3*N, :N] = hy * ZX_base
    H[:N, 2*N:3*N] = hy * ZX_base.T.conj()
    return H

def main():
    manager = KitaevDataManager()
    N1, N2, bc1, bc2 = 20, 20, -1, -1
    N = N1 * N2
    # 晶格矢量
    a1 = np.array([1.0, 0.0])
    a2 = np.array([0.5, np.sqrt(3)/2])
    
    # 动量空间高对称点
    Gamma = np.array([0.0, 0.0])
    K = np.array([4*np.pi/3, 0.0])
    
    tol = 1e-4 # 允许的误差
    max_iter = 50 # 最大迭代次数
    
    for Kx, Ky, Kz in [(1,1,1), (-1,-1,-1)]:
        for kappa in [0.0, 0.02, 0.04, 0.06]:
            params_1 = {'Kx': Kx, 'Ky': Ky, 'Kz': Kz, 'kappa': kappa}
            T_A_xy = manager.load_data("T_A_1_2", N1, N2, bc1, bc2, **params_1)
            T_A_yz = manager.load_data("T_A_2_3", N1, N2, bc1, bc2, **params_1)
            T_A_zx = manager.load_data("T_A_3_1", N1, N2, bc1, bc2, **params_1)
            T_B_xy = manager.load_data("T_B_1_2", N1, N2, bc1, bc2, **params_1)
            T_B_yz = manager.load_data("T_B_2_3", N1, N2, bc1, bc2, **params_1)
            T_B_zx = manager.load_data("T_B_3_1", N1, N2, bc1, bc2, **params_1)
            
            positive_eigvals_list = []
            GS_energy_list = []
            
            for bond in [0, 1, 2, 3]:
                params_2 = {'bond': bond, 'Kx': Kx, 'Ky': Ky, 'Kz': Kz, 'kappa': kappa}
                positive_eigvals = manager.load_data('positive_eigvals_u', N1, N2, bc1, bc2, **params_2)
                GS_energy = -np.sum(positive_eigvals) / 2.0
                
                positive_eigvals_list.append(positive_eigvals)
                GS_energy_list.append(GS_energy)
            
            Ex_val = GS_energy_list[1] - GS_energy_list[0] + positive_eigvals_list[1]
            Ey_val = GS_energy_list[2] - GS_energy_list[0] + positive_eigvals_list[2]
            Ez_val = GS_energy_list[3] - GS_energy_list[0] + positive_eigvals_list[3]
            
            if Kx == 1:
                k = Gamma
                print("Using Gamma point")
            elif Kx == -1:
                k = K
                print("Using K point")
            
            phase_xy = np.exp(-1j * np.dot(k, a1))
            phase_yz = np.exp(1j * np.dot(k, a1 - a2))
            phase_zx = np.exp(1j * np.dot(k, a2))
            
            XY_base = T_A_xy + phase_xy * T_B_xy
            YZ_base = T_A_yz + phase_yz * T_B_yz
            ZX_base = T_A_zx + phase_zx * T_B_zx
            
            del T_A_xy, T_A_yz, T_A_zx, T_B_xy, T_B_yz, T_B_zx
            gc.collect()
            
            # 粗扫磁场
            h_scan = np.linspace(0, 0.5, 6)
            gap_vals = []
            start_time = time.time()
            for h in h_scan:
                hx = hy = hz = h
                H_k = build_H_k(hx, hy, hz, N, Ex_val, Ey_val, Ez_val, XY_base, YZ_base, ZX_base)
                gap = la.eigh(H_k, subset_by_index=[0,0], eigvals_only=True)[0]
                
                gap_vals.append(gap)
                if gap < 0:
                    break
            end_time = time.time()
            print(f"粗扫磁场用时:{end_time-start_time:.4f}")
            # 找符号变化
            h_low, h_high = None, None
            gap_low, gap_high = None, None

            for i in range(len(gap_vals)-1):
                if gap_vals[i] * gap_vals[i+1] < 0:
                    h_low = h_scan[i]
                    h_high = h_scan[i+1]
                    gap_low = gap_vals[i]
                    gap_high = gap_vals[i+1]
                    break

            if h_low is None:
                print("未找到 gap closing（建议扩大粗扫 h 范围）")
            
            # 二分法找临界磁场
            start_time = time.time()
            for _ in range(max_iter):
                h_mid = 0.5 * (h_low + h_high)
                hx = hy = hz = h_mid
                H_k = build_H_k(hx, hy, hz, N, Ex_val, Ey_val, Ez_val, XY_base, YZ_base, ZX_base)
                
                gap_mid = la.eigh(H_k, subset_by_index=[0,0], eigvals_only=True)[0]
                
                if gap_mid < 0:
                    h_high = h_mid
                    gap_high = gap_mid
                else:
                    h_low = h_mid
                    gap_low = gap_mid
                
                if abs(h_high - h_low) < tol:
                    break
            
            h_c = 0.5 * (h_low + h_high)
            print(f"参数:K:{Kx}, kappa:{kappa}")
            print(f"h_c:{h_c:.4f}")
            end_time = time.time()
            print(f"求解临界磁场用时:{end_time-start_time:.4f}")
            
            start_time = time.time()
            H_k_c = build_H_k(h_c, h_c, h_c, N, Ex_val, Ey_val, Ez_val, XY_base, YZ_base, ZX_base)
            _, eigvecs = la.eigh(H_k_c, subset_by_index=[0,0])
            critical_vec = eigvecs[:, 0]
            end_time = time.time()
            print(f"求解能量最低本征值的本征向量用时:{end_time-start_time:.4f}")
            manager.save_data("h_c", h_c, N1, N2, bc1, bc2, **params_1)
            manager.save_data("critical_eigvec", critical_vec, N1, N2, bc1, bc2, **params_1) # 计算基态磁序要用
            
if __name__ == "__main__":
    main()
