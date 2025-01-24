import numpy as np
import matplotlib.pyplot as plt

# 假设过定点 (x_0,y_0)

class Linear_Regression_through_fixed_point:
    def __init__(self, X, Y, x_0, y_0):
        self.X = X
        self.Y = Y
        self.x_0 = x_0
        self.y_0 = y_0
        self.k = -0.1 # 设置初值为-1

        self.m = len(Y)

    def forward_propagation(self):
        Y_predict = self.k*self.X-self.k*self.x_0+self.y_0
        return Y_predict
    
    def update_coeffs(self, learning_rate):
        Y_predict = self.forward_propagation()
        self.k -= learning_rate / self.m * np.sum( (Y_predict - self.Y) * (self.X - self.x_0 ) )

    def compute_cost(self, Y_predict):
        print(f"current cost is : {1/(2*self.m) * np.sum( (Y_predict-self.Y)**2 ) }")

X1 = np.array([0.0, 20.0, 40.0, 60.0,])
Y1 = np.array([41.7, 41.6, 41.4, 41.4,])
x_0_1 = 80.0
y_0_1 = 41.2

learning_rate = 0.000001 # 我去，learning_rate 设成0.01, cost 简直要起飞了！超参数太重要了！
epoch = 10000

regressor1 = Linear_Regression_through_fixed_point(X1, Y1, x_0_1, y_0_1)

for i in range(epoch):
    Y_predict = regressor1.forward_propagation()
    regressor1.update_coeffs(learning_rate)
    if i % 10 == 0 :
        regressor1.compute_cost(Y_predict)


X3 = np.arange(350, 471, 20)
Y3 = np.array([20.8, 20.8, 20.8, 20.8, 20.8, 20.8, 21.0])
x_0_3 = 330
y_0_3 = 20.7
regressor3 = Linear_Regression_through_fixed_point(X3, Y3, x_0_3, y_0_3)

learning_rate = 0.000001 # 我去，learning_rate 设成0.01, cost 简直要起飞了！超参数太重要了！
epoch = 10000

for i in range(epoch):
    Y_predict = regressor3.forward_propagation()
    regressor3.update_coeffs(learning_rate)
    if i % 10 == 0 :
        regressor3.compute_cost(Y_predict)

        
print(f"直线1的斜率k为:{regressor1.k}")
print(f"直线1的斜截式为:y={regressor1.k}x+{regressor1.y_0-regressor1.k*regressor1.x_0}")
print(f"直线3的斜率k为:{regressor3.k}")
print(f"直线3的斜截式为:y={regressor3.k}x+{regressor3.y_0-regressor3.k*regressor3.x_0}")

