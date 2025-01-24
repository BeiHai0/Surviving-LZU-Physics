import numpy as np
import matplotlib.pyplot as plt

class Linear_Regression:
    def __init__(self, X, Y):
        self.X = X # 
        self.Y = Y # 
        self.k = 2 # 斜率初始化为2
        self.b = 0 # 截距初始化为0
    
    def update_coeffs(self, learning_rate): #梯度下降法更新参数
        Y_pred = self.predict() 
        m = len(self.Y)
        self.k -= learning_rate * (1/m) * np.sum( (Y_pred - self.Y) * self.X )
        self.b -= learning_rate * (1/m) * np.sum( Y_pred - self.Y )
    
    def predict(self, X = []):
        Y_pred = np.array([])
        if not X:
            X = self.X

        Y_pred = self.k * X + self.b
        return Y_pred
        
    def get_current_error(self, Y_pred): #计算当前相对误差
        return np.mean(abs(Y_pred - self.Y) / self.Y) #当前平均相对误差
    
    def compute_cost(self, Y_pred): #计算代价函数
        m = len(self.Y)
        J = (1 / (2*m)) * (np.sum((Y_pred - self.Y)*(Y_pred - self.Y)))
        return J
    

def u_A(array, N, t):
    average = np.average(array)
    u_A = np.sqrt( np.sum( (array-average)**2 ) / ( N*(N-1) ) ) * t
    return u_A
    

# 实验原始数据

m_0 = 0.5 * 1e-3 # 单个砝码质量 单位:kg 

m = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0]) * 1e-3 # 累加砝码质量 单位: kg

U_V = np.array([14.0, 28.1, 41.7, 56.2, 70.9, 84.6 ]) * 1e-3 # 与砝码对应的电压 单位: V

D_2 = np.array([33.10, 33.20, 33.18, 33.16, 33.16]) * 1e-3 # 圆环内径 单位: m

D_1 = np.array([34.80, 34.72, 34.82, 34.72, 34.72, 34.68]) * 1e-3 # 圆环外径 单位: m

U_1 = np.array([7.0, 7.2, 7.1, 7.3, 7.0]) * 1e-3 # U_1 单位: V

U_2 = np.array([-39.0, -38.8, -38.8, -38.8, -38.9]) * 1e-3 # U_2 单位: V

# 计算

g = 9.793 # 重力加速度 单位: m/s^2

delta_U = U_1 -U_2

delta_U_bar = np.average(delta_U)
u_A_delta_U = np.sqrt( np.sum((delta_U - delta_U_bar)**2) ) / np.sqrt(5*4) * 1.14
u_B_delta_U = 1e-4 / np.sqrt(3)
u_delta_U = np.sqrt(u_A_delta_U**2 + u_B_delta_U**2)

print(f"delta_U_bar:{delta_U_bar}")
print(f"u_A of delta_U:{u_A_delta_U}")
print(f"u_B of delta_U:{u_B_delta_U}")
print(f"u of delta_U:{u_delta_U}")

learning_rate = 1e-2

F = m * g

# 逐差法计算 k 的平均值

tmp = 0.0

for i in range(3):
    tmp += U_V[i+3] - U_V[i]

k_bar = tmp / (3 * m_0 * g) / 3

print(f"k_bar : {k_bar}")

# 求 D_1_bar

D_1_bar = np.average(D_1)
print(f"D_1_bar:{D_1_bar}")

# 求 D_2_bar

D_2_bar = np.average(D_2)
print(f"D_2_bar:{D_2_bar}")

# 计算表面张力系数平均值

sigma_bar = delta_U_bar / ( np.pi * k_bar * (D_1_bar + D_2_bar) ) 
print(f"sigma_bar:{sigma_bar}")

t = 1.11 # t因子，计算A类不确定度时用到

u_A_D_1 = u_A(D_1, 6, t)
u_B_D_1 = 2e-5 / np.sqrt(3)
u_D_1 = np.sqrt(u_A_D_1**2 + u_B_D_1**2)

u_A_D_2 = u_A(D_2, 6, t)
u_B_D_2 = 2e-5 / np.sqrt(3)
u_D_2 = np.sqrt(u_A_D_2**2 + u_B_D_2**2)

print(f"u_A of D_1:{u_A_D_1}")
print(f"u_B of D_1:{u_B_D_1}")
print(f"u of D_1:{u_D_1}")

print(f"u_A of D_2:{u_A_D_2}")
print(f"u_B of D_2:{u_B_D_2}")
print(f"u of D_1:{u_D_2}")

u_sigma = sigma_bar * np.sqrt( (u_delta_U/delta_U_bar)**2 + (u_D_1**2+u_D_2**2)/(D_1_bar + D_2_bar)**2 )
print(f"u of sigma:{u_sigma}")






# regressor = Linear_Regression(F, U_V)

# epoch = 100000

# for i in range(epoch):
#    regressor.update_coeffs(learning_rate)
#    if i % 10 == 0:
#        prediction = regressor.predict()
#        print(f"epoch: {i} ,mean relative error: {regressor.get_current_error(prediction)}")

# k = regressor.k
# b = regressor.b

# print(f"斜率为:{k}")
# print(f"截距为:{b}")


# 计算公式： sigma = delta_U / ( pi*k*(D_1+D_2) )



