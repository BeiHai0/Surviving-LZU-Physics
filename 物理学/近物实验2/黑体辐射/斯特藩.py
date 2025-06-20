import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from sklearn.linear_model import LinearRegression

# 设置中文字体
rcParams['font.sans-serif'] = ['SimHei']  # 黑体
rcParams['axes.unicode_minus'] = False   # 正常显示负号

# 实验数据
T4 = np.array([6.6906e13, 5.8873e13, 5.4736e13, 3.3178e13]).reshape(-1, 1)
E = np.array([3.7862, 3.2876, 2.8792, 1.8609])

# 拟合模型（强制过原点）
model = LinearRegression(fit_intercept=False)
model.fit(T4, E)

# 斜率（拟合出的斯特藩常数）
delta_fit = model.coef_[0]
r2 = model.score(T4, E)

# 绘图
plt.figure(figsize=(8, 6))
plt.scatter(T4, E, color='red', label='实验数据')
plt.plot(T4, model.predict(T4), color='blue', label=f'拟合直线: $E = {delta_fit:.3e} \\, T^4$\n$R^2 = {r2:.5f}$')

plt.xlabel('$T^4$ ($\\mathrm{K^4}$)')
plt.ylabel('$E_T$ ($\\mathrm{W/mm^2}$)')
plt.title('斯特藩–玻尔兹曼定律验证')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
