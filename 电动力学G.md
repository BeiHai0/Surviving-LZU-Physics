# 矢量分析

爱因斯坦求和约定：

$$
\vec{A}
=\vec{e}_i A_i,~~i=1,2,3
$$

$$
\vec{A}\cdot\vec{B}
=A_iB_i
$$

$$
\vec{A}\times\vec{B}
=\varepsilon_{ijk} A_i B_j \vec{e}_k
$$

$$
(\vec{A}\times\vec{B})_k
=\varepsilon_{ijk} A_i B_j
$$

混合积具有轮换对称性：

$$
\vec{A}\cdot(\vec{B}\times\vec{C})
=\vec{B}\cdot(\vec{C}\times\vec{A})
=\vec{C}\cdot(\vec{A}\times\vec{B})
$$

三叉积的性质：

$$
\vec{A}\times(\vec{B}\times\vec{C})
=\vec{B}(\vec{A}\cdot\vec{C})-\vec{C}(\vec{A}\cdot\vec{B})
$$

证明：

$$
\begin{aligned}
\vec{A}\times(\vec{B}\times\vec{C})
&=\varepsilon_{ijk} A_i (\vec{B}\times\vec{C})_j \vec{e}_k \\
&=\vec{e}_k\varepsilon_{ijk} A_i\vec{e}_k \varepsilon_{lmj} B_l C_m \\
&=\vec{e}_k\varepsilon_{jik} \varepsilon_{jml} A_i B_l C_m \\
&=\vec{e}_k(\delta_{im} \delta_{kl} -\delta_{il}\delta_{km} ) A_i B_l C_m \\
&=\vec{e}_kA_m B_k C_m - \vec{e}_kA_l B_l C_k \\
&=\vec{B}(\vec{A}\cdot\vec{C})-\vec{C}(\vec{A}\cdot\vec{B})
\end{aligned}
$$

其他恒等式：

$$
(\vec{A}\times\vec{B})\cdot(\vec{C}\times\vec{D})
=(\vec{A}\cdot\vec{C})(\vec{B}\cdot\vec{D})-(\vec{A}\cdot\vec{D})(\vec{B}\cdot\vec{C})
$$

$$
\vec{A}\times[\vec{B}\times(\vec{C}\times\vec{D})]
=\vec{B}[\vec{A}\cdot(\vec{C}\times\vec{D})] - (\vec{A}\cdot \vec{B})(\vec{C}\times\vec{D})
$$

位矢：

$$
\vec{r}
=x\vec{e}_x+y\vec{e}_y+z\vec{e}_z
$$

无穷小位移：

$$
\mathrm{d}\vec{l}
\equiv \vec{e}_x\mathrm{d}x +\vec{e}_y\mathrm{d}y +\vec{e}_z\mathrm{d}z
$$

间隔矢量（实在不会打）：

$$
\vec{\eta}
\equiv \vec{r}-\vec{r}'
$$

同一个向量在两个不同直角坐标系下表示的联系：

二维极坐标：

$$
\left\{
\begin{aligned}
&A_y=A\cos\theta \\
&A_z=A\sin\theta
\end{aligned}
\right.
$$

$$
\left\{
\begin{aligned}
&A_{y'}=A\cos\theta' \\
&A_{z'}=A\sin\theta'
\end{aligned}
\right.
$$

记：$\theta-\theta'\equiv \phi $

$$
\left\{
\begin{aligned}
&A_{y'}=A\cos(\theta-\phi)=A(\cos\theta\cos\phi+\sin\theta\sin\phi)=A_y\cos\phi+A_z\sin\phi \\
&A_{z'}=A\sin(\theta-\phi)=A(\sin\theta\cos\phi-\cos\theta\sin\phi)=-A_y\sin\phi+A_z\cos\phi
\end{aligned}
\right.
$$

写成矩阵形式：

$$
\begin{bmatrix}
A_{y'} \\
A_{z'}
\end{bmatrix}
=\begin{bmatrix}
\cos\phi &\sin\phi \\
-\sin\phi &\cos\phi
\end{bmatrix}
\begin{bmatrix}
A_y \\
A_z
\end{bmatrix}
$$

推广到三维情形：



## 矢量代数

## 微分

## 积分

## 曲线坐标系

## 狄拉克 $\delta$ 函数

## 矢量场

# 静电学

## 电场

## 静电场的散度和旋度

## 电势

## 静电场中的功和能

## 导体

# 电势

## 拉普拉斯方程

## ？

## 分离变量

## ？

# 介质中的电场

## 极化

## 极化电场

## 电位移

## 电介质

# 静磁学

## 洛伦兹力定律

## 毕奥-萨法尔定律

## 电场强度的散度和旋度

## ？

# 介质中的磁场

## 磁化

## 磁化物质的磁场

## ？

## 线性介质和非线性介质

# 电动力学

## ？

## ？

## 麦克斯韦方程组

# 守恒律

## 电荷和能量

## 动量

## ？

# 电磁波

## 一维电磁波

## ？

## 介质中的电磁波

## ？

## 

# 电势和电场

# 辐射

# 电动力学与相对论