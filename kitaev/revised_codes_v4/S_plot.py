# -*- coding: utf-8 -*-
from kitaev_data_manager import KitaevDataManager
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

manager = KitaevDataManager()

N1, N2, bc1, bc2 = 20, 20, -1, -1

Kx,Ky,Kz = 1,1,1
kappa = 0.0
hx,hy,hz = 0.3,0.3,0.3

params = {'Kx':Kx, 'Ky':Ky, 'Kz':Kz, 'kappa':kappa, 'hx':hx, 'hy':hy, 'hz':hz}

S = manager.load_data('S', N1, N2, bc1, bc2, **params)

q_list = manager.load_data('q_list', N1, N2, bc1, bc2, **params)
omega = manager.load_data('omega', N1, N2, bc1, bc2, **params)
node_idx = manager.load_data('node_idx', N1, N2, bc1, bc2, **params)

plt.figure(figsize=(6,5))
plt.imshow(np.log(S.T + 1),aspect='auto',origin='lower',extent=[0, len(q_list), omega[0], omega[-1]],cmap='Spectral_r')
plt.colorbar(label='S(ω,q)')
ax = plt.gca()

ax.yaxis.set_major_locator(MultipleLocator(1))   # 主刻度间隔
ax.yaxis.set_minor_locator(MultipleLocator(0.2))   # 次刻度更细

ax.tick_params(axis='y', which='major', length=6)
ax.tick_params(axis='y', which='minor', length=3)
plt.ylabel('ω')
plt.xlabel('k-path')
plt.xticks(node_idx, ['Γ','K',"M'","Γ'","K'","M",'Γ'])
plt.title(f"K=({Kx},{Ky},{Kz}), κ={kappa:.3f}, h={hx:.3f}")
plt.tight_layout()
plt.show()