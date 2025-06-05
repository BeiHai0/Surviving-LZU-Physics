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
=\int \frac{\mathrm{d}^3\vec{p} }{\left(2\pi \right)^3 }  \omega_p \left(a_p^\dag a_p + \frac{1 }{2 }  \right) 
$$

$$
\omega_p = \left|\vec{p} \right|
$$

二次量子化中，希尔伯特空间推广为 Fock 空间

$$
\mathcal{F}=\oplus_n \mathcal{H}_n
$$

### 2.3.1 

等时对易关系：

$$
\left[a_k , a_p^\dag \right] = \left(2\pi \right)^3 \delta^{3}\left(\vec{p}-\vec{k} \right)
$$

$$
\left[a_k , a_p \right] = \left[a_k^\dag , a_p^\dag \right] = 0
$$

$a_p^\dag $ 算符产生动量为 $p $ 的粒子：

$$
a_p^\dag\ket{0} = \frac{1 }{\sqrt{2\omega_p} } \Ket{\vec{p}},\quad
a_p\ket{0} = \ket{0}
$$

厄米共轭：

$$
\bra{0}a_p = \frac{1 }{\sqrt{2\omega_p} } \bra{\vec{p}},\quad
\bra{0}a_p^\dag = \bra{0}
$$

其中 $\ket{\vec{p}} $ 是具有动量 $\vec{p} $ 的单粒子态。

$$
\braket{0|0}=1
$$

导致：

$$
\begin{aligned}
\Braket{\vec{p}|\vec{k}}
&=2\sqrt{\omega_p\omega_k}\red{\Braket{0|a_pa_k^\dag|0}} \\
&=2\sqrt{\omega_p\omega_k}\Braket{0|\left[a_p , a_k^\dag \right] + a_k^\dag a_p|0} \\
&=2\sqrt{\omega_p\omega_k}\Braket{0|\left(2\pi \right)^3\delta^3\left(\vec{p}-\vec{k} \right) + a_k^\dag a_p|0} \\
&=2\sqrt{\omega_p\omega_{\blue{k}}}\left(2\pi \right)^3\delta^3\left(\vec{p}-\vec{k} \right) + 2\sqrt{\omega_p\omega_k}\Braket{0|a_k^\dag a_p|0} \\
&=2\sqrt{\omega_p\omega_{\blue{p}}}\left(2\pi \right)^3\delta^3\left(\vec{p}-\vec{k} \right) \\
&=2\omega_p\red{\left(2\pi \right)^3 \delta^3\left(\vec{p}-\vec{k} \right)} \\
\end{aligned}
$$

单粒子态恒等算符：

$$
\bold{1}
=\int\frac{\mathrm{d}^3\vec{p} }{\left(2\pi \right)^3 } \frac{1 }{2\omega_p } \ket{\vec{p}}\bra{\vec{p}}
$$

检验：

$$
\begin{aligned}
\Ket{\vec{k}}
&=\int\frac{\mathrm{d}^3\vec{p} }{\left(2\pi \right)^3 } \frac{1 }{2\omega_p } \ket{\vec{p}}\Braket{\vec{p}|\vec{k}} \\
&=\int\frac{\mathrm{d}^3\vec{p} }{\left(2\pi \right)^3 } \frac{1 }{2\omega_p } \ket{\vec{p}}2\omega_p\left(2\pi \right)^3\delta^3\left(\vec{p}-\vec{k} \right) \\
&=\Ket{\vec{k}}
\end{aligned}
$$

量子场：

$$
\phi_0(\vec{x})
=\int\frac{\mathrm{d}^3\vec{p} }{\left(2\pi \right)^3 } \frac{1 }{\sqrt{2\omega_p} } \left(a_p\mathrm{e}^{\mathrm{i}\vec{p}\cdot\vec{x}} + a_p^\dag \mathrm{e}^{-\mathrm{i}\vec{p}\cdot\vec{x}} \right)
$$

下标 $0 $ 代表自由场。$\phi_0(\vec{x}) $ 是厄米算符：

$$
\phi_0^\dag(\vec{x}) = \phi_(\vec{x})
$$

计算：

$$
\begin{aligned}
\Braket{\vec{p}|\phi_0(\vec{x})|0}
&=\Braket{0|\sqrt{2\omega_p} a_p \cdot \int\frac{\mathrm{d}^3\vec{k} }{\left(2\pi \right)^3 } \frac{1 }{\sqrt{2\omega_k} } \left(a_k\mathrm{e}^{\mathrm{i}\vec{k}\cdot\vec{x}} + a_k^\dag \mathrm{e}^{-\mathrm{i}\vec{k}\cdot\vec{x}} \right) |0 } \\
&=\int\frac{\mathrm{d}^3\vec{k} }{\left(2\pi \right)^3 } \sqrt{\frac{\omega_p }{\omega_k } }\left[\mathrm{e}^{\mathrm{i}\vec{k}\cdot\vec{x}}\Braket{0|a_pa_k|0} + \mathrm{e}^{-\mathrm{i}\vec{k}\cdot\vec{x}}\Braket{0|a_pa_k^\dag|0} \right] \\
&=\int\frac{\mathrm{d}^3\vec{k} }{\left(2\pi \right)^3 } \sqrt{\frac{\omega_p }{\omega_k } }\mathrm{e}^{-\mathrm{i}\vec{k}\cdot\vec{x}}\Braket{0|a_pa_k^\dag|0}  \\
&=\int\frac{\mathrm{d}^3\vec{k} }{\left(2\pi \right)^3 } \sqrt{\frac{\omega_{\blue{p}} }{\omega_k } }\mathrm{e}^{-\mathrm{i}\vec{k}\cdot\vec{x}}\left(2\pi \right)^3\delta^3\left(\vec{p}-\vec{k} \right)  \\
&=\int\frac{\mathrm{d}^3\vec{k} }{\left(2\pi \right)^3 } \sqrt{\frac{\omega_{\blue{k}} }{\omega_k } }\mathrm{e}^{-\mathrm{i}\vec{k}\cdot\vec{x}}\left(2\pi \right)^3\delta^3\left(\vec{p}-\vec{k} \right)  \\
&=\int\mathrm{d}^3\vec{k}\mathrm{e}^{-\mathrm{i}\vec{k}\cdot\vec{x}}\delta^3\left(\vec{p}-\vec{k} \right) \\
&=\mathrm{e}^{-\mathrm{i}\vec{p}\cdot\vec{x}}
\end{aligned}
$$

另一方面，

$$
\Braket{\vec{p}|\vec{x}} = \mathrm{e}^{-\mathrm{i}\vec{p}\cdot\vec{x}}
$$

对比可得：

$$
\phi_0(\vec{x})\ket{0}
=\ket{\vec{x}}
$$

即 $\phi_0(\vec{x}) $ 产生了一个位于 $\vec{x} $ 处的粒子。

由于 $\phi_0(\vec{x}) $ 是厄米算符，因此：

$$
\bra{0}\phi_0(\vec{x}) = \bra{\vec{x}}
$$

### 2.3.2 时间依赖性

在海森堡绘景中，算符随时间演化。

$$
a_p(t) = \mathrm{e}^{-\mathrm{i}\omega_p t}a_p,\quad
a_p^\dag(t) = \mathrm{e}^{\mathrm{i}\omega_p t}a_p^\dag
$$

其中 $a_p,a_p^\dag $ 不依赖于时间。

量子标量场：

$$
\phi_0(\vec{x},t)
=\int \frac{\mathrm{d}^3\vec{p} }{\left(2\pi \right)^3 } \frac{1 }{\sqrt{2\omega_p} } \left(a_p\mathrm{e}^{-\mathrm{i}p\cdot x} + a_p^\dag \mathrm{e}^{\mathrm{i}p\cdot x} \right)
$$

其中，$p^\mu\equiv \left(\omega_p,\vec{p} \right),\omega_p=\left|\vec{p} \right|,p\cdot x = \omega_p t-\vec{p}\cdot\vec{x} $

$$
\begin{aligned}
\left[H_0 , \phi_0(\vec{x},t) \right]
&=\left[\int \frac{\mathrm{d}^3\vec{p} }{\left(2\pi \right)^3 }  \omega_p \left(a_p^\dag a_p + \frac{1 }{2 }  \right) , \int \frac{\mathrm{d}^3\vec{k} }{\left(2\pi \right)^3 } \frac{1 }{\sqrt{2\omega_k} } \left(a_k\mathrm{e}^{-\mathrm{i}k\cdot x} + a_k^\dag \mathrm{e}^{\mathrm{i}k\cdot x} \right) \right] \\
&=\int \frac{\mathrm{d}^3\vec{p} }{\left(2\pi \right)^3 } \int \frac{\mathrm{d}^3\vec{k} }{\left(2\pi \right)^3 } \frac{\omega_p }{\sqrt{2\omega_k} } \left[ \blue{\left(a_p^\dag a_p + \frac{1 }{2 }  \right)} , \left(a_k\mathrm{e}^{-\mathrm{i}k\cdot x} + a_k^\dag \mathrm{e}^{\mathrm{i}k\cdot x} \right) \right] \\
&=\int \frac{\mathrm{d}^3\vec{p} }{\left(2\pi \right)^3 } \int \frac{\mathrm{d}^3\vec{k} }{\left(2\pi \right)^3 } \frac{\omega_p }{\sqrt{2\omega_k} } \left[ \blue{a_p^\dag a_p} , \left(a_k\mathrm{e}^{-\mathrm{i}k\cdot x} + a_k^\dag \mathrm{e}^{\mathrm{i}k\cdot x} \right) \right] \\
&=\int \frac{\mathrm{d}^3\vec{p} }{\left(2\pi \right)^3 } \int \frac{\mathrm{d}^3\vec{k} }{\left(2\pi \right)^3 } \frac{\omega_p }{\sqrt{2\omega_k} } \left\{\mathrm{e}^{-\mathrm{i}k\cdot x} \left[a_p^\dag a_p , a_k \right] + \mathrm{e}^{\mathrm{i}k\cdot x}\left[a_p^\dag a_p , a_k^\dag \right] \right\} \\
&=\int \frac{\mathrm{d}^3\vec{p} }{\left(2\pi \right)^3 } \int \frac{\mathrm{d}^3\vec{k} }{\left(2\pi \right)^3 } \frac{\omega_p }{\sqrt{2\omega_k} } \left\{\mathrm{e}^{-\mathrm{i}k\cdot x} \left(a_p^\dag \left[a_p , a_k \right] + \left[a_p^\dag , a_k \right]a_p \right)  + \mathrm{e}^{\mathrm{i}k\cdot x}\left(a_p^\dag\left[a_p , a_k^\dag \right] + \left[a_p^\dag , a_k^\dag \right]a_k^\dag \right) \right\} \\
&=\int \frac{\mathrm{d}^3\vec{p} }{\left(2\pi \right)^3 } \int \frac{\mathrm{d}^3\vec{k} }{\left(2\pi \right)^3 } \frac{\omega_p }{\sqrt{2\omega_k} } \left\{-\mathrm{e}^{-\mathrm{i}k\cdot x}\left(2\pi \right)^3\delta^3\left(\vec{k}-\vec{p} \right) a_p + \mathrm{e}^{\mathrm{i}k\cdot x} \left(2\pi \right)^3\delta^3\left(\vec{k}-\vec{p} \right)a_p^\dag \right\}  \\
&=\int \frac{\mathrm{d}^3\vec{p} }{\left(2\pi \right)^3 } \frac{1 }{\sqrt{2\omega_p} } \left\{-\mathrm{e}^{-\mathrm{i}k\cdot x}a_p + \mathrm{e}^{\mathrm{i}k\cdot x}a_p^\dag \right\} \\
&=-\mathrm{i}\partial_t \phi_0(\vec{x},t)
\end{aligned}
$$

对于任何哈密顿量，量子场满足海森堡运动方程：

$$
\mathrm{i}\partial_t \phi(x) = \left[\phi , H \right]
$$

二次量子化理论的一次量子化极限来自于单粒子态，在非相对论极限下是合适的。这些态的基：

$$
\bra{x}=\bra{\vec{x},t}
$$

$$
\bra{x}=\bra{0}\phi(\vec{x},t)
$$

薛定谔绘景下的波函数

$$
\psi(x)=\braket{x|\psi}
$$

$$
\mathrm{i}\partial_t \psi(x)
=\mathrm{i}\partial_t\braket{0|\phi(\vec{x},t)|\psi}
=\mathrm{i}\braket{0|\partial_t\phi(\vec{x},t)|\psi}
$$

对于有质量粒子，自由量子场 $\phi_0(x) $ 满足

$$
\partial_t^2\phi_0 = \left(\nabla^2-m^2 \right)\phi_0
$$

有质量情况色散关系

$$
\omega_p = \sqrt{\vec{p}^2+m^2}
$$

$$
\begin{aligned}
\mathrm{i}\braket{0|\partial_t\phi(\vec{x},t)|\psi}
&=\Braket{0|\int\frac{\mathrm{d}^3\vec{p} }{\left(2\pi \right)^3 }\frac{\sqrt{\vec{p}^2+m^2} }{\sqrt{2\omega_p} } \left(a_p\mathrm{e}^{-\mathrm{i}k\cdot x} - a_p^\dag\mathrm{e}^{\mathrm{i}k\cdot x} \right)|\psi } \\
&=\Braket{0|\sqrt{m^2-\nabla^2}\phi_0(x)|\psi}
\end{aligned}
$$

$$
\mathrm{i}\partial_t \psi(x)
=\sqrt{m^2-\nabla^2} \psi(x)
=\left[m-\frac{\nabla^2 }{2m } +\mathcal{O}\left(\frac{1 }{m^2 }  \right) \right]\psi(x)
$$

非相对论极限

$$
\mathrm{i}\partial_t \psi(x)
=-\frac{\nabla^2 }{2m } \psi(x)
$$

### 2.3.3 对易关系

一个场在两个不同点的对易子：

$$
\begin{aligned}
\left[\phi(\vec{x}) , \phi(\vec{y}) \right]
&=\int\frac{\mathrm{d}^3\vec{p} }{\left(2\pi \right)^3 } \int \frac{\mathrm{d}^3\vec{q} }{\left(2\pi \right)^3 } \frac{1 }{\sqrt{2\omega_p 2\omega_q} } \left[\left(a_p\mathrm{e}^{\mathrm{i}\vec{p}\cdot\vec{x}} + a_p^\dag \mathrm{e}^{-\mathrm{i}\vec{p}\cdot\vec{x}} \right) , \left(a_q\mathrm{e}^{\mathrm{i}\vec{q}\cdot\vec{y}} + a_q^\dag \mathrm{e}^{-\mathrm{i}\vec{q}\cdot\vec{y}} \right)  \right] \\
&=\int \frac{\mathrm{d}^3\vec{p} }{\left(2\pi \right)^3 } \frac{1 }{2\omega_p } \left(\mathrm{e}^{\mathrm{i}\vec{p}\cdot(\vec{x}-\vec{y})} - \mathrm{e}^{-\mathrm{i}\vec{p}\cdot(\vec{x}-\vec{y})} \right)
\end{aligned}
$$

由于 $\omega_p=\sqrt{\vec{p}^2+m^2} $ 在 $\vec{p}\to-\vec{p} $ 下不变，因此：

$$
\left[\phi(\vec{x}) , \phi(\vec{y}) \right] = 0
$$

场对时间微分在 $t=0 $ 时刻：

$$
\pi(\vec{x})
\equiv \partial_t \phi(x)\bigg|_{t=0}
=-\mathrm{i}\int \frac{\mathrm{d}^3\vec{p} }{\left(2\pi \right)^3 } \sqrt{\frac{\omega_p }{2 } }\left(a_p\mathrm{e}^{\mathrm{i}\vec{p}\cdot\vec{x}} - a_p^\dag \mathrm{e}^{-\mathrm{i}\vec{p}\cdot\vec{x}} \right)
$$

计算：

$$
\begin{aligned}
[\phi(\vec{x}) , \pi(\vec{y})]
&=\frac{\mathrm{i} }{2 } \int \frac{\mathrm{d}^3\vec{p} }{\left(2\pi \right)^3 } \left[\mathrm{e}^{\mathrm{i}\vec{p}\cdot(\vec{x}-\vec{y})} + \mathrm{e}^{-\mathrm{i}\vec{p}\cdot(\vec{x}-\vec{y})} \right] \\
&=\mathrm{i}\delta^3\left(\vec{x}-\vec{y} \right)
\end{aligned}
$$

# 3 经典场论

$$
H = \int\mathrm{d}^3 x \mathcal{H},\quad
L = \int\mathrm{d}^3 x \mathcal{L}
$$

哈密顿量（密度）是场和共轭动量的泛函 $\mathcal{H}\left[\phi,\pi \right] $，拉格朗日量（密度）是哈密顿量（密度）的勒让德变换：

$$
\mathcal{L}\left[\phi,\dot{\phi} \right]
=\pi\left[\phi,\dot{\phi} \right] \dot{\phi} - \mathcal{H}\left[\phi,\pi\left[\phi,\dot{\phi} \right] \right]
$$

其中 $\dot{\phi}=\partial_t\phi $，$\pi\left[\phi,\dot{\phi} \right] $ 由 $\partial \mathcal{H}\left[\phi,\pi \right]/\partial\pi = \dot{\phi} $ 隐式定义。

逆变换：

$$
\mathcal{H}\left[\phi,\pi \right]
=\pi \dot{\phi}\left[\phi,\pi \right] - \mathcal{L}\left[\phi,\dot{\phi}\left[\phi,\pi \right] \right]
$$

其中 $\dot{\pi}\left[\phi,\pi \right] $ 由 $\partial\mathcal{L}\left[\phi,\dot{\phi} \right]/\partial\dot{\phi}=\pi $ 隐式定义。

考虑：

$$
\mathcal{L}
=\frac{1 }{2 } \left(\partial_\mu\phi \right)\left(\partial_\mu\phi \right) - \mathcal{V}\left[\phi \right]
=\frac{1 }{2 } \dot{\phi}^2 - \frac{1 }{2 } \left(\nabla\phi \right)^2 - \mathcal{V}\left[\phi \right]
$$

其中 $\mathcal{V}[\phi] $ 为势（密度）。

$$
\pi
=\frac{\partial\mathcal{L} }{\partial\dot{\phi} } 
=\dot{\phi}
$$

$$
\dot{\phi}\left[\phi,\pi \right] = \pi
$$

$$
\mathcal{H}
=\pi\dot{\phi}\left[\phi,\pi \right] - \mathcal{L}\left[\phi,\dot{\phi}\left[\phi,\pi \right] \right]
=\frac{1 }{2 } \pi^2 + \frac{1 }{2 } \left(\nabla \phi \right)^2 + \mathcal{V}[\phi]
$$

$$
\mathcal{H} = \mathcal{K}  +\mathcal{V}
$$

$$
\mathcal{L} = \mathcal{K} - \mathcal{V}
$$

哈密顿量不是洛伦兹不变量。

动能项是双线性的。

相互作用项包含3个及以上的场。

## 3.2 欧拉-拉格朗日方程

作用量：

$$
S
=\int \mathrm{d}t L
=\int\mathrm{d}^4 x \mathcal{L}(x)
$$

$$
\begin{aligned}
\delta S
&=\int\mathrm{d}^4 x\left[\frac{\partial \mathcal{L} }{\partial \phi } \delta\phi + \frac{\partial\mathcal{L} }{\partial\left(\partial_\mu\phi \right) } \delta\left(\partial_\mu\phi \right) \right] \\
&=\int\mathrm{d}^4 x \left\{\left[\frac{\partial\mathcal{L} }{\partial\phi } -\partial_\mu\frac{\partial\mathcal{L} }{\partial\left(\partial_\mu\phi \right) }  \right]\delta\phi + \partial_\mu\left[\frac{\partial\mathcal{L} }{\partial\left(\partial_\mu\phi \right) } \delta\phi \right] \right\}
\end{aligned}
$$

$$
\frac{\partial\mathcal{L} }{\partial\phi } - \partial_\mu\frac{\partial\mathcal{L} }{\partial\left(\partial_\mu\phi \right) } 
=0
$$

若

$$
\mathcal{L}
=\frac{1 }{2 } \left(\partial_\mu\phi \right)\left(\partial_\mu\phi \right) - \frac{1 }{2 } m^2\phi^2
$$

则运动方程为：

$$
\left(\square + m^2 \right)\phi = 0
$$

其中

$$
\square\equiv \partial_\mu^2
$$

## 3.3 诺特定理

考虑如下拉式量

$$
\mathcal{L}
=\left|\partial_\mu\phi \right|^2 - m^2\left|\phi \right|^2
=\left(\partial_\mu\phi \right)\left(\partial_\mu\phi^* \right) - m^2\phi\phi^*
$$

此拉式量在变换 $\phi\to \phi'=\mathrm{e}^{-\mathrm{i}\alpha}\phi $ 下不变。这个变换是拉式量的一种对称变换。

假设拉式量具有一种依赖于参量 $\alpha $ 的对称性，即

$$
0
=\frac{\delta\mathcal{L} }{\delta \alpha } 
=\sum_{n}\left\{\left[\frac{\partial\mathcal{L} }{\partial\phi_n } -\partial_\mu\frac{\partial\mathcal{L} }{\partial\left(\partial_\mu\phi_n \right) } \right]\frac{\delta\phi_n }{\delta\alpha }  + \partial_\mu\left[\frac{\partial\mathcal{L} }{\partial\left(\partial_\mu\phi_n \right) } \frac{\delta\phi_n }{\delta\alpha }  \right]  \right\}
$$

当运动方程得以满足，则上式化简为：

$$
\partial_\mu J_\mu = 0,\quad
J_\mu\equiv \sum_{n} \frac{\partial\mathcal{L} }{\partial\left(\partial_\mu\phi_n \right) } \frac{\delta\phi_n }{\delta\alpha } 
$$

$J_\mu $ 称为诺特流。

满足 $\partial_\mu J_\mu $ 的矢量场 $J_\mu $ 称为守恒流。

总荷 $Q $ 定义为

$$
Q
\equiv \int \mathrm{d}^3\vec{x} J_0
$$

满足

$$
\partial_t Q
=\int\mathrm{d}^3\vec{x} \partial_t J_0
=\int\mathrm{d}^3\vec{x} \nabla\cdot\vec{J}
=0
$$

最后一步假设 $\vec{J} $ 在边界上为零。

诺特定理：若拉式量存在一种连续对称性，则存在一种当运动方程得到满足时与对称性相联系的守恒流。

### 3.3.1 能量-动量张量

### 3.3.2 流

## 3.4 库仑定律

### 3.4.1 傅里叶变换

### 3.4.2 库仑势

## 3.5 格林函数

---

## The Canonical Commutation Relations

考虑一个依赖于参数 $\varepsilon $ 的变换 $g(\varepsilon) $，其作用于场 $\phi $ 上，得到另一个场 $\phi' $：

$$
\phi\to \phi'=g(\varepsilon)\phi
$$

规定当 $\varepsilon\to 0 $ 时 $g(\varepsilon) $ 为无穷小变换（很接近恒等变换 $I $），因此当 $\varepsilon\to 0 $ 时，$g(\varepsilon) $ 形式上可写为：

$$
g(\varepsilon)
=I + \varepsilon G,\quad \varepsilon\to 0
$$

算符 $G $ 就称为生成元。

可以证明，若生成元为

$$
G
=-\mathrm{i}\frac{\partial }{\partial \phi } ,
$$

则场的变换为：

$$
\phi\to \phi'=g(\varepsilon) \phi=\phi-\mathrm{i}\varepsilon
$$

---

证明：

$$
\begin{aligned}
\phi'
&=g(\varepsilon) \phi \\
&=\left(1-\mathrm{i}\varepsilon\frac{\partial }{\partial\phi }  \right)\phi \\
&=\phi-\mathrm{i}\varepsilon
\end{aligned}
$$

---

quantum operator $\longleftrightarrow $ generator of symmetry

conjugate momentum density $\pi $ $\longleftrightarrow $ generator field shifts $-\mathrm{i}\partial/\partial\phi $

$$
\begin{aligned}
\left[\phi\left(t,\vec{x} \right) , \pi\left(t,\vec{y} \right) \right] \Ket{\psi }
&=\left[\phi\left(t,\vec{x} \right) , -\mathrm{i}\frac{\partial }{\partial \phi\left(t,\vec{y} \right) }  \right] \Ket{\psi } \\
&=\mathrm{i}\delta\left(\vec{x}-\vec{y} \right) \Ket{\psi }
\end{aligned}
$$

$$
\boxed{
\left[\phi\left(t,\vec{x} \right) , \pi\left(t,\vec{y} \right) \right]
=\mathrm{i} \delta\left(\vec{x}-\vec{y} \right)
}
$$

$$
\boxed{
\left[\phi\left(t,\vec{x} \right) , \phi\left(t,\vec{y} \right) \right]
=0
}
$$

$$
\boxed{
\left[\pi\left(t,\vec{x} \right) , \pi\left(t,\vec{y} \right) \right]
=0
}
$$

## Field Operators
