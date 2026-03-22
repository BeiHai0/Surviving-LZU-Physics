# -*- coding: utf-8 -*-
from kitaev_data_manager import KitaevDataManager
import numpy as np
import time
import matplotlib.pyplot as plt

manager = KitaevDataManager()

# ===== 系统参数 =====
N1, N2, bc1, bc2 = 20, 20, -1, -1
N = N1 * N2

# ===== 高对称点 =====
Gamma = np.array([0.0, 0.0])
K = np.array([4*np.pi/3, 0.0])

a1 = np.array([1.0, 0.0])
a2 = np.array([0.5, np.sqrt(3)/2])

# ===== 数值参数 =====
tol = 1e-7
max_iter = 50

plt.figure()
plt.xlabel(r'$\kappa$')
plt.ylabel(r'$h_c$')
plt.title(r'$h_c$ vs. $\kappa$')
plt.grid()

for Kx, Ky, Kz in [(-1,-1,-1)]:
    key = f"K={Kx}"
    kappa_list = []
    h_c_list = []
    
    for kappa in np.linspace(0, 0.1, 6):
        kappa_list.append(kappa)
        

        params = {'Kx':Kx, 'Ky':Ky, 'Kz':Kz, 'kappa':kappa}
        print("\n====", params, "====")

        # ===== load 数据 =====
        T_A_xy = manager.load_data('T_A_xy', N1, N2, bc1, bc2, **params)
        T_A_yz = manager.load_data('T_A_yz', N1, N2, bc1, bc2, **params)
        T_A_zx = manager.load_data('T_A_zx', N1, N2, bc1, bc2, **params)
        T_B_xy = manager.load_data('T_B_xy', N1, N2, bc1, bc2, **params)
        T_B_yz = manager.load_data('T_B_yz', N1, N2, bc1, bc2, **params)
        T_B_zx = manager.load_data('T_B_zx', N1, N2, bc1, bc2, **params)

        # ===== GS energy =====
        positive_eigvals_list = []
        GS_energy_list = []

        for i in [0,1,2,3]:
            positive_eigvals = manager.load_data(
                f'positive_eigvals_u_{i}', N1, N2, bc1, bc2, **params)
            positive_eigvals_list.append(positive_eigvals)
            GS_energy_list.append(-np.sum(positive_eigvals)/2)

        Ex_val = GS_energy_list[1] - GS_energy_list[0] + positive_eigvals_list[1]
        Ey_val = GS_energy_list[2] - GS_energy_list[0] + positive_eigvals_list[2]
        Ez_val = GS_energy_list[3] - GS_energy_list[0] + positive_eigvals_list[3]

        # ===== H_base =====
        H_base = np.zeros((3*N, 3*N), dtype=complex)
        H_base[range(0,N), range(0,N)] = Ex_val
        H_base[range(N,2*N), range(N,2*N)] = Ey_val
        H_base[range(2*N,3*N), range(2*N,3*N)] = Ez_val

        # ===== 固定 k 点 =====
        if Kx == 1:
            k = Gamma
            print("Using Gamma point")
        elif Kx == -1:
            k = K
            print("Using K point")

        p1 = np.exp(-1j * np.dot(k, a1))
        p2 = np.exp(1j * np.dot(k, a1 - a2))
        p3 = np.exp(1j * np.dot(k, a2))

        start_time = time.time()

        # ===== Step 1: 粗扫 =====
        h_scan = np.linspace(0, 0.5, 6)
        gap_vals = []

        for h in h_scan:
            hx = hy = hz = h

            H = H_base.copy()

            # XY
            H12 = hz * (T_A_xy + p1 * T_B_xy)
            H[0:N, N:2*N] = H12
            H[N:2*N, 0:N] = H12.T.conj()

            # YZ
            H23 = hx * (T_A_yz + p2 * T_B_yz)
            H[N:2*N, 2*N:3*N] = H23
            H[2*N:3*N, N:2*N] = H23.T.conj()

            # ZX
            H31 = hy * (T_A_zx + p3 * T_B_zx)
            H[2*N:3*N, 0:N] = H31
            H[0:N, 2*N:3*N] = H31.T.conj()

            eigvals = np.linalg.eigvalsh(H)
            gap_vals.append(eigvals[0])

        # ===== 找符号变化 =====
        h_low, h_high = None, None
        gap_low, gap_high = None, None

        for i in range(len(h_scan)-1):
            if gap_vals[i] * gap_vals[i+1] < 0:
                h_low = h_scan[i]
                h_high = h_scan[i+1]
                gap_low = gap_vals[i]
                gap_high = gap_vals[i+1]
                break

        if h_low is None:
            print("未找到 gap closing（建议扩大粗扫 h 范围）")
            continue

        # ===== Step 2: 二分法 =====
        for _ in range(max_iter):
            h_mid = 0.5 * (h_low + h_high)
            hx = hy = hz = h_mid

            H = H_base.copy()

            # XY
            H12 = hz * (T_A_xy + p1 * T_B_xy)
            H[0:N, N:2*N] = H12
            H[N:2*N, 0:N] = H12.T.conj()

            # YZ
            H23 = hx * (T_A_yz + p2 * T_B_yz)
            H[N:2*N, 2*N:3*N] = H23
            H[2*N:3*N, N:2*N] = H23.T.conj()

            # ZX
            H31 = hy * (T_A_zx + p3 * T_B_zx)
            H[2*N:3*N, 0:N] = H31
            H[0:N, 2*N:3*N] = H31.T.conj()

            eigvals = np.linalg.eigvalsh(H)
            gap_mid = eigvals[0]

            if abs(gap_mid) < tol and gap_mid > 0:
                break

            if gap_low * gap_mid < 0:
                h_high = h_mid
                gap_high = gap_mid
            else:
                h_low = h_mid
                gap_low = gap_mid

        h_c = 0.5 * (h_low + h_high)
        h_c_list.append(h_c)
        print(f"critical h = {h_c:.7f}")

        # ===== Step 3: 求本征向量 =====
        hx = hy = hz = h_c

        H = H_base.copy()

        H12 = hz * (T_A_xy + p1 * T_B_xy)
        H[0:N, N:2*N] = H12
        H[N:2*N, 0:N] = H12.T.conj()

        H23 = hx * (T_A_yz + p2 * T_B_yz)
        H[N:2*N, 2*N:3*N] = H23
        H[2*N:3*N, N:2*N] = H23.T.conj()

        H31 = hy * (T_A_zx + p3 * T_B_zx)
        H[2*N:3*N, 0:N] = H31
        H[0:N, 2*N:3*N] = H31.T.conj()

        eigvals, eigvecs = np.linalg.eigh(H)
        critical_vec = eigvecs[:, 0]

        params2 = {**params, 'h': h_c}

        manager.save_data('gap_closing_h', h_c, N1, N2, bc1, bc2, **params2)
        manager.save_data('gap_closing_vec', critical_vec, N1, N2, bc1, bc2, **params2)

        end_time = time.time()
        print(f"耗时: {end_time - start_time:.3f} 秒")
        print(critical_vec[0:5])
        print(critical_vec[N:N+5])
        print(critical_vec[2*N:2*N+5])

        # ===== 清理 =====
        del T_A_xy, T_A_yz, T_A_zx
        del T_B_xy, T_B_yz, T_B_zx
        del H_base
        
    plt.plot(kappa_list, h_c_list, 'o', label=key)
    plt.legend()
    plt.pause(0.01)

plt.show()

print("\n🎉 all done")