# -*- coding: utf-8 -*-
import os
import argparse
import time
import numpy as np
import scipy.linalg as la
from kitaev_data_manager import KitaevDataManager
import multiprocessing as mp

mp.set_start_method("fork", force=True)


# =========================
# 超算线程控制
# =========================
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"


# =========================
# multiprocessing 全局变量
# =========================
_GLOBAL = {}


def _init_worker(global_dict):
    global _GLOBAL
    _GLOBAL = global_dict


def _worker_q(q_idx):
    """
    每个 q 点的计算（并行核心）
    """
    start_time = time.time()
    
    q = _GLOBAL["q_list"][q_idx]

    N = _GLOBAL["N"]
    diag_1 = _GLOBAL["diag_1"]
    diag_2 = _GLOBAL["diag_2"]
    diag_3 = _GLOBAL["diag_3"]

    A_xy_h = _GLOBAL["A_xy_h"]
    B_xy_h = _GLOBAL["B_xy_h"]
    A_yz_h = _GLOBAL["A_yz_h"]
    B_yz_h = _GLOBAL["B_yz_h"]
    A_zx_h = _GLOBAL["A_zx_h"]
    B_zx_h = _GLOBAL["B_zx_h"]

    phase_xy = _GLOBAL["phase_xy_list"][q_idx]
    phase_yz = _GLOBAL["phase_yz_list"][q_idx]
    phase_zx = _GLOBAL["phase_zx_list"][q_idx]

    delta_list = _GLOBAL["delta_list"]
    p_A_list = _GLOBAL["p_A_list"]
    p_B_list = _GLOBAL["p_B_list"]

    # =========================
    # build H_k
    # =========================
    H_k = np.zeros((3 * N, 3 * N), dtype=complex)

    H_k[np.arange(N), np.arange(N)] = diag_1
    H_k[np.arange(N, 2 * N), np.arange(N, 2 * N)] = diag_2
    H_k[np.arange(2 * N, 3 * N), np.arange(2 * N, 3 * N)] = diag_3

    H12 = A_xy_h + phase_xy * B_xy_h
    H23 = A_yz_h + phase_yz * B_yz_h
    H31 = A_zx_h + phase_zx * B_zx_h

    H_k[0:N, N:2 * N] = H12
    H_k[N:2 * N, 0:N] = H12.T.conj()

    H_k[N:2 * N, 2 * N:3 * N] = H23
    H_k[2 * N:3 * N, N:2 * N] = H23.T.conj()

    H_k[2 * N:3 * N, 0:N] = H31
    H_k[0:N, 2 * N:3 * N] = H31.T.conj()

    eigvals, eigvecs = la.eigh(H_k, overwrite_a=True, check_finite=False)

    eigvecs = eigvecs.reshape(3, N, 3 * N)

    # =========================
    # weights
    # =========================
    f = [None]
    q = _GLOBAL["q_list"][q_idx]

    for mu in [1, 2, 3]:
        f.append(
            p_A_list[mu] +
            np.exp(-1j * np.dot(q, delta_list[mu])) * p_B_list[mu]
        )

    weights = np.zeros(3 * N)
    for mu in [1, 2, 3]:
        amp = f[mu] @ eigvecs[mu - 1]
        weights += np.abs(amp) ** 2
        
    end_time = time.time()
    
    print(f"这个 q 用时={end_time-start_time:.3f}")

    return q_idx, eigvals, weights.real


# =========================
# argparse
# =========================
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--Kx", type=int)
    parser.add_argument("--Ky", type=int)
    parser.add_argument("--Kz", type=int)
    parser.add_argument("--kappa", type=float)
    return parser.parse_args()


# =========================
# k-path（不改）
# =========================
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


def fold_to_1BZ(q, b1, b2):
    B = np.column_stack((b1, b2))
    coeff = np.linalg.solve(B, q)
    coeff_fold = coeff - np.round(coeff)
    return B @ coeff_fold


# =========================
# main
# =========================
def main():

    args = parse_args()

    manager = KitaevDataManager()

    N1, N2, bc1, bc2 = 60, 60, -1, -1
    N = N1 * N2

    Kx, Ky, Kz = args.Kx, args.Ky, args.Kz
    kappa = args.kappa

    print(f"[RUN] K={Kx}, kappa={kappa}", flush=True)

    a1 = np.array([1.0, 0.0])
    a2 = np.array([0.5, np.sqrt(3)/2])

    b1 = 2 * np.pi * np.array([1, -1 / np.sqrt(3)])
    b2 = 2 * np.pi * np.array([0, 2 / np.sqrt(3)])

    delta_x = np.array([-0.5, -0.5 / np.sqrt(3)])
    delta_y = np.array([0.5, -0.5 / np.sqrt(3)])
    delta_z = np.array([0, 1 / np.sqrt(3)])
    delta_list = [None, delta_x, delta_y, delta_z]

    Gamma = np.array([0.0, 0.0])
    K = (2 * b1 + b2) / 3
    M_prime = b1 + b2 / 2
    Gamma_prime = b1 + b2
    K_prime = 2 * np.pi * np.array([1.0 / 3, 1.0 / np.sqrt(3)])
    M = b2 / 2

    points = [Gamma, K, M_prime, Gamma_prime, K_prime, M, Gamma]
    q_interval_number = 20
    q_list, q_dist, node_idx = k_path(points, q_interval_number)

    q_fold_list = np.array([fold_to_1BZ(q, b1, b2) for q in q_list])

    phase_xy_list = np.exp(-1j * (q_fold_list @ a1))
    phase_yz_list = np.exp(1j * (q_fold_list @ (a1 - a2)))
    phase_zx_list = np.exp(1j * (q_fold_list @ a2))

    # =========================
    # load data
    # =========================
    params0 = {'Kx': Kx, 'Ky': Ky, 'Kz': Kz, 'kappa': kappa}

    T_dict = {}
    keys_to_load = [
        'T_A_1_2', 'T_B_1_2',
        'T_A_2_3', 'T_B_2_3',
        'T_A_3_1', 'T_B_3_1'
    ]

    for key in keys_to_load:
        T_dict[key] = manager.load_data(key, N1, N2, bc1, bc2, **params0)

    positive_eigvals_list = []
    GS_energy_list = []

    for bond in [0, 1, 2, 3]:
        params1 = {'bond': bond, **params0}
        eig = manager.load_data('positive_eigvals_u', N1, N2, bc1, bc2, **params1)
        positive_eigvals_list.append(eig)
        GS_energy_list.append(-0.5 * np.sum(eig))

    diag_1 = GS_energy_list[1] - GS_energy_list[0] + positive_eigvals_list[1]
    diag_2 = GS_energy_list[2] - GS_energy_list[0] + positive_eigvals_list[2]
    diag_3 = GS_energy_list[3] - GS_energy_list[0] + positive_eigvals_list[3]

    p_A_list = [None]
    p_B_list = [None]

    for k in [
        'sigma_A_d_dag_GS_exp_bond_1',
        'sigma_A_d_dag_GS_exp_bond_2',
        'sigma_A_d_dag_GS_exp_bond_3'
    ]:
        p_A_list.append(manager.load_data(k, N1, N2, bc1, bc2, **params0))

    for k in [
        'sigma_B_d_dag_GS_exp_bond_1',
        'sigma_B_d_dag_GS_exp_bond_2',
        'sigma_B_d_dag_GS_exp_bond_3'
    ]:
        p_B_list.append(manager.load_data(k, N1, N2, bc1, bc2, **params0))

    h_c = manager.load_data('h_c', N1, N2, bc1, bc2, **params0)

    step = 0.1
    h_list = list(np.arange(0.0, h_c, step))
    h_list.append(h_c)

    # =========================
    # parallel config
    # =========================
    nproc = 16

    # =========================
    # h loop
    # =========================
    for h in h_list:

        print(f"\n[h] = {h}", flush=True)

        params2 = {
            'Kx': Kx, 'Ky': Ky, 'Kz': Kz,
            'kappa': kappa,
            'hx': h, 'hy': h, 'hz': h
        }

        eigvals_all = np.zeros((len(q_list), 3 * N))
        weights_all = np.zeros((len(q_list), 3 * N))

        A_xy_h = h * T_dict['T_A_1_2']
        B_xy_h = h * T_dict['T_B_1_2']
        A_yz_h = h * T_dict['T_A_2_3']
        B_yz_h = h * T_dict['T_B_2_3']
        A_zx_h = h * T_dict['T_A_3_1']
        B_zx_h = h * T_dict['T_B_3_1']

        # =========================
        # h = 0（不并行）
        # =========================
        if np.abs(h) < 1e-6:

            eigvals = np.concatenate([
                diag_1, diag_2, diag_3
            ])
            eigvals_all[:] = eigvals

        # =========================
        # h ≠ 0（并行 q）
        # =========================
        else:

            global_dict = {
                "N": N,
                "diag_1": diag_1,
                "diag_2": diag_2,
                "diag_3": diag_3,
                "A_xy_h": A_xy_h,
                "B_xy_h": B_xy_h,
                "A_yz_h": A_yz_h,
                "B_yz_h": B_yz_h,
                "A_zx_h": A_zx_h,
                "B_zx_h": B_zx_h,
                "phase_xy_list": phase_xy_list,
                "phase_yz_list": phase_yz_list,
                "phase_zx_list": phase_zx_list,
                "delta_list": delta_list,
                "p_A_list": p_A_list,
                "p_B_list": p_B_list,
                "q_list": q_list
            }

            with mp.Pool(
                processes=nproc,
                initializer=_init_worker,
                initargs=(global_dict,)
            ) as pool:

                results = pool.map(_worker_q, range(len(q_list)))

            for q_idx, eigvals, weights in results:
                eigvals_all[q_idx] = eigvals
                weights_all[q_idx] = weights

        # =========================
        # SAVE
        # =========================
        manager.save_data(f'eigvals_q_interval_number_{q_interval_number}',
                          eigvals_all, N1, N2, bc1, bc2, **params2)

        manager.save_data(f'weights_q_interval_number_{q_interval_number}',
                          weights_all, N1, N2, bc1, bc2, **params2)

        manager.save_data(f'q_list_q_interval_number_{q_interval_number}',
                          q_list, N1, N2, bc1, bc2, **params2)

        manager.save_data(f'node_idx_q_interval_number_{q_interval_number}',
                          node_idx, N1, N2, bc1, bc2, **params2)


if __name__ == "__main__":
    main()