import numpy as np

# y = a x + b

x = np.array([0.99, 1.04, 1.09, 1.14, 1.19, 1.24, 1.29])
y = np.array([28, 29, 31, 32, 33, 35, 36])

N = np.size(x) # 数据点个数

t =  2.78# t因子

x_bar = np.mean(x)
y_bar = np.mean(y)

a = np.sum( (x-x_bar)*(y-y_bar) ) / np.sum( (x-x_bar)**2 ) # 斜率a的估计值
b = y_bar - a*x_bar # 截距b的估计值

sigma = np.sqrt( 1/(N-2) * np.sum( (y-b-a*x)**2 ) )
s_x = np.sqrt( 1/N * np.sum( (x-x_bar)**2 ) )

UA_a = t * sigma / np.sqrt(N) / s_x # 斜率a的A类不确定度
UA_b = t * sigma / np.sqrt(N) * np.sqrt(1 + x_bar**2 / s_x**2) # 截距b的A类不确定度

print("斜率a的估计值:a=",a)
print("截距b的估计值:b=",b)
print("斜率a的A类不确定度:UA_a=",UA_a)
print("截距b的A类不确定度:UA_b=",UA_b)




