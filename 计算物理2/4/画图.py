import matplotlib.pylab as plt
import numpy as np

plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题

data_x1 = np.loadtxt("a.txt")
data_y1 = np.loadtxt("b.txt")



X = np.linspace(-5.0, 5.0, 500, endpoint=True)
Y = 0.551931*X -0.024893

plt.scatter(data_x1, data_y1, c = 'r', marker = '*', label = "数据点")

plt.plot(X, Y, label = "p(x)=-0.024893+0.551931x" )
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()