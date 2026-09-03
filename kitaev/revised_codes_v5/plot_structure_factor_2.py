# -*- coding: utf-8 -*-

from kitaev_data_manager import KitaevDataManager
import numpy as np
import matplotlib.pyplot as plt

# =========================
# 参数
# =========================

manager = KitaevDataManager()

N1, N2, bc1, bc2 = 20, 20, -1, -1

Kx, Ky, Kz = 1, 1, 1
kappa = 0.0

hx, hy, hz = 0.0, 0.0, 0.0

q_interval_number = 500

eta = 0.04              # 这里可以改
omega_max = 7
omega_number = 701

omega = np.linspace(0, omega_max, omega_number)

params = {
    'Kx': Kx,
    'Ky': Ky,
    'Kz': Kz,
    'kappa': kappa,
    'hx': hx,
    'hy': hy,
    'hz': hz
}

# =========================
# 读取数据
# =========================

eigvals_all = manager.load_data(
    f'eigvals_q_interval_number_{q_interval_number}',
    N1, N2, bc1, bc2,
    **params
)

weights_all = manager.load_data(
    f'weights_q_interval_number_{q_interval_number}',
    N1, N2, bc1, bc2,
    **params
)

q_list = manager.load_data(
    f'q_list_q_interval_number_{q_interval_number}',
    N1, N2, bc1, bc2,
    **params
)

node_idx = manager.load_data(
    f'node_idx_q_interval_number_{q_interval_number}',
    N1, N2, bc1, bc2,
    **params
)

# =========================
# 重构 S(omega, q)
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

plt.figure(figsize=(8, 6))

plt.imshow(
    S.T,
    aspect='auto',
    origin='lower',
    extent=[0, len(q_list)-1, omega[0], omega[-1]],
    cmap='Spectral_r'
)

plt.colorbar(label=r'$S$')

# 高对称点标签
labels = [r'$\Gamma$', r'$K$', r'$M$', r'$\Gamma$', r'$K$', r'$M$', r'$\Gamma$']

plt.xticks(node_idx, labels)

for idx in node_idx:
    plt.axvline(idx, color='k', linestyle='--', linewidth=0.5)

plt.xlabel(r'$\mathbf{{k}}$-path')
plt.ylabel(r'$\omega$')

plt.title(
    rf'$S(\omega,\mathbf{{q}})$'
    '\n'
    rf'$K=({Kx},{Ky},{Kz}),\ '
    rf'\kappa={kappa},\ '
    rf'h=({hx:.2f},{hy:.2f},{hz:.2f}),\ '
    rf'\eta={eta}$'
)

plt.tight_layout()
plt.show()