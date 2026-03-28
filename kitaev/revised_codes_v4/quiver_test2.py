import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 三个箭头
X = [0, 0, 0]
Y = [0, 0, 0]
Z = [0, 0, 0]

U = [1, 0, 0]
V = [0, 1, 0]
W = [0, 0, 1]

ax.quiver(X, Y, Z, U, V, W, length=1)

ax.set_box_aspect([1,1,1])
plt.show()