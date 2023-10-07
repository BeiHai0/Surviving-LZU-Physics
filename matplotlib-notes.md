plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体

plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题

import matplotlib.pylab as plt

```
plt.scatter(X, Y, c = 'r', marker = '*', label = "measured data")
plt.plot(X, Y_pred, label = "fitting line")
plt.xlabel("ln T ")
plt.ylabel("ln L_n")
plt.title("弦振动实验数据直线拟合")
plt.legend()
plt.show()
```
