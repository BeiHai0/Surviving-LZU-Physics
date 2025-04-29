## Logistic Regression

假如我们有数据集,共有$m$组数据：
$$
(\vec{x}^{(1)},y^{(1)}),(\vec{x}^{(2)},y^{(2)}),\cdots,(\vec{x}^{(m)},y^{(m)})
$$
其中，向量$\vec{x}^{(i)} $有$n$个元素：
$$
\vec{x}^{(i)}=
\begin{bmatrix}
x^{(i)}_1 \\
x^{(i)}_2 \\
\vdots \\
x^{(i)}_n
\end{bmatrix}
$$

定义：
$$
\vec{w}=
\begin{bmatrix}
w_1 \\
w_2 \\
\vdots \\
w_n
\end{bmatrix}
$$

为神经网络的$n$个参数.

定义：$b$也是神经网络的参数

定义：
$$
z^{(i)}
=\vec{w}^T\vec{x}^{(i)}+b=w_1x^{(i)}_1+w_2x^{(i)}_2+\cdots+w_nx^{(i)}_n+b
$$

$$
\hat{y}^{(i)}= \sigma(z^{(i)})=\frac{1}{1+e^{-z^{(i)}}}
$$

其中，$\sigma(x)$定义为：
$$
\sigma(x)=\frac{1}{1+e^{-x}}
$$

显然，$\sigma(x)\in(0,1) $,这对只有$0,1$两种结果的学习很有好处.

定义一个数据点的损失函数：
$$
\mathcal{L}(\hat{y}^{(i)},y^{(i)})=-(y\ln\hat{y}+(1-y)\ln{(1-\hat{y}})   )
$$

对于整个训练集，定义代价函数：
$$
J=J(\vec{w},b)=\frac{1}{m}\sum_{i=1}^m\mathcal{L}(\hat{y}^{(i)},y^{(i)})
$$

为了让整个训练集的代价函数最小，要通过梯度下降法来调整$\vec{w},b $的取值，也就是要调整$w_1,w_2,\cdots,w_n,b $的取值.

由梯度下降法知，要作如下调整：
$$
w_j\rightarrow w_j-\alpha\frac{\partial J(\vec{w},b)}{\partial w_j} \\

b\rightarrow b-\alpha\frac{\partial J(\vec{w},b)}{\partial b}
$$

其中，$\alpha$称为学习率，$\alpha$必须大于零才能使得$w_i,b$向着使得代价函数减小的方向改变.

所以关键是求出那两个偏导数.

给定训练集：
$$
(\vec{x}^{(i)},y^{(i)})(i=1,2,\cdots,n)
$$

我们要找到使代价函数最小的:
$$
\vec{w},b
$$

在寻找的过程中，$\vec{w},b $是变量，训练集是给定的，不变的，我们通过梯度下降法原理不断微调$\vec{w},b $,使得最后的$\vec{w},b $能使得代价函数尽可能小.


回想各变量间的关系：
$$
\vec{w},b
\rightarrow
z^{(i)}=\vec{w}^T\vec{x}^{(i)}+b
=(w_1x^{(i)}_1+w_2x^{(i)}_2+\cdots+w_nx^{(i)}_n)+b
\rightarrow
\hat{y}=\sigma(z^{(i)})
\rightarrow
\mathcal{L}(\hat{y},y^{(i)})
\rightarrow
J(\vec{w},b)
$$

所以由链式法则：
$$
\frac{\partial J(\vec{w},b)}{\partial w_j}
=\frac{\partial }{\partial w_j}\bigg[\frac{1}{m}\sum_{i=1}^m \mathcal{L}(\hat{y}^{(i)},y^{(i)}) \bigg]
=\frac{1}{m}\sum_{i=1}^m \frac{\partial \mathcal{L}(\hat{y}^{(i)},y^{(i)})}{\partial w_j}
=\frac{1}{m}\sum_{i=1}^m\frac{\partial \mathcal{L}(\hat{y}^{(i)},y^{(i)})}{\partial\hat{y}^{(i)}}\frac{\partial \hat{y}^{(i)}}{\partial z^{(i)}}\frac{\partial z^{(i)}}{\partial w_j}
$$

同理：
$$
\frac{\partial J(\vec{w},b)}{\partial b}
=\frac{1}{m}\sum_{i=1}^m \frac{\partial \mathcal{L}(\hat{y}^{(i)},y^{(i)})}{\partial\hat{y}^{(i)}}\frac{\partial \hat{y}^{(i)}}{\partial z^{(i)}}\frac{\partial z^{(i)}}{\partial b}
$$

首先注意到，以上两个偏导数的推导结果中都是另外三个偏导数相乘的形式，其中前两项偏导完全一样.

然后注意到：
$$
\frac{\partial \mathcal{L}(\hat{y}^{(i)},y^{(i)})}{\partial\hat{y}^{(i)}}
=\frac{\partial}{\partial \hat{y^{(i)}}}[-(y^{(i)}\ln\hat{y}^{(i)}+(1-y^{(i)})\ln(1-\hat{y}^{(i)})]
=\frac{1-y^{(i)}}{1-\hat{y}^{(i)}}-\frac{y^{(i)}}{\hat{y}^{(i)}}
$$

$$
\frac{\partial \hat{y}^{(i)}}{\partial z^{(i)}}
=\frac{\partial \sigma(z^{(i)})}{\partial z^{(i)}}
=\frac{e^{z^{(i)}}}{(1+e^{-z^{(i)}})^2}
=\hat{y}^{(i)}(1-\hat{y}^{(i)})
$$

$$
\frac{\partial z^{(i)}}{\partial w_j}=x^{(i)}_j
$$

$$
\frac{\partial z^{(i)}}{\partial b}=1
$$

于是：
$$
\frac{\partial J(\vec{w},b)}{\partial w_j}
=\frac{1}{m}\sum_{i=1}^m \bigg[\frac{1-y^{(i)}}{1-\hat{y}^{(i)}}-\frac{y^{(i)}}{\hat{y}^{(i)}}\bigg] \hat{y}^{(i)} (1-\hat{y}^{(i)}) x^{(i)}_j
=\frac{1}{m}\sum_{i=1}^m (\hat{y}^{(i)}-y^{(i)})x^{(i)}_j
=\frac{1}{m}\sum_{i=1}^m(\sigma(\vec{w}^T\vec{x}^{(i)}+b)-y^{(i)})x^{(i)}_j
$$

$$
\frac{\partial J(\vec{w},b)}{\partial b}
=\frac{1}{m}\sum_{i=1}^m \bigg[\frac{1-y^{(i)}}{1-\hat{y}^{(i)}}-\frac{y^{(i)}}{\hat{y}^{(i)}}\bigg] \hat{y}^{(i)} (1-\hat{y}^{(i)})
=\frac{1}{m}\sum_{i=1}^m (\hat{y}^{(i)}-y^{(i)})
=\frac{1}{m}\sum_{i=1}^m(\sigma(\vec{w}^T\vec{x}^{(i)}+b)-y^{(i)})
$$

由上可知，为了求出这两个偏导，我们需要准备“材料”(注意，在实际编程过程中，由于偏导数不好表示，于是我们把一个样本点的损失函数对某个变量$x$的偏导记为$dx$)：
$$
dz^{(i)}
= \frac{\partial \mathcal{L}(\hat{y}^{(i)},y^{(i)})}{\partial \hat{y}^{(i)}}\frac{\partial \hat{y}^{(i)}}{\partial z^{(i)}} \\
d\hat{y}^{(i)}
= \\
J=
$$

$J$只是用来记录一下利用梯度下降法求$\vec{w},b $的过程中的损失函数.

## for 循环实现：

很慢，要尽量减少for循环的使用

## 向量化实现(Vectorization)：

已知神经网络的参数：
$$
\vec{w}
=
\begin{bmatrix}
w_1 \\
w_2 \\
\vdots \\
w_n
\end{bmatrix}
和b
$$

为了避免使用python中的for循环，要想办法利用numpy库中的函数,如np.dot(),来进行快速计算以节省时间.

构造：
$$
X = 
\begin{bmatrix}
\vec{x}^{(1)}, \vec{x}^{(2)},\cdots,\vec{x}^{(n)}
\end{bmatrix}
$$

$$
Y = 
\begin{bmatrix}
y^{(1)}, y^{(2)}, \cdots, y^{(n)}
\end{bmatrix}
$$

定义：
$$
Z = 
\vec{w}X+b
=
\vec{w}
\begin{bmatrix}
\vec{x}^{(1)}, \vec{x}^{(2)},\cdots,\vec{x}^{(n)}
\end{bmatrix}
+b
=
\begin{bmatrix}
\vec{w}\vec{x}^{(1)}+b, \vec{w}\vec{x}^{(2)}+b ,\cdots, \vec{w}\vec{x}^{(n)}+b
\end{bmatrix}
$$

注意到，$Z$是一个$1\times n$的行向量.之前我们定义了$\sigma $函数，此函数输入一个数，相应地输出一个数.在这里我们扩展$\sigma$函数的定义，规定当一个行向量作为$\sigma$函数的输入时，相应的输出是一个同样规模的行向量,输出的行向量的各元素是输入行向量对应位置上元素受$\sigma$函数作用后所输出的数.即规定：
$$
\sigma(Z)
=
\begin{bmatrix}
\sigma(\vec{w}\vec{x}^{(1)}+b),
\sigma(\vec{w}\vec{x}^{(2)}+b),
\cdots,
\sigma(\vec{w}\vec{x}^{(n)}+b)
\end{bmatrix}
$$

定义：
$$
dZ=\sigma(Z)-Y=
$$












softmax 函数

$$
y_k=\frac{\exp(a_k)}{\sum_{i=1}^n \exp(a_i)}
$$

性质：

所有神经元输出都在0,1之间；输出之和为1，可以看作“概率”

防止softmax函数溢出的处理：

$$
y_k=\frac{\exp(a_k+C)}{\sum_{i=1}^n\exp(a_i+C)}
$$



one-hot 表示

将正确解标签表示为1，其他标签表示为0


均方误差(mean squared error)

$y_k$表示神经网络输出数据的第$k$维，$t_k$表示监督数据的第$k$维

$$
E=\frac{1}{2}\sum_k(y_k-t_k)^2
$$



交叉熵误差(cross entropy error)

只计算正确解标签的输出的自然对数的相反值

$$
E=-\sum_k t_k\ln y_k
$$

对所有训练数据：

假设共有$N$个训练数据，$t_{nk} $表示第$n$个监督数据的第$k$个元素，$y_{nk} $是神经网络的输出的第$k$个元素

$$
E=-\frac{1}{N}\sum_n\sum_k t_{nk}\ln y_{nk}
$$

mini-batch 学习

从一大批数据中选取一小批数据进行学习

前向差分：



中心差分：

another activate function:

$$
\tanh (z)=\frac{e^z-e^{-z}}{e^z+e^{-z}}
$$

性质:$-1$到$1$之间；奇函数

Leaky-Relu:

max(0.01z,z)


autograd:

只有浮点数才能计算梯度，整型不能计算梯度(因为可能计算出的梯度值为浮点数)

不能重复调用.backward()，否则会报错

x.grad : 利用链式法则计算对x的偏导

$$
x = [x_1,x_2,\cdots,x_n] \\

$$

z.backward()

若z为标量，括号里可以不要参数. 也就是说，backward可以自动计算标量对矩阵的梯度

但若z为矩阵，括号里必须要参数，否则会报错.比如，若想计算梯度，括号里的参数应为与z形状一样的、元素全为1的矩阵.作用是:

先计算$z* torch.ones\_like(z)$(元素级乘法)，于是得到了一个标量：

$z_{11}+z_{12}+\cdots+$

这时候再求梯度就没问题了

那么类似地，下面的代码也应该能正确计算梯度：

z.sum().backward()

实验证明，确实如此


对bias : np.zeros()

对weights : np.random.randn()*0.01 

$$
z^{[l]}=W^{[l]}a^{[l-1]}+b^{[l]} \\
a^{[l]}=g^{[l]}(z^{[l]})
$$

vectorized:

$$
Z^{[l]}=W^{[l]}A^{[l-1]}+b^{[l]}~~~(broadcast) \\
A^{[l]}=g^{[l]}(Z^{[l]})
$$


$$
W^{[l]}:n^{[l]}\times n^{[l-1]} matrix \\
b^{[l]}:n^{[l]}\times 1 matrix
$$

vectorized(presume $m$ samples):

$$
(l\ne 1)Z^{[l]}:n^{[l]}\times m~~~ matrix \\
(l\ne 1)A^{[l]}:n^{[l]}\times m~~~ matrix
$$
