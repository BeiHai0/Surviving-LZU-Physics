import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体与负号正常显示
rcParams['font.sans-serif'] = ['SimHei']  # 或 ['Microsoft YaHei']
rcParams['axes.unicode_minus'] = False

# 数据
T = np.array([2940, 2860, 2770, 2720, 2400])
lambda_max_nm = np.array([966, 1020, 1034, 1086, 1274])
lambda_max_mm = lambda_max_nm / 1000000
inv_T = 1 / T

# 拟合：强制过原点
a = np.sum(inv_T * lambda_max_mm) / np.sum(inv_T**2)

# 创建更广范围的 x 值：从 0 到略大于 max(1/T)
x_fit = np.linspace(0, max(inv_T) * 1.1, 200)
y_fit = a * x_fit

# 画图
plt.figure(figsize=(8, 5))
plt.scatter(inv_T, lambda_max_mm, color='blue', label='实验数据')
plt.plot(x_fit, y_fit, color='red', label=f'线性拟合: λ = {a:.3f} × (1/T)')

# 添加坐标轴原点线
plt.axhline(0, color='gray', linewidth=1)
plt.axvline(0, color='gray', linewidth=1)

# 图形标签与说明
plt.xlabel('1 / T (K$^{-1}$)')
plt.ylabel('λ_max (mm)')
plt.title('维恩位移定律线性拟合图（过原点）')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
