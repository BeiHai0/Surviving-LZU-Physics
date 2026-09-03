# -*- coding: utf-8 -*-

from kitaev_data_manager import KitaevDataManager
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib.patches as mpatches
from matplotlib.ticker import AutoMinorLocator

def k_path(points, total_interval_number):
    points = np.array(points)
    diffs = np.diff(points, axis=0)
    seg_lengths = np.linalg.norm(diffs, axis=1)
    total_length = np.sum(seg_lengths)
    target_step = total_length / (total_interval_number)

    k_list = []
    k_dist = []
    node_indices = []
    current_cumulative_dist = 0.0

    for i in range(len(diffs)):
        node_indices.append(len(k_list))
        n_seg_intervals = max(1, int(round(seg_lengths[i] / target_step)))
        seg = np.linspace(points[i], points[i + 1], n_seg_intervals, endpoint=False)
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

# 处理数据格式

def fmt_h(h, h_c):
    if np.isclose(h, h_c):
        return f"{h:.3f}"
    elif np.isclose(h, 0.):
        return "0"
    else:
        return f"{h:.1f}"
    
def fmt_kappa(kappa):
    if np.isclose(kappa, 0.):
        return "0"
    else:
        return f"{kappa:.2f}"
# =========================
# 参数
# =========================

manager = KitaevDataManager()

N1, N2, bc1, bc2 = 60, 60, -1, -1

K_list = [(1,1,1)]
kappa_list = [0.0, ]
h_step = 0.1

q_interval_number = 300
eta = 0.04
omega_max = 6
omega_number = 601

omega = np.linspace(0, omega_max, omega_number)

b1 = 2 * np.pi * np.array([1, -1 / np.sqrt(3)])
b2 = 2 * np.pi * np.array([0, 2 / np.sqrt(3)])

Gamma = np.array([0.0, 0.0])
K = (2 * b1 + b2) / 3
M_prime = b1 + b2 / 2
Gamma_prime = b1 + b2
K_prime = 2 * np.pi * np.array([1.0 / 3, 1.0 / np.sqrt(3)])
M = b2 / 2

points = [Gamma, K, M_prime, Gamma_prime, K_prime, M, Gamma]

# =========================
# 读取 q_list 和 node_idx
# =========================

# q_list 和 node_idx 对所有参数都是相同的
params_dummy = {'Kx':1, 'Ky':1, 'Kz':1, 'kappa':0.0, 'hx':0.0, 'hy':0.0, 'hz':0.0}
q_list, q_dist, node_idx = k_path(points, q_interval_number)
# q_list = manager.load_data(f'q_list_q_interval_number_{q_interval_number}', N1, N2, bc1, bc2, **params_dummy)
# node_idx = manager.load_data(f'node_idx_q_interval_number_{q_interval_number}', N1, N2, bc1, bc2, **params_dummy)
labels = [r'$\Gamma$', r'$\mathrm{K}$', r'$\mathrm{M}^\prime$', r'$\Gamma^\prime$', r'$\mathrm{K}^\prime$', r'$\mathrm{M}$', r'$\Gamma$']

# =========================
# 循环参数并绘图
# =========================

for Kx, Ky, Kz in K_list:
    for kappa in kappa_list:
        # 先获取临界磁场 h_c
        params_hc = {'Kx':Kx, 'Ky':Ky, 'Kz':Kz, 'kappa':kappa}
        h_c = manager.load_data('h_c', N1, N2, bc1, bc2, **params_hc)

        h_list = np.arange(0.0, h_c, h_step)
        h_list = np.append(h_list, h_c)  # 确保包含 h_c

        for h in h_list:
            hx = hy = hz = h
            params = {'Kx':Kx, 'Ky':Ky, 'Kz':Kz, 'kappa':kappa, 'hx':hx, 'hy':hy, 'hz':hz}

            # =========================
            # 读取数据
            # =========================
            eigvals_all = manager.load_data(f'eigvals_q_interval_number_{q_interval_number}', N1, N2, bc1, bc2, **params)
            weights_all = manager.load_data(f'weights_q_interval_number_{q_interval_number}', N1, N2, bc1, bc2, **params)

            # =========================
            # 重构 S(q, omega)
            # =========================
            num_q = eigvals_all.shape[0]
            S = np.zeros((num_q, len(omega)), dtype=float)
            omega_col = omega[:, None]

            for q_idx in range(num_q):
                eigvals = eigvals_all[q_idx]
                weights = weights_all[q_idx]
                lor = eta / ((omega_col - eigvals[None, :])**2 + eta**2 )
                S[q_idx] = lor @ weights

            # =========================
            # 作图
            # =========================
            min_val = 0.0
            max_val = 4.0
            
            plt.rcParams.update({
                "font.size": 16,
                "font.family": "serif",
                "mathtext.fontset": "cm",
            
                "axes.linewidth": 1.2,
                "xtick.direction": "out",
                "ytick.direction": "out",
                "xtick.major.size": 6,
                "ytick.major.size": 6,
                "ytick.labelsize": 24,
            })
            plt.figure(figsize=(8,6))
            plt.pcolormesh(
                q_dist,
                omega,
                np.log(1 + S.T),
                shading='auto',
                cmap='inferno',
                vmin=min_val,
                vmax=max_val
            )
            plt.colorbar()
            plt.xticks(q_dist[node_idx], labels, fontsize=32)
            ax = plt.gca()
            ax.yaxis.set_minor_locator(AutoMinorLocator(5))
            # plt.tick_params(axis='y', colors='white')
            # for idx in node_idx:
            #     plt.axvline(q_dist[idx], color='k', linestyle='--', linewidth=0.5)
            # plt.xlabel(r'$\boldsymbol{q}$-path')
            plt.ylabel(r'$\omega$', fontsize=32)
            # plt.title(
            #     r'$S(\omega,\boldsymbol{q})$'
            # )
            info = mpatches.Patch(
                color='none',
                label=rf'$(K,\kappa,h)=({Kx},{fmt_kappa(kappa)},{fmt_h(h,h_c)})$'
            )
            
            plt.legend(handles=[info], loc='upper right', frameon=False, labelcolor='white', fontsize=24)
            plt.tight_layout()
            save_dir = (
                Path("kitaev_data")
                / f"N1_{N1}_N2_{N2}_bc1_{bc1}_bc2_{bc2}"
                / "structure_factor"
            )
            
            save_dir.mkdir(parents=True, exist_ok=True)
            
            filename = save_dir / (
                f"Swq_"
                f"Kx={Kx},Ky={Ky},Kz={Kz},"
                f"kappa={kappa:.3f},"
                f"hx={hx:.3f},hy={hy:.3f},hz={hz:.3f},"
                f"eta={eta:.3f}.png"
            )
            
            print(f"Saved to:\n{filename}")
            plt.savefig(filename, dpi=600)
            plt.close()