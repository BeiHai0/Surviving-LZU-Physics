# -*- coding: utf-8 -*-
from kitaev_data_manager import KitaevDataManager
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

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
N1, N2, bc1, bc2 = 10, 10, -1, -1
N = N1 * N2

params = {'Kx': 1, 'Ky': 1, 'Kz': 1, 'kappa': 0.0}

T_suffixes = ['Axy', 'Ayz', 'Azx', 'Bxy', 'Byz', 'Bzx']
T = {}

for s in T_suffixes:
    T[s] = manager.load_data(f'T_{s}', N1, N2, bc1, bc2, **params)

vison_pair_suffixes = ['std', 'vison_pair_x', 'vison_pair_y', 'vison_pair_z']
positive_sorted_eigvals = {}
GS_energy = {}

for s in vison_pair_suffixes:
    positive_sorted_eigvals[s] = manager.load_data(f'eigvals_positive_{s}', N1, N2, bc1, bc2, **params)
    GS_energy[s] = -np.sum(positive_sorted_eigvals[s]) / 2

Ex = np.diag(GS_energy['vison_pair_x'] - GS_energy['std'] + positive_sorted_eigvals['vison_pair_x'])
Ey = np.diag(GS_energy['vison_pair_y'] - GS_energy['std'] + positive_sorted_eigvals['vison_pair_y'])
Ez = np.diag(GS_energy['vison_pair_z'] - GS_energy['std'] + positive_sorted_eigvals['vison_pair_z'])

Gamma = np.array([0.0, 0.0])
K = np.array([4*np.pi/3, 0.0])
M = np.array([np.pi, np.pi/np.sqrt(3)])

points = [Gamma, K, M, Gamma]
total_interval_number = 100

k_list, k_dist, node_idx = k_path(points, total_interval_number)

a1 = np.array([1.0, 0.0])
a2 = np.array([0.5, np.sqrt(3)/2])

hx, hy, hz = 0.1, 0.1, 0.1

k_number = k_list.shape[0]

phase1 = np.exp(-1j * np.dot(k_list, a1))
phase2 = np.exp(1j * np.dot(k_list, a1 - a2))
phase3 = np.exp(1j * np.dot(k_list, a2))

H_stack = np.zeros((k_number, 3*N, 3*N), dtype=complex)

H_stack[:, 0:N, 0:N] = Ex
H_stack[:, N:2*N, N:2*N] = Ey
H_stack[:, 2*N:3*N, 2*N:3*N] = Ez

H12 = hz * (T['Axy'] + phase1[:, None, None] * T['Bxy'])
H_stack[:, 0:N, N:2*N] = H12
H_stack[:, N:2*N, 0:N] = np.swapaxes(np.conj(H12), 1, 2)

H23 = hx * (T['Ayz'] + phase2[:, None, None] * T['Byz'])
H_stack[:, N:2*N, 2*N:3*N] = H23
H_stack[:, 2*N:3*N, N:2*N] = np.swapaxes(np.conj(H23), 1, 2)

H31 = hy * (T['Azx'] + phase3[:, None, None] * T['Bzx'])
H_stack[:, 2*N:3*N, 0:N] = H31
H_stack[:, 0:N, 2*N:3*N] = np.swapaxes(np.conj(H31), 1, 2)

energies = np.linalg.eigvalsh(H_stack)

labels = [r'$\Gamma$', 'K', 'M', r'$\Gamma$']

plt.figure(figsize=(8, 6), dpi=100)

# 1. 绘制所有能带
# energies 的形状是 (k_number, 3*N)，直接 plot 会按列画出 3N 条线
plt.plot(k_dist, energies[:, :4], color='blue', alpha=0.6)

# 2. 绘制高对称点垂直线
for idx in node_idx:
    plt.axvline(k_dist[idx], color='black', linestyle='-', lw=0.8, alpha=0.6)

# 3. 设置横轴刻度
plt.xticks(k_dist[node_idx], labels, fontsize=12)
plt.xlim(k_dist[0], k_dist[-1])

# 4. 其它细节美化
plt.ylabel('Energy', fontsize=12)
plt.title(f'Band Structure (N1={N1}, N2={N2}, $\kappa$={params["kappa"]})', fontsize=14)
plt.grid(axis='y', alpha=0.3, linestyle=':')

# 如果有费米能级可以标出（假设为0）
plt.axhline(0, color='gray', linestyle='--', lw=0.8)

plt.tight_layout()
plt.show()


