import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 示例数据（你可以替换成自己的数据）
x = np.array([1.16, 1.46, 1.78, 2.12, 2.46, 2.78, 3.08])
y = np.array([3.500, 3.550, 3.600, 3.650, 3.700, 3.750, 3.800])

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
plt.xlabel('SEV信号U/V')
plt.ylabel('螺旋测微头读数L/mm')
plt.title('螺旋测微头读数与SEV信号关系')
plt.legend()
plt.grid(True)
plt.show()
