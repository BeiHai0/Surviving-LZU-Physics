import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"]=["SimHei"] # 设置字体
plt.rcParams["axes.unicode_minus"]=False # 该语句解决图像中的“-”负号的乱码问题

class Linear_Regression:
    def __init__(self, X, Y):
        self.X = X # ln t
        self.Y = Y # ln L_n
        self.k = 1 # 斜率初始化为1
        self.b = 1 # 截距初始化为1
    
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
        
#理论公式：L_n = 1/(2f) sqrt(T/sigma)
#两边取自然对数：ln L_n = 1/2 ln T - ln (2f sqrt(sigma))
#以 ln T 为横坐标，ln L_n 为纵坐标，测得的数据为训练集拟合出一条直线，看拟合出的直线与理论计算得出的直线有多大差别

delta = 1e-6 #当对数函数的输入很小时，输出会很大，加上一个小量防止这种情况
f = 50 #弦线频率
sigma = 3.25 * 1e-4 #弦线线密度
L_n = np.array([
    0.4250, 0.3123, 0.2369, 0.1503, 0.1274
]) #驻波波长
T = np.array([
    0.482, 0.242, 0.186, 0.093, 0.089
]) #拉力

X = np.log(T + delta) # ln T
Y = np.log(L_n + delta) # ln L_n


learning_rate = 0.005 #学习率
epoch = 100000 #训练次数

regressor = Linear_Regression(X, Y)

for i in range(epoch):
    Y_pred = regressor.predict()
    if(i % 10 == 0):
        cost = regressor.compute_cost(Y_pred)
        print(f"epoch : {i}:当前cost为 : {cost}")
        error = regressor.get_current_error(Y_pred)
        print(f"epoch : {i}:当前误差为 : {error}")
        
    regressor.update_coeffs(learning_rate)

k = regressor.k
b = regressor.b

print(f"拟合后线性函数的斜率 : {k}")
print(f"拟合后线性函数的截距 : {b}")
print(f"根据数据计算得出的弦线线密度 : { 1/(20*f*f)*np.sum(T / L_n**2) }")

print(f"斜率k与1/2的误差为 : {(k-1/2)*2}")
print(f"截距b与 -ln ( 2f sqrt(sigma) )的误差为 : \
{(b + np.log(2*f*np.sqrt(sigma)))/(-np.log(2*f*np.sqrt(sigma)))}")

plt.scatter(X, Y, c = 'r', marker = '*', label = "measured data")
plt.plot(X, Y_pred, label = "fitting line")
plt.xlabel("ln T ")
plt.ylabel("ln L_n")
plt.title("弦振动实验数据直线拟合")
plt.legend()
plt.show()