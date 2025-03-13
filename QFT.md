# 1 辐射的微观理论

## 1.1 黑体辐射

## 1.2 爱因斯坦系数

## 1.3 量子场论

# 2 洛伦兹不变性和二次量子化

取 $\hbar=c=1 $。

## 2.1 洛伦兹不变性

### 2.1.1 旋转

2维旋转

$$
x\to x'=x\cos\theta+y\sin\theta
$$

$$
y\to y'=-x\sin\theta+y\cos\theta
$$

$$
\begin{bmatrix}
x \\
y
\end{bmatrix} \to 
\begin{bmatrix}
x' \\
y'
\end{bmatrix}
=\begin{bmatrix}
\cos\theta &\sin\theta \\
-\sin\theta &\cos\theta
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix}
$$

$$
x_i\to x_i'=R_{ij}x_j,\quad 
x_i=\begin{bmatrix}
x \\
y
\end{bmatrix},\quad i=1,2
$$

行矢量：

$$
x^i
=\begin{bmatrix}
x &y
\end{bmatrix}
\to \begin{bmatrix}
x' &y'
\end{bmatrix}
=\begin{bmatrix}
x &y
\end{bmatrix}
\begin{bmatrix}
\cos\theta &-\sin\theta \\
\sin\theta &\cos\theta
\end{bmatrix}
=x^j \left(R^{\mathrm{T}} \right)^{ji}
$$

$$
R^{\mathrm{T}} R = I
$$

$$
\left(R^{\mathrm{T}} \right)_{ij}R_{ik}=\delta_{ik}
$$

$$
x^i x_i
=x^2+y^2
$$

$$
x'^ix'_i
=x^j\left(R^{\mathrm{T}} \right)^{ji} R_{ik}x_k
=x^j\delta_{jk}x_k
=x^jx_j
$$

### 2.1.2 洛伦兹变换

$$
s^2\equiv t^2-x^2-y^2-z^2
$$

## 2.2 经典平面波作为谐振子

### 2.2.1 简单谐振子

经典谐振子

$$
m\ddot{x}+kx=0
$$

通解

$$
x(t)=c_1\mathrm{e}^{\mathrm{i}\omega t} + c_2\mathrm{e}^{-\mathrm{i}\omega t},\quad \omega=\sqrt{\frac{k }{m } }
$$

体系哈密顿量

$$
H=\frac{p^2 }{2m } + \frac{1 }{2 } m\omega^2 x^2
$$

为了对谐振子进行量子化，把 $x,p $ 视为算符，且它们满足正则对易关系

$$
\left[x,p \right]=\mathrm{i}
$$

构造湮灭算符和产生算符

$$
a=\sqrt{\frac{m\omega }{2 } }\left(x+\frac{\mathrm{i}p }{m\omega }  \right),\quad
a^\dag=\sqrt{\frac{m\omega }{2 } }\left(x-\frac{\mathrm{i}p }{m\omega } \right)
$$

它们的对易关系为：

$$
\left[a,a^\dag \right]=1
$$

哈密顿量可由它们表达：

$$
H=\omega\left(a^\dag a+\frac{1 }{2 }  \right)
$$

构造粒子数算符

$$
\hat{N}\equiv a^\dag a
$$

计算发现其与哈密顿算符对易：

$$
\left[\hat{N},H \right]
=\left[a^\dag a , \omega\left(a^\dag a+\frac{1 }{2 }  \right) \right]
=0
$$

因此它们有共同本征态。

粒子数算符的本征方程记为：

$$
\hat{N}\ket{n}=n\ket{n}
$$

$a^\dag,a $ 对 $\ket{n} $ 的作用效果为：

$$
a^\dag\ket{n} = \sqrt{n+1}\ket{n+1}
$$

$$
a\ket{n} = \sqrt{n}\ket{n-1}
$$

在海森堡绘景中，算符随时间演化而态矢不随时间演化。$a $ 随时间演化服从海森堡运动方程：

$$
\mathrm{i}\frac{\mathrm{d} }{\mathrm{d}t } a
=\left[a , H \right]
=\left[a , \omega\left(a^\dag a+\frac{1 }{2 }\right) \right]
=\omega a
$$

即：

$$
\frac{\mathrm{d}a }{a } = -\mathrm{i}\omega\mathrm{d}t
$$

积分得：

$$
a(t) = \mathrm{e}^{-\mathrm{i}\omega t}a(0)
$$

### 2.2.2 与SR的联系

最简单的洛伦兹不变的场的运动方程：

$$
\square \phi = \left(\partial_t^2 - \nabla^2 \right)\phi = 0
$$

一种特解是平面波解：

$$
\phi(\vec{x},t)
=a_p(t)\mathrm{e}^{\mathrm{i}\vec{p}\cdot\vec{x}}
$$

其中 $a_p(t) $ 满足：

$$
\left(\partial_t^2 + \vec{p}\cdot\vec{p} \right)a_p(t) = 0
$$

可以解得：

$$
a_p(t)
=a_p\mathrm{e}^{-\mathrm{i}\omega_p t},\quad\omega_p\equiv \left|\vec{p} \right|
$$

其中 $a_p $ 是复常数。

通解则可写为：

$$
\begin{aligned}
\phi(\vec{x},t)
&=\frac{1 }{\left(2\pi \right)^3 } \int \mathrm{d}^3\vec{p}\left[a_p(t)\mathrm{e}^{\mathrm{i}\vec{p}\cdot\vec{x}} + a_p^*(t)\mathrm{e}^{-\mathrm{i}\vec{p}\cdot\vec{x}} \right] \\
&=\frac{1 }{\left(2\pi \right)^3 } \int \mathrm{d}^3\vec{p}\left[a_p\mathrm{e}^{\mathrm{i}\left(-\omega_p t + \vec{p}\cdot\vec{x} \right)} + a_p^*\mathrm{e}^{-\mathrm{i}\left(-\omega_p + \vec{p}\cdot\vec{x} \right)} \right] \\
&=\frac{1 }{\left(2\pi \right)^3 } \int \mathrm{d}^3\vec{p} \left(a_p\mathrm{e}^{-\mathrm{i}p\cdot x} + a_p^*\mathrm{e}^{\mathrm{i}p\cdot x} \right)
\end{aligned}
$$

其中

$$
p_\mu=\left(\omega_p,\vec{p} \right),\quad\omega_p\equiv \left|\vec{p} \right|
$$

$$
p\cdot x
\equiv p^\mu x_\mu
=\omega_p x_0 - \vec{p}\cdot\vec{x}
$$

电磁场张量：

$$
F_{\mu\nu}
\equiv\begin{bmatrix}
0 &E_x &E_y &E_z \\
-E_x &0 &-B_z &B_y \\
-E_y &B_z &0 &-B_x \\
-E_z &-B_y &B_x &0
\end{bmatrix}
$$

麦克斯韦方程：

$$
\partial_\mu F_{\mu\nu} = 0,\quad
\partial_\mu F_{\nu\rho} + \partial_\nu F_{\rho\mu} + \partial_\rho F_{\mu\nu} = 0
$$

其与电磁势关系：

$$
F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu
$$

洛伦兹规范：

$$
\partial_\mu A_\mu = 0
$$

洛伦兹规范下，麦克斯韦方程可化为关于电磁势的方程：

$$
0=\partial_\mu F_{\mu\nu}
=\partial_\mu\left(\partial_\mu A_\nu - \partial_\nu A_\mu \right)
=\partial_\mu\partial_\mu A_\nu
=\square A_\nu
$$

即 $A_\nu $ 的每个分类都满足最小洛伦兹不变方程。

## 2.3 二次量子化

$$
H_0
=\frac{1 }{\left(2\pi \right)^3 } \int \mathrm{d}^3\vec{p} \omega_p \left(a_p^\dag a_p + \frac{1 }{2 }  \right) 
$$

$$
\omega_p = \left|\vec{p} \right|
$$

二次量子化中，希尔伯特空间推广为 Fock 空间

$$
\mathcal{F}=\oplus_n \mathcal{H}_n
$$

### 2.3.1 




