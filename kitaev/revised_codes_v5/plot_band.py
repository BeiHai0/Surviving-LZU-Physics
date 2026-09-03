# -*- coding: utf-8 -*-

from kitaev_data_manager import KitaevDataManager
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib.ticker as ticker


# ============================================================
# k-path
# ============================================================

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

        seg = np.linspace(points[i], points[i + 1], n_seg_intervals, endpoint=False)
        dists = np.linspace(current_cumulative_dist,
                            current_cumulative_dist + seg_lengths[i],
                            n_seg_intervals,
                            endpoint=False)

        k_list.extend(seg)
        k_dist.extend(dists)

        current_cumulative_dist += seg_lengths[i]

    node_indices.append(len(k_list))
    k_list.append(points[-1])
    k_dist.append(current_cumulative_dist)

    return np.array(k_list), np.array(k_dist), node_indices

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

plt.rcParams.update({
    "font.size": 24,
    "axes.labelsize": 14,
    "xtick.labelsize": 24,
    "ytick.labelsize": 24,
    "font.family": "serif",
    "mathtext.fontset": "cm",
})

# ============================================================
# Main
# ============================================================

if __name__ == "__main__":

    manager = KitaevDataManager()

    # --------------------------------------------------------
    # System size
    # --------------------------------------------------------

    N1, N2 = 60, 60
    bc1, bc2 = -1, -1

    # --------------------------------------------------------
    # k-path
    # --------------------------------------------------------

    Gamma = np.array([0.0, 0.0])
    K = np.array([4 * np.pi / 3, 0.0])
    M = np.array([np.pi, np.pi / np.sqrt(3)])

    points = [Gamma, K, M, Gamma]
    total_interval_number = 200

    k_list, k_dist, node_idx = k_path(points, total_interval_number)

    # --------------------------------------------------------
    # Plot parameters
    # --------------------------------------------------------

    n_band_plot = 20

    # --------------------------------------------------------
    # First pass: find global energy scale
    # --------------------------------------------------------

    all_energies = []

    K_list = [(1, 1, 1)]
    kappa_list = [0.0]

    for Kx, Ky, Kz in K_list:
        for kappa in kappa_list:

            params_base = {'Kx': Kx, 'Ky': Ky, 'Kz': Kz, 'kappa': kappa}

            h_c = manager.load_data('h_c', N1, N2, bc1, bc2, **params_base)
            step = 0.1
            h_list = [(h, h, h) for h in np.arange(0, h_c, step)]
            h_list.append((h_c, h_c, h_c))

            for hx, hy, hz in h_list:

                params = {'Kx': Kx, 'Ky': Ky, 'Kz': Kz, 'kappa': kappa, 'hx': hx, 'hy': hy, 'hz': hz}

                energies = manager.load_data('k_space_energy', N1, N2, bc1, bc2, **params)

                if energies is not None:
                    all_energies.append(energies)

    all_energies = np.array(all_energies)
    y_max = np.nanmax(all_energies)

    # --------------------------------------------------------
    # Plot with unified scale
    # --------------------------------------------------------

    for Kx, Ky, Kz in K_list:
        for kappa in kappa_list:

            params_base = {'Kx': Kx, 'Ky': Ky, 'Kz': Kz, 'kappa': kappa}

            h_c = manager.load_data('h_c', N1, N2, bc1, bc2, **params_base)
            step = 0.1
            h_list = [(h, h, h) for h in np.arange(0, h_c, step)]
            h_list.append((h_c, h_c, h_c))

            for hx, hy, hz in h_list:

                params = dict(**params_base, hx=hx, hy=hy, hz=hz)

                print("\n" + "=" * 60)
                print(params)
                print("=" * 60)

                energies = manager.load_data('k_space_energy', N1, N2, bc1, bc2, **params)

                if energies is None:
                    print("Data not found.")
                    continue
                
                plt.figure(figsize=(6, 4)) # 如果是 .pdf 格式，就不用 dpi 这个参数

                plt.plot(k_dist, energies[:, :n_band_plot], color='black', lw=0.6, alpha=1.0)

                for idx_node in node_idx:
                    plt.axvline(k_dist[idx_node], color='black', lw=0.5, alpha=0.3) # chat 说高对称点竖线别太粗
                
                labels = [r'$\Gamma$', r'$\mathrm{K}$', r'$\mathrm{M}$', r'$\Gamma$']
                plt.xticks(k_dist[node_idx], labels, fontsize=32)
                plt.xlim(k_dist[0], k_dist[-1])

                # ====================================================
                # LaTeX labels
                # ====================================================

                plt.ylabel(r'$E_\boldsymbol{k}$', fontsize=36)
                
                plt.ylim(0, 0.6)
                
                ax = plt.gca()
                ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())
                ax.set_yticks(np.arange(0, 0.7, 0.1))

                ax.text(
                    0.98, 0.95,
                    rf"$(K,\kappa,h)=({Kx},{fmt_kappa(kappa)},{fmt_h(hx, h_c)})$",
                    transform=ax.transAxes,
                    ha='right',
                    va='top',
                    fontsize=24,
                    #bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none", alpha=0.6) 不需要背景
                )
                
                E_top = energies[:, :20].max()
                ax.axhspan(
                    E_top,
                    0.6,
                    color='gray',
                    alpha=0.2,
                    zorder=0
                )
                
                
                
                plt.tight_layout()

                save_dir = Path("kitaev_data") / f"N1_{N1}_N2_{N2}_bc1_{bc1}_bc2_{bc2}" / "band"
                save_dir.mkdir(parents=True, exist_ok=True)

                filename = save_dir / (
                    f"band_N1={N1},N2={N2},bc1={bc1},bc2={bc2},"
                    f"Kx={Kx},Ky={Ky},Kz={Kz},"
                    f"kappa={kappa:.3f},"
                    f"hx={hx:.3f},hy={hy:.3f},hz={hz:.3f}.pdf"
                )

                plt.savefig(filename, bbox_inches='tight')
                plt.close()

                print(f"Saved to:\n{filename}")

    print("\n" + "=" * 60)
    print("All plots finished.")
    print("=" * 60)