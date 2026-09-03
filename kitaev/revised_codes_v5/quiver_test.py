import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

# ==========================================
# Honeycomb lattice
# ==========================================

a1 = np.array([1.0, 0.0])
a2 = np.array([0.5, np.sqrt(3)/2])

deltaA = np.array([0.0, 0.0])
deltaB = np.array([0.5, np.sqrt(3)/6])

Lx = 4
Ly = 4

positions = []
spins = []

# ==========================================
# Generate example spin texture
# ==========================================

for i in range(Lx):
    for j in range(Ly):

        R = i*a1 + j*a2

        theta = 0.6*(i+j)

        # A sublattice
        rA = R + deltaA

        positions.append([rA[0], rA[1], 0.0])

        spins.append([
            np.cos(theta),
            np.sin(theta),
            0.8*np.cos(2*theta)
        ])

        # B sublattice
        rB = R + deltaB

        positions.append([rB[0], rB[1], 0.0])

        spins.append([
            -np.cos(theta),
            -np.sin(theta),
            -0.8*np.cos(2*theta)
        ])

positions = np.array(positions)
spins = np.array(spins)

# ==========================================
# Normalize spins
# ==========================================

norm = np.linalg.norm(spins, axis=1)

spins = spins / norm[:, None]

# ==========================================
# Plot
# ==========================================

fig = plt.figure(figsize=(9,9))

ax = fig.add_subplot(111, projection='3d')

# positions
X = positions[:,0]
Y = positions[:,1]
Z = positions[:,2]

# spin components
U = spins[:,0]
V = spins[:,1]
W = spins[:,2]

# colors from Sc
colors = plt.cm.coolwarm((W + 1)/2)

# arrows
ax.quiver(
    X, Y, Z,
    U, V, W,
    length=0.4,
    normalize=True,
    colors=colors,
    linewidth=1.5
)

# lattice sites
ax.scatter(
    X, Y, Z,
    c='black',
    s=20
)

# ==========================================
# Formatting
# ==========================================

ax.set_box_aspect([1,1,0.5])

ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('c')

# viewing angle
ax.view_init(elev=30, azim=-60)

plt.tight_layout()
plt.show()