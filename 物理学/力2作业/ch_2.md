### 1(a)

选取 $\alpha,\beta$ 为广义坐标

以 $O$ 为原点，过 $O$ 竖直向下为 $x$ 轴正方向，过 $O$ 水平向右为 $y$ 轴正方向建系

各质点的位矢：

$$
\left\{
\begin{aligned}
\vec{r}_1
&=l\cos\alpha\vec{e}_x+l\sin\alpha\vec{e}_y \\
\vec{r}_2
&=l\cos\alpha\vec{e}_x-l\sin\alpha\vec{e}_y \\
\vec{r}_3
&=(l\cos\alpha-l\sin\alpha\cdot\frac{1}{\tan\beta})\vec{e}_x
\end{aligned}
\right.
$$

各质点位矢对各广义坐标的偏导：

$$
\left\{
\begin{aligned}
\frac{\partial \vec{r}_1}{\partial \alpha}
&=-l\sin\alpha\vec{e}_x+l\cos\alpha\vec{e}_y \\[1mm]
\frac{\partial \vec{r}_2}{\partial \alpha}
&=-l\sin\alpha\vec{e}_x-l\cos\alpha\vec{e}_y \\[1mm]
\frac{\partial \vec{r}_3}{\partial \alpha}
&=(-l\sin\alpha-l\cos\alpha\cdot\frac{1}{\tan\beta})\vec{e}_x
\end{aligned}
\right.
$$

$$
\left\{
\begin{aligned}
\frac{\partial \vec{r}_1}{\partial \beta}
&=\vec{0}\\
\frac{\partial \vec{r}_2}{\partial \beta}
&=\vec{0} \\
\frac{\partial \vec{r}_3}{\partial \beta}
&=(l\sin\alpha\cdot\frac{1}{\sin^2\beta})\vec{e}_x
\end{aligned}
\right.
$$

主动力：

$$
\left\{
\begin{aligned}
\vec{F}_1^{(A)}
&=(mg+N\cos\beta)\vec{e}_x+N\sin\beta\vec{e}_y \\
\vec{F}_2^{(A)}
&=(mg+N\cos\beta)\vec{e}_x-N\sin\beta\vec{e}_y \\
\vec{F}_3^{(A)}
&=(mg-2N\cos\beta)\vec{e}_x \\
\end{aligned}
\right.
$$

广义力：

$$
\begin{aligned}
Q_\alpha
&\equiv \vec{F}_i^{(A)}\cdot\frac{\partial \vec{r}_i}{\partial \alpha} \\
&=-3mgl\sin\alpha+2lN\cos\alpha\sin\beta-\frac{mgl\cos\alpha}{\tan\beta}+\frac{2lN\cos\alpha\cos\beta}{\tan\beta}
\end{aligned}
$$

$$
\begin{aligned}
Q_\beta
&\equiv \vec{F}_i^{(A)}\cdot\frac{\partial \vec{r}_i}{\partial \beta} \\
&=\frac{l\sin\alpha}{\sin^2\beta}\cdot(mg-2N\cos\beta)
\end{aligned}
$$

虚功原理要求：

$$
\begin{cases}
Q_\alpha
=0 \\
Q_\beta
=0
\end{cases}
$$

由 $Q_\beta=0$ 得到：

$$
N
=\frac{mg}{2\cos\beta}
$$

代入方程 $Q_\alpha=0$ 得到：

$$
\tan\beta
=3\tan\alpha
$$

### 1(b)

利用 $\tan\beta=3\tan\alpha$：

$$
\left\{
\begin{aligned}
\vec{r}_1
&=l\cos\alpha\vec{e}_x+l\sin\alpha\vec{e}_y \\
\vec{r}_2
&=l\cos\alpha\vec{e}_x-l\sin\alpha\vec{e}_y \\
\vec{r}_3
&=(l\cos\alpha-l\sin\alpha\cdot\frac{1}{\tan\beta})\vec{e}_x
=\frac{2l\cos\alpha}{3}\vec{e}_x
\end{aligned}
\right.
$$

于是：

$$
\left\{
\begin{aligned}
\dot{\vec{r}}_1
&=-l\dot{\alpha}\sin\alpha\vec{e}_x+l\dot{\alpha}\cos\alpha\vec{e}_y \\
\dot{\vec{r}}_2
&=-l\dot{\alpha}\sin\alpha\vec{e}_x-l\dot{\alpha}\cos\alpha\vec{e}_y \\
\dot{\vec{r}}_3
&=-\frac{2l\dot{\alpha}\sin\alpha}{3}\vec{e}_x
\end{aligned}
\right.
$$

取原点 $O$ 所在平面为零势能面，则：

$$
\begin{aligned}
L
&\equiv T-V \\
&=\frac{1}{2}m(\dot{\vec{r}}_1^2+\dot{\vec{r}}_2^2+\dot{\vec{r}}_3^2)-mg\bigg[2\cdot l\cos\alpha+\frac{2l\cos\alpha}{3}\bigg] \\
&=ml^2\dot{\alpha}^2(1+\frac{2\sin^2\alpha}{9})-\frac{8}{3}mgl\cos\alpha
\end{aligned}
$$

欧拉-拉格朗日方程：

$$
\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial \dot{\alpha}}-\frac{\partial L}{\partial \alpha}
=0
$$

即：

$$
(2+\frac{4\sin^2\alpha}{9})l\ddot{\alpha}+(\frac{8l}{9}\sin\alpha\cos\alpha)\dot{\alpha}^2-\frac{8}{3}g\sin\alpha
=0
$$

### 2

选取质心坐标 $x_c,y_c$ 作为广义坐标

$$
\vec{r}_c
=x_c\vec{e}_x+y_c\vec{e}_y
$$

$$
\delta \vec{r}_c
=\delta x_c\vec{e}_x+\delta y_c\vec{e}_y
$$

主动力：

$$
\vec{F}^{(A)}
=-mg\vec{e}_y
$$

理想约束下的虚功：

$$
\delta 
W
=\vec{F}^{(A)}\cdot\delta\vec{r}_c
=-mg\delta y_c
$$

虚功原理要求：

$$
\delta W
=0
$$

即：

$$
-mg\delta y_c
=0
$$

得到：

$$
y_c
=\rm{const}
$$

由初始状态杆贴墙知：

$$
y_c
=\frac{L}{2}
$$

设 $B(x,y)$，由几何关系知：

$$
\left\{
\begin{aligned}
x
&=L\sin\theta \\
y
&=\frac{L}{2}-\frac{L}{2}\cos\theta
\end{aligned}
\right.
$$

利用 $\sin^2\theta+\cos^2\theta=1$ 消去 $\theta$ 得：

$$
(\frac{x}{L})^2+(\frac{2y}{L}-1)^2
=1
$$

这就是杆下端 $B$ 点所在约束面的形状

### 3

设 $\vec{r}_i=\vec{r}_i(q_1,q_2,\cdots,q_s;t)$，由链式法则，有：

$$
\dot{\vec{r}}_i
=\frac{\partial \vec{r}_i}{\partial t}+\sum_{\alpha=1}^{s}\frac{\partial \vec{r}_i}{\partial q_\alpha}\dot{q}_\alpha
$$

于是：

$$
\frac{\partial \dot{\vec{r}}_i}{\partial \dot{q}_\alpha}
=\frac{\partial \vec{r}_i}{\partial q_\alpha} \tag{1}
$$

其中，$\dot{\vec{r}}_i=\dot{\vec{r}}_i(q_1,q_2,\cdots,q_s;\dot{q}_1,\dot{q}_2,\cdots,\dot{q}_s;t)$

---

注意到，$\frac{\partial \vec{r}_i}{\partial q_\alpha}=\frac{\partial \vec{r}_i}{\partial q_\alpha}(q_1,q_2,\cdots,q_\alpha;t)$，于是：

$$
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial \vec{r}_i}{\partial q_\alpha}
&=\frac{\partial }{\partial t}(\frac{\partial \vec{r}_i}{\partial q_\alpha})+\sum_{\beta=1}^{s}\bigg[\frac{\partial }{\partial q_\beta}(\frac{\partial \vec{r}_i}{\partial q_\alpha})\bigg]\dot{q}_\beta \\
&=\frac{\partial }{\partial q_\alpha}(\frac{\partial \vec{r}_i}{\partial t})+\frac{\partial}{\partial q_\alpha}\sum_{\beta=1}^{s} \frac{\partial \vec{r}_i}{\partial q_\beta}\dot{q}_\beta \\
&=\frac{\partial}{\partial q_\alpha}\bigg[ \frac{\partial \vec{r}_i}{\partial t}+\sum_{\beta=1}^{s}\frac{\partial \vec{r}_i}{\partial q_\beta}\dot{q}_\beta \bigg] \\
&=\frac{\partial }{\partial q_\alpha}(\frac{\mathrm{d}\vec{r}_i}{\mathrm{d}t}) 
\end{aligned}
$$

即：

$$
\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial \vec{r}_i}{\partial q_\alpha}
=\frac{\partial \dot{\vec{r}}_i}{\partial q_\alpha} \tag{2}
$$


于是：

$$
\begin{aligned}
\sum_{i=1}^{N}m_i\ddot{\vec{r}}_i\cdot\delta\vec{r}_i
&=\sum_{i=1}^{N}m_i\ddot{\vec{r}}_i\cdot\sum_{\alpha=1}^{s}\frac{\partial \vec{r}_i}{\partial q_\alpha} \delta q_\alpha \\
&=\sum_{i=1}^{N}\sum_{\alpha=1}^{s}m_i\ddot{\vec{r}}_i\cdot\frac{\partial \vec{r}_i}{\partial q_\alpha}\delta q_\alpha \\
&=\sum_{\alpha=1}^{s}\sum_{i=1}^{N}m_i\ddot{\vec{r}}_i\cdot\frac{\partial \vec{r}_i}{\partial q_\alpha}\delta q_\alpha \\
&=\sum_{\alpha=1}^{s}\delta q_\alpha\sum_{i=1}^{N}m_i\ddot{\vec{r}}_i\cdot\frac{\partial \vec{r}_i}{\partial q_\alpha} \\
&=\sum_{\alpha=1}^{s}\delta q_\alpha\sum_{i=1}^{N}\frac{\mathrm{d}(m_i\dot{\vec{r}}_i)}{\mathrm{d}t}\cdot\frac{\partial {\vec{r}}_i}{\partial {q}_\alpha} \\
&=\sum_{\alpha=1}^{s}\delta q_\alpha\sum_{i=1}^{N}\bigg[\frac{\mathrm{d}}{\mathrm{d}t}(m_i{{\dot{\vec{r}}}_i\cdot\frac{\partial {\vec{r}}_i}{\partial {q}_\alpha}})-m_i\dot{\vec{r}}_i\cdot\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial {\vec{r}}_i}{\partial {q}_\alpha} \bigg] \\
[(1)(2)代入]&=\sum_{\alpha=1}^{s}\delta q_\alpha\sum_{i=1}^{N}\bigg[\frac{\mathrm{d}}{\mathrm{d}t}(m_i{{\dot{\vec{r}}}_i\cdot\frac{\partial \dot{{\vec{r}}}_i}{\partial \dot{{q}}_\alpha}}) - m_i\dot{\vec{r}}_i\cdot\frac{\partial \dot{\vec{r}}_i}{\partial {q}_\alpha} \bigg] \\
&=\sum_{\alpha=1}^{s}\delta q_\alpha\sum_{i=1}^{N}\bigg[\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial (\frac{1}{2}m_i\dot{\vec{r}}_i^2 )}{\partial \dot{q}_\alpha}-\frac{\partial (\frac{1}{2}m_i\dot{\vec{r}}_i^2)}{\partial q_\alpha} \bigg] \\
&=\sum_{\alpha=1}^{s}\bigg[\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial T}{\partial \dot{q}_\alpha}-\frac{\partial T}{\partial q_\alpha} \bigg]\delta q_\alpha
\end{aligned}
$$

其中，$T\equiv \sum\limits_{i=1}^{N}\frac{1}{2}m_i\dot{\vec{r}}_i^2 $

### 4

取图中的 $x,y$ 为广义坐标，设斜面高度为 $h$

各质点坐标：

$$
\left\{
\begin{aligned}
\vec{r}_1
&=(x+y\cos\theta)\vec{e}_x+(h-y\sin\theta)\vec{e}_y \\
\vec{r}_2
&=x\vec{e}_x
\end{aligned}
\right.
$$

各质点速度：

$$
\left\{
\begin{aligned}
\dot{\vec{r}}_1
&=(\dot{x}+\dot{y}\cos\theta)\vec{e}_x-\dot{y}\sin\theta\vec{e}_y \\
\dot{\vec{r}}_2
&=\dot{x}\vec{e}_x
\end{aligned}
\right.
$$

以斜面顶端水平面为零势能面，有：

$$
\begin{aligned}
L
&\equiv T-V \\
&=\frac{1}{2}m_1\dot{\vec{r}}_1^2+\frac{1}{2}m_2\dot{\vec{r}}_2^2-m_1gy\sin\theta \\
&=\frac{1}{2}(m_1+m_2)\dot{x}^2+\frac{1}{2}m_1\dot{y}^2+m_1\cos\theta\cdot\dot{x}\dot{y}-m_1g\sin\theta\cdot y
\end{aligned}
$$

欧拉-拉格朗日方程：

$$
\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial \dot{q}_\alpha}-\frac{\partial L}{\partial q_\alpha}
=0
$$

代入得：

$$
(m_1+m_2)\ddot{x}+m_1\cos\theta\cdot\ddot{y}
=0
$$

$$
m_1\ddot{y}+m_1\cos\theta\cdot\ddot{x}-m_1g\sin\theta=0
$$

解得：

$$
\ddot{x}
=\frac{m_1g\sin\theta\cos\theta}{-m_1\sin^2\theta -m_2}
$$

$$
\ddot{y}
=\frac{(m_1+m_2)g\sin\theta}{m_1\sin^2\theta+m_2}
$$

斜面加速度：

$$
\vec{a}_2
\equiv \ddot{\vec{r}}_2
=\frac{m_1g\sin\theta\cos\theta}{-m_1\sin^2\theta -m_2}\vec{e}_x
$$

方块加速度：

$$
\vec{a}_1
\equiv \ddot{\vec{r}}_1
=\frac{m_2 g\sin\theta\cos\theta}{m_1\sin^2\theta+m_2}\vec{e}_x-\frac{m_1 g\sin^2\theta\cos\theta}{m_1\sin^2\theta-m_2}\vec{e}_y
$$

方块相对斜面的加速度：

$$
\vec{a}_{12}
=\vec{a}_1-\vec{a}_2
=\frac{(m_1+m_2) g\sin\theta\cos\theta}{m_1\sin^2\theta+m_2}\vec{e}_x-\frac{m_1 g\sin^2\theta\cos\theta}{m_1\sin^2\theta-m_2}\vec{e}_y
$$

### 5

$$
\begin{aligned}
\vec{a}_1
&=(\ddot{x}+\ddot{y}\cos\theta)\vec{e}_x-\ddot{y}\sin\theta\vec{e}_y \\
\vec{a}_2
&=\ddot{x}\vec{e}_x
\end{aligned}
$$

$$
\begin{aligned}
\vec{F}_1^{(A)}
=-m_1g\vec{e}_y \\
\vec{F}_2^{(A)}
=-m_2g\vec{e}_y
\end{aligned}
$$

$$
\begin{aligned}
Z
&\equiv \frac{1}{2}\sum_{i} m_i(\vec{a}_i-\frac{\vec{F}_i^{(A)}}{m_i})^2 \\
&=\frac{m_1+m_2}{2}\ddot{x}^2+\frac{m_1}{2}\ddot{y}^2+m_1\cos\theta\cdot\ddot{x}\ddot{y}-m_1g\sin\theta\cdot\ddot{y}+\frac{m_1+m_2}{2}g^2
\end{aligned}
$$

高斯原理要求：

$$
\frac{\partial Z}{\partial \ddot{x}}
=0 \\[1mm]
\frac{\partial Z}{\partial \ddot{y}}
=0 
$$

即：

$$
\begin{aligned}
(m_1+m_2)\ddot{x}+m_1\cos\theta\cdot\ddot{y}
&=0 \\
m_1\ddot{y}+m_1\cos\theta\cdot\ddot{x}-m_1g\sin\theta
&=0
\end{aligned}
$$

解得：

$$
\ddot{x}
=\frac{m_1g\sin\theta\cos\theta}{-m_1\sin^2\theta -m_2}
$$

$$
\ddot{y}
=\frac{(m_1+m_2)g\sin\theta}{m_1\sin^2\theta+m_2}
$$

### 6

#### 齐次方程的解

运动方程对应的齐次方程 $\ddot{x}+\lambda\dot{x}+\omega^2 x=0$ 的特征方程为：

$$
r^2+\lambda r+\omega^2=0
$$

1）若 $\lambda^2-4\omega^2=0$ ：

特征根为：

$$
r_{1,2}
=-\frac{\lambda}{2}
$$

齐次方程 $\ddot{x}+\lambda\dot{x}+\omega^2 x=0$ 的通解为：

$$
X(t)
=e^{-\frac{\lambda}{2}t}(C_1+C_2 t)
$$

2）若 $\lambda^2-4\omega^2>0$ ：

特征根为：

$$
r_{1,2}
=\frac{-\lambda\pm\sqrt{\lambda^2-4\omega^2}}{2}
$$

齐次方程 $\ddot{x}+\lambda\dot{x}+\omega^2 x=0$ 的通解为：

$$
X(t)
=C_1e^{r_1 t}+C_2e^{r_2 t}
$$

3）若 $\lambda^2-4\omega^2<0$ ：

特征根为：

$$
r_{1,2}
=\frac{-\lambda\pm\mathrm{i}\sqrt{4\omega^2-\lambda^2}}{2}
$$

齐次方程 $\ddot{x}+\lambda\dot{x}+\omega^2 x=0$ 的通解为：

$$
X(t)
=e^{-\frac{\lambda}{2}t}(C_1\cos\frac{\sqrt{4\omega^2-\lambda^2}}{2}t+C_2\sin\frac{\sqrt{4\omega^2-\lambda^2}}{2}t)
$$

利用辅助角公式可以将 $X(t)$ 改写为：

$$
X(t)
=C_3e^{-\frac{\lambda}{2}t}\cos(\frac{\sqrt{4\omega^2-\lambda^2}}{2}t+\phi)
$$

其中，$C_3=\sqrt{C_1^2+C_2^2},\cos\phi=\frac{C_1}{\sqrt{C_1^2+C_2^2}},\sin\phi=-\frac{C_2}{\sqrt{C_1^2+C_2^2}}$

#### 非齐次方程的形式特解

设方程 $\ddot{x}+\lambda\dot{x}+\omega^2 x=F\cos\Omega t$ 的形式特解为：

$$
\chi(t)
=A\cos\Omega t+B\sin\Omega t
$$

则：

$$
\dot{\chi}(t)
=\Omega B\cos\Omega t-\Omega A\sin\Omega t
$$

$$
\ddot{\chi}(t)
=-\Omega^2 A\cos\Omega t-\Omega^2 B\sin\Omega t
$$

代入方程 $\ddot{x}+\lambda\dot{x}+\omega^2 x=F\cos\Omega t$ 得：

$$
[-\Omega^2 A+\lambda\Omega B+\omega^2 A]\cos\Omega t+[-\Omega^2 B-\lambda\Omega A+\omega^2 B]\sin\Omega t
=F\cos\Omega t
$$

对应项系数相等，得到：

$$
-\Omega^2 A+\lambda\Omega B+\omega^2 A
=F \\
-\Omega^2 B-\lambda\Omega A+\omega^2 B
=0
$$

解得：

$$
A
=\frac{(\omega^2-\Omega^2)F}{\lambda^2\Omega^2+(\omega^2-\Omega^2)^2} \\[2mm]
B
=\frac{\lambda \Omega F}{\lambda^2\Omega^2+(\omega^2-\Omega^2)^2}
$$

于是形式特解为：

$$
\chi(t)
=\frac{(\omega^2-\Omega^2)F}{\lambda^2\Omega^2+(\omega^2-\Omega^2)^2}\cos\Omega t+\frac{\lambda \Omega F}{\lambda^2\Omega^2+(\omega^2-\Omega^2)^2}\sin\Omega t
$$

利用辅助角公式，可以把 $\chi(t)$ 化为：

$$
\chi(t)
=\frac{F}{\sqrt{\lambda^2\Omega^2+(\omega^2-\Omega^2)^2}}\cos(\Omega t +\varphi)
$$

其中，$\cos\varphi=\frac{\omega^2-\Omega^2}{\sqrt{\lambda^2\Omega^2+(\omega^2-\Omega^2)^2}},\sin\varphi=-\frac{\lambda\Omega}{\sqrt{\lambda^2\Omega^2+(\omega^2-\Omega^2)^2}}$

---

原方程的解为：

$$
\begin{aligned}
x(t)
&=X(t)+\chi(t) \\
&=\left\{
    \begin{aligned}
&e^{-\frac{\lambda}{2}t}(C_1+C_2 t)+ \frac{F}{\sqrt{\lambda^2\Omega^2+(\omega^2-\Omega^2)^2}}\cos(\Omega t +\varphi) &,\lambda^2=4\omega^2 \\
&C_1e^{r_1 t}+C_2e^{r_2 t}+ \frac{F}{\sqrt{\lambda^2\Omega^2+(\omega^2-\Omega^2)^2}}\cos(\Omega t +\varphi) &,\lambda^2>4\omega^2\\
&C_3e^{-\frac{\lambda}{2}t}\cos(\frac{\sqrt{4\omega^2-\lambda^2}}{2}t+\phi)+ \frac{F}{\sqrt{\lambda^2\Omega^2+(\omega^2-\Omega^2)^2}}\cos(\Omega t +\varphi) &,\lambda^2<4\omega^2
    \end{aligned}
\right.
\end{aligned}
$$

1）当 $\lambda \to 0$ 时，振幅不随时间发生变化

注意到：

$$
\lambda^2\Omega^2+(\omega^2-\Omega^2)^2
=(\Omega^2-\frac{2\omega^2-\lambda^2}{2})^2+\lambda^2\omega^2-\frac{\lambda^4}{4}
$$

于是当 $\Omega=\sqrt{\omega^2-\frac{\lambda^2}{2}}\approx\omega$ 时发生共振，

2）当 $\Omega \to \omega$ 时，振幅随时间的增加而减小，当时间 $t\to +\infty$ 时振幅保持不变，其值为：

$$
A
=\frac{F}{\lambda\omega}
$$



3）当$\lambda=0,\Omega=\omega$ 时，振幅不随时间改变，且发生共振，振幅为：

$$
A=+\infty
$$


### 7

以 $O$ 为原点，过 $O$ 竖直向下为 $x$ 轴正方向，过 $O$ 水平向右为 $y$ 轴正方向建系

能量守恒：

$$
\frac{1}{2}mv^2
=mgx
\Longrightarrow
v
=\sqrt{2gx}
$$

而：

$$
v
\equiv \frac{\mathrm{d}s}{\mathrm{d}t}
=\sqrt{1+(\frac{\mathrm{d}x}{\mathrm{d}y})^2}\frac{\mathrm{d}y}{\mathrm{d}t}
$$

于是：

$$
\mathrm{d}t
=\sqrt{\frac{1+x'^2}{2gx}}\mathrm{d}y
$$

积分得：

$$
t
=\frac{1}{\sqrt{2g}}\int_{0}^{y}\sqrt{\frac{1+x'^2}{x}}\mathrm{d}y
$$

最小作用量原理：

$$
S
\equiv \int_{t_0}^{t} L(q,\dot{q},t)\mathrm{d}t
$$

$S$ 取极小值要求 $L$ 满足：

$$
\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial \dot{q}_\alpha} -\frac{\partial L}{\partial q_\alpha}
=0
$$

类比可知，$t$ 取极小值要求：

$$
\frac{\mathrm{d}}{\mathrm{d}y}\frac{\partial }{\partial x'}\sqrt{\frac{1+x'^2}{x}}-\frac{\partial }{\partial x}\sqrt{\frac{1+x'^2}{x}}
=0
$$

整理得：

$$
x'^2+2xx''+1=0
$$

上面等式等号左右两边同乘 $x'$ 得：

$$
x'\cdot(1+x'^2)+x\cdot(2x'x'')
=0
$$

即：

$$
(1+x'^2)\cdot\frac{\mathrm{d}}{\mathrm{d}y}(x)+x\cdot\frac{\mathrm{d}}{\mathrm{d}y}(1+x'^2)
=0
$$

即：

$$
\frac{\mathrm{d}}{\mathrm{d}y}[x(1+x'^2)]
=0
$$

于是：

$$
x(1+x'^2)
=C_1
$$

即：

$$
\mathrm{d}y
=\sqrt{\frac{x}{C_1-x}}\mathrm{d}x
$$

积分得：

$$
y
=\int \sqrt{\frac{x}{C_1-x}}\mathrm{d}x
$$

令 $x=C_1\sin^2\theta$，则：

$$
\begin{aligned}
\int \sqrt{\frac{x}{C_1-x}}\mathrm{d}x
&=2C_1\int\sin^2\theta\mathrm{d}\theta \\
&=C_1\theta-\frac{C_1}{2}\sin2\theta+C_2 \\
&=C_1\arcsin \sqrt\frac{x}{C_1}-C_1\sqrt{x(C_1-x)}+C_3
\end{aligned}
$$

于是：

$$
y
=C_1\arcsin \sqrt\frac{x}{C_1}-C_1\sqrt{x(C_1-x)}+C_4
$$

当 $x=0$ 时，$y=0$，于是 $C_4=0$

设轨道下降终点坐标为 $x=a,y=b$，则曲线方程可表达为：

$$
y
=C_1\arcsin \sqrt\frac{x}{C_1}-C_1\sqrt{x(C_1-x)}
$$

其中，$C_1$ 满足：

$$
b=C_1\arcsin\sqrt{\frac{a}{C_1}}-C_1\sqrt{a(C_1-a)}
$$

### 8

设球面半径为 $R$

$$
\left\{
\begin{aligned}
x
&=R\sin\theta\cos\varphi \\
y
&=R\sin\theta\sin\varphi \\
z
&=R\cos\theta
\end{aligned}
\right.
$$

$$
\begin{aligned}
\mathrm{d}s
&\equiv\sqrt{\mathrm{d}x^2+\mathrm{d}y^2+\mathrm{d}z^2} \\
&=R\sqrt{\mathrm{d}\theta^2+\sin^2\theta\mathrm{d}\varphi^2} \\
&=R\sqrt{1+\sin^2\theta(\frac{\mathrm{d}\varphi}{\mathrm{d}\theta})^2}\mathrm{d}\theta \\
&=R\sqrt{1+\sin^2\theta\varphi'^2}\mathrm{d}\theta
\end{aligned}
$$

设球面上两点 $A,B$ 坐标的球坐标描述为：

$$
\theta_A
=0
$$

$$
\theta_B
=\Theta,\varphi_B=0
$$

其中，$\Theta\in [0,\pi]$ 是常数 


球面上连结 $A,B$ 的曲线方程设为 $\varphi=\varphi(\theta)$，其长度为：

$$
\begin{aligned}
S
&=\int \mathrm{d}s \\
&=R\int_{0}^{\Theta} \sqrt{1+\sin^2\theta\varphi'^2}\mathrm{d}\theta
\end{aligned}
$$

$S$ 取极小值要求：

$$
\frac{\mathrm{d}}{\mathrm{d}\theta}\frac{\partial \sqrt{1+\sin^2\theta\varphi'^2}}{\partial \varphi'}-\frac{\partial \sqrt{1+\sin^2\theta\varphi'^2}}{\partial \varphi}
=0
$$

即：

$$
\frac{\mathrm{d}}{\mathrm{d}\theta}\frac{\partial \sqrt{1+\sin^2\theta\varphi'^2}}{\partial \varphi'}
=0
$$

于是：

$$
\frac{\partial \sqrt{1+\sin^2\theta\varphi'^2}}{\partial \varphi'}
=C_1
$$

即：

$$
\frac{\varphi'\sin^2\theta}{\sqrt{1+\varphi'\sin^2\theta}}
=C_1
$$

构造函数：

$$
f(x)
=\frac{x}{\sqrt{1+x}}
$$

其在定义域上单调，故

$$
\frac{\varphi'\sin^2\theta}{\sqrt{1+\varphi'\sin^2\theta}}
=C_1
$$

当且仅当 $\varphi'\sin^2\theta=C_2$

曲线过 $A$ 点，而 $\theta_A=0$，于是：

$$
C_2
=0
$$

$\theta$ 是变量，$\varphi'\sin^2\theta$ 恒为零，则：

$$
\varphi'
=0
$$

即：

$$
\frac{\mathrm{d}\varphi}{\mathrm{d}\theta}
=0
$$

这就是说，$A,B$ 两点之间的短程线是大圆在两点间的劣弧段 







