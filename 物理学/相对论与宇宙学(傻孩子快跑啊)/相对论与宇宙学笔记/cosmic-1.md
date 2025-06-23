## 宇宙的组成

- Planets

- Stars and nebulae

- Milky Way and other galaxies

- Galaxy clusters（星系团）

- Large-scale structures

## 中心力场运动

若运动质点所受的力的作用线始终通过某个定点，则称该质点受中心力作用，定点为力心。

### 拉格朗日量

体系拉格朗日量：

$$
\begin{aligned}
L
&=T-V \\
&=\frac{1}{2}m\dot{\vec{r}}^2-U(r) \\
&=\frac{1}{2}m\left(\dot{r}\vec{\mathrm{e}}_r + r\dot{\theta}\vec{\mathrm{e}}_\theta \right)^2  - U(r) \\
&=\frac{1}{2}m\left(\dot{r}^2+r^2\dot{\theta}^2 \right) - U(r)
\end{aligned}
$$

### 运动方程

体系拉格朗日量：

$$
L
=\frac{1}{2}m\left(\dot{r}^2+r^2\dot{\theta}^2 \right) - U(r)
$$

代入 E-L 方程

$$
\frac{\partial L }{\partial q_i } - \frac{\mathrm{d} }{\mathrm{d}t } \frac{\partial L }{\partial \dot{q}_i } 
=0
$$

可得体系运动方程：

$$
m\ddot{r}-mr\dot{\theta}^2+\frac{\mathrm{d} U(r)}{\mathrm{d} r}
=0
$$

$$
\frac{\mathrm{d}}{\mathrm{d}t}\left(mr^2\dot{\theta}\right)
=0
$$

由于角动量为 $l=m r^2 \dot{\theta} $，因此上面第二条方程就是说角动量守恒。

由于角动量 $l $ 是个守恒量，利用这个守恒量把 $\dot{\theta}=l/\left(m r^2 \right) $ 代入第一条运动方程可简化之：

$$
m\ddot{r} - \frac{l^2 }{m r^3 } + \frac{\mathrm{d}U(r) }{\mathrm{d}r } 
=0
$$

### 守恒量

中心力场运动体系角动量守恒、能量守恒。

#### 根据诺特定理由对称性分析守恒量

（1）角动量守恒

体系拉格朗日量

$$
L
=\frac{1}{2}m\left(\dot{r}^2+r^2\dot{\theta}^2 \right) - U(r)
$$

只取决于 $\vec{r}$ 的大小 $r $，故 $L$ 具有空间旋转对称性，故角动量守恒。

由于角动量守恒，于是质点在做平面运动，采用极坐标系。

角动量定义为：

$$
\vec{l}
\equiv \vec{r}\times\vec{p}
=m\vec{r}\times\dot{\vec{r}}
$$

其大小为：

$$
\begin{aligned}
l
&=m\left|\vec{r}\times\dot{\vec{r}} \right| \\
&=m\left|r\vec{\mathrm{e}}_r\times\left(\dot{r}\vec{\mathrm{e}}_r+r\dot{\theta} \vec{\mathrm{e}}_\theta\right) \right| \\
&=mr^2\dot{\theta}
\end{aligned}
$$

（2）能量守恒

体系拉格朗日量

$$
L
=\frac{1}{2}m\left(\dot{r}^2+r^2\dot{\theta}^2 \right) - U(r)
$$

不显含时间，拉格朗日量具有时间平移对称性，因此体系能量守恒。

#### 由运动方程分析守恒量

（1）角动量守恒

$\theta$ 为循环坐标，其相应的广义动量是个守恒量，而 $\theta$ 对应的广义动量恰为角动量：

$$
p_\theta
=\frac{\partial L}{\partial \dot{\theta}}
=mr^2\dot{\theta}
=l
$$

角动量守恒导致开普勒第二定律：质点径矢单位时间扫过的面积相等。

设位矢在 $\mathrm{d}t$ 时间内转过 $\mathrm{d}\theta$ 角度，扫过的面积为：

$$
\mathrm{d}A
=\frac{1}{2} r^2 \mathrm{d}\theta
$$

于是单位时间内扫过的面积为：

$$
\frac{\mathrm{d}A}{\mathrm{d}t}
=\frac{1}{2}r^2\frac{\mathrm{d}\theta}{\mathrm{d}t}
=\frac{1}{2}r^2\dot{\theta}
=\frac{l}{2m}
=\mathrm{const}
$$

（2）能量守恒

体系能量：

$$
\begin{aligned}
E
&=T+V \\
&=\frac{1}{2}m\left(\dot{r}^2+r^2\dot{\theta}^2 \right) + U(r)
\end{aligned}
$$

利用角动量这个守恒量 $l=m r^2 \dot{\theta} $ 可把能量简化为：

$$
\begin{aligned}
E
&=\frac{1}{2}m\left(\dot{r}^2+r^2\dot{\theta}^2 \right) + U(r) \\
&=\frac{1}{2}m\left[\dot{r}^2+r^2\left(\frac{l }{m r^2 } \right)^2 \right] + U(r) \\
&=\frac{1 }{2 } m \dot{r}^2 + \frac{l^2 }{2m r^2 } + U(r)
\end{aligned}
$$

利用运动方程

$$
m\ddot{r} - \frac{l^2 }{m r^3 } + \frac{\mathrm{d}U(r) }{\mathrm{d}r } 
=0
$$

可计算能量对时间的全微商：

$$
\begin{aligned}
\frac{\mathrm{d}E }{\mathrm{d}t } 
&=m \dot{r} \ddot{r} - \frac{l^2 }{m r^3} \dot{r} + \frac{\mathrm{d}U(r) }{\mathrm{d}r } \dot{r} \\
&=\dot{r}\left(m\ddot{r} - \frac{l^2 }{m r^3 } + \frac{\mathrm{d}U(r) }{\mathrm{d}r }  \right) \\
&=0
\end{aligned}
$$

从上式可见，体系能量守恒。

#### 中心力场轨道微分方程（比耐公式）

中心力场的微分轨道方程：

$$
\frac{\mathrm{d}^2 u}{\mathrm{d}\theta^2}+u+\frac{m}{l^2}\frac{\mathrm{d}U}{\mathrm{d}u}
=0
$$

其中，$u=1/r $，上面方程称为**比耐公式**。

证明：

第一条运动方程：

$$
m\ddot{r} - \frac{l^2 }{m r^3 } + \frac{\mathrm{d}U(r) }{\mathrm{d}r } 
=0 \tag{1}
$$

$(1) $ 中出现了 $r $ 对时间的二阶微商。但我们想要轨道方程，即 $r $ 与 $\theta $ 的关系，为此，利用角动量这个守恒量把对时间 $t $ 的微商转化为对角度 $\theta $ 的微商。

$$
l
=mr^2\dot{\theta}
\Longrightarrow
\frac{\mathrm{d}}{\mathrm{d}t}
=\frac{\mathrm{d}\theta}{\mathrm{d}t} \frac{\mathrm{d}}{\mathrm{d}\theta}\
=\frac{l}{mr^2}\frac{\mathrm{d}}{\mathrm{d}\theta}
$$

$$
\frac{\mathrm{d}^2}{\mathrm{d}t^2}
=\frac{l}{mr^2}\frac{\mathrm{d}}{\mathrm{d}\theta}\left(\frac{l}{mr^2}\frac{\mathrm{d}}{\mathrm{d}\theta}\right)
$$

于是 $(1)$ 可以表示为：

$$
\frac{l}{r^2}\frac{\mathrm{d}}{\mathrm{d}\theta}\left(\frac{l}{mr^2}\frac{\mathrm{d}r}{\mathrm{d}\theta}\right)-\frac{l^2}{mr^3} + \frac{\mathrm{d}U }{\mathrm{d}r } 
=0 \tag{2}
$$

令：

$$
r = 1/u
$$

$$
\mathrm{d}r
=-\frac{1 }{u^2 } \mathrm{d}u
$$

代入 $(2) $ 整理得到用 $u=1/r $ 表达的中心力场轨道微分方程（比耐公式）：

$$
\frac{\mathrm{d}^2 u}{\mathrm{d}\theta^2}+u+\frac{m}{l^2}\frac{\mathrm{d}U}{\mathrm{d}u}
=0
$$

#### 中心力场轨道积分方程

注意到，角动量 $l$ 和能量 $E$ 是两个守恒量：

$$
E
=\frac{1}{2}m\dot{r}^2 + \frac{l^2}{2mr^2} + U(r)
\Longrightarrow
\mathrm{d}t
=\frac{\mathrm{d}r}{\sqrt{\frac{2}{m}\left[E-U(r)-\frac{l^2}{2mr^2}\right]}}
$$

$$
l
=mr^2\dot{\theta}
\Longrightarrow
\mathrm{d}t
=\frac{mr^2}{l}\mathrm{d}\theta
$$

消去 $\mathrm{d}t$，积分得：

$$
\theta
=\theta_0 + \int_{r_0}^{r} \frac{l\mathrm{d}r/r^2}{\sqrt{2m[E-U(r)]-(l/r)^2}}
$$

这就是轨道方程，其中，$E,l,r_0,\theta_0$ 是常数。

## 开普勒运动问题：平方反比吸引力

### 圆锥曲线的焦点-准线定义

在平面上，所有到一个定点的距离与到一条定直线的距离的比值是一个固定常数的点的轨迹，称为圆锥曲线。其中，定点称为圆锥曲线的焦点（focus），定直线称为圆锥曲线的准线（directrix），二者互相对应，对应的焦点与准线的距离称作焦准距（focal parameter），通常记作 $p $，比值称作圆锥曲线的离心率（eccentricity），通常记作 $e .$

当 $e=0 $ 时，轨迹称为圆；

当 $e\in(0,1) $ 时，轨迹称为椭圆；

当 $e=1 $ 时，轨迹称为抛物线；

当 $e>1 $ 时，轨迹称为双曲线。

### 极坐标下圆锥曲线的方程

选焦点作为原点，对称轴作为极轴，建立极坐标。考虑焦准距为 $p $，离心率为 $e $ 的圆锥曲线上一点 $(r,\theta) $，由定义有：

$$
\frac{r }{p-r\cos(\pi-\theta) } 
=e
$$

即：

$$
r
=\frac{ep }{1-e\cos\theta } 
$$

### 开普勒第一定律（椭圆定律）

每一个行星都沿着各自的椭圆轨道环绕着太阳，而太阳则处在椭圆的一个焦点上。

万有引力：

$$
F
=-\frac{GMm}{r^2}
=-\frac{k}{r^2}
\Longleftrightarrow
U(r)
=-\frac{k}{r}
$$

此时轨道具有圆锥曲线方程的形式：

$$
r
=\frac{p}{1+e\cos(\theta-\theta_0)},\quad
p
=\frac{l^2}{mk},\quad
e
=\sqrt{1+\frac{2El^2}{mk^2}}
$$

该圆锥曲线的焦点即为力心，$p$ 为圆锥曲线的焦准距，$e$ 为圆锥曲线的离心率。

#### 标准积分公式

$$
\begin{aligned}
\int \frac{\mathrm{d}x}{\sqrt{ax^2+bx+c}}
&=\frac{1}{\sqrt{-a}}\arccos\frac{-(b+2ax)}{\sqrt{b^2-4ac}}
\end{aligned}
$$

#### 椭圆轨迹的推导

令 $r=\frac{1}{u}$

$$
\theta
=\theta_0-\int\frac{\mathrm{d}u}{\sqrt{\frac{2mE}{l^2}+\frac{2mku}{l^2}-u^2}}
$$

标准积分公式给出：

$$
\int\frac{\mathrm{d}x}{\sqrt{\alpha+\beta x+\gamma x^2}}
=\frac{1}{\sqrt{-\gamma}}\arccos\frac{-(\beta+2\gamma x)}{\sqrt{\beta^2-4\alpha \gamma}}
$$

令 $\alpha=\frac{2mE}{l^2},\beta=\frac{2mk}{l^2},\gamma=-1 $ 得到：

$$
\theta
=\theta_0-\arccos\frac{\frac{l^2 u}{mk}-1}{\sqrt{1+\frac{2El^2}{mk^2}}}
$$

最后得到：

$$
\frac{1}{r}
=\frac{mk}{l^2}\left[1+\sqrt{1+\frac{2El^2}{mk^2}}\cos(\theta-\theta_0)\right]
$$

$e$ 不同，圆锥曲线可以分为椭圆、抛物线和双曲线，而 $e$ 又取决于体系的能量，故：

（1）当 $E=-\frac{mk^2}{2l^2} $ 时，$e=0$，轨迹为圆

（2） 当 $E<0$ 时，$e<1$，轨迹为椭圆，此时可证：

椭圆的半长轴 $a$ 只与能量有关：$a=\frac{r_{\min}+r_{\max}}{2}=\frac{p}{1-e^2}=-\frac{k}{2E}$

给定能量 $E$ 后，椭圆的偏心率 $e$ 由角动量 $l$ 决定：$e=\sqrt{1-\frac{l^2}{mka}} $

（3）当 $E=0$ 时，$e=1$，轨迹为抛物线 

（4）当 $E>0$ 时，$e>1$，轨迹为双曲线

### 开普勒第二定律（面积定律）

质点径矢单位时间扫过的面积相等。

证明：

设位矢在 $\mathrm{d}t$ 时间内转过 $\mathrm{d}\theta$ 角度，扫过的面积为：

$$
\mathrm{d}A
=\frac{1}{2} r^2 \mathrm{d}\theta
$$

于是单位时间内扫过的面积为：

$$
\frac{\mathrm{d}A}{\mathrm{d}t}
=\frac{1}{2}r^2\frac{\mathrm{d}\theta}{\mathrm{d}t}
=\frac{1}{2}r^2\dot{\theta}
=\frac{l}{2m}
=\mathrm{const}
$$

### 开普勒第三定律（椭圆轨道 $(E<0)$ 运动周期）

椭圆轨道半长轴 $a $ 的三次方 $a^3 $ 与周期 $T $ 的平方 $T^2 $ 成正比：

$$
\frac{a^3 }{T^2 }
=\mathrm{const}
$$

在一般中心吸引力场的作用下，束缚运动的轨道不一定是闭合的。椭圆运动周期，记为 $\tau$，定义为质点从近日点出发到再次返回近日点所需的时间。可以求出：

$$
\tau
=2\pi a^{\frac{3}{2}}\sqrt{\frac{m}{k}}
$$

证明：

将万有引力场 $U(r)=-\frac{k}{r} $，代入得：

$$
t
=\sqrt{\frac{m}{2}}\int_{r_0}^{r}\frac{\mathrm{d}r}{\sqrt{\frac{k}{r}-\frac{l^2}{2mr^2}+E}}
=\sqrt{\frac{ma}{k}}\int_{r_0}^{r}\frac{r\mathrm{d}r}{\sqrt{-(r-a)^2+e^2a^2}}
$$

令 $r=a(1-e\cos\psi)$，结合轨道方程可看出，$\theta$ 经历一周，$\psi$ 将通过

$$
t
=\sqrt{\frac{ma^3}{k}}\int_{\psi_0}^{\psi}(1-e\cos\psi)\mathrm{d}\psi
$$

## Cosmic scales

$1~\mathrm{AU}\approx 150~\mathrm{million~km} $： 地-日平均距离

$1~\mathrm{lightyear(ly)} $：光年

$1~\mathrm{parsec(pc)}\approx 3.26~\mathrm{ly} $

$1~\mathrm{Kpc}=10^3~\mathrm{pc} $

$1~\mathrm{Mpc=10^6~\mathrm{pc}} $


## Red shift

### Comoving coordinates（共动坐标）

共动坐标是一种随宇宙一起膨胀的坐标系。

宇宙中任意两个天体之间的实际物理距离 $D(t) $ 通常表示为：

$$
D(t)
=a(t) \cdot \chi
$$

其中，$a(t) $ 是尺度因子，用于描述宇宙的膨胀；$\chi $ 就是共动距离，它在宇宙膨胀过程中保持不变。

### 红移

红移是光的波长被拉长的现象，通常用符号 $z $ 表示：

$$
z
\equiv \frac{\lambda_{\mathrm{obs}} - \lambda_{\mathrm{emit}} }{\lambda_{\mathrm{emit}} } 
=\frac{\lambda_{\mathrm{obs}} }{\lambda_{\mathrm{emit}} } - 1
$$

其中，$\lambda_{\mathrm{emit}} $ 是光发出时的波长，$\lambda_{\mathrm{obs}} $ 是光被我们观测到时的波长。

#### 三种红移来源

|类型 | 原因 | 示例|
|:---:|:---|:---|
|多普勒红移 | 天体在远离我们 | 星系运动、光谱偏红|
|引力红移 | 强引力场使光能量下降 | 黑洞附近|
|宇宙学红移 | 宇宙膨胀“拉伸”了光的波长 | 远处星系、宇宙微波背景辐射|

#### 宇宙学红移 $z $ 和尺度因子 $a(t) $ 的关系

$$
1 + z
=\frac{a(t_{\mathrm{obs}}) }{a(t_{\mathrm{emit}}) } 
$$

推导：

设光的周期为 $\Delta t $，若不考虑宇宙膨胀，光的波长（共动距离）为：

$$
\lambda_0 = c\Delta t
$$

先考虑宇宙膨胀，在光发出的时刻 $t_{\mathrm{emit}} $，宇宙尺度因子为 $a(t_{\mathrm{emit}}) $，根据实际距离 $D(t) $，尺度因子 $a(t) $ 和共动距离 $\chi $ 的关系

$$
D(t) = a(t) \cdot \chi
$$

有：

$$
\lambda_{\mathrm{emit}}
=a(t_{\mathrm{emit}}) \lambda_0
$$

类似地，在光被接收的时刻 $t_{\mathrm{obs}} $，宇宙尺度因子为 $a(t_{\mathrm{obs}}) $，有：

$$
\lambda_{\mathrm{obs}}
=a(t_{\mathrm{obs}}) \lambda_0
$$

因此：

$$
z
\equiv \frac{\lambda_{\mathrm{obs}} - \lambda_{\mathrm{emit}} }{\lambda_{\mathrm{emit}} } 
=\frac{\lambda_{\mathrm{obs}} }{\lambda_{\mathrm{emit}} } - 1
=\frac{a(t_{\mathrm{obs}}) }{a(t_{\mathrm{emit}}) } - 1
$$

即：

$$
1+z
=\frac{a(t_{\mathrm{obs}}) }{a(t_{\mathrm{emit}}) } 
$$


### 哈勃常数

哈勃常数 $H_0 $ 是描述宇宙当前膨胀速度的参数，定义为：

$$
H_0(t_0)
\equiv \frac{\dot{a}(t) }{a(t) }\bigg|_{t=t_0} 
$$

#### 低红移时红移和哈勃常数的关系

红移 $z $ 和尺度因子 $a(t) $ 的关系

$$
1 + z
=\frac{a(t_{\mathrm{obs}}) }{a(t_{\mathrm{emit}}) } 
$$

若 $\Delta t\equiv t_{\mathrm{obs}} - t_{\mathrm{emit}} $ 很小，则 $a(t_{\mathrm{obs}}) $ 在 $t=t_{\mathrm{emit}} $ 处展开，保留至一阶小量：

$$
\begin{aligned}
1+z
&=\frac{a(t_{\mathrm{obs}}) }{a(t_{\mathrm{emit}}) }
\approx \frac{a(t_{\mathrm{emit}}) + \dot{a}(t_{\mathrm{emit}}) \Delta t }{a(t_{\mathrm{emit}}) } \\
&=1 + \frac{\dot{a}(t_{\mathrm{emit}}) }{a(t_{\mathrm{emit}}) } \Delta t \\
&=1 + H(t_{\mathrm{emit}}) \Delta t \\
&\approx 1 + H(t_{\mathrm{obs}}) \Delta t \\
&=1 + H(t_{\mathrm{obs}}) \frac{D }{c } \\
\end{aligned}
$$

即：

$$
z
\approx H(t_{\mathrm{obs}}) \frac{D }{c }
$$

### 现代宇宙学的假设

（isotropic）宇宙是各向同性的；

（homogeneous）宇宙是均匀的；

The expansion receding speed is greater the farther apart. 距离我们越远的星系，它们因为宇宙膨胀而“退行”的速度越快。

The universe has grown from the tiny primitive universe to how it looks today. 宇宙从最初那个微小、原始的宇宙，演化成了今天这个样子。

The universe began about 14 billion years ago(Big Bang). 宇宙大约始于 140 亿年前（大爆炸）。

At the beginning, the universe was very dense, at extremely high temperature.

10-44 seconds after its birth, the universe expands rapidly, in 10-34 seconds by a factor of 10100, in a phase called "Inflation".

After inflation, the universe expands and cools until today.

### 哈勃定律

$$
v = H d
$$

$v $-recession speed, $d $-distance, $H $-Hubble constant

### 宇宙微波背景辐射（CMB）

CMB 是从宇宙中各个方向射来的微波辐射，其本质是宇宙在大爆炸后约 38 万年冷却到可以形成中性原子时释放出的光。

大爆炸早期（宇宙年龄 < 38 万年），宇宙高温高密，充满光子、电子、质子。光子被自由电子散射（康普顿散射），无法自由传播。

重组时期（宇宙年龄 ≈ 38 万年，温度约 3000K），宇宙膨胀冷却到可以形成中性氢原子。光子不再频繁散射，开始自由传播。这些光子就是现在的 CMB。

今天的观测（经过138亿年膨胀），由于宇宙膨胀，光波被拉长成微波波段。光子温度降为约 2.73 K，对应波长在毫米级。

#### 观测特征

几乎各向同性：从任何方向看，CMB 的温度几乎一致。

温度微扰（$~10^{-5}$）：小尺度的温度涨落揭示了早期宇宙的密度扰动，是星系形成的“种子”。

黑体谱：CMB 的光谱极度接近理想黑体，峰值在 160 GHz 左右。

### 暗物质

暗物质是一种只通过引力相互作用、极弱的可能的弱相互作用参与宇宙动力学的物质成分。

暗物质不参与电磁相互作用（即不吸光、不发光、不反射光）

#### 暗物质存在的证据

（1）星系旋转曲线异常：

按牛顿引力理论，星系外围的恒星应转得更慢，但实际观察显示它们的转速远超预期，说明有额外“看不见”的质量在拉扯它们。

（2）星系团中引力不足：

星系团中星系运动太快，仅靠可见物质无法束缚它们。

弗里茨·兹威基（1930s）最早提出“暗物质”来解释这一现象。

（3）引力透镜效应：

大质量天体弯曲背景光形成“透镜”。

观测到的光线弯曲比可见质量预测的更强。

（4）宇宙微波背景辐射（CMB）涨落模式：

精细的涨落结构表明宇宙中有大量不参与辐射相互作用的冷物质。

（5）宇宙大尺度结构形成：

如果只有普通物质，宇宙膨胀太快，无法形成今天这样密集的星系结构。


### 暗能量

在广义相对论框架中，暗能量可以看作是一种具有负压的流体或场，其压强 $p $ 和能量密度 $\rho $ 满足状态方程：

$$
p = w \rho
$$

当 $w<-1/3 $ 会导致宇宙加速膨胀。

$$
-4\pi G \rho
=3\left(H^2+\dot{H} \right)
$$

$$
P_\Lambda
=-\rho_\Lambda
=-\frac{\Lambda c^2 }{8 \pi G } 
$$

加速方程

$$
\boxed{
\frac{\ddot{a} }{a } 
=\frac{4\pi G }{3 } \left(\rho + 3 p \right) + \frac{\Lambda c^2 }{3 } 
}
$$

Frieman 方程

$$
\boxed{
H^2
=\frac{8\pi G }{3 } \rho - \frac{k c^2 }{a^2 } + \frac{\Lambda c^2 }{3 } 
}
$$