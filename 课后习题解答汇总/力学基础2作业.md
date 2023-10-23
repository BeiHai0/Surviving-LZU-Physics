## 1(a)

$$
\begin{cases}
x=\sigma\tau \\
y=\frac{1}{2}(\tau^2-\sigma^2)
\end{cases}
\Longrightarrow
\begin{cases}
\mathrm{d}x
=\sigma\mathrm{d}\tau+\tau\mathrm{d}\sigma \\
\mathrm{d}y
=\tau\mathrm{d}\tau-\sigma\mathrm{d}\sigma
\end{cases}
$$

线元：

$$
\begin{aligned}
\mathrm{d}s^2
&\equiv \mathrm{d}x^2+\mathrm{d}y^2 \\
&=(\sigma\mathrm{d}\tau+\tau\mathrm{d}\sigma)^2 + (\tau\mathrm{d}\tau-\sigma\mathrm{d}\sigma)^2 \\
&=\sigma^2\mathrm{d}\tau^2+2\sigma\tau\mathrm{d}\tau\mathrm{d}\sigma+\tau^2\mathrm{d}\sigma^2+\tau^2\mathrm{d}\tau^2-2\tau\sigma\mathrm{d}\tau\mathrm{d}\sigma+\sigma^2\mathrm{d}\sigma^2 \\
&=(\sigma^2+\tau^2)(\mathrm{d}\sigma^2+\mathrm{d}\tau^2)
\end{aligned}
$$

计算偏导数：

$$
\frac{\partial x}{\partial \sigma}
=\tau,
\frac{\partial x}{\partial \tau}
=\sigma,
\frac{\partial y}{\partial \sigma}
=-\sigma,
\frac{\partial y}{\partial \tau}
=\tau
$$

雅可比行列式：

$$
\bigg|\frac{\partial (x,y)}{\partial (\sigma,\tau)}\bigg|
=\begin{vmatrix}
\frac{\partial x}{\partial\sigma} &\frac{\partial x}{\partial \tau} \\[1mm]
\frac{\partial y}{\partial \sigma} &\frac{\partial y}{\partial\tau}
\end{vmatrix}
=\tau^2+\sigma^2
$$

面元：

$$
\mathrm{d}A
\equiv \mathrm{d}x\mathrm{d}y
=\bigg|\frac{\partial (x,y)}{\partial (\sigma,\tau)}\bigg|\mathrm{d}\sigma\mathrm{d}\tau
=(\tau^2+\sigma^2)\mathrm{d}\sigma\mathrm{d}\tau
$$

## 1(b)

设 $u=u_1(x,y)=u_2(\sigma,\tau)$

由链式法则，有：

$$
\begin{aligned}
\partial_\sigma u
&=\partial_x u\partial_\sigma x+\partial_y u\partial_\sigma y \\
&=\tau\partial_x u-\sigma\partial_y u
\end{aligned}
$$

$$
\begin{aligned}
\partial_\tau u
&=\partial_x u\partial_\tau x+\partial_y u\partial_\tau y \\
&=\sigma\partial_x u+\tau\partial_y u
\end{aligned}
$$

于是：

$$
\begin{cases}
\partial_\sigma=\tau\partial_x-\sigma\partial_y \\
\partial_\tau=\sigma\partial_x+\tau\partial_y
\end{cases}
$$

## 2

自然坐标系下，

$$
\vec{v}
=\dot{s}\vec{e}_\tau \\
\vec{a}
=\frac{\dot{s}^2}{\rho}\vec{e}_n+\ddot{s}\vec{e}_\tau
$$

于是：

$$
\vec{a}\times\vec{v}
=\frac{\dot{s}^3}{\rho}\vec{e}_k
$$

得到：

$$
\rho
=\frac{\dot{s}^3}{|\vec{a}\times\vec{v}|} \tag{1}
$$

这里，

$$
\dot{s}
\equiv\frac{\mathrm{d}s}{\mathrm{d}t}
=\sqrt{\dot{x}^2+\dot{y}^2+\dot{z}^2}
$$

$$
\vec{v}
\equiv\frac{\mathrm{d}\vec{r}}{\mathrm{d}t}
=(\dot{x},\dot{y},\dot{z})
$$

$$
\vec{a}
\equiv\frac{\mathrm{d}\vec{v}}{\mathrm{d}t}
=(\ddot{x},\ddot{y},\ddot{z})
$$

代入$(1)$，得：

$$
\rho
=\frac{\bigg(\dot{x}^2+\dot{y}^2+\dot{z}^2 \bigg)^{\frac{3}{2}}}{\sqrt{(\dot{y}\ddot{z}-\dot{z}\ddot{y})^2+(\dot{x}\ddot{z}-\dot{z}\ddot{x})^2+(\dot{x}\ddot{y}-\dot{y}\ddot{x})^2}}
$$

## 3(a)

$$
\left\{
\begin{aligned}
x'&=\frac{x-ut}{\sqrt{1-\frac{u^2}{c^2}}} \\
y'&=y \\
z'&=z \\
t'&=\frac{t-\frac{u}{c^2}x}{\sqrt{1-\frac{u^2}{c^2}}}
\end{aligned}
\right.
$$

## 3(b)

由于 $y'=y,z'=z$，要证明 $x^\mu x_\mu$ 是一个$\rm{Lorentz}$标量，只要证明：

$$
c^2 t^2-x^2
=c^2t'^2-x'^2
$$

而：

$$
\begin{aligned}
c^2t'^2-x'^2
&=c^2\frac{(t-\frac{u}{c^2}x)^2}{1-(\frac{u}{c})^2} - \frac{(x-ut)^2}{1-(\frac{u}{c})^2} \\
&=\frac{(ct-\frac{u}{c}x)^2-(x-ut)^2}{1-(\frac{u}{c})^2} \\
&=\frac{c^2t^2-u^2t^2+\frac{u^2}{c^2}x^2-x^2}{1-(\frac{u}{c})^2} \\
&=\frac{c^2t^2(1-\frac{u^2}{c^2})+x^2(\frac{u^2}{c^2}-1)}{1-(\frac{u}{c})^2} \\
&=c^2t^2-x^2
\end{aligned}
$$

于是 $x^\mu x_\mu$ 是一个 $\rm{Lorentz}$ 标量

## 3(c)

此变换为线性变换，于是有：

$$
\begin{bmatrix}
ct' \\
x'
\end{bmatrix}
=\begin{bmatrix}
a_{11} &a_{12} \\
a_{21} &a_{22}
\end{bmatrix}
\begin{bmatrix}
ct \\
x
\end{bmatrix}
$$

结合条件(ii)，有：

$$
\left\{
\begin{aligned}
ct'&=a_{11} ct+a_{12} x \\
x'&=a_{21}ct+a_{22}x \\
c^2t^2-x^2&=c^2t'^2-x'^2
\end{aligned}
\right.
$$

消去 $t',x'$，得：

$$
c^2t^2-x^2
=(a_{11}ct+a_{12}x)^2-(a_{21}ct+a_{22}x)^2
$$

由对应项系数相等，得到：

$$
\left\{
\begin{align}
a_{11}^2-a_{21}^2&=1  \\
a_{12}^2-a_{22}^2&=-1 \\
a_{11}a_{12}-a_{21}a_{22} &=0
\end{align}
\right.
$$

$(1)(2)$ 代入 $(3)$，消去 $a_{11}^2,a_{12}^2$，得：

$$
a_{22}^2
=a_{21}^2+1
$$

令 $a_{11}=k$，则：

$$
\begin{cases}
a_{11}&=k \\
a_{21}&=\pm\sqrt{k^2-1} \\
a_{12}&=\pm\sqrt{k^2-1} \\
a_{22}&=\pm k
\end{cases}
$$

其中，正负号还要满足 $(3)$，于是，与此线性变换对应的矩阵的所有可能为：

$$
\begin{bmatrix}
k &\sqrt{k^2-1} \\
\sqrt{k^2-1} &k
\end{bmatrix},
\begin{bmatrix}
k &\sqrt{k^2-1} \\
-\sqrt{k^2-1} &-k
\end{bmatrix},
\begin{bmatrix}
k &-\sqrt{k^2-1} \\
\sqrt{k^2-1} &-k
\end{bmatrix},
\begin{bmatrix}
k &-\sqrt{k^2-1} \\
-\sqrt{k^2-1} &k
\end{bmatrix}
$$

从左往右数第四个矩阵即为四维时空$\rm{Lorentz}$变换的二维对应

## 3(d)

伽利略变换：

$$
\left\{
\begin{aligned}
x'&=x-ut \\
y'&=y \\
z'&=z \\
t'&=t
\end{aligned}
\right.
$$

对于伽利略变换：

$$
(t,\vec{r})\to(t,\vec{r}+\vec{v}t)
$$

在 $K$ 系内，

$$
\vec{F}
=m\ddot{\vec{r}}
$$

在 $K'$ 系内，

$$
\vec{F'}
=\vec{F}
=m\ddot{\vec{r}}
=m\frac{\mathrm{d}^2{(\vec{r}+\vec{v}t)}}{\mathrm{d}t^2}
$$

两者形式一致，于是牛顿运动方程在伽利略变换 $(t,\vec{r})\to(t,\vec{r}+\vec{v}t)$ 下保持不变

## 3(e)

在伽利略变换下，

$$
x^\mu x_\mu
\equiv c^2t^2-x^2-y^2-z^2
$$

$$
x'^\mu x'_\mu
\equiv c^2t^2-x'^2-y'^2-z'^2
=c^2t^2-(x+v_x t)^2-(y+v_y t)^2-(z+v_z t)^2
\ne x^\mu x_\mu
$$

## 3(f)

$$
\left\{
\begin{aligned}
x'&=\frac{x-ut}{\sqrt{1-(\frac{u}{c})^2}} \\
y'&=y \\
z'&=z \\
t'&=\frac{t-\frac{u}{c^2}x}{\sqrt{1-(\frac{u}{c})^2}}
\end{aligned}
\right.
$$

注意到，

$$
\frac{\mathrm{d}x'}{\mathrm{d}t}
=\frac{\mathrm{d}x'}{\mathrm{d}t'}\cdot\frac{\mathrm{d}t'}{\mathrm{d}t}
=\frac{1-\frac{u}{c^2}v_x}{\sqrt{1-(\frac{u}{c})^2}}v'_x
$$

对第一行等式左右两边同时对 $t$ 求导得：

$$
v'_x
=\frac{v_x-u}{1-\frac{u}{c^2}v_x}
$$

同理有：

$$
v'_y
=\frac{v_y\sqrt{1-(\frac{u}{c})^2}}{1-\frac{u}{c^2}v_x}
$$

$$
v'_z
=\frac{v_z\sqrt{1-(\frac{u}{c})^2}}{1-\frac{u}{c^2}v_x}
$$

## 3(g)

令：

$$
v_x^2+v_y^2+v_z^2=c^2
$$

则：

$$
\begin{aligned}
v_x'^2+v_y'^2+v_z'^2
&=\frac{(v_x-u)^2+v_y^2(1-\frac{u^2}{c^2})+v_z^2(1-\frac{u^2}{c^2})}{(1-\frac{u}{c^2}v_x)^2} \\
&=\frac{(v_x^2+v_y^2+v_z^2)(1-\frac{u^2}{c^2})-v_x^2(1-\frac{u^2}{c^2})+(v_x-u)^2}{(1-\frac{u}{c^2}v_x)^2} \\
&=\frac{\frac{u^2}{c^2}v_x^2-2uv_x+c^2}{(1-\frac{u}{c^2}v_x)^2} \\
&=\frac{(\frac{u}{c}v_x-c)^2}{(1-\frac{u}{c^2}v_x)^2} \\
&=\frac{c^2(\frac{u}{c^2}v_x-1)^2}{(1-\frac{u}{c^2}v_x)^2} \\
&=c^2
\end{aligned}
$$

这就是说，光速不变

## 3(h)

由：

$$
\left\{
\begin{aligned}
v'_x &=\frac{v_x-u}{1-\frac{u}{c^2}v_x} \\
v'_y &=\frac{v_y\sqrt{1-(\frac{u}{c})^2}}{1-\frac{u}{c^2}v_x} \\
v'_z &=\frac{v_z\sqrt{1-(\frac{u}{c})^2}}{1-\frac{u}{c^2}v_x} \\
t'&=\frac{t-\frac{u}{c^2}x}{\sqrt{1-(\frac{u}{c})^2}} 
\end{aligned}
\right.
$$

对所有等式两边同时对 $t$ 求导，并结合链式法则，得：

$$
\left\{
\begin{aligned}
a_x'
&=\frac{(1-\frac{u^2}{c^2})^{\frac{3}{2}}a_x}{(1-\frac{u}{c^2}v_x)^3} \\
a_y'&=\frac{(1-\frac{u^2}{c^2})[(1-\frac{u}{c^2}v_x)a_y+\frac{uv_y}{c^2}a_x]}{(1-\frac{u}{c^2}v_x)^3} \\
a_z'&=\frac{(1-\frac{u^2}{c^2})[(1-\frac{u}{c^2}v_x)a_z+\frac{uv_z}{c^2}a_x]}{(1-\frac{u}{c^2}v_x)^3}
\end{aligned} 
\right.
$$

## 4(a)

$$
\vec{p}c
=cm\vec{v}
$$

$$
E\frac{\vec{v}}{c}
=mc^2\frac{\vec{v}}{c}
=cm\vec{v}
$$

于是

$$
\vec{p}c
=E\frac{\vec{v}}{c}
$$

## 4(b)

$$
\begin{aligned}
p^\mu p_\mu
&=\frac{E^2}{c^2}-p^2 \\
&=\frac{m^2c^4}{c^2}-m^2v^2 \\
&=m^2(c^2-v^2) \\
&=\frac{m_0^2}{1-\frac{v^2}{c^2}}(c^2-v^2) \\
&=\frac{c^2m_0^2}{c^2-v^2}(c^2-v^2) \\
&=m_0^2c^2
\end{aligned}
$$

## 4(c)

设 $K'$ 惯性系相对 $K$ 惯性系以 $\vec{u}=u\vec{e}_x$ 的速度运动，两惯性系坐标轴指向一致，在 $t=0,t'=0$ 时刻两惯性系原点重合

设某粒子在 $K$ 系中的速度为 $\vec{v}=v_x\vec{e}_x+v_y\vec{e}_y+v_z\vec{e}_z$，在 $K'$ 系中的速度为 $\vec{v}'=v_x'\vec{e}_x+v_y'\vec{e}_y+v_z'\vec{e}_z$，根据能量-动量矢量的定义，该粒子在 $K$ 系中的能量-动量矢量为：

$$
p^\mu
=\frac{m_0}{\sqrt{1-\frac{v^2}{c^2}}}
\begin{bmatrix}
c \\
v_x \\
v_y \\
v_z
\end{bmatrix}
$$

该粒子在 $K'$ 系中的能量-动量矢量为：

$$
p'^{\mu}
=\frac{m_0}{\sqrt{1-\frac{v'^2}{c^2}}}
\begin{bmatrix}
c \\
v_x' \\
v_y' \\
v_z'
\end{bmatrix}
$$

要验证 $p^\mu$ 是一个 $\rm{Lorentz}$ 四维矢量，只需要验证从 $p^\mu$ 到 $p'^\mu$ 的变换是洛伦兹变换，也就是要验证下面等式成立：

$$
\frac{m_0}{\sqrt{1-\frac{v'^2}{c^2}}}
\begin{bmatrix}
c \\
v_x' \\
v_y' \\
v_z'
\end{bmatrix}
=\begin{bmatrix}
\gamma &-\beta\gamma &0 &0 \\
-\beta\gamma &\gamma &0 &0 \\
0 &0 &1 &0 \\
0 &0 &0 &1
\end{bmatrix}
\frac{m_0}{\sqrt{1-\frac{v^2}{c^2}}}
\begin{bmatrix}
c \\
v_x \\
v_y \\
v_z
\end{bmatrix}
$$

其中，$\gamma=\frac{1}{\sqrt{1-\frac{u^2}{c^2}}},\beta=\frac{u}{c},v'^2=v_x'^2+v_y'^2+v_z'^2,v^2=v_x^2+v_y^2+v_z^2$,

也就是验证下面四条等式成立：

$$
\frac{c}{\sqrt{1-\frac{v'^2}{c^2}}}
=\frac{1}{\sqrt{1-\frac{v^2}{c^2}}}\cdot\frac{c-\frac{uv_x}{c}}{\sqrt{1-\frac{u^2}{c^2}}} \tag{1}
$$

$$
\frac{v_x'}{\sqrt{1-\frac{v'^2}{c^2}}}
=\frac{1}{\sqrt{1-\frac{v^2}{c^2}}}\cdot\frac{v_x-u}{\sqrt{1-\frac{u^2}{c^2}}} \tag{2}
$$

$$
\frac{v_y'}{\sqrt{1-\frac{v'^2}{c^2}}}
=\frac{v_y}{\sqrt{1-\frac{v^2}{c^2}}} \tag{3}
$$

$$
\frac{v_z'}{\sqrt{1-\frac{v'^2}{c^2}}}
=\frac{v_z}{\sqrt{1-\frac{v^2}{c^2}}} \tag{4}
$$

由3(f)知：

$$
\left\{
\begin{aligned}
v'_x &=\frac{v_x-u}{1-\frac{u}{c^2}v_x} \\
v'_y &=\frac{v_y\sqrt{1-\frac{u^2}{c^2}}}{1-\frac{u}{c^2}v_x} \\
v'_z &=\frac{v_z\sqrt{1-\frac{u^2}{c^2}}}{1-\frac{u}{c^2}v_x} 
\end{aligned}
\right.
$$

再注意到重要结论 $(*)$：

$$
\begin{aligned}
\sqrt{1-\frac{v'^2}{c^2}}
&=\sqrt{1-\frac{v_x'^2+v_y'^2+v_z'^2}{c^2}} \\
&=\sqrt{1-\frac{1}{c^2}\cdot\frac{1}{(1-\frac{u}{c^2}v_x)^2}\cdot\bigg[(v_x-u)^2+(1-\frac{u^2}{c^2})v_y^2+(1-\frac{u^2}{c^2})v_z^2\bigg]} \\
&=\sqrt{1-\frac{1}{c^2}\cdot\frac{1}{(1-\frac{u}{c^2}v_x)^2}\cdot\bigg[ (1-\frac{u^2}{c^2})(v_x^2+v_y^2+v_z^2)+(v_x-u)^2-(1-\frac{u^2}{c^2})v_x^2 \bigg]} \\
&=\sqrt{1-\frac{1}{c^2}\cdot\frac{1}{(1-\frac{u}{c^2}v_x)^2}\cdot\bigg[ (1-\frac{u^2}{c^2})v^2+\frac{u^2v_x^2}{c^2}-2uv_x+u^2 \bigg]} \\
&=\sqrt{1-\frac{1}{c^2}\cdot\frac{1}{(1-\frac{u}{c^2}v_x)^2}\cdot\bigg[(1-\frac{u^2}{c^2})v^2+ \frac{u^2v_x^2}{c^2}-2uv_x+ c^2+u^2-c^2\bigg]} \\
&=\sqrt{1-\frac{1}{c^2}\cdot\frac{1}{(1-\frac{u}{c^2}v_x)^2}\cdot\bigg[ (1-\frac{u^2}{c^2})v^2+(\frac{uv_x}{c}-c)^2+u^2-c^2 \bigg]} \\
&=\sqrt{1-\frac{1}{c^2}\cdot\frac{1}{(1-\frac{u}{c^2}v_x)^2}\cdot\bigg[ (1-\frac{u^2}{c^2})v^2+u^2-c^2 \bigg]-1} \\
&=\frac{1}{1-\frac{u}{c^2}v_x}\cdot\sqrt{(1-\frac{u^2}{c^2})-\frac{1}{c^2}\cdot(1-\frac{u^2}{c^2})v^2} \\
&=\frac{1}{1-\frac{u}{c^2}v_x}\cdot\sqrt{1-\frac{u^2}{c^2}}\cdot\sqrt{1-\frac{v^2}{c^2}}
\end{aligned} 
$$

验证$(1)$：

$$
\begin{aligned}
左边
&=\frac{c}{\sqrt{1-\frac{v'^2}{c^2}}} \\
(利用结论*)&=\frac{c(1-\frac{u}{c^2}v_x)}{\sqrt{1-\frac{u^2}{c^2}}\sqrt{1-\frac{v^2}{c^2}}} \\
&=\frac{1}{\sqrt{1-\frac{v^2}{c^2}}}\cdot\frac{c-\frac{uv_x}{c}}{\sqrt{1-\frac{u^2}{c^2}}} \\
&=右边
\end{aligned}
$$

于是等式 $(1)$ 成立

验证$(2)$：

$$
\begin{aligned}
左边
&=\frac{v_x'}{\sqrt{1-\frac{v'^2}{c^2}}} \\
(利用结论*)&=\frac{v_x-u}{1-\frac{u}{c^2}v_x}\cdot\frac{1-\frac{u}{c^2}v_x}{\sqrt{1-\frac{u^2}{c^2}}\sqrt{1-\frac{v^2}{c^2}}} \\
&=\frac{1}{\sqrt{1-\frac{v^2}{c^2}}}\cdot\frac{v_x-u}{\sqrt{1-\frac{u^2}{c^2}}} \\
&=右边
\end{aligned}
$$

于是等式 $(2)$ 成立

验证$(3)$：

$$
\begin{aligned}
左边
&=\frac{v_y'}{\sqrt{1-\frac{v'^2}{c^2}}} \\
(利用结论*)&=\frac{v_y\sqrt{1-\frac{u^2}{c^2}}}{1-\frac{u}{c^2}v_x}\cdot \frac{1-\frac{u}{c^2}v_x}{\sqrt{1-\frac{u^2}{c^2}}\sqrt{1-\frac{v^2}{c^2}}} \\ 
&=\frac{v_y}{\sqrt{1-\frac{v^2}{c^2}}} \\
&=右边
\end{aligned}
$$

于是等式 $(3)$ 成立

验证$(4)$：

由于 $y,z$ 地位相同，$(3)$ 成立，则 $(4)$ 也成立

综上所述，$p^\mu$ 是一个 $\rm{Lorentz}$ 四维矢量

## 5

证明：

设质点组由 $N$ 个质点组成，第 $i$ 个质点的质量记为 $m_i$，质心的质量记为 $M=\sum\limits_{i}m_i$，第 $i$ 个质点在惯性系 $K$ 中的速度记为 $\vec{v}_i$，质心在惯性系 $K$ 中的速度记为 $\vec{v}_c=\frac{1}{M}\sum\limits_{i} m_i\vec{v}_i $,第 $i$ 个质点在质心系中的速度记为 $\vec{v}_{ic}$


$$
\begin{aligned}
\sum_{i} \frac{1}{2} m_i v_i^2
&=\sum_{i}\frac{1}{2}m_i(\vec{v}_c+\vec{v}_{ic})^2 \\
&=\sum_{i}\frac{1}{2}m_i (v_c^2+v_{ic}^2+2\vec{v}_c\cdot\vec{v}_{ic}) \\
&=\frac{1}{2}Mv_c^2+\sum_{i}\frac{1}{2}m_iv_{ic}^2+\sum_{i} m_i\vec{v}_c\cdot\vec{v}_{ic}
\end{aligned} \tag{1}
$$

注意到，

$$
\begin{aligned}
\sum_{i}m_i\vec{v}_c\cdot\vec{v}_{ic}
&=\sum_{i}m_i\vec{v}_c\cdot(\vec{v}_i-\vec{v}_c) \\
&=\sum_{i}m_i\vec{v}_c\cdot\vec{v}_i-\sum_{i}m_iv_c^2 \\
&=\vec{v}_c\cdot\sum_{i}m_i\vec{v}_i-v_c^2\sum_{i}m_i \\
&=M\vec{v}_c\cdot\frac{1}{M}\sum_{i}m_i\vec{v}_i-Mv_c^2 \\
&=Mv_c^2-Mv_c^2 \\
&=0
\end{aligned}
$$

代回$(1)$ 得：

$$
\sum_{i} \frac{1}{2} m_i v_i^2
=\frac{1}{2}Mv_c^2+\sum_{i}\frac{1}{2}m_iv_{ic}^2
$$

这就是柯尼希定理

## 6

对于球坐标系，有：

$$
\begin{cases}
x=r\sin\theta\cos\varphi \\
y=r\sin\theta\sin\varphi \\
z=r\cos\theta
\end{cases}
$$

于是：

$$
\begin{aligned}
\vec{r}
&\equiv x\vec{e}_x+y\vec{e}_y+z\vec{e}_z \\
&=r\sin\theta\cos\varphi\vec{e}_x+r\sin\theta\sin\varphi\vec{e}_y+r\cos\theta\vec{e}_z
\end{aligned}
$$

而：

$$
\begin{aligned}
\vec{e}_r
&=\frac{\partial \vec{r}}{\partial r}\bigg/\bigg|\frac{\partial \vec{r}}{\partial r}\bigg| \\
&=\sin\theta\cos\varphi\vec{e}_x+\sin\theta\sin\varphi\vec{e}_y+\cos\theta\vec{e}_z
\end{aligned}
$$

$$
\begin{aligned}
\vec{e}_\theta
&=\frac{\partial \vec{r}}{\partial\theta}\bigg/\bigg|\frac{\partial \vec{r}}{\partial\theta}\bigg| \\
&=\cos\theta\cos\varphi\vec{e}_x+\cos\theta\sin\varphi\vec{e}_y-\sin\theta\vec{e}_z
\end{aligned}
$$

$$
\begin{aligned}
\vec{e}_\varphi
&=\frac{\partial \vec{r}}{\partial\varphi}\bigg/\bigg|\frac{\partial \vec{r}}{\partial\varphi}\bigg| \\
&=-\sin\varphi\vec{e}_x+\cos\varphi\vec{e}_y+0\vec{e}_z
\end{aligned}
$$

这等价于：

$$
\begin{bmatrix}
\sin\theta \cos\varphi &\sin\theta\sin\varphi &\cos\theta \\
\cos\theta\cos\varphi &\cos\theta\sin\varphi &-\sin\theta \\
-\sin\varphi &\cos\varphi &0
\end{bmatrix}
\begin{bmatrix}
\vec{e}_x \\
\vec{e}_y \\
\vec{e}_z
\end{bmatrix}
=\begin{bmatrix}
\vec{e}_r \\
\vec{e}_\theta \\
\vec{e}_\varphi
\end{bmatrix}
$$

由克拉默法则，得：

$$
\begin{aligned}
\vec{e}_x
&=\sin\theta\cos\varphi\vec{e}_r+\cos\theta\cos\varphi\vec{e}_\theta-\sin\varphi\vec{e}_\varphi \\
\vec{e}_y
&=\sin\theta\sin\varphi\vec{e}_r+\cos\theta\sin\varphi\vec{e}_\theta+\cos\varphi\vec{e}_\varphi \\
\vec{e}_z
&=\cos\theta \vec{e}_r-\sin\theta\vec{e}_\theta+0\vec{e}_\varphi
\end{aligned}
$$

$\vec{e}_r,\vec{e}_\theta,\vec{e}_\varphi$ 分别对 $t$ 求导，得：

$$
\begin{aligned}
\dot{\vec{e}}_r
&=\dot{\theta}(\cos\theta\cos\varphi\vec{e}_x+\cos\theta\sin\varphi\vec{e}_y-\sin\theta\vec{e}_z) + \dot{\varphi}\sin\theta(-\sin\varphi\vec{e}_x+\cos\varphi\vec{e}_y+0\vec{e}_z) \\
&=\dot{\theta}\vec{e}_\theta+\dot{\varphi}\sin\theta\vec{e}_\varphi
\end{aligned}
$$

$$
\begin{aligned}
\dot{\vec{e}}_\theta
&=-\dot{\theta}(\sin\theta\cos\varphi\vec{e}_x+\sin\theta\sin\varphi\vec{e}_y+\cos\theta\vec{e}_z)+\dot{\varphi}\cos\theta(-\sin\varphi \vec{e}_x+\cos\varphi\vec{e}_y+0\vec{e}_z) \\
&=-\dot{\theta}\vec{e}_r+\dot{\varphi}\cos\theta\vec{e}_\varphi
\end{aligned}
$$

$$
\begin{aligned}
\dot{\vec{e}}_\varphi
&=-\dot{\varphi}(\cos\varphi\vec{e}_x+\sin\varphi\vec{e}_y+0\vec{e}_z) \\
&=-\dot{\varphi}(\sin\theta\vec{e}_r+\cos\theta\vec{e}_\theta) \\
&=-\dot{\varphi}\sin\theta\vec{e}_r-\dot{\varphi}\cos\theta\vec{e}_\theta
\end{aligned}
$$

于是：

$$
\begin{aligned}
\vec{v}
&\equiv\frac{\mathrm{d}(r\vec{e}_r)}{\mathrm{d}t} \\
&=\dot{r}\vec{e}_r+r\dot{\vec{e}}_r \\
&=\dot{r}\vec{e}_r+r\dot{\theta}\vec{e}_\theta+r\dot{\varphi}\sin\theta\vec{e}_\varphi
\end{aligned}
$$

$$
\begin{aligned}
\vec{a}
&\equiv\frac{\mathrm{d}\vec{v}}{\mathrm{d}t} \\
&=\ddot{r}\vec{e}_r+\dot{r}\dot{\vec{e}}_r+(\dot{r}\dot{\theta}+r\ddot{\theta})\vec{e}_\theta+r\dot{\theta}\dot{\vec{e}}_\theta+(\dot{r}\dot{\varphi}\sin\theta+r\ddot{\varphi}\sin\theta+r\dot{\varphi}\dot{\theta}\cos\theta)\vec{e}_\varphi+r\dot{\varphi}\sin\theta\dot{\vec{e}}_\varphi\ \\
&=(\ddot{r}-r\dot{\theta}^2-r\dot{\varphi}^2\sin^2\theta)\vec{e}_r+(r\ddot{\theta}+2\dot{r}\dot{\theta}-r\dot{\varphi}^2\sin\theta\cos\theta)\vec{e}_\theta+(r\ddot{\varphi}\sin\theta+2\dot{r}\dot{\varphi}\sin\theta+2r\dot{\theta}\dot{\varphi}\cos\theta)\vec{e}_\varphi
\end{aligned}
$$

