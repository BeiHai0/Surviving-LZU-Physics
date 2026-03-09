# -*- coding: utf-8 -*-
import os
import time
from pathlib import Path
import numpy as np
import cupy as cp
import matplotlib.pyplot as plt
from kitaev_data_manager import KitaevDataManager

def k_path(points, total_interval_number):
    points = np.array(points)
    diffs = np.diff(points, axis=0)
    seg_lengths = np.linalg.norm(diffs, axis=1)
    total_length = np.sum(seg_lengths)
    target_step = total_length / total_interval_number

    k_list, k_dist, node_indices = [], [], []
    current_cumulative_dist = 0.0

    for i in range(len(diffs)):
        node_indices.append(len(k_list))
        n_seg_intervals = max(1, int(round(seg_lengths[i] / target_step)))
        seg = np.linspace(points[i], points[i+1], n_seg_intervals, endpoint=False)
        dists = np.linspace(current_cumulative_dist,
                            current_cumulative_dist + seg_lengths[i],
                            n_seg_intervals, endpoint=False)
        k_list.extend(seg)
        k_dist.extend(dists)
        current_cumulative_dist += seg_lengths[i]

    node_indices.append(len(k_list))
    k_list.append(points[-1])
    k_dist.append(current_cumulative_dist)
    return np.array(k_list), np.array(k_dist), node_indices

# --- 显卡选择 ---
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
cp.get_default_memory_pool().free_all_blocks()
manager = KitaevDataManager()

N1, N2, bc1, bc2 = 50, 50, -1, -1
N = N1 * N2

# --- 布里渊区路径 ---
Gamma = np.array([0.0, 0.0])
K = np.array([4*np.pi/3, 0.0])
M = np.array([np.pi, np.pi/np.sqrt(3)])
points = [Gamma, K, M, Gamma]
total_interval_number = 50
k_list, k_dist, node_idx = k_path(points, total_interval_number)

a1 = np.array([1.0, 0.0])
a2 = np.array([0.5, np.sqrt(3)/2])
k_number = k_list.shape[0]

# 几何相位 GPU
phase1_gpu = cp.array(np.exp(-1j * np.dot(k_list, a1)), dtype=cp.complex128)
phase2_gpu = cp.array(np.exp(1j * np.dot(k_list, a1 - a2)), dtype=cp.complex128)
phase3_gpu = cp.array(np.exp(1j * np.dot(k_list, a2)), dtype=cp.complex128)

for Kx, Ky, Kz in [(1, 1, 1)]:
    for kappa in np.linspace(0, 0.2, 3):
        params = {'Kx':Kx, 'Ky':Ky, 'Kz':Kz, 'kappa':kappa}
        # --- T 矩阵搬到 GPU ---
        T_data = {key: cp.array(manager.load_data(key, N1, N2, bc1, bc2, **params), dtype=cp.complex128)
                  for key in ['T_A_xy','T_B_xy','T_A_yz','T_B_yz','T_A_zx','T_B_zx']}

        # 正本征值与基态能量
        pos_list = [manager.load_data(f'positive_eigvals_u_{i}', N1, N2, bc1, bc2, **params) for i in range(4)]
        GS_list = [-np.sum(p)/2 for p in pos_list]

        diag_vals = [cp.array(GS_list[i] - GS_list[0] + pos_list[i], dtype=cp.complex128) for i in [1,2,3]]

        for hx, hy, hz in [(v,v,v) for v in np.linspace(0, 0.5, 6)]:
            start_time = time.time()

            energies_cpu = np.zeros((k_number, 3*N), dtype=np.float64)

            # --- 核心：单 k 点 GPU 对角化 ---
            for idx in range(k_number):
                H_curr = cp.zeros((3*N,3*N), dtype=cp.complex128)
                # 对角块
                H_curr[0:N,0:N] = diag_vals[0]
                H_curr[N:2*N,N:2*N] = diag_vals[1]
                H_curr[2*N:3*N,2*N:3*N] = diag_vals[2]
                # 非对角块
                p1, p2, p3 = phase1_gpu[idx], phase2_gpu[idx], phase3_gpu[idx]
                H_curr[0:N, N:2*N] = hz * (T_data['T_A_xy'] + p1 * T_data['T_B_xy'])
                H_curr[N:2*N, 0:N] = H_curr[0:N, N:2*N].conj().T
                H_curr[N:2*N, 2*N:3*N] = hx * (T_data['T_A_yz'] + p2 * T_data['T_B_yz'])
                H_curr[2*N:3*N, N:2*N] = H_curr[N:2*N, 2*N:3*N].conj().T
                H_curr[2*N:3*N, 0:N] = hy * (T_data['T_A_zx'] + p3 * T_data['T_B_zx'])
                H_curr[0:N, 2*N:3*N] = H_curr[2*N:3*N, 0:N].conj().T

                # 本征值
                energies_cpu[idx,:] = cp.asnumpy(cp.linalg.eigvalsh(H_curr, UPLO='L'))

                del H_curr
                cp.get_default_memory_pool().free_all_blocks()

            # 保存与绘图
            params2 = {'Kx':Kx,'Ky':Ky,'Kz':Kz,'kappa':kappa,'hx':hx,'hy':hy,'hz':hz}
            manager.save_data('k_space_energy', energies_cpu, N1,N2,bc1,bc2,**params2)

            labels = [r'$\Gamma$','K','M',r'$\Gamma$']
            plt.figure(figsize=(8,6), dpi=100)
            plt.plot(k_dist, energies_cpu[:,:20], color='black', alpha=0.6)
            for idx_node in node_idx:
                plt.axvline(k_dist[idx_node], color='black', linestyle='-', lw=0.8, alpha=0.6)
            plt.xticks(k_dist[node_idx], labels, fontsize=12)
            plt.xlim(k_dist[0], k_dist[-1])
            plt.ylabel('Energy', fontsize=12)
            plt.title(f'N1=N2={N1}, bc1=bc2={bc1}, Kx=Ky=Kz={Kx}, kappa={kappa:.3f}, hx=hy=hz={hx:.3f}', fontsize=14)
            plt.grid(axis='y', alpha=0.3, linestyle=':')
            plt.tight_layout()
            save_dir = Path("kitaev_data") / f"N1_{N1}_N2_{N2}_bc1_{bc1}_bc2_{bc2}" / "band"
            save_dir.mkdir(parents=True, exist_ok=True)
            filename = save_dir / f"band_N1={N1},N2={N2},bc1={bc1},bc2={bc2},Kx=Ky=Kz={Kx},kappa={kappa:.3f},hx=hy=hz={hx:.3f}.png"
            plt.savefig(filename)
            plt.close()

            print(f"单 k 点 GPU 耗时: {time.time()-start_time:.4f} 秒")

        del T_data
        cp.get_default_memory_pool().free_all_blocks()

print("all done")