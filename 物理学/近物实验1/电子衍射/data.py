import numpy as np
import matplotlib as plt

v = np.arange(10, 18, 1)

v = v * 1e3 # 加速电压

print(v)

lambda_1 = np.sqrt(150 / v) # 根据加速电压计算德布罗意波长，单位为埃

print(lambda_1)

d = np.array([[3.9, 3.9, 4.0, 4.05, 4],
              [3.8, 3.75, 3.75, 3.85, 3.85],
              [3.65, 3.65, 3.65, 3.62, 3.65],
              [3.5, 3.55, 3.55, 3.5, 3.5],
              [3.25, 3.45, 3.4, 3.45, 3.45],
              [3.35, 3.3, 3.35, 3.35, 3.25],
              [3.25,3.2, 3.25, 3.25, 3.21],
              [3.15, 3.17, 3.12, 3.1, 3.15]]) # 密勒指数(220) 在不同电压对应的环直径测5次，单位为 cm

print(d)

d_bar = np.average(d, axis=1)

print(d_bar)

r_bar = d_bar/2

r_bar = r_bar * 10 ## 单位变为 mm

print(r_bar)

lambda_2 = np.zeros(8)

D = 258 ## 金箔到荧光屏距离，单位为mm
a = 4.0786 ## 金的晶格常数，单位为埃

for i in range(8):
    lambda_2[i] = r_bar[i] / D * a / np.sqrt(2**2 + 2**2 +0**2)

print(lambda_2)

d2 = np.array([[1.9, 1.9, 1.8, 1.9, 1.9], ## 17 kV 第1个环半径测5次，对应密勒指数 (111)
               [3.12, 3.15, 3.2, 3.18, 3.15], ## 17 kV 第3个环半径测5次 ，对应密勒指数 (200)
               [3.65, 3.7, 3.82, 3.7, 3.7]])  ## 17 kV 第4个环半径测5次，对应密勒指数 (220)

d2_bar = np.average(d2, axis = 1)

print(d2_bar)

r2_bar = d2_bar / 2 ## 单位为 cm

r2_bar = r2_bar *10 ## 单位为mm

print(r2_bar)

lambda3 = np.sqrt(150/17e3) 

print(lambda3)

a_m = np.zeros(3)

a_m[0] = lambda3 * D / r2_bar[0] * np.sqrt(1**2 + 1**2 + 1**2)
a_m[1] = lambda3 * D / r2_bar[1] * np.sqrt(2**2 + 0**2 + 0**2)
a_m[2] = lambda3 * D / r2_bar[2] * np.sqrt(2**2 + 2**2 + 2**2)

print(a_m)

a_measure = np.average(a_m)

print(a_measure)

error = np.abs(a_measure-a) / a

print(error) 