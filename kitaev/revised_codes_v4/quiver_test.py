from mayavi import mlab
import numpy as np

x, y, z = np.mgrid[-1:1:5j, -1:1:5j, -1:1:5j]

u = -y
v = x
w = z

mlab.quiver3d(x, y, z, u, v, w, scale_factor=0.5)
mlab.show()