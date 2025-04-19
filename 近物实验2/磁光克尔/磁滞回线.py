import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# 字体设置
rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_excel('data.xlsx', sheet_name='实验数据')
x = df['磁感应强度/mT'].values
y = df['克尔转角/度(未平移)'].values

# 用 pandas 的 rolling 做平滑（可调 window 大小）
df['y_smooth'] = pd.Series(y).rolling(window=5, center=True).mean()

# 计算磁滞回线中心
x_center = (x.max() + x.min()) / 2
y_center = (y.max() + y.min()) / 2

# 平移后的数据
x_shifted = x - x_center
y_shifted = y - y_center
y_smooth_shifted = df['y_smooth'] - y_center

delta_theta = y.max() - y.min()
print(f"克尔转角最大差值为：{delta_theta:.3f} °")

# 绘图
plt.figure(figsize=(8, 5))
plt.plot(x_shifted, y_smooth_shifted, label='平滑曲线（平移后）', color='orange')
plt.scatter(x_shifted, y_shifted, color='blue', label='原始数据点（平移后）')
plt.axhline(0, color='gray', linestyle='--', linewidth=1)
plt.axvline(0, color='gray', linestyle='--', linewidth=1)
plt.xlabel('磁感应强度 B (mT)')
plt.ylabel('克尔转角 θ (°)')
plt.title('磁滞回线（平移后）', fontsize=14)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
