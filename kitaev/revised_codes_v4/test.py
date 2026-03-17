import numpy as np
import scipy.linalg
import time

N = 4000   # 可以先小一点测试

print("building matrix...")

A = np.random.randn(N, N) + 1j*np.random.randn(N, N)
A = (A + A.conj().T)/2

# numpy
print("numpy eigvalsh...")

start = time.time()
np.linalg.eigvalsh(A)
t_np = time.time() - start

print("numpy time =", t_np)


# scipy
print("scipy eigvalsh...")

start = time.time()
scipy.linalg.eigvalsh(A)
t_sp = time.time() - start

print("scipy time =", t_sp)

print("\nratio scipy/numpy =", t_sp/t_np)