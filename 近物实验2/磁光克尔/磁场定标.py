import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 示例数据（你可以替换成自己的数据）
x = np.array([0.99, 1.04, 1.09, 1.14, 1.19, 1.24, 1.29])
y = np.array([28, 29, 31, 32, 33, 35, 36])

# 进行线性拟合（y = m*x + b）
slope, intercept = np.polyfit(x, y, 1)

# 输出拟合参数
print(f"斜率 (slope): {slope:.4f}")
print(f"截距 (intercept): {intercept:.4f}")

# 拟合直线的y值
y_fit = slope * x + intercept

# 绘图
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='blue', label='数据点')
plt.plot(x, y_fit, color='red', label=f'拟合直线: y = {slope:.2f}x + {intercept:.2f}')
plt.xlabel('磁铁电源I/A')
plt.ylabel('特斯拉计读数B/mT')
plt.title('磁场强度定标')
plt.legend()
plt.grid(True)
plt.show()
