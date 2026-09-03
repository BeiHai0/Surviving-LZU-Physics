# -*- coding: utf-8 -*-
from kitaev_data_manager import KitaevDataManager
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

manager = KitaevDataManager()

# =========================
# 参数
# =========================

N1, N2, bc1, bc2 = 20, 20, -1, -1

Kx, Ky, Kz = -1, -1, -1
kappa = 0.0
hx, hy, hz = 0.0, 0.0, 0.0

q_interval_number = 500
omega_number = 701
eta = 0.04

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

S = manager.load_data(f'S_q_interval_number_{q_interval_number}_omega_number_{omega_number}_eta_{eta:.2f}', N1, N2, bc1, bc2, **params)

q_list = manager.load_data(f'q_list_q_interval_number_{q_interval_number}', N1, N2, bc1, bc2, **params)

omega = manager.load_data(f'omega_omega_number_{omega_number}', N1, N2, bc1, bc2, **params)

node_idx = manager.load_data(f'node_idx_q_interval_number_{q_interval_number}', N1, N2, bc1, bc2, **params)

# =========================
# 作图
# =========================

fig, ax = plt.subplots(figsize=(7,5), dpi=150)

# log scale
S_plot = S.T

im = ax.imshow(
    S_plot,
    aspect='auto',
    origin='lower',
    extent=[0, len(q_list)-1, omega[0], omega[-1]],
    cmap='Spectral_r',
    interpolation='nearest'
)

# colorbar
cbar = plt.colorbar(im, ax=ax)
cbar.set_label(r'$\log(1+S(\mathbf{q},\omega))$')

# y axis
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_minor_locator(MultipleLocator(0.2))

ax.tick_params(axis='y', which='major', length=6)
ax.tick_params(axis='y', which='minor', length=3)

# labels
ax.set_ylabel(r'$\omega$')
ax.set_xlabel('Momentum path')

# high symmetry points
ax.set_xticks(node_idx)
ax.set_xticklabels(['Γ', 'K', "M'", "Γ'", "K'", "M", 'Γ'])

# vertical guide lines
for idx in node_idx:
    ax.axvline(idx, color='k', lw=0.5, alpha=0.3)

# title
ax.set_title(
    rf'$K=({Kx},{Ky},{Kz}),\ \kappa={kappa:.3f},\ h={hx:.3f}$'
)

plt.tight_layout()
plt.show()