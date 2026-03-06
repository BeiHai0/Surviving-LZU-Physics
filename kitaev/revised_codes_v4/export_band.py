# -*- coding: utf-8 -*-
from kitaev_data_manager import KitaevDataManager
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import time

def k_path(points, total_interval_number):
    points = np.array(points)
    # 1. 计算每一段的物理长度
    diffs = np.diff(points, axis=0)
    seg_lengths = np.linalg.norm(diffs, axis=1)
    total_length = np.sum(seg_lengths)
    
    # 2. 计算目标步长 (总长度 / 总间隔数)
    target_step = total_length / (total_interval_number)
    
    k_list = []
    k_dist = []
    node_indices = []
    current_cumulative_dist = 0.0

    for i in range(len(diffs)):
        # 记录当前段起点（高对称点）的索引
        node_indices.append(len(k_list))
        
        # 计算这一段应该分多少个间隔（取整）
        # 这样能保证这一段的步长最接近 target_step
        n_seg_intervals = max(1, int(round(seg_lengths[i] / target_step)))
        
        # 生成这一段的点（包含起点，不含终点，避免重复）
        seg = np.linspace(points[i], points[i+1], n_seg_intervals, endpoint=False)
        dists = np.linspace(current_cumulative_dist, 
                            current_cumulative_dist + seg_lengths[i], 
                            n_seg_intervals, endpoint=False)
        
        k_list.extend(seg)
        k_dist.extend(dists)
        current_cumulative_dist += seg_lengths[i]

    # 3. 循环结束后，手动补上整条路径的最后一个点
    node_indices.append(len(k_list))
    k_list.append(points[-1])
    k_dist.append(current_cumulative_dist)

    return np.array(k_list), np.array(k_dist), node_indices

manager = KitaevDataManager() # 不传参，默认 root 为 kitaev_data
N1, N2, bc1, bc2 = 20, 20, -1, -1
N = N1 * N2

Gamma = np.array([0.0, 0.0])
K = np.array([4*np.pi/3, 0.0])
M = np.array([np.pi, np.pi/np.sqrt(3)])

points = [Gamma, K, M, Gamma]
total_interval_number = 100

k_list, k_dist, node_idx = k_path(points, total_interval_number)

a1 = np.array([1.0, 0.0])
a2 = np.array([0.5, np.sqrt(3)/2])

k_number = k_list.shape[0]
phase1 = np.exp(-1j * np.dot(k_list, a1))
phase2 = np.exp(1j * np.dot(k_list, a1 - a2))
phase3 = np.exp(1j * np.dot(k_list, a2))

for Kx, Ky, Kz in [(1, 1, 1), (-1, -1, -1)]:
    for kappa in np.linspace(0, 0, 1):
        params = {'Kx':Kx, 'Ky':Ky, 'Kz':Kz, 'kappa':kappa}
        T_A_xy = manager.load_data('T_A_xy', N1, N2, bc1, bc2, **params)
        T_A_yz = manager.load_data('T_A_yz', N1, N2, bc1, bc2, **params)
        T_A_zx = manager.load_data('T_A_zx', N1, N2, bc1, bc2, **params)
        T_B_xy = manager.load_data('T_B_xy', N1, N2, bc1, bc2, **params)
        T_B_yz = manager.load_data('T_B_yz', N1, N2, bc1, bc2, **params)
        T_B_zx = manager.load_data('T_B_zx', N1, N2, bc1, bc2, **params)
        
        positive_eigvals_list = []
        GS_energy_list = []
        
        for i in [0, 1, 2, 3]:
            positive_eigvals = manager.load_data(f'positive_eigvals_u_{i}', N1, N2, bc1, bc2, **params)
            positive_eigvals_list.append(positive_eigvals)
            
            GS_energy = -np.sum(positive_eigvals) / 2
            GS_energy_list.append(GS_energy)
        print(params)
        print(GS_energy_list)
        print(GS_energy_list-GS_energy_list[0])
        Ex = np.diag(GS_energy_list[1] - GS_energy_list[0] + positive_eigvals_list[1])
        Ey = np.diag(GS_energy_list[2] - GS_energy_list[0] + positive_eigvals_list[2])
        Ez = np.diag(GS_energy_list[3] - GS_energy_list[0] + positive_eigvals_list[3])
        
        H_stack = np.zeros((k_number, 3*N, 3*N), dtype=complex)

        H_stack[:, 0:N, 0:N] = Ex
        H_stack[:, N:2*N, N:2*N] = Ey
        H_stack[:, 2*N:3*N, 2*N:3*N] = Ez
        
        for hx, hy, hz in [(v,v,v) for v in np.linspace(0, 0.5, 6)]:
            start_time = time.time()
            H12 = hz * (T_A_xy + phase1[:, None, None] * T_B_xy)
            H_stack[:, 0:N, N:2*N] = H12
            H_stack[:, N:2*N, 0:N] = np.swapaxes(np.conj(H12), 1, 2)
    
            H23 = hx * (T_A_yz + phase2[:, None, None] * T_B_yz)
            H_stack[:, N:2*N, 2*N:3*N] = H23
            H_stack[:, 2*N:3*N, N:2*N] = np.swapaxes(np.conj(H23), 1, 2)
    
            H31 = hy * (T_A_zx + phase3[:, None, None] * T_B_zx)
            H_stack[:, 2*N:3*N, 0:N] = H31
            H_stack[:, 0:N, 2*N:3*N] = np.swapaxes(np.conj(H31), 1, 2)
            
            params2 = {'Kx':Kx, 'Ky':Ky, 'Kz':Kz, 'kappa':kappa, 'hx':hx, 'hy':hy, 'hz':hz}
            energies = np.linalg.eigvalsh(H_stack)
            manager.save_data('k_space_energy', energies, N1, N2, bc1, bc2, **params2)
            
            labels = [r'$\Gamma$', 'K', 'M', r'$\Gamma$']
    
            plt.figure(figsize=(8, 6), dpi=100)

            # 1. 绘制所有能带
            # energies 的形状是 (k_number, 3*N)，直接 plot 会按列画出 3N 条线
            print(energies)
            plt.plot(k_dist, energies[:, :20], color='black', alpha=0.6)

            # 2. 绘制高对称点垂直线
            for idx in node_idx:
                plt.axvline(k_dist[idx], color='black', linestyle='-', lw=0.8, alpha=0.6)

            # 3. 设置横轴刻度
            plt.xticks(k_dist[node_idx], labels, fontsize=12)
            plt.xlim(k_dist[0], k_dist[-1])

            # 4. 其它细节美化
            plt.ylabel('Energy', fontsize=12)
            plt.title(f'N1=N2={N1}, bc1=bc2={bc1}, Kx=Ky=Kz={Kx}, kappa={kappa:.3f}, hx=hy=hz={hx:.3f}', fontsize=14)
            plt.grid(axis='y', alpha=0.3, linestyle=':')

            plt.tight_layout()
            save_dir = Path("kitaev_data") / f"N1_{N1}_N2_{N2}_bc1_{bc1}_bc2_{bc2}" / "band"
            save_dir.mkdir(parents=True, exist_ok=True)
            filename = save_dir / f"band_N1={N1}, N2={N2}, bc1={bc1}, bc2={bc2}, Kx=Ky=Kz={Kx}, kappa={kappa:.3f}, hx=hy=hz={hx:.3f}.png"
            plt.savefig(filename)
            plt.show()
            # plt.close()
            end_time = time.time() 
            print(f"能带计算耗时: {end_time - start_time:.6f} 秒")
            
            del H12, H23, H31
            del energies
            
        del T_A_xy, T_A_yz, T_A_zx, T_B_xy, T_B_yz, T_B_zx, Ex, Ey, Ez, H_stack













