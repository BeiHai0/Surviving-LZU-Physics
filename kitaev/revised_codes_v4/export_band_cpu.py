# -*- coding: utf-8 -*-
from kitaev_data_manager import KitaevDataManager
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import time


def k_path(points, total_interval_number):

    points = np.array(points)

    diffs = np.diff(points, axis=0)
    seg_lengths = np.linalg.norm(diffs, axis=1)
    total_length = np.sum(seg_lengths)

    target_step = total_length / total_interval_number

    k_list = []
    k_dist = []
    node_indices = []

    current_cumulative_dist = 0.0

    for i in range(len(diffs)):

        node_indices.append(len(k_list))

        n_seg_intervals = max(1, int(round(seg_lengths[i] / target_step)))

        seg = np.linspace(points[i], points[i+1], n_seg_intervals, endpoint=False)

        dists = np.linspace(
            current_cumulative_dist,
            current_cumulative_dist + seg_lengths[i],
            n_seg_intervals,
            endpoint=False
        )

        k_list.extend(seg)
        k_dist.extend(dists)

        current_cumulative_dist += seg_lengths[i]

    node_indices.append(len(k_list))

    k_list.append(points[-1])
    k_dist.append(current_cumulative_dist)

    return np.array(k_list), np.array(k_dist), node_indices


manager = KitaevDataManager()

N1, N2, bc1, bc2 = 20, 20, -1, -1
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

for Kx, Ky, Kz in [(1, 1, 1)]:

    for kappa in np.linspace(0, 0.2, 3):

        params = {'Kx':Kx, 'Ky':Ky, 'Kz':Kz, 'kappa':kappa}

        T_A_xy = manager.load_data('T_A_xy', N1, N2, bc1, bc2, **params)
        T_A_yz = manager.load_data('T_A_yz', N1, N2, bc1, bc2, **params)
        T_A_zx = manager.load_data('T_A_zx', N1, N2, bc1, bc2, **params)

        T_B_xy = manager.load_data('T_B_xy', N1, N2, bc1, bc2, **params)
        T_B_yz = manager.load_data('T_B_yz', N1, N2, bc1, bc2, **params)
        T_B_zx = manager.load_data('T_B_zx', N1, N2, bc1, bc2, **params)

        positive_eigvals_list = []
        GS_energy_list = []

        for i in [0,1,2,3]:

            positive_eigvals = manager.load_data(
                f'positive_eigvals_u_{i}',
                N1, N2, bc1, bc2,
                **params
            )

            positive_eigvals_list.append(positive_eigvals)

            GS_energy = -np.sum(positive_eigvals)/2
            GS_energy_list.append(GS_energy)

        print(params)

        Ex_val = GS_energy_list[1] - GS_energy_list[0] + positive_eigvals_list[1]
        Ey_val = GS_energy_list[2] - GS_energy_list[0] + positive_eigvals_list[2]
        Ez_val = GS_energy_list[3] - GS_energy_list[0] + positive_eigvals_list[3]

        # 预分配 Hamiltonian
        H_curr = np.zeros((3*N,3*N), dtype=complex)

        diag1 = np.arange(N)
        diag2 = np.arange(N,2*N)
        diag3 = np.arange(2*N,3*N)

        for hx, hy, hz in [(v,v,v) for v in np.linspace(0,0.5,6)]:

            start_time = time.time()

            energies = np.zeros((k_number,3*N))

            # 预乘磁场
            A_xy_h = hz*T_A_xy
            B_xy_h = hz*T_B_xy

            A_yz_h = hx*T_A_yz
            B_yz_h = hx*T_B_yz

            A_zx_h = hy*T_A_zx
            B_zx_h = hy*T_B_zx

            for idx in range(k_number):

                H_curr.fill(0)

                # 对角块
                H_curr[diag1,diag1] = Ex_val
                H_curr[diag2,diag2] = Ey_val
                H_curr[diag3,diag3] = Ez_val

                p1 = phase1[idx]
                p2 = phase2[idx]
                p3 = phase3[idx]

                # XY block
                H12 = A_xy_h + p1*B_xy_h
                H_curr[0:N,N:2*N] = H12
                H_curr[N:2*N,0:N] = H12.conj().T

                # YZ block
                H23 = A_yz_h + p2*B_yz_h
                H_curr[N:2*N,2*N:3*N] = H23
                H_curr[2*N:3*N,N:2*N] = H23.conj().T

                # ZX block
                H31 = A_zx_h + p3*B_zx_h
                H_curr[2*N:3*N,0:N] = H31
                H_curr[0:N,2*N:3*N] = H31.conj().T

                energies[idx,:] = np.linalg.eigvalsh(H_curr)

            params2 = {
                'Kx':Kx,'Ky':Ky,'Kz':Kz,
                'kappa':kappa,
                'hx':hx,'hy':hy,'hz':hz
            }

            manager.save_data(
                'k_space_energy',
                energies,
                N1,N2,bc1,bc2,
                **params2
            )

            labels=[r'$\Gamma$','K','M',r'$\Gamma$']

            plt.figure(figsize=(8,6),dpi=100)

            plt.plot(k_dist,energies[:,:20],color='black',alpha=0.6)

            for idx_node in node_idx:
                plt.axvline(k_dist[idx_node],color='black',lw=0.8,alpha=0.6)

            plt.xticks(k_dist[node_idx],labels,fontsize=12)
            plt.xlim(k_dist[0],k_dist[-1])

            plt.ylabel('Energy',fontsize=12)

            plt.title(
                f'N1=N2={N1}, bc1=bc2={bc1}, '
                f'Kx=Ky=Kz={Kx}, '
                f'kappa={kappa:.3f}, '
                f'hx=hy=hz={hx:.3f}',
                fontsize=14
            )

            plt.grid(axis='y',alpha=0.3,linestyle=':')

            plt.tight_layout()

            save_dir = Path("kitaev_data") / \
                f"N1_{N1}_N2_{N2}_bc1_{bc1}_bc2_{bc2}" / "band"

            save_dir.mkdir(parents=True,exist_ok=True)

            filename = save_dir / \
                f"band_N1={N1},N2={N2},bc1={bc1},bc2={bc2}," \
                f"Kx=Ky=Kz={Kx},kappa={kappa:.3f},hx=hy=hz={hx:.3f}.png"

            plt.savefig(filename)
            plt.close()

            end_time = time.time()

            print(f"能带计算耗时: {end_time-start_time:.6f} 秒")

            del energies

        del T_A_xy,T_A_yz,T_A_zx
        del T_B_xy,T_B_yz,T_B_zx
        del Ex_val,Ey_val,Ez_val

print("all done")