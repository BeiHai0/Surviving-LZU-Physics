# -*- coding: utf-8 -*-

import os

os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["MKL_DYNAMIC"] = "FALSE" # 防止 MKL 乱抢线程

from kitaev_data_manager import KitaevDataManager
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh
from multiprocessing import Pool
import time
from multiprocessing import get_context

# import mkl

# print(mkl.get_max_threads())

# k-path
# 考虑闭合回路，总 k 点数=总间隔数 + 1(Gamma 点重复计算)

def k_path(points, total_interval_number):

    points = np.array(points)

    diffs = np.diff(points, axis=0)
    seg_lengths = np.linalg.norm(diffs, axis=1)

    total_length = np.sum(seg_lengths)

    target_step = total_length / total_interval_number

    k_list = []
    k_dist = []
    node_indices = [] # 高对称点的 index

    current_cumulative_dist = 0.0

    for i in range(len(diffs)):

        node_indices.append(len(k_list))

        n_seg_intervals = max(1,int(round(seg_lengths[i] / target_step))) # 每一段直线路径的间隔数

        seg = np.linspace(points[i], points[i + 1], n_seg_intervals, endpoint=False)
        dists = np.linspace(current_cumulative_dist, current_cumulative_dist + seg_lengths[i], n_seg_intervals, endpoint=False)

        k_list.extend(seg)
        k_dist.extend(dists)

        current_cumulative_dist += seg_lengths[i]
        
    # 补上最后一个重复的 Gamma 点
    node_indices.append(len(k_list))
    k_list.append(points[-1])
    k_dist.append(current_cumulative_dist)

    return (np.array(k_list), np.array(k_dist), node_indices)


# Global shared data

GLOBAL_DATA = {}

# Worker initializer

def init_worker(data):

    global GLOBAL_DATA

    GLOBAL_DATA = data

# Single k-point solver

def solve_one_k(idx):

    t0 = time.time()
    
    global GLOBAL_DATA

    N = GLOBAL_DATA['N']

    p1 = GLOBAL_DATA['phase1'][idx]
    p2 = GLOBAL_DATA['phase2'][idx]
    p3 = GLOBAL_DATA['phase3'][idx]

    Ex_val = GLOBAL_DATA['Ex_val']
    Ey_val = GLOBAL_DATA['Ey_val']
    Ez_val = GLOBAL_DATA['Ez_val']

    A_xy_h = GLOBAL_DATA['A_xy_h']
    B_xy_h = GLOBAL_DATA['B_xy_h']

    A_yz_h = GLOBAL_DATA['A_yz_h']
    B_yz_h = GLOBAL_DATA['B_yz_h']

    A_zx_h = GLOBAL_DATA['A_zx_h']
    B_zx_h = GLOBAL_DATA['B_zx_h']

    # Build sparse blocks

    D1 = sparse.diags(Ex_val, format='csr')
    D2 = sparse.diags(Ey_val, format='csr')
    D3 = sparse.diags(Ez_val, format='csr')

    H12 = sparse.csr_matrix(A_xy_h + p1 * B_xy_h)
    H23 = sparse.csr_matrix(A_yz_h + p2 * B_yz_h)
    H31 = sparse.csr_matrix(A_zx_h + p3 * B_zx_h)

    H = sparse.bmat(
        [
            [D1,              H12,             H31.conj().T],
            [H12.conj().T,    D2,              H23          ],
            [H31,             H23.conj().T,    D3           ]
        ],
        format='csr'
    )

    # Lowest 20 eigenvalues
    vals = eigsh(H, k=20, which='SA', return_eigenvectors=False, tol=1e-10, maxiter=50000) # 'SA' 代表最小本征值
    vals.sort() # eigsh 不保证本征值有序

    dt = time.time() - t0
    print(f"k={idx:4d} finished in {dt:.2f} s")

    return idx, vals


# Main

if __name__ == "__main__":

    start_total = time.time()

    manager = KitaevDataManager()

    # Lattice
    N1, N2 = 60, 60
    N = N1 * N2
    bc1, bc2 = -1, -1

    # k path
    Gamma = np.array([0.0, 0.0])
    K = np.array([4 * np.pi / 3, 0.0])
    M = np.array([np.pi, np.pi / np.sqrt(3)])

    points = [Gamma, K, M, Gamma]

    total_interval_number = 200

    k_list, k_dist, node_idx = k_path(points, total_interval_number)
    k_number = k_list.shape[0]

    # Reciprocal phases
    
    a1 = np.array([1.0, 0.0])
    a2 = np.array([0.5, np.sqrt(3) / 2])

    phase1 = np.exp(-1j * np.dot(k_list, a1))
    phase2 = np.exp(1j * np.dot(k_list, a1 - a2))
    phase3 = np.exp(1j * np.dot(k_list, a2))

    # Parallel setup
    
    nproc = 32

    print(f"Using {nproc} worker processes")

    # Model parameters
    K_list = [(1, 1, 1), (-1, -1, -1)] 
    kappa_list = [0.0, 0.02, 0.04, 0.06]
    
    for Kx, Ky, Kz in K_list:

        for kappa in kappa_list:

            params = {'Kx': Kx, 'Ky': Ky, 'Kz': Kz, 'kappa': kappa}

            print(params)

            # Load hopping matrices
            # 代码中的 T 矩阵不依赖于磁场

            T_A_xy = manager.load_data('T_A_1_2', N1, N2, bc1, bc2, **params)
            T_A_yz = manager.load_data('T_A_2_3', N1, N2, bc1, bc2, **params)
            T_A_zx = manager.load_data('T_A_3_1', N1, N2, bc1, bc2, **params)
            T_B_xy = manager.load_data('T_B_1_2', N1, N2, bc1, bc2, **params)
            T_B_yz = manager.load_data('T_B_2_3', N1, N2, bc1, bc2, **params)
            T_B_zx = manager.load_data('T_B_3_1', N1, N2, bc1, bc2, **params)

            # Flux-sector energies

            positive_eigvals_list = []
            GS_energy_list = []

            for bond in [0, 1, 2, 3]:

                params_2 = {'bond': bond, 'Kx': Kx, 'Ky': Ky, 'Kz': Kz, 'kappa': kappa}

                positive_eigvals = manager.load_data(f'positive_eigvals_u', N1, N2, bc1, bc2, **params_2)
                positive_eigvals_list.append(positive_eigvals)

                GS_energy = -np.sum(positive_eigvals) / 2
                GS_energy_list.append(GS_energy)

            Ex_val = (GS_energy_list[1] - GS_energy_list[0] + positive_eigvals_list[1])

            Ey_val = (GS_energy_list[2] - GS_energy_list[0] + positive_eigvals_list[2])

            Ez_val = (GS_energy_list[3] - GS_energy_list[0] + positive_eigvals_list[3])

            # Magnetic field
            # --------------------------------------------
            # Fix : h=0 严格平带，这里只修正 h=0 的情况
            # --------------------------------------------
                
            
            h_c = manager.load_data('h_c', N1, N2, bc1, bc2, **params)
            step = 0.1
            h_list = [(0.0, 0.0, 0.0)]
            h_list.append((h_c, h_c, h_c))

            for hx, hy, hz in h_list:

                start_time = time.time()

                print(f"hx=hy=hz={hx:.3f}")
                
                # --------------------------------------------
                # Result array
                # --------------------------------------------
                
                energies = np.zeros((k_number, 20), dtype=float)
                
                # ============================================
                # Special case: h = 0
                # H is exactly diagonal and k-independent
                # ============================================
                
                if np.isclose(hx, 0) and np.isclose(hy, 0) and np.isclose(hz, 0):
                    vals = np.concatenate([Ex_val, Ey_val, Ez_val])
                    vals.sort()

                    vals = vals[:20]

                    energies[:] = vals

                    print("h = 0 detected")
                    print("Skipped eigsh")
                    print("Exact flat bands used")
                    
                else:
    
                    # --------------------------------------------
                    # Field-dressed matrices
                    # --------------------------------------------
    
                    A_xy_h = hz * T_A_xy
                    B_xy_h = hz * T_B_xy
                    A_yz_h = hx * T_A_yz
                    B_yz_h = hx * T_B_yz
                    A_zx_h = hy * T_A_zx
                    B_zx_h = hy * T_B_zx
    
                    # --------------------------------------------
                    # Shared data
                    # --------------------------------------------
    
                    shared_data = {
    
                        'N': N,
    
                        'phase1': phase1,
                        'phase2': phase2,
                        'phase3': phase3,
    
                        'Ex_val': Ex_val,
                        'Ey_val': Ey_val,
                        'Ez_val': Ez_val,
                        'A_xy_h': A_xy_h,
                        'B_xy_h': B_xy_h,
                        'A_yz_h': A_yz_h,
                        'B_yz_h': B_yz_h,
                        'A_zx_h': A_zx_h,
                        'B_zx_h': B_zx_h
                    }                
    
                    # --------------------------------------------
                    # Parallel solve
                    # --------------------------------------------
                    
                    ctx = get_context("fork")
    
                    with ctx.Pool(processes=nproc, initializer=init_worker, initargs=(shared_data,)) as pool:
    
                        for idx, vals in pool.imap_unordered(solve_one_k, range(k_number)):
    
                            energies[idx, :] = vals
    
                    # --------------------------------------------
                    # Save
                    # --------------------------------------------
    
                    params2 = {'Kx': Kx, 'Ky': Ky, 'Kz': Kz, 'kappa': kappa, 'hx': hx, 'hy': hy, 'hz': hz}
    
                    manager.save_data('k_space_energy', energies, N1, N2, bc1, bc2, **params2)
    
                    end_time = time.time()
    
                    print(f"Elapsed time: "f"{end_time - start_time:.2f} s")
    
                del energies

            # ------------------------------------------------
            # Cleanup
            # ------------------------------------------------

                del T_A_xy
                del T_A_yz
                del T_A_zx
    
                del T_B_xy
                del T_B_yz
                del T_B_zx
    
                del Ex_val
                del Ey_val
                del Ez_val

    end_total = time.time()

    print(
        f"All done. "
        f"Total elapsed time: "
        f"{end_total - start_total:.2f} s"
    )