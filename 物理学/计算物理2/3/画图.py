import matplotlib.pylab as plt
import numpy as np

plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题

data_x1 = np.loadtxt("a.txt")
data_y1 = np.loadtxt("b.txt")

data_x2 = np.loadtxt("c.txt")
data_y2 = np.loadtxt("d.txt")

X = np.linspace(0, 2*np.pi,100,endpoint=True)
Y = np.sin(X)

plt.scatter(data_x1, data_y1, c = 'r', marker = '*', label = "4次函数")
plt.scatter(data_x2, data_y2, c = 'r', marker = '.', label = "8次插值")
plt.plot(X, Y, label = "正弦曲线" )
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()