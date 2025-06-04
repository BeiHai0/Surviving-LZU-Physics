import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import matplotlib

# 设置中文和负号显示
matplotlib.rcParams['font.family'] = 'SimSun'
matplotlib.rcParams['axes.unicode_minus'] = False

# 1. 已知样品数据（折射率，波长位移 Δλ）
n_known = np.array([1.3395, 1.3460, 1.3540, 1.3616, 1.3676]).reshape(-1, 1)
delta_lambda_known = np.array([0, 11.68, 25.90, 40.41, 54.96])

# 2. 拟合：Δλ = a·n + b
model = LinearRegression()
model.fit(n_known, delta_lambda_known)

a = model.coef_[0]
b = model.intercept_
print(f"拟合直线: Δλ = {a:.5f} × n + {b:.5f}")

# 3. 未知样品波长位移；n_measured 作为真值
delta_lambda_unknown = np.array([4.12, 36.16])
n_measured = np.array([1.3425, 1.3685])

# 4. 根据波长位移和拟合直线预测未知样品折射率
# Δλ = a·n + b  →  n = (Δλ - b)/a
n_predicted = (delta_lambda_unknown - b) / a

# 5. 相对误差
relative_error = (n_predicted - n_measured) / n_measured * 100

for i in range(len(n_predicted)):
    print(f"未知{i+1}: 测量 n = {n_predicted[i]:.5f}, 真值 n = {n_measured[i]:.5f}, 相对偏差 = {relative_error[i]:.2f}%")

# 6. 绘图
plt.figure(figsize=(8, 6))

# 拟合曲线
n_fit = np.linspace(1.338, 1.370, 200).reshape(-1, 1)
delta_lambda_fit = model.predict(n_fit)
plt.plot(n_fit, delta_lambda_fit, label='线性拟合', color='blue')


# 已知点
plt.scatter(n_known, delta_lambda_known, color='green', label='已知样品', zorder=5)

# 预测点及横线
for i in range(len(delta_lambda_unknown)):
    dl = delta_lambda_unknown[i]
    n_pred = n_predicted[i]
    n_meas = n_measured[i]

    # 横线
    plt.hlines(y=dl, xmin=1.338, xmax=n_pred, color='gray', linestyles='dashed')
    # 交点（预测点）
    plt.scatter(n_pred, dl, color='red', marker='x', s=100, label='预测折射率' if i == 0 else "")
    # 注释
    plt.text(n_pred + 0.0003, dl + 0.8,
             f"n测量: {n_pred:.5f}\nn真值: {n_meas:.5f}",
             fontsize=9, color='black')

# 图形设置
plt.xlabel("折射率 n")
plt.ylabel("波长位移 Δλ (nm)")
plt.title("折射率与波长位移线性拟合\n并估算未知溶液折射率")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
