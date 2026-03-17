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
N1, N2, bc1, bc2 = 50, 50, -1, -1
N = N1 * N2

Gamma = np.array([0.0, 0.0])
K = np.array([4*np.pi/3, 0.0])
M = np.array([np.pi, np.pi/np.sqrt(3)])

points = [Gamma, K, M, Gamma]
total_interval_number = 50

k_list, k_dist, node_idx = k_path(points, total_interval_number)

a1 = np.array([1.0, 0.0])
a2 = np.array([0.5, np.sqrt(3)/2])

k_number = k_list.shape[0]
phase1 = np.exp(-1j * np.dot(k_list, a1))
phase2 = np.exp(1j * np.dot(k_list, a1 - a2))
phase3 = np.exp(1j * np.dot(k_list, a2))

for Kx, Ky, Kz in [(1, 1, 1),(-1, -1, -1)]:
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
        #print(GS_energy_list)
        #print(GS_energy_list-GS_energy_list[0])
        
        # 优化点1：预先计算对角块的值
        Ex_val = GS_energy_list[1] - GS_energy_list[0] + positive_eigvals_list[1]
        Ey_val = GS_energy_list[2] - GS_energy_list[0] + positive_eigvals_list[2]
        Ez_val = GS_energy_list[3] - GS_energy_list[0] + positive_eigvals_list[3]
        
        # 优化点2：构造一个基础的对角矩阵模版，避免在k循环中重复调用np.diag
        H_base = np.zeros((3*N, 3*N), dtype=complex)
        H_base[range(0, N), range(0, N)] = Ex_val
        H_base[range(N, 2*N), range(N, 2*N)] = Ey_val
        H_base[range(2*N, 3*N), range(2*N, 3*N)] = Ez_val
        
        for hx, hy, hz in [(v,v,v) for v in np.linspace(0.3, 0.5, 3)]:
            start_time = time.time()
            
            energies = np.zeros((k_number, 3*N))
            
            # 核心优化循环
            for idx in range(k_number):
                # 优化点3：使用 copy() 快速获取基础对角阵，而不是从零开始填充
                H_curr = H_base.copy()
                
                # 优化点4：减少冗余乘法，直接填充非对角块
                # 利用 T_A_xy + p * T_B_xy 的线性性质
                p1, p2, p3 = phase1[idx], phase2[idx], phase3[idx]
                
                # XY 块
                H12 = hz * (T_A_xy + p1 * T_B_xy)
                H_curr[0:N, N:2*N] = H12
                H_curr[N:2*N, 0:N] = H12.T.conj()
                
                # YZ 块
                H23 = hx * (T_A_yz + p2 * T_B_yz)
                H_curr[N:2*N, 2*N:3*N] = H23
                H_curr[2*N:3*N, N:2*N] = H23.T.conj()
                
                # ZX 块
                H31 = hy * (T_A_zx + p3 * T_B_zx)
                H_curr[2*N:3*N, 0:N] = H31
                H_curr[0:N, 2*N:3*N] = H31.T.conj()
                
                # 计算该 k 点的本征值
                energies[idx, :] = np.linalg.eigvalsh(H_curr)
            
            params2 = {'Kx':Kx, 'Ky':Ky, 'Kz':Kz, 'kappa':kappa, 'hx':hx, 'hy':hy, 'hz':hz}
            manager.save_data('k_space_energy', energies, N1, N2, bc1, bc2, **params2)
            
            labels = [r'$\Gamma$', 'K', 'M', r'$\Gamma$']
    
            plt.figure(figsize=(8, 6), dpi=100)

            # 1. 绘制所有能带
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
            plt.close()
            end_time = time.time() 
            print(f"能带计算耗时: {end_time - start_time:.6f} 秒")
            
            del energies
            
        del T_A_xy, T_A_yz, T_A_zx, T_B_xy, T_B_yz, T_B_zx, Ex_val, Ey_val, Ez_val, H_base


print("all done")