import numpy as np  
import matplotlib.pyplot as plt  
from scipy.special import jn  # 导入scipy库中的贝塞尔函数  
  
# 选择一个贝塞尔函数的阶数n和对应的零点k  
n = 1  # 例如，选择一阶贝塞尔函数  
k = jn_zeros(n, 1)[0]  # 获取一阶贝塞尔函数的第一个零点  
  
# 创建极坐标网格  
r = np.linspace(0.01, 1, 200)  # 避免r=0是为了防止除以零  
theta = np.linspace(0, 2 * np.pi, 360)  
R, Theta = np.meshgrid(r, theta)  
  
# 计算本征解  
u = jn(n, k * R) * np.cos(n * Theta)  
  
# 将极坐标转换为笛卡尔坐标以进行绘图  
x = R * np.cos(Theta)  
y = R * np.sin(Theta)  
  
# 绘制本征解图像  
plt.figure(figsize=(6, 6))  
plt.pcolormesh(x, y, u, shading='gouraud', cmap='viridis')  
plt.colorbar(label='u(r, θ)')  
plt.axis('equal')  # 保持x和y轴的比例相同  
plt.title('Eigensolution of the Helmholtz Equation in a Unit Circle')  
plt.show()

