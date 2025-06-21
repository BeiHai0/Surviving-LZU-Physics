# 0 记号约定

## 爱因斯坦求和约定

本文采用爱因斯坦求和约定，即两个重复的指标（不管指标在上面还是在下面）默认对指标所有可能的取值求和。不采用爱因斯坦求和约定的地方会明确指出。

## 张量的广义定义与R场论指标位置约定

### 协变张量

设有一个由 $n $ 个下指标描述的量 $U_{i_1i_2\cdots i_n} $，当坐标有如下变换

$$
x'^k
=x'^k\left(x^1,x^2,\cdots,x^l\right),\quad k=1,2,\cdots,l
$$

时，若 $U_{i_1i_2\cdots i_n} $ 按照如下规律变化

$$
U_{i_1i_2\cdots i_n}'
=U_{j_1j_2\cdots j_n}\frac{\partial x^{j_1} }{\partial x'^{i_1} } \frac{\partial x^{j_2} }{\partial x'^{i_2} } \cdots \frac{\partial x^{j_n} }{\partial x'^{i_n} } 
$$

则称 $U_{i_1i_2\cdots i_n} $ 为 $l $ 维空间的 $n $ 阶**协变张量**。

### 逆变张量

设有一个由 $n $ 个上指标描述的量 $U^{i_1i_2\cdots i_n} $，当坐标有如下变换

$$
x'^k
=x'^k\left(x^1,x^2,\cdots,x^l\right),\quad k=1,2,\cdots,l
$$

时，若 $U^{i_1i_2\cdots i_n} $ 按照如下规律变化

$$
U'^{i_1i_2\cdots i_n}
=U^{j_1j_2\cdots j_n}\frac{\partial x'^{i_1} }{\partial x^{j_1} } \frac{\partial x'^{i_2} }{\partial x^{j_2} } \cdots \frac{\partial x'^{i_n} }{\partial x^{j_n} } 
$$

则称 $U^{i_1i_2\cdots i_n} $ 为 $l $ 维空间的 $n $ 阶**协变张量**。

### 混合张量

设有一个由 $n $ 个下指标和 $m $ 个上指标描述的量 $U^{j_1j_2\cdots j_m}_{i_1i_2\cdots i_n} $，当坐标有如下变换

$$
x'^k
=x'^k\left(x^1,x^2,\cdots,x^l\right),\quad i=1,2,\cdots,l
$$

时，按照规律

$$
U'^{j_1j_2\cdots j_m}_{i_1i_2\cdots i_n}
=U^{\beta_1\beta_2\cdots\beta_m}_{\alpha_1\alpha_2\cdots\alpha_n} \cdot 
\frac{\partial x'^{j_1} }{\partial x^{\beta_1} } \frac{\partial x'^{j_2} }{\partial x^{\beta_2} } \cdots \frac{\partial x'^{j_m} }{\partial x^{\beta_m} }\cdot \frac{\partial x^{\alpha_1} }{\partial x'^{i_1} } \frac{\partial x^{\alpha_2} }{\partial x'^{i_2} } \cdots \frac{\partial x^{\alpha_n} }{\partial x'^{i_n} }
$$

变化的量称为**混合张量**。

> 简单记忆变换规则：一对上下指标才求和+求和的都是不带撇的坐标。

### 为什么R场论的指标统一写成下指标

狭义相对论中时空坐标共四维，时空坐标的变换规律具体为广义洛伦兹变换：

$$
x'^\mu = A^\mu_{\nu} x^\nu + b^\mu,\quad \mu=1,2,3,4,\quad  X' = AX + b
$$

> 注意，这里 $A^\mu_{\nu} $ 并非张量。R场论中， $A^\mu_{\nu} $ 代表矩阵 $A $ 的 $\mu $ 行 $\nu $ 列矩阵元；$A^\nu_{\mu} $ 代表矩阵 $A $ 的 $\nu $ 行 $\mu $ 列矩阵元。

容易得到**变换后**的时空坐标对**变换前**的时空坐标的偏导：

$$
\frac{\partial x'^\mu }{\partial x^\nu } = A^\mu_{\nu}
$$

为了求出**变换前**的时空坐标对**变换后**的时空坐标的偏导，考虑矩阵形式的广义洛伦兹变换：

$$
X' = AX + b
$$

$$
A^{-1} X' = X + A^{-1} b
$$

$$
X = A^{-1} X' - A^{-1} b
$$

回到分量形式：

$$
x^\mu = \left(A^{-1} \right)^\mu_{\nu} x'^\nu - \left(A^{-1} \right)^\mu_{\nu} b^\nu
$$

因此，**变换前**的时空坐标对**变换后**的时空坐标的偏导为：

$$
\frac{\partial x^\mu }{\partial x'^\nu } = \left(A^{-1} \right)^\mu_{\nu}
$$

考虑洛伦兹变换矩阵的正交性：

$$
A^\mathrm{T} A = I
\Longrightarrow A^{-1} = A^\mathrm{T}
$$

因此：

$$
\frac{\partial x^\mu }{\partial x'^\nu }
=\left(A^{-1} \right)^\mu_{\nu}
=\left(A^{\mathrm{T}} \right)^\mu_{\nu}
=A_\mu^{\nu}
$$

总之，若 $x^\mu $ 的变换规律为广义洛伦兹变换 $x^\mu\to x'^\mu=A^\mu_{\nu} x^\nu + b^\mu $，则有：

$$
\frac{\partial x'^\mu }{\partial x^\nu } = A^\mu_{\nu},\quad 
\frac{\partial x^\mu }{\partial x'^\nu } = A^\nu_{\mu}
$$

狭义相对论中，当时空坐标进行广义洛伦兹变换 $x^\mu\to x'^\mu=A^\mu_{\nu} x^\nu + b^\mu $ 时，协变张量的变换规律为：

$$
\begin{aligned}
U_{\mu_1\mu_2\cdots \mu_n}'
&=U_{\nu_1\nu_2\cdots \nu_n}\frac{\partial x^{\nu_1} }{\partial x'^{\mu_1} } \frac{\partial x^{\nu_2} }{\partial x'^{\mu_2} } \cdots \frac{\partial x^{\nu_n} }{\partial x'^{\mu_n} } \\
&=A^{\mu_1}_{\nu_1} A^{\mu_2}_{\nu_2}\cdots A^{\mu_n}_{\nu_n} U_{\nu_1\nu_2\cdots \nu_n}
\end{aligned}
$$

当时空坐标进行广义洛伦兹变换 $x^\mu\to x'^\mu=A^\mu_{\nu} x^\nu + b^\mu $ 时，逆变张量的变换规律：

$$
\begin{aligned}
U'^{\mu_1\mu_2\cdots \mu_n}
&=U^{\nu_1\nu_2\cdots \nu_n}\frac{\partial x'^{\mu_1} }{\partial x^{\nu_1} } \frac{\partial x'^{\mu_2} }{\partial x^{\nu_2} } \cdots \frac{\partial x^{\mu_n} }{\partial x^{\nu_n} } \\
&=A^{\mu_1}_{\nu_1} A^{\mu_2}_{\nu_2} \cdots A^{\mu_n}_{\nu_n} U^{\nu_1\nu_2\cdots \nu_n}
\end{aligned}
$$

因此，在这种约定下，协变张量、逆变张量和混合张量三者没有区别（张量指标在上还是在下都服从相同的变换规律），因此把它们统称为张量，并且**约定张量的指标全部写为下标**。

约定时空坐标的广义洛伦兹变换写为：

$$
\boxed{
x_\mu\to x'_\mu=A_{\mu\nu} x_\nu + b_\mu
}
$$

> 这种约定下，$A_{\mu\nu} $ 代表矩阵 $A $ 的 $\mu $ 行 $\nu $ 列矩阵元。

当时空坐标进行广义洛伦兹变换 $x_\mu\to x'_\mu=A_{\mu\nu} x_\nu + b_\mu $ 时，$n $ 阶张量的变换规律统一写为：

$$
\boxed{
U'_{\mu_1\mu_2\cdots \mu_n}
=A_{\mu_1\nu_1}A_{\mu_2\nu_2} \cdots A_{\mu_n\nu_n} U_{\nu_1\nu_2\cdots \nu_n} 
}
$$

# 1 粒子物理与量纲分析

## 粒子物理

### 61种基本粒子

<p align="center">
  <img src="fig/1.png" alt="" width="50%">
</p>

只参与弱相互作用和电磁相互作用，不参与强相互作用的费米子称为**轻子**（Lepton）。

|Lepton name| Symbol | $M$ | $Q$ | $J$ | $L_e$ | $L_\mu$ | $L_\tau$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Electron|$e^-$|$0.511 $|$-1$|$1/2$|$+1 $|$0 $|$0 $|
|anti-Electron|$e^+ $|$0.511$|$+1 $|$1/2 $|$-1 $|$0 $|$0 $|
|Electron neutrino|$\nu_e $|$<2\times 10^{-6} $|$0 $|$1/2 $|$+1 $|$0 $|$0 $|
|anti-Electron neutrino |$\tilde{\nu}_e $|$<2\times 10^{-6} $|$0 $|$1/2 $|$-1 $|$0 $|$0 $|
|muon|$\mu^- $|$105.66 $|$-1 $|$1/2 $|$0 $|$+1 $|$0 $|
|anti-muon|$\mu^+ $|$105.66 $|$+1 $|$1/2 $|$0 $|$-1 $|$0 $|
|muon neutrino|$\nu_\mu $|$<2\times 10^{-6} $|$0 $|$1/2 $|$0 $|$+1 $|$0 $|
|anti muon neutrino|$\tilde{\nu}_\mu $|$<2\times 10^{-6} $|$0 $|$1/2 $|$0 $|$-1 $|$0 $|
|tau|$\tau^- $|$1776.86 $|$-1 $|$1/2 $|$0 $|$0 $|$+1 $|
|anti-tau|$\tau^+ $|$1776.86 $|$+1 $|$1/2 $|$0 $|$0 $|$-1 $|
|tau neutrino|$\nu_\tau $|$<2\times 10^{-6} $|$0 $|$1/2 $|$0 $|$0 $|$+1 $|
|anti tau neutrino|$\tilde{\nu}_\tau $|$<2\times 10^{-6} $|$0 $|$1/2 $|$0 $|$0 $|$-1 $|

在轻子参与的各类反应中，各类轻子数守恒。

参与强相互作用的粒子称为**强子**。质子和中子都是强子。

自旋为零和整数的强子称为**介子**（Meson），自旋为半整数的强子称为**重子**（Baryon）。

具有奇异量子数的重子称为**超子**（Hyperon）。

重子由三个夸克组成，介子由夸克和反夸克组成。

每种夸克具有色量子数（红、绿、蓝），每种反夸克具有另外三种色量子数（青、洋红、黄）

| Quark flavour | $M$ (MeV) | $Q$ | $J$ | $B$ | $I_3$ | $C$ | $S$ | $T$ | $B'$ |
|:-------------:|:---------:|:---:|:---:|:---:|:-----:|:---:|:---:|:---:|:----:|
| $u$           | $2.2$     | $+\frac{2}{3}$ | $\frac{1}{2}$ | $+\frac{1}{3}$ | $+\frac{1}{2}$ | $0$ | $0$ | $0$ | $0$ |
| $d$           | $4.7$     | $-\frac{1}{3}$ | $\frac{1}{2}$ | $+\frac{1}{3}$ | $-\frac{1}{2}$ | $0$ | $0$ | $0$ | $0$ |
| $c$           | $1270$    | $+\frac{2}{3}$ | $\frac{1}{2}$ | $+\frac{1}{3}$ | $0$ | $+1$ | $0$ | $0$ | $0$ |
| $s$           | $96$      | $-\frac{1}{3}$ | $\frac{1}{2}$ | $+\frac{1}{3}$ | $0$ | $0$ | $-1$ | $0$ | $0$ |
| $t$           | $172760$  | $+\frac{2}{3}$ | $\frac{1}{2}$ | $+\frac{1}{3}$ | $0$ | $0$ | $0$ | $+1$ | $0$ |
| $b$           | $4180$    | $-\frac{1}{3}$ | $\frac{1}{2}$ | $+\frac{1}{3}$ | $0$ | $0$ | $0$ | $0$ | $-1$ |

| Quark flavour | $M$ (MeV) | $Q$ | $J$ | $B$ | $I_3$ | $C$ | $S$ | $T$ | $B'$ |
|:-------------:|:---------:|:---:|:---:|:---:|:-----:|:---:|:---:|:---:|:----:|
| $\bar{u}$     | $2.2$     | $-\frac{2}{3}$ | $\frac{1}{2}$ | $-\frac{1}{3}$ | $-\frac{1}{2}$ | $0$ | $0$ | $0$ | $0$ |
| $\bar{d}$     | $4.7$     | $+\frac{1}{3}$ | $\frac{1}{2}$ | $-\frac{1}{3}$ | $+\frac{1}{2}$ | $0$ | $0$ | $0$ | $0$ |
| $\bar{c}$     | $1270$    | $-\frac{2}{3}$ | $\frac{1}{2}$ | $-\frac{1}{3}$ | $0$ | $-1$ | $0$ | $0$ | $0$ |
| $\bar{s}$     | $96$      | $+\frac{1}{3}$ | $\frac{1}{2}$ | $-\frac{1}{3}$ | $0$ | $0$ | $+1$ | $0$ | $0$ |
| $\bar{t}$     | $172760$  | $-\frac{2}{3}$ | $\frac{1}{2}$ | $-\frac{1}{3}$ | $0$ | $0$ | $0$ | $-1$ | $0$ |
| $\bar{b}$     | $4180$    | $+\frac{1}{3}$ | $\frac{1}{2}$ | $-\frac{1}{3}$ | $0$ | $0$ | $0$ | $0$ | $+1$ |

### 守恒定律

存在 $\ell_e,\ell_\mu,\ell_\tau $ 三种轻子数。在轻子参与的各种反应中，各类轻子数分别守恒。

在强子的粒子反应中，电荷 $Q $ 和重子数 $B $ 守恒。

在各种反应中，能量、动量、电荷、角动量守恒。

强相互作用中，能量、动量、电荷、角动量守恒、**同位旋、奇异数、宇称、重子数**守恒。

电磁相互作用中，能量、动量、电荷、角动量守恒、**奇异数、宇称、重子数守恒**；**同位旋不守恒**。

弱相互作用中，电荷、轻子数、重子数、角动量守恒；同位旋不守恒、宇称不守恒、奇异数不守恒、CP不守恒。

### $\mathrm{U}(1) $ 规范理论

QED 是关于带电粒子、光子 $\gamma $ 及其相互作用的量子场论，是 $\mathrm{U}(1) $ 规范场理论，即阿贝尔规范场理论。光子是传递电磁相互作用的规范玻色子。

### $\mathrm{SU}(2)\times\mathrm{U}(1) $ 规范理论

基本粒子衰变是一种弱相互作用。电弱统一理论是 $\mathrm{SU}(2)\times\mathrm{U}(1) $ 规范理论。

电弱统一理论包括：QED 中传递电磁相互作用的光子 $\gamma $；传递弱相互作用的 $W^{\pm},Z^0 $ 三类规范玻色子，称为中间玻色子。

电弱统一理论克服了费米理论（四个费米子直接相互作用）不能重整化的困难，预言了与 $Z^0 $ 对应的中性流，与实验符合得很好。

电弱统一理论中，规范玻色子 $W^{\pm},Z^0 $ 的质量由 Higgs 场真空自发破缺导致。

### $\mathrm{SU}(3) $ 规范理论

QCD 是 $\mathrm{SU(3)_C} $ 非阿贝尔规范理论。

$\mathrm{SU(3)} $ 群的作用以夸克三种颜色为变换对象，并以 $8 $ 种 $J=1 $ 的规范玻色子传递相互作用。在色夸克间传递强相互作用的规范玻色子称为**胶子**。

**夸克禁闭**：自然界不存在自由夸克。

### 标准模型

标准模型是以三代轻子和三代夸克作为基本粒子、以强子的夸克模型和电弱统一理论和 QCD 为基础建立起来的。

## 量纲分析与自然单位制

$$
[\hbar]
=\frac{[M] [L]^2 }{[t] } ,\quad
[c]
=\frac{[L] }{[t] } ,\quad
[k_B]
=\frac{[M] [L]^2}{[t]^2 [T] } ,\quad
[G]
=\frac{[L]^3 }{[t]^2 [M] } 
$$

自然单位制取 $\hbar=c=k_B=1 $，此时：

$$
[L] = [t] = [M]^{-1} = [T]^{-1}
$$

# 2 广义洛伦兹变换

## R场论的四维时空坐标

R场论定义了两套常用的四维时空坐标。

三维空间坐标 $x,y,z $ 与时间 $t $ 构成第一套四维时空坐标 $x_\mu(\mu=1,2,3,4) $：

$$
x_1=x,\quad x_2=y,\quad x_3=z,\quad x_4=\mathrm{i}ct
$$

第二套四维时空坐标 $x_\mu(\mu=0,1,2,3) $：

$$
x_0=ct,\quad x_1=x,\quad x_2=y,\quad x_3=z
$$

## 线元

线元 $\mathrm{d}s^2 $ 定义为：

$$
\mathrm{d}s^2\equiv -\mathrm{d}x^2-\mathrm{d}y^2-\mathrm{d}z^2+c^2\mathrm{d}t^2
$$

## 广义洛伦兹变换

R场论采用第一套时空坐标

$$
x_1=x,\quad x_2=y,\quad x_3=z,\quad x_4=\mathrm{i}ct
$$

描述广义洛伦兹变换。

### 广义洛伦兹变换的定义

使得线元

$$
\mathrm{d}s^2
\equiv -\mathrm{d}x^2-\mathrm{d}y^2-\mathrm{d}z^2+c^2\mathrm{d}t^2
=-\left(\mathrm{d}x_1 \right)^2-\left(\mathrm{d}x_2 \right)^2-\left(\mathrm{d}x_3 \right)^2-\left(\mathrm{d}x_4 \right)^2
=-\mathrm{d}x_\mu \mathrm{d}x_\mu
$$

保持不变，即

$$
\mathrm{d}s'^2
=\mathrm{d}s^2
$$

的四维时空坐标变换

$$
x_\mu \to x'_\mu = A_{\mu\nu} x_\nu + b_\mu 
$$

称为**广义洛伦兹变换**。

### 广义洛伦兹变换的两条正交关系

$$
\boxed{
A_{\mu\rho} A_{\mu\lambda}=\delta_{\rho\lambda}
}
$$

$$
\boxed{
A_{\mu\lambda}A_{\nu\lambda} = \delta_{\mu\nu}
}
$$

#### 证明第一条正交关系

广义洛伦兹变换最广形式解可设为：

$$
x'_\mu = A_{\mu\nu} x_\nu + b_\mu
$$

两边取微分：

$$
\mathrm{d}x'_\mu=A_{\mu\nu}\mathrm{d}x_\nu
$$

因此若广义洛伦兹变换下 $x_\mu $ 变换为 $x'_\mu $，则 $x' $ 系中的线元 $\mathrm{d}s'^2 $ 也可由 $x $ 系的时空坐标 $x_\mu $ 表达：

$$
\mathrm{d}s'^2
=-\mathrm{d}x'_\mu\mathrm{d}x'_\mu
=-\left(A_{\mu\rho}\mathrm{d}x_\rho \right)\left(A_{\mu\lambda}\mathrm{d}x_\lambda\right)
=-A_{\mu\rho} A_{\mu\lambda}\mathrm{d}x_\rho\mathrm{d}x_\lambda
$$

而 $\mathrm{d}s^2 $ 定义为：

$$
\mathrm{d}s^2
=-\mathrm{d}x_\lambda\mathrm{d}x_\lambda
=-\delta_{\rho\lambda}\mathrm{d}x_\rho\mathrm{d}x_\lambda
$$

由广义洛伦兹变换定义，线元 $\mathrm{d}s^2 $ 在广义洛伦兹变换下保持不变，即：

$$
\mathrm{d}s^2=\mathrm{d}s'^2
$$

对比可得广义洛伦兹变换第一条正交关系：

$$
\boxed{
A_{\mu\rho} A_{\mu\lambda}=\delta_{\rho\lambda}
}
$$

#### 证明第二条正交关系

广义洛伦兹变换

$$
x'_\mu = A_{\mu\nu} x_\nu + b_\mu
$$

是从 $x $ 系到 $x' $ 系的坐标变换规律。

为了推导广义洛伦兹变换第二条正交关系，需要先找到从 $x' $ 到 $x $ 系的坐标变换规律（广义洛伦兹逆变换）。

广义洛伦兹变换：

$$
x'_\mu = A_{\mu\nu} x_\nu + b_\mu
$$

上式两边同乘 $A_{\mu\lambda} $，并利用第一条正交关系 $A_{\mu\lambda} A_{\mu\nu} =\delta_{\lambda\nu} $，有：

$$
\begin{aligned}
A_{\mu\lambda} x'_\mu
&=A_{\mu\lambda}A_{\mu\nu} x_\nu + A_{\mu\lambda}b_\mu
=\delta_{\lambda\nu}x_\nu + A_{\mu\lambda}b_\mu \\
&=x_\lambda + A_{\mu\lambda} b_\mu
\end{aligned}
$$

两边微分：

$$
A_{\mu\lambda}\mathrm{d}x'_\mu
=\mathrm{d}x_\lambda
$$

因此，线元 $\mathrm{d}s^2 $：

$$
\begin{aligned}
\mathrm{d}s^2
&\equiv -\mathrm{d}x_\lambda\mathrm{d}x_\lambda
=-\left(A_{\mu\lambda}\mathrm{d}x'_\mu \right)\left(A_{\nu\lambda}\mathrm{d}x'_\nu \right) \\
&=-A_{\mu\lambda}A_{\nu\lambda}\mathrm{d}x'_\mu\mathrm{d}x'_\nu
\end{aligned}
$$

线元 $\mathrm{d}s'^2 $

$$
\mathrm{d}s'^2
\equiv -\mathrm{d}x'_\mu\mathrm{d}x'_\mu
=-\delta_{\mu\nu}\mathrm{d}x'_\mu\mathrm{d}x'_\nu
$$

由广义洛伦兹变换的定义 $\mathrm{d}s^2=\mathrm{d}s'^2 $，对比可得：

$$
\boxed{
A_{\mu\lambda}A_{\nu\lambda} = \delta_{\mu\nu}
}
$$

### 广义洛伦兹变换的矩阵形式

广义洛伦兹变换是保持线元不变 $\mathrm{d}s^2=\mathrm{d}s'^2$ 的变换 $x_\mu\to x'_\mu=A_{\mu\nu}x_\nu + b_\mu $，保持线元不变等价于两条正交关系 $A_{\mu\nu}A_{\mu\lambda}=\delta_{\nu\lambda},A_{\mu\lambda}A_{\nu\lambda}=\delta_{\mu\nu} $。

令：

$$
X
=\begin{bmatrix}
x_1 \\
x_2 \\
x_3 \\
x_4
\end{bmatrix},\quad
X'
=\begin{bmatrix}
x'_1 \\
x'_2 \\
x'_3 \\
x'_4
\end{bmatrix},\quad
A=[A_{\mu\nu}],\quad
b
=\begin{bmatrix}
b_1 \\
b_2 \\
b_3 \\
b_4
\end{bmatrix}
$$

则广义洛伦兹变换的矩阵形式为：

$$
X'=AX+b
$$

其中矩阵 $A $ 满足 $A^{\mathrm{T}}A=AA^{\mathrm{T}}=I $，或 $A^{-1}=A^{\mathrm{T}} $。

#### 广义洛伦兹变换矩阵 $A $ 的性质

（1）$A^{\mathrm{T}}A=AA^{\mathrm{T}}=I $，或 $A^{-1}=A^{\mathrm{T}} $。

（2）

由于 $\mathrm{det}\left(A^{\mathrm{T}} \right)=\mathrm{det}\left(A \right) $，因此矩阵 $A $ 满足：

$$
\mathrm{det}\left(A \right) = \pm 1
$$

（3）

由于 $A_{\mu\nu}=\partial x'_\mu/\partial x_\nu $，而 $x_\mu=\left(x,y,z,\mathrm{i}ct \right) $，因此 $A_{i4}=\partial x'_i/\partial x_4 = \frac{1 }{\mathrm{i}c } \partial x'_i/\partial t (i=1,2,3) $ 是纯虚数，$A_{44}=\partial t'/\partial t $ 是实数。

利用正交关系 $A_{\mu\nu}A_{\mu\lambda}=\delta_{\nu\lambda} $，可以计算

$$
A_{\mu 4}A_{\mu 4} = \delta_{44}=1
$$

即：

$$
1=A_{\mu 4}A_{\mu 4}
=\sum_{i=1}^{3} A_{i4}^2 + A_{44}^2
=-\sum_{i=1}^{3} \left|A_{i4} \right|^2 + A_{44}^2
$$

即：

$$
A_{44}^2
=1+\sum_{i=1}^{3} \left|A_{i4} \right|^2
\geqslant 1
$$

因此：

$$
A_{44}\geqslant 1\quad \mathrm{or} \quad 
A_{44}\leqslant -1
$$

$A_{44}\geqslant 1 $ 称为**正时条件**，$A_{44}\leqslant -1 $ 称为**负时条件**。

### 几种特殊广义洛伦兹变换

对于广义洛伦兹变换 $X'=AX+b,A^{\mathrm{T}}A=AA^{\mathrm{T}}=I $，可依据 $A $ 的性质对广义洛伦兹变换进行分类。

**固有洛伦兹变换**：$x'_\mu=A_{\mu\nu}x_\nu $，其中 $\mathrm{det}\left(A \right)=1,A_{44}\geqslant 1 $。特别的，把固有洛伦兹变换矩阵记为 $a_{\mu\nu} $。

$$
\mathrm{det}(a) = 1,\quad a_{44} \geqslant 1
$$

**空间反射变换**：$x'_\mu=A_{\mu\nu}x_\nu $，其中 $A_{\mu\nu}=\mathrm{diag}(-1,-1,-1,+1) $。特别地，把空间反射变换矩阵记为 $\sigma_{\mu\nu} $。

$$
\sigma = \mathrm{diag}(-1,-1,-1,+1)
$$

$$
\mathrm{det}(\sigma) = -1,\quad \sigma_{44} = 1 \geqslant 1
$$

**时间反演变换**：$x'_\mu=A_{\mu\nu}x_\nu $，其中 $A_{\mu\nu}=\mathrm{diag}(+1,+1,+1,-1) $。特别地，把时间反演变换矩阵记为 $\tau_{\mu\nu} $。

$$
\tau = \mathrm{diag}(+1,+1,+1,-1)
$$

$$
\mathrm{det}(\tau) = -1,\quad \tau_{44} = -1\leqslant -1
$$

**位移变换**：$x'_\mu = x_\mu + b_\mu $

所有广义洛伦兹变换可看成以上四种变换的组合。

比如**四维时空坐标反射变换**：

$$
\rho=\sigma\tau=\mathrm{diag}(-1,-1,-1,-1)
$$

$$
\mathrm{det}(\rho) = 1,\quad \rho_{44} = -1\leqslant -1
$$

### 广义洛伦兹变换的分类

可以依据广义洛伦兹变换矩阵 $A $ 的性质对广义洛伦兹变换进行分类。

$$
\left\{
\begin{aligned}
&\mathrm{det}(A) = +1
\left\{
\begin{aligned}
&A_{44}\geqslant +1,\quad A = a \\
&A_{44}\leqslant -1,\quad A = \rho,\rho a
\end{aligned}
\right. \\
&\mathrm{det}(A) = -1
\left\{
\begin{aligned}
&A_{44}\geqslant +1,\quad A = \sigma,\sigma a,a\sigma \\
&A_{44}\leqslant -1,\quad A = \tau,\tau a,a\tau
\end{aligned}
\right. \\
\end{aligned}
\right.
$$

### 给几种特殊广义洛伦兹变换命名

**齐次正交变换**：$X'=Ax $

**非齐次洛伦兹变换**：$X'=AX+b $

**固有洛伦兹变换**：$X'=aX $

**不连续分立变换**：$X'=\sigma X,X'=\tau X,X'=\rho X $

# 3 张量、赝张量及其变换规律

## Levi-Civita 符号

### Levi-Civita 符号的定义

$n $ 阶 Levi-Civita 符号 $\varepsilon_{i_1i_2\cdots i_n}(i_j\in\left\{1,\cdots,n \right\},j=1,2,\cdots,n) $ 定义如下：

$$
\varepsilon_{i_1i_2\cdots i_n}
\equiv\left\{
\begin{aligned}
&+1&&,\quad 当 i_1i_2\cdots i_n 进行偶数次相邻两数交换后能还原为 12\cdots n \\
&-1&&,\quad 当 i_1i_2\cdots i_n 进行奇数次相邻两数交换后能还原为 12\cdots n \\
&0&&,\quad 当 i_1,i_2,\cdots i_n 中有任意二指标相等
\end{aligned}
\right.
$$

> 注意，$i_1 $ 与 $i_n $ 不算“相邻”。

$$
\varepsilon_{i_1i_2\cdots i_n}\varepsilon_{i_1i_2\cdots i_n}
=n!
$$

### 两个 Levi-Civita 符号指标缩并规律

#### 一般规律

两个 $n $ 阶 Levi-Civita 符号中 $m(m\leqslant n) $ 个指标缩并的一般规律：

$$
\boxed{
\varepsilon_{\red{k_1\cdots k_m} i_{1\cdots } \cdots i_{n-m}} \varepsilon_{\red{k_1\cdots k_m} j_{1\cdots } \cdots j_{n-m}}
=m! \left(\varepsilon_{l_1 \cdots l_{n-m}} \delta_{i_1 j_{l_1}} \cdots \delta_{i_{n-m} j_{l_{n-m}}} \right)
}
$$

#### 两个 $4 $ 阶 Levi-Civita 符号中 $4 $ 个指标缩并

$$
\begin{aligned}
\varepsilon_{\mu\nu\lambda\rho} \varepsilon_{\mu\nu\lambda\rho}
&=4!
\end{aligned}
$$

#### 两个 $4 $ 阶 Levi-Civita 符号中 $3 $ 个指标缩并

$$
\begin{aligned}
\varepsilon_{\mu\nu\lambda \alpha_1} \varepsilon_{\mu\nu\lambda \beta_1}
&=3!\left(\varepsilon_{\rho_1} \delta_{\alpha_1 \beta_{\rho_1}} \right) \\
&=3! \delta_{\alpha_1 \beta_1}
\end{aligned}
$$

> 注意，$\varepsilon_{\rho_1} $ 是 $1 $ 阶 Levi-Civita 符号，$\rho_1 $ 的爱因斯坦求和只能取 $\rho_1=1 .$

#### 两个 $4 $ 阶 Levi-Civita 符号中 $2 $ 个指标缩并

$$
\begin{aligned}
\varepsilon_{\mu \nu \alpha_1 \alpha_2} \varepsilon_{\mu \nu \beta_1 \beta_2}
&=2!\left(\varepsilon_{\rho_1 \rho_2} \delta_{\alpha_1 \beta_{\rho_1}} \delta_{\alpha_2 \beta_{\rho_2}} \right) \\
&=2!\left(\delta_{\alpha_1 \beta_1} \delta_{\alpha_2 \beta_2} - \delta_{\alpha_1 \beta_2} \delta_{\alpha_2 \beta_1} \right)
\end{aligned}
$$

> 注意，$\varepsilon_{\rho_1 \rho_2} $ 是 $2 $ 阶 Levi-Civita 符号，$\rho_1,\rho_2 $ 的爱因斯坦求和只能取 $\rho_1,\rho_2\in \left\{1,2 \right\} .$

#### 两个 $4 $ 阶 Levi-Civita 符号中 $1 $ 个指标缩并

$$
\begin{aligned}
\varepsilon_{\mu \alpha_1 \alpha_2 \alpha_3} \varepsilon_{\mu \beta_1 \beta_2 \beta_3}
&=1!\left(\varepsilon_{\rho_1 \rho_2 \rho_3} \delta_{\alpha_1 \beta_{\rho_1}} \delta_{\alpha_2 \beta_{\rho_2}} \delta_{\alpha_3 \beta_{\rho_3}} \right) \\
&=\delta_{\alpha_1 \beta_1} \delta_{\alpha_2 \beta_2} \delta_{\alpha_3 \beta_3} - \delta_{\alpha_{1} \beta_{1}} \delta_{\alpha_{2} \beta_{3}} \delta_{\alpha_{3} \beta_{2}} \\
&-\delta_{\alpha_{1} \beta_{2}} \delta_{\alpha_{2} \beta_{1}} \delta_{\alpha_{3} \beta_{3}} + \delta_{\alpha_{1} \beta_{2}} \delta_{\alpha_{2} \beta_{3}} \delta_{\alpha_{3} \beta_{1}} \\
&+\delta_{\alpha_{1} \beta_{3}} \delta_{\alpha_{2} \beta_{1}} \delta_{\alpha_{3} \beta_{2}} - \delta_{\alpha_{1} \beta_{3}} \delta_{\alpha_{2} \beta_{2}} \delta_{\alpha_{3} \beta_{1}}
\end{aligned}
$$

> 注意，$\varepsilon_{\rho_1 \rho_2 \rho_3} $ 是 $3 $ 阶 Levi-Civita 符号，$\rho_1,\rho_2,\rho_3 $ 的爱因斯坦求和只能取 $\rho_1,\rho_2,\rho_3\in \left\{1,2,3 \right\} .$

## 行列式

### 行列式的定义

$$
\boxed{
\begin{aligned}
\mathrm{det}(A)
&\equiv \begin{vmatrix}
A_{11} &\cdots &A_{1n} \\
\vdots &\ddots &\vdots \\
A_{n1} &\cdots &A_{nn}
\end{vmatrix} \\
&=\varepsilon_{j_1j_2\cdots j_n}A_{1j_1}A_{2j_2}\cdots A_{nj_n} \\
&=\frac{1 }{n! } \varepsilon_{i_1i_2\cdots i_n}\varepsilon_{j_1j_2\cdots j_n}A_{i_1j_1}A_{i_2j_2}\cdots A_{i_nj_n}
\end{aligned}
}
$$

### Levi-Civita 符号与行列式相乘

$$
\boxed{
\begin{aligned}
\varepsilon_{i_1i_2\cdots i_n}\mathrm{det}(A)
&=\varepsilon_{i_1i_2\cdots i_n}\varepsilon_{j_1j_2\cdots j_n}A_{1j_1}A_{2j_2}\cdots A_{nj_n} \\
&=\varepsilon_{j_1j_2\cdots j_n}A_{i_1j_1}A_{i_2j_2}\cdots A_{i_nj_n}
\end{aligned}
}
$$

## 场论中常用的张量和赝张量

### SR中张量的定义

在四维闵氏时空中，当时空坐标进行广义洛伦兹变换 $x_\mu\to x'_\mu=A_{\mu\nu} x_\nu + b_\mu $ 时，若 $U_{\mu_1\mu_2\cdots \mu_n} $ 按照如下的规律

$$
\boxed{
U'_{\mu_1\mu_2\cdots \mu_n}
=A_{\mu_1\nu_1}A_{\mu_2\nu_2} \cdots A_{\mu_n\nu_n} U_{\nu_1\nu_2\cdots \nu_n} 
}
$$

进行变换，则 $U_{\mu_1\mu_2\cdots \mu_n} $ 称为（四维时空的）$n $ 阶张量。

### 对称张量

设有一个张量，若将其任意两个指标交换后张量的值不变，则称其为对称张量。

### 反对称张量

设有一个张量，若将其任意两个指标交换后张量的值变为原值的相反数，则称其为反对称张量。

### 标量

零阶张量称为标量。由张量的定义，当时空坐标进行广义洛伦兹变换 $x_\mu\to x'_\mu=A_{\mu\nu} x_\nu + b_\mu $ 时，标量 $\phi(x) $ 服从以下变换规律：

$$
\boxed{
\phi'(x') = \phi(x)
}
$$

即标量是广义洛伦兹变换的不变量。

### 矢量

一阶张量称为矢量。由张量的定义，当时空坐标进行广义洛伦兹变换 $x_\mu\to x'_\mu=A_{\mu\nu} x_\nu + b_\mu $ 时，矢量 $\phi_\mu(x) $ 服从以下变换规律：

$$
\boxed{
\phi'_\mu(x')
=A_{\mu\alpha} \phi_\alpha(x)
}
$$

### 二阶张量

由张量的定义，当时空坐标进行广义洛伦兹变换 $x_\mu\to x'_\mu=A_{\mu\nu} x_\nu + b_\mu $ 时，二阶张量 $\phi_{\mu\nu}(x) $ 服从以下变换规律：

$$
\boxed{
\phi'_{\mu\nu}(x')
=A_{\mu\alpha} A_{\nu\beta} \phi_{\alpha\beta}(x)
}
$$

### 三阶张量

由张量的定义，当时空坐标进行广义洛伦兹变换 $x_\mu\to x'_\mu=A_{\mu\nu} x_\nu + b_\mu $ 时，三阶张量 $\phi_{\mu\nu\lambda}(x) $ 服从以下变换规律：

$$
\boxed{
\phi'_{\mu\nu\lambda}(x')
=A_{\mu\alpha} A_{\nu\beta} A_{\lambda\gamma} \phi_{\alpha\beta\gamma}(x)
}
$$

### 赝标量

#### 赝标量的两种定义

设 $\phi_{\mu\nu\lambda\rho}(x) $ 是一个四阶全反对称张量，则

$$
\boxed{
\tilde{\phi}\equiv \phi_{1234}(x) 
}
$$

称为**赝标量**。

利用赝标量，四阶全反对称张量可表示为：

$$
\phi_{\mu\nu\lambda\rho}(x)
=\varepsilon_{\mu\nu\lambda\rho}\tilde{\phi}(x)
$$

可见四阶全反对称张量 $\phi_{\mu\nu\lambda\rho} $ 的取值只有 $\tilde{\phi},0,-\tilde{\phi} $ 三种可能。上式两边同乘 $\varepsilon_{\mu\nu\lambda\rho} $，并利用

$$
\varepsilon_{\mu\nu\lambda\rho} \varepsilon_{\mu\nu\lambda\rho}
=4!
$$

则赝标量也可定义为：

$$
\boxed{
\tilde{\phi}(x)
=\frac{1 }{4! } \varepsilon_{\mu\nu\lambda\rho} \phi_{\mu\nu\lambda\rho}(x)
}
$$

#### 赝标量的变换规律

利用公式

$$
\begin{aligned}
\varepsilon_{i_1i_2\cdots i_n}\mathrm{det}(A)
&=\varepsilon_{j_1j_2\cdots j_n}A_{i_1j_1}A_{i_2j_2}\cdots A_{i_nj_n} \\
&=\varepsilon_{j_1j_2\cdots j_n}A_{j_1i_1}A_{j_2i_2}\cdots A_{j_ni_n}
\end{aligned}
$$

当时空坐标进行广义洛伦兹变换 $x_\mu\to x'_\mu=A_{\mu\nu} x_\nu + b_\mu $ 时，赝标量变换规律为：

$$
\begin{aligned}
\tilde{\phi}'(x')
&=\frac{1 }{4! } \varepsilon_{\mu\nu\lambda\rho}\phi'_{\mu\nu\lambda\rho}(x') \\
&=\frac{1 }{4! } \varepsilon_{\mu\nu\lambda\rho} A_{\mu\alpha} A_{\nu\beta} A_{\lambda\gamma} A_{\rho\delta} \phi_{\alpha\beta\gamma\delta}(x) \\
&=\frac{1 }{4! } \varepsilon_{\alpha\beta\gamma\delta}\left|A \right| \phi_{\alpha\beta\gamma\delta}(x) \\
&=\left|A \right| \left[\frac{1 }{4! } \varepsilon_{\alpha\beta\gamma\delta} \phi_{\alpha\beta\gamma\delta}(x) \right] \\
&=\left|A \right|\tilde{\phi}(x)
\end{aligned}
$$

$$
\boxed{
x'_\mu = A_{\mu\nu} x_\nu + b_\mu,\quad
\tilde{\phi}'(x')
=\left|A \right|\tilde{\phi}(x)
}
$$

### 赝矢量

#### 赝矢量的定义

在四维闵氏时空，设 $\phi_{\mu\nu\lambda}(x) $ 为一个三阶全反对称张量，则赝矢量定义为：

$$
\boxed{
\tilde{\phi}_\mu(x)
\equiv \frac{1 }{3! } \varepsilon_{\mu\nu\lambda\rho}\phi_{\nu\lambda\rho}(x)
}
$$

#### 赝矢量的变换规律

利用洛伦兹变换矩阵的正交关系

$$
A_{\mu\tau} A_{\eta\tau}
=\delta_{\mu \eta}
$$

以及公式

$$
\begin{aligned}
\varepsilon_{i_1i_2\cdots i_n}\mathrm{det}(A)
&=\varepsilon_{j_1j_2\cdots j_n}A_{i_1j_1}A_{i_2j_2}\cdots A_{i_nj_n} \\
&=\varepsilon_{j_1j_2\cdots j_n}A_{j_1i_1}A_{j_2i_2}\cdots A_{j_ni_n}
\end{aligned}
$$

可知，当时空坐标进行广义洛伦兹变换 $x_\mu\to x'_\mu=A_{\mu\nu} x_\nu + b_\mu $ 时，赝矢量的变换规律为：

$$
\begin{aligned}
\tilde{\phi}'_\mu(x')
&=\frac{1 }{3! } \varepsilon_{\mu\nu\lambda\rho}\phi'_{\nu\lambda\rho}(x') \\
&=\frac{1 }{3! } \varepsilon_{\red{\mu}\nu\lambda\rho} A_{\nu\alpha} A_{\lambda\beta} A_{\rho\gamma} \phi_{\alpha\beta\gamma}(x) \\
&=\frac{1 }{3! } \delta_{\mu\eta} \varepsilon_{\eta\nu\lambda\rho} A_{\nu\alpha} A_{\lambda\beta} A_{\rho\gamma} \phi_{\alpha\beta\gamma}(x) \\
&=\frac{1 }{3! } A_{\mu\tau} A_{\eta\tau} \varepsilon_{\eta\nu\lambda\rho} A_{\nu\alpha} A_{\lambda\beta} A_{\rho\gamma} \phi_{\alpha\beta\gamma}(x) \\
&=\frac{1 }{3! } A_{\mu\tau} \left(\varepsilon_{\eta\nu\lambda\rho} A_{\eta\tau} A_{\nu\alpha} A_{\lambda\beta} A_{\rho\gamma} \right) \phi_{\alpha\beta\gamma}(x) \\
&=\frac{1 }{3! } A_{\mu\tau} \varepsilon_{\tau\alpha\beta\gamma} \left|A \right| \phi_{\alpha\beta\gamma}(x) \\
&=\left|A \right| A_{\mu\tau} \frac{1 }{3! } \varepsilon_{\tau\alpha\beta\gamma} \phi_{\alpha\beta\gamma}(x) \\
&=\left|A \right|A_{\mu\tau}\tilde{\phi}_\tau(x)
\end{aligned}
$$

$$
\boxed{
x'_\mu=A_{\mu\nu} x_\nu + b_\mu,\quad 
\tilde{\phi}'_\mu(x')
=\left|A \right| A_{\mu\tau} \tilde{\phi}_\tau(x)
}
$$

### 二阶赝张量

#### 二阶赝张量的定义

设 $\phi_{\mu\nu} $ 为一个二阶全反对称张量，则赝张量 $\tilde{\phi}_{\mu\nu} $ 的的定义为：

$$
\tilde{\phi}_{\mu\nu}(x)
\equiv \frac{1 }{2! } \varepsilon_{\mu\nu\lambda\rho}\phi_{\lambda\rho}(x)
$$

#### 二阶赝张量的变换规律

利用洛伦兹变换矩阵正交关系

$$
\delta_{\mu\eta}
=A_{\mu\sigma} A_{\eta\sigma},\quad
\delta_{\nu\theta}
=A_{\nu\tau} A_{\theta\tau}
$$

以及公式

$$
\begin{aligned}
\varepsilon_{i_1i_2\cdots i_n}\mathrm{det}(A)
&=\varepsilon_{j_1j_2\cdots j_n}A_{i_1j_1}A_{i_2j_2}\cdots A_{i_nj_n} \\
&=\varepsilon_{j_1j_2\cdots j_n}A_{j_1i_1}A_{j_2i_2}\cdots A_{j_ni_n}
\end{aligned}
$$

可知，当时空坐标进行广义洛伦兹变换 $x_\mu\to x'_\mu=A_{\mu\nu} x_\nu + b_\mu $ 时，二阶赝张量的变换规律为：

$$
\begin{aligned}
\tilde{\phi}'_{\mu\nu}(x')
&=\frac{1 }{2! } \varepsilon_{\mu\nu\lambda\rho}\phi'_{\lambda\rho}(x') \\
&=\frac{1 }{2! } \varepsilon_{\mu\nu\lambda\rho} A_{\lambda\alpha}A_{\rho\beta}\phi_{\alpha\beta}(x) \\
&=\frac{1 }{2! } \delta_{\mu\eta} \delta_{\nu\theta} \varepsilon_{\eta\theta\lambda\rho} A_{\lambda\alpha}A_{\rho\beta}\phi_{\alpha\beta}(x) \\
&=\frac{1 }{2! } A_{\mu\sigma} A_{\eta\sigma} A_{\nu\tau} A_{\theta\tau} \varepsilon_{\eta\theta\lambda\rho} A_{\lambda\alpha}A_{\rho\beta}\phi_{\alpha\beta}(x) \\
&=\frac{1 }{2! } \left(A_{\eta\sigma} A_{\theta\tau} A_{\lambda\alpha} A_{\rho\beta} \varepsilon_{\eta\theta\lambda\rho} \right) A_{\mu\sigma} A_{\nu\tau} \phi_{\alpha\beta}(x) \\
&=\frac{1 }{2! } \left|A \right|\varepsilon_{\sigma\tau\alpha\beta} A_{\mu\sigma} A_{\nu\tau} \phi_{\alpha\beta}(x) \\
&=\left|A \right|A_{\mu\sigma} A_{\nu\tau}\left[\frac{1 }{2! } \varepsilon_{\sigma\tau\alpha\beta} \phi_{\alpha\beta}(x) \right] \\
&=\left|A \right|A_{\mu\sigma} A_{\nu\tau}\tilde{\phi}_{\sigma\tau}(x)
\end{aligned}
$$

$$
\boxed{
x'_\mu = A_{\mu\nu} x_\nu + b_\mu,\quad
\tilde{\phi}'_{\mu\nu}(x')
=\left|A \right|A_{\mu\sigma} A_{\nu\tau}\tilde{\phi}_{\sigma\tau}(x)
}
$$

# 4 场方程

## 达朗贝尔算符

达朗贝尔算符 $\square $ 定义为：

$$
\square
\equiv \partial_\mu \partial_\mu
=\partial_x^2 + \partial_y^2 + \partial_z^2 - \frac{1 }{c^2 } \partial_t^2
=\nabla^2 - \frac{1 }{c^2 } \partial_t^2
$$

## 实标量场方程

$$
\left(\square - m_0^2 \right)\phi(x)
=0
$$

## 复标量场方程

$$
\left(\square - m_0^2 \right)\phi(x)
=0
$$

$$
\left(\square - m_0^2 \right)\phi^*(x)
=0
$$

## 矢量场方程

$$
\square A_\mu = -\mu_0 j_\mu
$$

## 旋量场方程

$$
\left(\gamma_\mu \partial_\mu + m_0 \right)\psi(x)
=0
$$

$$
\partial_\mu \bar{\psi} \gamma_\mu - m_0 \bar{\psi}
=0
$$

# 5 Clifford 代数、$\gamma $ 矩阵、旋量表示、旋量与 Dirac 方程

## Clifford 代数与 $\gamma $ 矩阵

### R场论中的 Clifford 代数

R场论中，Clifford 代数是 $n $ 维复向量空间生成的结合代数。

设 $V $ 是 $n $ 维复向量空间，则由 $V $ 生成的结合代数就是 Clifford 代数，记为 $C_n(V) .$

$V $ 中向量的几何乘积具有以下性质：

$$
a(bc)
=(ab)c
$$

$$
a(b+c)
=ab+ac
$$

$$
(a+b)c
=ac+bc
$$

$$
\alpha(ab)
=(\alpha a)b
=a(\alpha b),\quad \alpha\in \mathbb{F}
$$

定义内积：

$$
a\cdot b
\equiv \frac{1 }{2 } (ab+ba)
$$

定义外积：

$$
a \wedge b
\equiv \frac{1 }{2 } (ab-ba)
$$

### 由 $V $ 的正交归一基生成 $C_n(V) $ 的基

设 $\left\{e_1,e_2,\cdots,e_n \right\} $ 是 $V $ 的一组正交归一基，即它们的内积满足正交归一性：

$$
e_\mu \cdot e_\nu
=\delta_{\mu\nu} \bold{1}
$$

其中，$\bold{1} $ 是乘法单位元。

根据内积的定义，上式等价于：

$$
e_\mu e_\nu + e_\nu e_\mu 
=2\delta_{\mu\nu} \bold{1}
$$

特别地，当 $\mu\ne \nu $ 时，有：

$$
e_\mu e_\nu = -e_\nu e_\mu,\quad \mu\ne \nu
$$

基于 $n $ 维复向量空间 $V $ 的一组基 $\left\{e_\mu \right\} $ 可构造 Clifford 代数 $C_n(V) $ 的一组基二阶反对称张量基 $\left\{e_\mu e_\nu,\mu\ne \nu \right\} .$

类似，$\left\{e_{\mu_1} e_{\mu_2} \cdots e_{\mu_m},\mu_1\ne \mu_2 \ne \cdots \ne \mu_m \right\} $ 也是 $C_n(V) $ 的一组基，直到最高反对称基 $e_1 e_2 \cdots e_n .$

可以证明：

$$
e_{\mu_1} \wedge e_{\mu_2}
=e_{\mu_1} e_{\mu_2}
$$

$$
e_{\mu_1} \wedge e_{\mu_2} \wedge \cdots \wedge e_{\mu_r}
=e_{\mu_1} e_{\mu_2} \cdots e_{\mu_r}
$$

### r-矢量

$$
A_r
\equiv a_1 \wedge a_2 \wedge \cdots \wedge a_r,\quad
a_1,a_2,\cdots,a_r \in V
$$

若 $a\in V $，则

$$
a\wedge A_r
=\frac{1 }{2 } \left[a A_r + (-1)^r A_r a \right]
$$

$$
a\cdot A_r
=\frac{1 }{2 } \left[a A_r - (-1)^r A_r a \right]
$$

### $C_n(V) $ 中元素的一般形式

$C_n(V) $ 中的元素 $A\in C_n(V) $ 一般可写为：

$$
A
=a + a_\mu e_\mu + \frac{1 }{2! } a_{\mu_1\mu_2} e_{\mu_1} \wedge e_{\mu_2} + \cdots + \frac{1 }{n! } a_{\mu_1\mu_2\cdots \mu_n} e_{\mu_1} \wedge e_{\mu_2} \wedge \cdots \wedge e_{\mu_n}
$$

### Clifford 代数的代数表示

$$
\Gamma : C_n(V) \to \mathrm{End}(W),\quad
\mathrm{dim}~V = n,\quad
\mathrm{dim}~W = d
$$

其中 $W $ 为复向量空间，$\mathrm{End}(W) $ 为 $W $ 上所有线性变换（可看作矩阵）的全体，满足：

$$
\Gamma(a + b)
=\Gamma(a) + \Gamma(b)
$$

$$
\Gamma(ab)
=\Gamma(a) \Gamma(b)
$$

$$
\Gamma(\alpha a)
=\alpha \Gamma(a)
$$

$$
\Gamma(\bold{1})
=I
$$

> 可见“代数表示”比“群线性表示”多了一个“保持加法”的性质。

可以证明，Clifford 代数 $C_n(V) $ 的矢量基 $\left\{e_1,e_2,\cdots,e_n \right\} $ 可以有 $d\times d $ 矩阵表示 $\left(d=2^{\left[\frac{n }{2 }  \right]} \right) .$

#### $\gamma $ 矩阵作为 Clifford 代数矢量基的代数表示

把 Clifford 代数 $C_n(V) $ 中的矢量基 $\left\{e_\mu,\mu=1,2,\cdots,n \right\} $ 的某个代数表示 $\Gamma(e_\mu) $ 定义为 $\gamma_\mu $ 矩阵，即：

$$
\gamma_\mu
\equiv \Gamma(e_\mu),\quad \mu=1,2,\cdots,n
$$

由于

$$
e_\mu e_\nu + e_\nu e_\mu 
=2\delta_{\mu\nu} \bold{1}
$$

则：

$$
\Gamma(e_\mu) \Gamma(e_\nu) + \Gamma(e_\nu) \Gamma(e_\mu) = 2\delta_{\mu\nu} \Gamma(\bold{1})
$$

$$
\boxed{
\gamma_\mu \gamma_\nu + \gamma_\nu \gamma_\mu
=2\delta_{\mu\nu} I
}
$$

特别地，当 $\mu=\nu $ 时，有

$$
\boxed{
\gamma_\mu^2
=I
}
$$

当 $\mu \ne \nu $ 时，有

$$
\boxed{
\mu \ne \nu,\quad
\gamma_\mu \gamma_\nu
=-\gamma_\nu \gamma_\mu
}
$$

注意到

$$
\gamma_\mu^\dag \gamma_\nu^\dag + \gamma_\nu^\dag \gamma_\mu^\dag
=2\delta_{\mu\nu} I
$$

因此可人为约定 $\gamma $ 矩阵还满足

$$
\boxed{
\gamma_\mu^\dag
=\gamma_\mu
}
$$

结合

$$
\gamma_\mu^2
=I
$$

可得

$$
\boxed{
\gamma_\mu^\dag
=\gamma_\mu^{-1} 
=\gamma_\mu
}
$$

### $\gamma $ 矩阵的性质

$$
\gamma_\mu \gamma_\nu + \gamma_\nu \gamma_\mu
=2\delta_{\mu\nu}
$$

特别地

$$
\gamma_\mu \gamma_\nu
=-\gamma_\nu \gamma_\mu,\quad \mu\ne \nu
$$

$$
\gamma_\mu^2 = I
$$


### R 场论中的 $\gamma $ 矩阵

可以证明，Clifford 代数 $C_n(V) $ 的矢量基 $\left\{e_1,e_2,\cdots,e_n \right\} $ 可以有 $d\times d $ 矩阵表示 $\left(d=2^{\left[\frac{n }{2 }  \right]} \right) .$ 这些表示矩阵称为 $\gamma $ 矩阵，满足正交关系：

$$
\gamma_\mu\gamma_\nu + \gamma_\nu\gamma_\mu = 2\delta_{\mu\nu} I
$$

R场论中，时空坐标共 $4 $ 个，因此考虑 $C_4(V) .$

$C_4(V) $ 的四个代数矢量基 $\left\{e_1,e_2,e_3,e_4 \right\} $ 有 $4\times 4$ 矩阵表示 $\left\{\gamma_1,\gamma_2,\gamma_3,\gamma_4 \right\} $，满足：

$$
\boxed{
\gamma_\mu\gamma_\nu + \gamma_\nu\gamma_\mu = 2\delta_{\mu\nu} I,\quad \mu,\nu\in \left\{1,2,3,4 \right\}
}
$$

并且仍然人为约定

$$
\boxed{
\gamma_\mu^\dag
=\gamma_\mu
}
$$

### R场论中 $\gamma $ 矩阵的性质

$\gamma $ 矩阵的定义：

$$
\boxed{
\gamma_\mu \gamma_\nu + \gamma_\nu \gamma_\mu
=2\delta_{\mu\nu} I
}
$$

上式的两个直接推论：

$$
\boxed{
\gamma_\mu^2 = I
}
$$

$$
\boxed{
\gamma_\mu \gamma_\nu
=-\gamma_\nu \gamma_\mu,\quad \mu\ne \nu
}
$$

人为约定：

$$
\boxed{
\gamma_\mu^\dag
=\gamma_\mu^{-1} 
=\gamma_\mu
}
$$

### $\gamma_5 $ 矩阵

$\gamma_5 $ 矩阵定义如下：

$$
\boxed{
\gamma_5
\equiv \gamma_1 \gamma_2 \gamma_3 \gamma_4
}
$$

$\gamma_5 $ 矩阵也可写为：

$$
\boxed{
\gamma_5
=\frac{1 }{4! } \varepsilon_{\mu\nu\lambda\rho}  \gamma_\mu \gamma_\nu \gamma_\lambda \gamma_\rho
}
$$



$$
\boxed{
\gamma_5 \gamma_\mu + \gamma_\mu \gamma_5 = 0,\quad \mu=1,2,3,4
}
$$

$$
\boxed{
\gamma_5^2 = I
}
$$

$$
\boxed{
\gamma_5 \gamma_\mu \gamma_5^{-1}
=-\gamma_\mu
}
$$

$$
\boxed{
\gamma_5 \gamma_\mu \gamma_\nu \gamma_5^{-1}
=\gamma_\mu \gamma_\nu
}
$$

$$
\boxed{
\gamma_5 \gamma_{\mu_1}\cdots\gamma_{\mu_n} \gamma_5^{-1}
=(-1)^n \gamma_{\mu_1} \cdots \gamma_{\mu_n}
}
$$

$$
\boxed{
\mathrm{Tr}\left(\gamma_{\mu_1} \cdots \gamma_{\mu_n} \right)
=(-1)^n \mathrm{Tr}\left(\gamma_{\mu_1} \cdots \gamma_{\mu_n} \right)
}
$$

奇数个 $\gamma_\mu $ 矩阵的迹为零。

$$
\boxed{
\mathrm{Tr}(\gamma_\mu)=0,\quad \mathrm{Tr}(\gamma_5)=0
}
$$

偶数个 $\gamma_\mu $ 矩阵的迹：

$$
\boxed{
\mathrm{Tr}\left(\gamma_{\mu_1} \cdots \gamma_{\mu_n} \right)
=4 \sum_p \delta_p \delta_{\nu_1\nu_2} \delta_{\nu_3\nu_4} \cdots \delta_{\nu_{n-1}\nu_n}
}
$$

$$
\delta_p
\equiv \left\{
\begin{aligned}
+1 , \mu_1 \cdots \mu_n 经过偶次置换变为 \nu_1 \cdots \nu_n \\
-1 , \mu_1 \cdots \mu_n 经过偶次置换变为 \nu_1 \cdots \nu_n
\end{aligned}
\right.
$$

其中，求和对 $\nu_1,\nu_2,\cdots,\nu_n $ 所有可能的取值求和（并非取全排列，共有 $(n-1)!! $ 项），具体解释如下：

用 $(\mu) $ 表示 $(\mu_1,\mu_2,\cdots,\mu_n) $ 有序数对，用 $(\mu)\backslash \mu_i $ 表示有序数对中去掉 $\mu_i $ 变量，即 $(\mu)\backslash \mu_i=(\mu_1,\cdots ,\mu_{i-1},\mu_{i+1},\cdots,\mu_n) $

用 $\nu_i\in (\mu) $ 表示变量 $\nu_i $ 取有序数对 $(\mu) $ 中的某一个变量。

用 $\nu_i = (\mu)_\mathrm{first} $ 表示变量 $\nu_i $ 取有序数对 $(\mu) $ 中的第一个变量。

$\nu_1=(\mu)_\mathrm{first}=\mu_1 $

$\nu_2\in (\mu)\backslash \nu_1 = (\mu)\backslash\mu_1 $ 

$\nu_3=\left((\mu)\backslash\nu_1,\nu_2 \right)_\mathrm{first}  $

$\nu_4\in (\mu)\backslash\nu_1,\nu_2,\nu_3 $

以此类推，最后 $(\nu_1,\nu_2,\cdots,\nu_n) $ 是 $\mu_1,\mu_2,\cdots,\mu_n $ 的一个排列，设 $m $ 为把 $(\nu_1,\nu_2,\cdots,\nu_n) $ 还原为排列 $(\mu_1,\mu_2,\cdots,\mu_n) $ 所需的置换次数，则 $\delta_p=(-1)^m .$

$$
\boxed{
\mathrm{Tr}\left(\gamma_\mu\gamma_\nu \right)
=4\delta_{\mu\nu}
}
$$

$$
\boxed{
\mathrm{Tr}\left(\gamma_\mu\gamma_\nu\gamma_\lambda\gamma_\rho \right)
=4\left(\delta_{\mu\nu}\delta_{\lambda\rho} - \delta_{\mu\lambda}\delta_{\rho\nu} + \delta_{\mu\rho}\delta_{\nu\lambda} \right)
}
$$

## Lorentz 群的旋量表示

设 $\gamma_\mu $ 矩阵可进行广义齐次 Lorentz 变换：

$$
\gamma_\mu'
=A_{\mu\nu} \gamma_\nu
$$

可以计算得到：

$$
\gamma_\mu' \gamma_\nu' + \gamma_\nu' \gamma_\mu'
=2\delta_{\mu\nu} I
$$

即 $\gamma_\mu' $ 也可作为 $\gamma $ 矩阵。

可以证明，$\gamma_\mu' $ 与 $\gamma_\mu $ 相似，即存在相似变换矩阵 $\Lambda $ 使得：

$$
\Lambda^{-1} \gamma_\mu \Lambda
=A_{\mu\nu} \gamma_\nu
$$

R场论中还进一步规定

$$
\left|\Lambda \right|
=1
$$

$\Lambda $ 决定于 $A $，但多个 $\Lambda $ 与 一个 $A $ 对应。

- $\Lambda $ 与 $A $ 都构成群，两个群准同构；

- $A $ 为广义齐次 Lorentz 变换的变换矩阵；

- $\Lambda $ 为广义齐次 Lorentz 变换群的线性不可约表示，$\Lambda(A) $ 称为 Lorentz 群的旋量表示。

## $\mathrm{SO}(n) $ 群的生成元

### $\mathrm{SO}(n) $ 群的定义

$$
\mathrm{SO}(n)
\equiv \left\{A \in \mathrm{GL}(n,\R) | A^\mathrm{T} A = I,\mathrm{det}(A)=1 \right\}
$$

### 生成元的定义

设 Lie 群的群元 $D(\alpha) $ 由一组参数 $\left\{\alpha_i \right\} $ 描述，且参数取 $\alpha=0 $ 对应群恒元。与参数 $\alpha_i $ 对应的生成元 $I_i $ 定义为：

$$
I_i
\equiv \frac{\partial D(\alpha) }{\partial \alpha_i } \bigg|_{\alpha=0}
$$

### $\mathrm{SO}(n) $ 群的生成元

设 $A\in \mathrm{SO}(n) $ 非常接近单位矩阵，则其可写为：

$$
A
=I + \alpha
$$

由

$$
A^\mathrm{T} A
=I
$$

可知：

$$
\alpha^\mathrm{T}
=-\alpha
$$

即 $\alpha $ 的矩阵元满足：

$$
\alpha_{ab}
=-\alpha_{ba}
$$

选取 $\alpha $ 的矩阵元 $\alpha_{ab} $ 作为 $\mathrm{SO}(n) $ 群的参数。

生成元：

$$
I_{ab}
\equiv \frac{\partial A(\alpha) }{\partial \alpha_{ab} } \bigg|_{\alpha=0}
=\frac{\partial \alpha }{\partial \alpha_{ab} } \bigg|_{\alpha=0}
$$

生成元的矩阵元：

$$
\left(I_{ab} \right)_{cd}
=\frac{\partial \alpha_{cd} }{\partial \alpha_{ab} } \bigg|_{\alpha=0}
=\delta_{ac}\delta_{bd} - \delta_{ad}\delta_{bc}
$$


一方面，在恒元附近可将 $A $ 展开：

$$
A(\alpha)
=I + \frac{1 }{2 }  \frac{\partial A(\alpha) }{\partial \alpha_{ab} } \bigg|_{\alpha=0} \alpha_{ab}
\equiv I + \frac{1 }{2 } I_{ab} \alpha_{ab}
$$

另一方面，我们假设

$$
A(\alpha)
=I + \alpha
$$

### $\mathrm{SO}(n) $ 群李代数

$$
\left(I_{ab} \right)_{cd}
=\delta_{ac}\delta_{bd} - \delta_{ad}\delta_{bc}
$$

$$
I_{\mu\nu}
=-I_{\nu\mu}
$$

$$
\begin{aligned}
\left[I_{\mu\nu} , I_{\alpha\beta} \right]_{ab}
&=\left(I_{\mu\nu} \right)_{ac} \left(I_{\alpha\beta} \right)_{cb} - \left(I_{\alpha\beta} \right)_{ac} \left(I_{\mu\nu} \right)_{cb} \\
&=\left(\delta_{\mu a}\red{\delta_{\nu c}} - \blue{\delta_{\mu c}}\delta_{\nu a} \right) \left(\green{\delta_{\alpha c}}\delta_{\beta b} - \delta_{\alpha b}\purple{\delta_{\beta c}} \right) - \left(\delta_{\alpha a}\purple{\delta_{\beta c}} - \green{\delta_{\alpha c}}\delta_{\beta a} \right)\left(\blue{\delta_{\mu c}}\delta_{\nu b} - \delta_{\mu b}\red{\delta_{\nu c}} \right) \\
&=\red{\delta_{\nu c}}\green{\delta_{\alpha c}}\left(\delta_{\mu a}\delta_{\beta b} - \delta_{\beta a}\delta_{\mu b} \right) + \red{\delta_{\nu c}}\purple{\delta_{\beta c}}\left(-\delta_{\mu a}\delta_{\alpha b} + \delta_{\alpha a}\delta_{\mu b} \right) + \blue{\delta_{\mu c}}\green{\delta_{\alpha c}}\left(-\delta_{\nu a}\delta_{\beta b} + \delta_{\beta a}\delta_{\nu b} \right) + \blue{\delta_{\mu c}}\purple{\delta_{\beta c}}\left(\delta_{\nu a}\delta_{\alpha b} - \delta_{\alpha a}\delta_{\nu b} \right) \\
&=\red{\delta_{\nu c}}\green{\delta_{\alpha c}}\left(I_{\mu\beta} \right)_{ab} + \red{\delta_{\nu c}}\purple{\delta_{\beta c}}\left(I_{\alpha\mu} \right)_{ab} + \blue{\delta_{\mu c}}\green{\delta_{\alpha c}}\left(I_{\beta\nu} \right)_{ab} + \blue{\delta_{\mu c}}\purple{\delta_{\beta c}}\left(I_{\nu \alpha} \right)_{ab} \\
&=\delta_{\nu\alpha} \left(I_{\mu\beta} \right)_{ab} + \delta_{\nu\beta} \left(I_{\alpha\mu} \right)_{ab} + \delta_{\mu\alpha} \left(I_{\beta\nu} \right)_{ab} + \delta_{\mu\beta} \left(I_{\nu \alpha} \right)_{ab} \\
&=\delta_{\nu\alpha} \left(I_{\mu\beta} \right)_{ab} + \delta_{\nu\beta} \left(-I_{\mu\alpha} \right)_{ab} + \delta_{\mu\alpha} \left(-I_{\nu\beta} \right)_{ab} + \delta_{\mu\beta} \left(I_{\nu \alpha} \right)_{ab} \\
&=\left(\delta_{\nu\alpha} I_{\mu\beta} + \delta_{\mu\beta}I_{\nu\alpha} - \delta_{\mu\alpha} I_{\nu\beta} - \delta_{\nu\beta} I_{\mu\alpha} \right)_{ab}
\end{aligned}
$$

$$
\left[I_{\mu\nu} , I_{\alpha\beta} \right]
=\left(\delta_{\nu\alpha} I_{\mu\beta} + \delta_{\mu\beta}I_{\nu\alpha} - \delta_{\mu\alpha} I_{\nu\beta} - \delta_{\nu\beta} I_{\mu\alpha} \right)
$$

### Lorentz 群旋量表示的生成元

考虑固有 Lorentz 变换

$$
x'_\mu
=a_{\mu\nu} x_\nu
$$

把 $a_{\mu\nu} $ 作如下分解：

$$
a_{\mu\nu}
=\delta_{\mu\nu} + \alpha_{\mu\nu},\quad
$$

则固有 Lorentz 变换可写为：

$$
x'_\mu
=a_{\mu\nu} x_\nu
=\left(\delta_{\mu\nu} + \alpha_{\mu\nu} \right) x_\nu
=x_\mu + \alpha_{\mu\nu} x_\nu
$$

在R场论中，固有 Lorentz 变换矩阵群 $\left\{a \right\} $ 的旋量表示 $\Lambda $ 记为 $S $，即：

$$
S^{-1} \gamma_\mu S
=a_{\mu\nu} \gamma_\nu
$$

现在把 $a_{\mu\nu} $ 分解了，此时的 $S $ 依赖于参数 $\alpha_{\mu\nu} $，即：

$$
S
=S(\alpha)
$$

$$
S^{-1}(\alpha) \gamma_\mu S(\alpha)
=(\delta_{\mu\nu} + \alpha_{\mu\nu}) \gamma_\nu
=\gamma_\mu + \alpha_{\mu\nu} \gamma_\nu
$$

考虑无穷小固有 Lorentz 变换，即 $x'_\mu $ 与 $x_\mu $ 差别很小的固有 Lorentz 变换，这对应于参数 $\alpha_{\mu\nu}\to 0 .$

由正交关系

$$
a_{\mu \tau} a_{\nu \tau}
=\delta_{\mu\nu}
$$

可得

$$
\left(\delta_{\mu\tau} + \alpha_{\mu\tau} \right)\left(\delta_{\nu\tau} + \alpha_{\nu\tau} \right)
=\delta_{\mu\nu}
$$

由于 $\alpha_{\mu\nu}\to 0 $，因此可忽略二阶小量 $\alpha_{\mu\tau}\alpha_{\nu\tau} $，上式化为

$$
\alpha_{\mu\nu}
=-\alpha_{\nu\mu},\quad \alpha_{\mu\nu} \to 0
$$

当 $\alpha\to 0 $ 时，$S(\alpha) $ 可展为

$$
\begin{aligned}
S(\alpha)
&=S(0) + \frac{1 }{2 } \frac{\partial S(\alpha) }{\partial \alpha_{\mu\nu} } \bigg|_{\alpha=0} \alpha_{\mu\nu} \\
&=I + \frac{1 }{2 } I_{\mu\nu} \alpha_{\mu\nu},\quad \alpha\to 0
\end{aligned}
$$

群论告诉我们

$$
S^{-1}(\alpha)
=I - \frac{1 }{2 } I_{\mu\nu} \alpha_{\mu\nu},\quad \alpha\to 0
$$

把上面两式代入 $S^{-1}(\alpha) \gamma_\mu S(\alpha)=\gamma_\mu + \alpha_{\mu\nu} \gamma_\nu $，忽略二阶小量可得：

$$

$$

> 实际上在无穷小变换情况下，只有 $6 $ 个独立的非零群参数 $\left\{\alpha_{12},\alpha_{13},\alpha_{13},\alpha_{23},\alpha_{24},\alpha_{34} \right\} $，但由于采用爱因斯坦求和，$\mu,\nu $ 都要取遍 $1,2,3,4 $，而 $\displaystyle{\frac{\partial S(\alpha) }{\partial \alpha_{12} } \bigg|_{\alpha=0} \alpha_{12 } = \frac{\partial S(\alpha) }{\partial \alpha_{21} } \bigg|_{\alpha=0} \alpha_{21 } }$，因此即使是一阶项前面也要有 $1/2 $ 因子来去掉求和带来的重复。

$$
\left[\gamma_\mu , I_{\alpha\beta} \right]
=\delta_{\mu\alpha}\gamma_\beta - \delta_{\mu\beta}\gamma_\alpha
$$

设

$$
I_{\alpha\beta}
=k \left(\gamma_\alpha\gamma_\beta - \gamma_\beta\gamma_\alpha \right)
$$

可以解得

$$
k=\frac{1 }{4 }  
$$

$$
I_{\alpha\beta}
=\frac{1 }{4 } \left(\gamma_\alpha\gamma_\beta - \gamma_\beta\gamma_\alpha \right)
$$

利用公式

$$
\left[\gamma_\mu , I_{\alpha\beta} \right]
=\delta_{\mu\alpha}\gamma_\beta - \delta_{\mu\beta}\gamma_\alpha
$$

可以求得生成元对易关系：

$$
\begin{aligned}
\left[I_{\mu\nu} , I_{\alpha\beta} \right]
&=\frac{1 }{4 } \left[\gamma_\mu\gamma_\nu - \gamma_\nu\gamma_\mu , I_{\alpha\beta} \right] \\
&=\frac{1 }{4 } \left(\gamma_\mu \left[\gamma_\nu , I_{\alpha\beta} \right] + \left[\gamma_\mu , I_{\alpha\beta} \right] \gamma_\nu \right) - \frac{1 }{4 } \left(\gamma_\nu \left[\gamma_\mu , I_{\alpha\beta} \right] + \left[\gamma_\nu , I_{\alpha\beta} \right] \gamma_\mu \right) \\
&=\frac{1 }{4 } \left(\gamma_\mu \left(\delta_{\nu\alpha} \gamma_\beta - \delta_{\nu\beta} \gamma_\alpha \right) + \left(\delta_{\mu\alpha} \gamma_\beta - \delta_{\mu\beta} \gamma_\alpha \right) \gamma_\nu \right) - \frac{1 }{4 } \left(\gamma_\nu \left(\delta_{\mu\alpha} \gamma_\beta - \delta_{\mu\beta} \gamma_\alpha \right) + \left(\delta_{\nu\alpha} \gamma_\beta - \delta_{\nu\beta} \gamma_\alpha \right) \gamma_\mu \right) \\
&=\frac{1 }{4 } \delta_{\nu\alpha} \left(\gamma_\mu\gamma_\beta - \gamma_\beta\gamma_\mu \right) + \frac{1 }{4 } \delta_{\nu\beta}\left(\gamma_\alpha\gamma_\mu - \gamma_\mu\gamma_\alpha \right) + \frac{1 }{4 } \delta_{\mu\alpha} \left(\gamma_\beta\gamma_\nu - \gamma_\nu\gamma_\beta \right) + \frac{1 }{4 } \delta_{\mu\beta} \left(\gamma_\nu\gamma_\alpha - \gamma_\alpha\gamma_\nu \right) \\
&=\delta_{\nu\alpha} I_{\mu\beta} + \delta_{\nu\beta} I_{\alpha\mu} + \delta_{\mu\alpha} I_{\beta\nu} + \delta_{\mu\beta} I_{\nu\alpha} \\
&=-\delta_{\mu\alpha} I_{\nu\beta} + \delta_{\mu\beta} I_{\nu\alpha} + \delta_{\nu\alpha} I_{\mu\beta} - \delta_{\nu\beta} I_{\mu\alpha}
\end{aligned}
$$

### $\Lambda $ 与 $\gamma_5 $ 的关系

已经知道

$$
\Lambda^{-1} \gamma_\mu \Lambda
=A_{\mu\nu} \gamma_\nu
$$

可作为 $\Lambda $ 的定义。现在想知道 $\Lambda^{-1} \gamma_5 \Lambda .$ 

$$
\begin{aligned}
\Lambda^{-1}\gamma_5\Lambda
&=\Lambda^{-1}\left(\frac{1 }{4! } \varepsilon_{\mu\nu\lambda\rho}\gamma_\mu\gamma_\nu\gamma_\lambda\gamma_\rho \right)\Lambda \\
&=\frac{1 }{4! } \varepsilon_{\mu\nu\lambda\rho} \left(\Lambda^{-1}\gamma_\mu\Lambda \right)\left(\Lambda^{-1}\gamma_\nu\Lambda \right)\left(\Lambda^{-1}\gamma_\lambda\Lambda \right)\left(\Lambda^{-1}\gamma_\rho\Lambda \right) \\
&=\frac{1 }{4! } \varepsilon_{\mu\nu\lambda\rho} \left(A_{\mu\alpha}\gamma_\alpha \right) \left(A_{\mu\beta}\gamma_\beta \right)\left(A_{\mu\sigma}\gamma_\sigma \right)\left(A_{\mu\tau}\gamma_\tau\right) \\
&=\frac{1 }{4! } \varepsilon_{\alpha\beta\sigma\tau}\left|A \right|\gamma_\alpha\gamma_\beta\gamma_\sigma\gamma_\tau \\
&=\left|A \right|\gamma_5
\end{aligned}
$$

### 几种特殊的旋量表示 $S,P,T $

广义 Lorentz 变换矩阵 $A $ 的旋量表示 $\Lambda(A) $ 依赖于广义 Lorentz 变换矩阵 $A $，而 $A $ 可按行列式 $\mathrm{det}(A) $ 和 $A_{44} $ 划分成四个分支。

#### $S $ 矩阵

固有 Lorentz 变换矩阵的旋量表示记为 $S $，即：

$$
S
\equiv \Lambda(a),\quad
S=S(a)
$$

$$
S^{-1} \gamma_\mu S
=a_{\mu\nu} \gamma_\nu
$$

#### $P $ 矩阵

空间反射变换矩阵 $\sigma $ 的旋量表示记为 $P $，即：

$$
P
\equiv \Lambda(\sigma),\quad
P
=P(\sigma)
$$

$$
P^{-1} \gamma_\mu P
=\sigma_{\mu\nu} \gamma_{\nu}
$$

特别地

$$
P^{-1} \gamma_i P
=\sigma_{i\nu} \gamma_\nu
=-\gamma_i
$$

$$
\boxed{
\gamma_i P
=-P \gamma_i
=0
}
$$

以及

$$
P^{-1} \gamma_4 P
=\sigma_{4\nu} \gamma_{\nu}
=\gamma_4
$$

$$
\boxed{
\gamma_4 P
=P \gamma_4
}
$$

可以猜到

$$
P
=\eta_P \gamma_4
$$

若人为要求

$$
\left|P \right|
=1
$$

则

$$
\boxed{
P
=\eta_P \gamma_4,\quad \left|\eta_P \right|=1
}
$$

#### $T $ 矩阵

拉卡型时间反演变换矩阵 $\tau $ 的旋量表示记为 $T $ 即：

$$
T
\equiv \Lambda(\tau),\quad T=T(\tau)
$$

由旋量表示地定义，有

$$
T^{-1} \gamma_\mu T 
=\tau_{\mu\nu} \gamma_\nu
$$

特别地

$$
T^{-1} \gamma_i T 
=\tau_{i\nu} \gamma_\nu
=\gamma_i,\quad i=1,2,3
$$

$$
T^{-1} \gamma_4 T 
=\tau_{4\nu} \gamma_\nu
=-\gamma_4
$$

即

$$
\gamma_i T
=T\gamma_i
$$

$$
\gamma_4 T
=-\gamma_4 T
$$

可以猜到

$$
T
=\eta_T \gamma_1 \gamma_2 \gamma_3
$$

若人为要求

$$
\left|T \right|=1
$$

则

$$
\boxed{
T
=\eta_T \gamma_1 \gamma_2 \gamma_3,\quad
\left|\eta_T \right|
=1
}
$$

#### $ $

### $\Lambda^\dag $ 的表达式

$A_{ij},A_{44} $ 为实数，$A_{i4},A_{4i} $ 为虚数。

$$
A_{ij}^*=A_{ij},\quad A_{44}^*=A_{44}
$$

$$
A_{i4}^*=-A_{i4},\quad A_{4i}^*=-A_{4i}
$$

$\gamma_\mu $ 矩阵满足

$$
\gamma_\mu^\dag
=\gamma_\mu^{-1}
=\gamma_\mu
$$

$\Lambda $ 矩阵的定义：

$$
\Lambda^{-1} \gamma_\mu \Lambda
=A_{\mu\nu} \gamma_\nu
$$

取厄米共轭得

$$
\Lambda^\dag \gamma_\mu \left(\Lambda^{-1} \right)^\dag
=A_{\mu\nu}^* \gamma_\nu
$$

特别地，对于前三个 $\gamma_i $ 矩阵和 $\gamma_4 $ 矩阵要分开讨论：

$$
\left\{
\begin{aligned}
&\Lambda^\dag \gamma_i \left(\Lambda^{-1} \right)^\dag
=A_{i\nu}^* \gamma_\nu
=A_{ij}^* \gamma_j + A_{i4}^*\gamma_4
=A_{ij} \gamma_j - A_{i4} \gamma_4 \\
&\Lambda^\dag \gamma_4 \left(\Lambda^{-1} \right)^\dag
=A_{4\nu}^* \gamma_\nu
=A_{4j}^* \gamma_j + A_{44}^*\gamma_4
=-A_{4j} \gamma_j + A_{44} \gamma_4
\end{aligned}
\right.
$$

上面两式左、右各乘 $\gamma_4 $：

$$
\begin{aligned}
\gamma_4 \Lambda^\dag \gamma_i \left(\Lambda^{-1} \right)^\dag \gamma_4
&=\gamma_4 \left(A_{ij} \gamma_j - A_{i4} \gamma_4 \right) \gamma_4 \\
&=A_{ij} \gamma_4 \gamma_{j} \gamma_4 - A_{i4} \gamma_4 \gamma_4 \gamma_4 \\
&=-A_{ij} \gamma_j \gamma_4^2 - A_{i4} \gamma_4 \\
&=-A_{ij} \gamma_j - A_{i4} \gamma_4 \\
&=-A_{i\nu} \gamma_\nu \\
&=-\Lambda^{-1} \gamma_i \Lambda
\end{aligned}
$$

$$
\begin{aligned}
\gamma_4 \Lambda^\dag \gamma_4 \left(\Lambda^{-1} \right)^\dag \gamma_4
&=\gamma_4 \left(-A_{4j} \gamma_j + A_{44} \gamma_4 \right) \gamma_4 \\
&=A_{4j} \gamma_j + A_{44} \gamma_4 \\
&=A_{4\nu} \gamma_\nu \\
&=\Lambda^{-1} \gamma_4 \Lambda
\end{aligned}
$$

对上面两式左乘 $\Lambda $，右乘 $\gamma_4 \Lambda^\dag$：

$$
\Lambda\left(\gamma_4 \Lambda^\dag \gamma_i \left(\Lambda^{-1} \right)^\dag \gamma_4 \right) \gamma_4 \Lambda^\dag
=\Lambda \left(-\Lambda^{-1} \gamma_i \Lambda \right) \gamma_4 \Lambda^\dag
$$

$$
\Lambda \left(\gamma_4 \Lambda^\dag \gamma_4 \left(\Lambda^{-1} \right)^\dag \gamma_4 \right) \gamma_4 \Lambda^\dag
=\Lambda \left(\Lambda^{-1} \gamma_4 \Lambda \right) \gamma_4 \Lambda^\dag
$$

即：

$$
\Lambda \gamma_4 \Lambda^\dag \gamma_i
=-\gamma_i \Lambda \gamma_4 \Lambda^\dag
$$

$$
\Lambda \gamma_4 \Lambda^\dag \gamma_4
=\gamma_4 \Lambda \gamma_4 \Lambda^\dag
$$

加上括号看得更清楚一点：

$$
\left(\Lambda \gamma_4 \Lambda^\dag \right) \gamma_i
=-\gamma_i \left(\Lambda \gamma_4 \Lambda^\dag \right)
$$

$$
\left(\Lambda \gamma_4 \Lambda^\dag \right) \gamma_4
=\gamma_4 \left(\Lambda \gamma_4 \Lambda^\dag \right)
$$

$\left(\Lambda \gamma_4 \Lambda^\dag \right) $ 是一个与 $\gamma_i $ 反对易、与 $\gamma_4 $ 对易的矩阵，可以猜到

$$
\Lambda \gamma_4 \Lambda^\dag
=k \gamma_4
$$

上式左乘 $\gamma_4 \Lambda^{-1} $ 就解出 $\Lambda^\dag $：

$$
\boxed{
\Lambda^\dag
=k \gamma_4 \Lambda^{-1} \gamma_4
}
$$

由于 $\Lambda $ 依赖于 Lorentz 变换矩阵 $A $，因此不同的 $A $ 可能给出不同的 $k .$

- 考虑 $A=a $，即固有 Lorentz 群，此时 $\Lambda(A)=\Lambda(a)=S $ 为固有 Lorentz 群的旋量表示，其中包含了恒元。把恒元代入上式

$$
I^\dag
=k \gamma_4 I^{-1} \gamma_4
$$

解得

$$
k=1
$$

- 考虑 $A=\sigma $，此时 $\Lambda(A)=\Lambda(\sigma)=P $，而 $P=\eta_P \gamma_4,\left|\eta_P \right|=1 $，代入得

$$
\eta_P^* \gamma_4^\dag
=k \gamma_4 \eta_P^{-1} \gamma_4^{-1} \gamma_4
$$

解得

$$
k
=\eta_P^* \eta_P
=\left|\eta_P \right|^2
=1
$$

- 考虑 $A=\tau $，此时 $\Lambda(A)=\Lambda(\tau)=T $，而 $T=\eta_T \gamma_1\gamma_2\gamma_3,\left|\eta_T \right|=1 $，代入得

$$
\eta_T^*\left(\gamma_1\gamma_2\gamma_3 \right)^\dag
=k \eta_T^{-1} \gamma_4 \left( \gamma_1\gamma_2\gamma_3 \right)^{-1} \gamma_4
$$

解得

$$
k
=-\left|\eta_T \right|^2
=-1
$$

综上有

$$
\boxed{
\Lambda^\dag
=\left\{
\begin{aligned}
&\gamma_4 \Lambda^{-1} \gamma_4 &&,\Lambda = S,P \\
&-\gamma_4 \Lambda^{-1} \gamma_4 &&,\Lambda = T
\end{aligned}
\right.
}
$$

## 旋量

### 旋量的定义

设 $\psi(x) $ 为四元单列矩阵函数

$$
\psi(x)
=\begin{bmatrix}
\psi_1(x) \\
\psi_2(x) \\
\psi_3(x) \\
\psi_4(x) \\
\end{bmatrix}
$$

当时空坐标进行广义洛伦兹变换 $x'_\mu=A_{\mu\nu} x_\nu + b_\mu $ 时，若 $\psi(x) $ 按照规律

$$
\psi'(x')
=\Lambda \psi(x)
$$

变换，则称 $\psi(x) $ 为四元旋量，简称旋量。其中，$\Lambda=\Lambda(A) $ 是广义 Lorentz 变换矩阵 $A $ 的旋量表示。

### 共轭旋量

定义旋量 $\psi(x) $ 的共轭旋量 $\bar{\psi}(x) $：

$$
\bar{\psi}(x)
\equiv \psi^\dag(x) \gamma_4
$$

由旋量的变换规律

$$
\psi'(x')
=\Lambda \psi(x)
$$

以及 $\Lambda^\dag $ 的表达式

$$
\Lambda^\dag
=k \gamma_4 \Lambda^{-1} \gamma_4
$$

$$
\Lambda^\dag
=\left\{
\begin{aligned}
&\gamma_4 \Lambda^{-1} \gamma_4 &&,\Lambda = S,P \\
&-\gamma_4 \Lambda^{-1} \gamma_4 &&,\Lambda = T
\end{aligned}
\right.
$$

可知，$\bar{\psi}(x) $ 的变换规律为：

$$
\begin{aligned}
\bar{\psi}'(x')
&=\psi'^\dag(x')\gamma_4 \\
&=\left[\Lambda \psi(x) \right]^\dag \gamma_4 \\
&=\psi^\dag (x) \Lambda^\dag \gamma_4 \\
&=\psi^\dag (x) \left(k \gamma_4 \Lambda^{-1} \gamma_4 \right) \gamma_4 \\
&=k \psi^\dag(x) \gamma_4 \Lambda^{-1} \\
&=k \bar{\psi}(x) \Lambda^{-1}
\end{aligned}
$$

$$
\boxed{
\bar{\psi}'(x')
=k\bar{\psi}(x)\Lambda^{-1},\quad
k=\begin{cases}
+1&,\Lambda=S,P \\
-1&,\Lambda=T
\end{cases}
}
$$

### 由 $\bar{\psi} $ 和 $\psi $ 组成的张量或赝张量

先回顾一下 $\psi(x) $ 和 $\bar{\psi}(x)\equiv \psi^\dag(x)\gamma_4 $ 的变换规律：

$$
\boxed{
\psi'(x')
=\Lambda \psi(x)
}
$$

$$
\boxed{
\bar{\psi}'(x')
=k\bar{\psi}(x)\Lambda^{-1},\quad
k=\begin{cases}
+1&,\Lambda=S,P \\
-1&,\Lambda=T
\end{cases}
}
$$

#### $\bar{\psi}(x) \psi(x) $作为标量或赝标量

$$
\begin{aligned}
\bar{\psi}'(x') \psi'(x')
&=\left(k \bar{\psi}(x) \Lambda^{-1} \right) \left(\Lambda \psi(x) \right) \\
&=k \bar{\psi}(x) \psi(x)
\end{aligned}
$$

对于 $S,P $ 变换，$k=+1 $，$\bar{\psi}(x) \psi(x) $ 是标量；

对于 $T $ 变换，$k=-1 $，$\bar{\psi}(x) \psi(x) $ 是赝标量。

#### $\bar{\psi}(x) \gamma_5 \psi(x) $

利用 $\Lambda $ 与 $\gamma_5 $ 的关系

$$
\Lambda^{-1} \gamma_5 \Lambda
=\left|A \right|\gamma_5
$$

可得

$$
\begin{aligned}
\bar{\psi}'(x') \gamma_5 \psi'(x')
&=\left(k \bar{\psi}(x) \Lambda^{-1} \right) \gamma_5 \left(\Lambda \psi(x) \right) \\
&=k \left|A \right| \bar{\psi}(x) \gamma_5 \psi(x)
\end{aligned}
$$

对于 $S,P $ 变换，$k=+1 $，$\bar{\psi}(x) \gamma_5 \psi(x) $ 是赝标量。

#### $\bar{\psi}(x) \gamma_\mu \psi(x) $ 的变换规律

利用 $\Lambda $ 的定义

$$
\Lambda^{-1} \gamma_\mu \Lambda
=A_{\mu\nu} \gamma_\nu
$$

可得

$$
\begin{aligned}
\bar{\psi}'(x') \gamma_\mu \psi'(x')
&=\left(k \bar{\psi}(x) \Lambda^{-1} \right) \gamma_\mu \left(\Lambda \psi(x) \right) \\
&=k A_{\mu\nu} \bar{\psi}(x) \gamma_\nu \psi(x)
\end{aligned}
$$

对于 $S,P $ 变换，$k=+1 $，$\bar{\psi}(x) \gamma_\mu \psi(x) $ 是矢量。

#### $\bar{\psi}(x) \gamma_\mu \gamma_5 \psi(x) $ 的变换规律

利用 $\Lambda $ 的定义以及 $\Lambda $ 与 $\gamma_5 $ 的关系

$$
\Lambda^{-1} \gamma_\mu \Lambda
=A_{\mu\nu} \gamma_\nu,\quad
\Lambda^{-1} \gamma_5 \Lambda
=\left|A \right|\gamma_5
$$

可得

$$
\begin{aligned}
\bar{\psi}'(x') \gamma_\mu \gamma_5 \psi'(x')
&=\left(k \bar{\psi}(x) \Lambda^{-1} \right) \gamma_\mu \gamma_5 \left(\Lambda \psi(x) \right) \\
&=k \bar{\psi}(x) \Lambda^{-1} \gamma_\mu \Lambda \Lambda^{-1} \gamma_5 \Lambda \psi(x) \\
&=k \left|A \right| A_{\mu\nu} \bar{\psi}(x) \gamma_\nu \gamma_5 \psi(x)
\end{aligned}
$$

对于 $S,P $ 变换，$k=+1 $，$\bar{\psi}(x) \gamma_\mu \gamma_5 \psi(x) $ 是赝矢量。

#### $\bar{\psi}(x)\gamma_{\alpha_1}\gamma_{\alpha_2}\cdots\gamma_{\alpha_n}\psi(x) $ 的变换规律

当四维时空坐标进行广义洛伦兹变换时，

$$
U_{\alpha_1\alpha_2\cdot \cdots\alpha_n}
=\bar{\psi}\gamma_{\alpha_1}\gamma_{\alpha_2}\cdots\gamma_{\alpha_n}\psi 
$$

的变换规律为：

$$
\begin{aligned}
U'_{\alpha_1\alpha_2\cdot \cdots\alpha_n}(x')
&=\bar{\psi}'(x')\gamma_{\alpha_1}\gamma_{\alpha_2}\cdots\gamma_{\alpha_n}\psi'(x') \\
&=k\bar{\psi}(x) \Lambda^{-1} \gamma_{\alpha_1}\gamma_{\alpha_2}\cdots\gamma_{\alpha_n} \Lambda \psi(x) \\
&=k\bar{\psi}(x) \left(\Lambda^{-1} \gamma_{\alpha_1} \Lambda \right) \left(\Lambda^{-1} \gamma_{\alpha_2} \Lambda \right) \cdots \left(\Lambda^{-1} \gamma_{\alpha_n} \Lambda \right) \psi(x) \\
&=k A_{\alpha_1\beta_1} A_{\alpha_2\beta_2} \cdots A_{\alpha_n\beta_n} \bar{\psi}(x) \gamma_{\beta_1}\gamma_{\beta_2}\cdots\gamma_{\beta_n} \psi(x) \\
&=k A_{\alpha_1\beta_1} A_{\alpha_2\beta_2} \cdots A_{\alpha_n\beta_n} U_{\beta_1\beta_2\cdots\beta_n}(x)
\end{aligned}
$$

#### $n $ 阶赝张量 $\bar{\psi}(x)\gamma_{\alpha_1}\gamma_{\alpha_2}\cdots\gamma_{\alpha_n}\gamma_5\psi(x) $

#### 标量 $\bar{\psi}(x) \gamma_\mu\partial_\mu \psi(x) $

## Dirac 方程（旋量场方程）

### Dirac 方程（旋量场方程）的导出

一方面，假设自由旋量粒子哈密顿量可写为：

$$
H = \vec{\alpha}\cdot\hat{\vec{p}} + \beta m_0
$$

旋量场 $\psi $ 满足薛定谔方程：

$$
\mathrm{i}\partial_t \psi
=H \psi
=\left(\vec{\alpha}\cdot\hat{\vec{p}} + \beta m_0 \right)\psi
$$

$\mathrm{i}\partial_t $ 两次作用于 $\psi $：

$$
\begin{aligned}
-\partial_t^2 \psi(x)
&=H^2 \psi(x) \\
&=\left(\vec{\alpha}\cdot\hat{\vec{p}} + \beta m_0 \right)^2\psi(x) \\
&=\left[\frac{1 }{2 } \left(\alpha_i\alpha_j + \alpha_j\alpha_i \right)\hat{p}_i\hat{p}_j + \left(\alpha_i\beta+\beta\alpha_i \right)\hat{p}_im_0 + \beta^2m_0^2 \right]\psi(x)
\end{aligned}
$$

另一方面，假设旋量场 $\psi(x) $ 要满足标量场方程（即旋量的四个分量都要满足标量场方程）：

$$
\left(\square-m_0^2 \right)\psi(x) = 0 \Longrightarrow
-\partial_t^2 \psi(x)
=\left(-\nabla^2+m_0^2 \right)\psi(x)
=\left(\hat{\vec{p}}^2+m_0^2 \right)\psi(x)
=\left(\hat{p}_i \hat{p}_i + m_0^2 \right)\psi(x)
$$

对比

$$
\left\{
\begin{aligned}
&-\partial_t^2 \psi(x)
=\left[\frac{1 }{2 } \left(\alpha_i\alpha_j + \alpha_j\alpha_i \right)\hat{p}_i\hat{p}_j + \left(\alpha_i\beta+\beta\alpha_i \right)\hat{p}_im_0 + \beta^2m_0^2 \right]\psi(x) \\
&-\partial_t^2 \psi(x)
=\left(\hat{p}_i \hat{p}_i + m_0^2 \right)\psi(x)
\end{aligned}
\right.
$$

可得：

$$
\left\{
\begin{aligned}
&\alpha_i\alpha_j + \alpha_j\alpha_i = 2\delta_{ij} I,\quad i,j=1,2,3 \\
&\alpha_i\beta + \beta\alpha_i = 0 \\
&\beta^2 = I
\end{aligned}
\right.
$$

定义：

$$
\boxed{
\gamma_i\equiv -\mathrm{i}\beta \alpha_i,\quad i=1,2,3
}
$$

$$
\boxed{
\gamma_4\equiv \beta
}
$$

或者反过来

$$
\boxed{
\alpha_i = \mathrm{i} \gamma_4 \gamma_i
}
$$

$$
\boxed{
\beta
=\gamma_4
}
$$

则上面的定义结合 $\alpha_i,\beta $ 矩阵的性质可得：

$$
\gamma_\mu\gamma_\nu + \gamma_\nu\gamma_\mu = 2\delta_{\mu\nu} I
$$

$$
\gamma_\mu^\dag = \gamma_\mu
$$

即这样用 $\alpha_i,\beta $ 矩阵定义的 $\gamma $ 矩阵恰好符合 Clifford 代数中 $\gamma $ 矩阵的定义。

定义 Clifford 代数中的梯度算符：

$$
\hat{\partial}
\equiv \gamma_\mu\partial_\mu
$$

利用二阶偏微分可交换的性质，有：

$$
\begin{aligned}
\hat{\partial}^2
&=\gamma_\mu\partial_\mu \gamma_\nu\partial_\nu \\
&=\frac{1 }{2 } \left(\gamma_\mu \gamma_\nu \partial_\mu \partial_\nu + \gamma_\mu \gamma_\nu \partial_\mu \partial_\nu \right) \\
&=\frac{1 }{2 } \left(\gamma_\mu \gamma_\nu \partial_\mu \partial_\nu + \gamma_\mu \gamma_\nu \partial_\nu \partial_\mu \right) \\
交换第二项\mu,\nu指标&=\frac{1 }{2 } \left(\gamma_\mu \gamma_\nu \partial_\mu \partial_\nu + \gamma_\nu \gamma_\mu \partial_\mu \partial_\nu \right) \\
&=\delta_{\mu\nu} I \partial_\mu \partial_\nu \\
&=I \partial_\mu \partial_\mu \\
&\equiv I \square
\end{aligned}
$$

因此，旋量场满足的标量场方程

$$
\left(\square-m_0^2 \right)\psi(x) = 0
\Longleftrightarrow \left(I \square-m_0^2 \right)\psi(x) = 0
$$

可以写为：

$$
\left(\hat{\partial}^2 - m_0^2 \right)\psi(x)
=0
$$

因式分解：

$$
\left(\hat{\partial}-m_0 \right)\left(\hat{\partial}+m_0 \right)\psi(x) = 0
$$

Dirac 认为

$$
\left(\hat{\partial}+m_0 \right)\psi(x)
\equiv \left(\gamma_\mu\partial_\mu + m_0 \right)\psi(x)
=0
$$

是旋量场方程。

$$
\boxed{
\left(\gamma_\mu\partial_\mu + m_0 \right)\psi(x)
=0
}
$$

### Dirac 方程的共轭方程

考虑 Dirac 方程

$$
\left(\gamma_\mu\partial_\mu + m_0 \right)\psi(x)
=0
$$

其可写为

$$
\gamma_i\partial_i\psi(x) + \gamma_4\partial_4\psi(x) + m_0\psi(x)
=0
$$

两边取厄米共轭，考虑到 $x_4=\mathrm{i}t,\left(\partial_4\psi(x) \right)^\dag = -\partial_4\psi^\dag(x) $ 且 $\gamma_\mu $ 是厄米矩阵满足 $\gamma_\mu^\dag=\gamma_\mu $，则有：

$$
\partial_i\psi^\dag(x) \gamma_i - \partial_4 \psi^\dag(x)\gamma_4 + m_0\psi^\dag(x)
=0
$$

上式右乘 $\gamma_4 $，并利用 $\gamma_4 $ 与 $\gamma_i $ 的反对易关系 $\gamma_4\gamma_i + \gamma_i\gamma_4 = 0 $ 得：

$$
-\partial_i\psi^\dag(x) \gamma_4\gamma_i - \partial_4 \psi^\dag(x)\gamma_4\gamma_4 + m_0\psi^\dag(x)\gamma_4
=0
$$

再利用 $\bar{\psi}(x)=\psi^\dag(x)\gamma_4 $ 得：

$$
-\partial_i\bar{\psi}(x)\gamma_i - \partial_4 \bar{\psi}(x)\gamma_4 + m_0\bar{\psi}(x)
=0
$$

即 Dirac 方程的共轭方程：

$$
\boxed{
\partial_\mu\bar{\psi}\gamma_\mu - m_0\bar{\psi}
=0
}
$$

### Dirac 方程的协变性

Dirac 方程的协变性就是说，当时空坐标进行广义 Lorentz 变换时，Dirac 方程在变换前后的参考系内具有相同的形式。

考虑时空坐标进行广义 Lorentz 变换，即 $x'_\mu = A_{\mu\nu} x_\nu + b_\mu .$

$x' $ 系的 Dirac 方程为：

$$
\gamma_\rho\partial_\rho'\psi'(x') + m\psi'(x')
=0
$$

把 $x' $ 系的物理量用 $x $ 系的物理量表达：

$$
\partial_\rho'
\equiv \frac{\partial }{\partial x'_\rho } 
=\frac{\partial x_\nu}{\partial x'_\rho } \frac{\partial }{\partial x_\nu } 
=A_{\rho\nu}\partial_\nu
$$

$$
\psi'(x')
=\Lambda\psi(x)
$$

因此 $x' $ 系的 Dirac 方程可写为：

$$
\begin{aligned}
0
&=\gamma_\rho\partial_\rho'\psi'(x') + m\psi'(x') \\
&=\gamma_\rho A_{\rho\nu}\partial_\nu \Lambda \psi(x) + m\Lambda \psi(x) \\
\end{aligned}
$$

上式左乘 $\Lambda^{-1} $（注意 $\Lambda $ 依赖于 $A $，但不依赖于时空坐标），并利用 $\Lambda^{-1} \gamma_\rho \Lambda = A_{\rho\alpha} \gamma_\alpha $ 和正交关系 $A_{\rho\alpha}A_{\rho\nu}=\delta_{\alpha\nu} $：

$$
\begin{aligned}
0
&=\Lambda^{-1}\gamma_\rho A_{\rho\nu}\partial_\nu\Lambda \psi(x) + \Lambda^{-1}m\Lambda\psi(x) \\
&=\Lambda^{-1}\gamma_\rho \Lambda A_{\rho\nu}\partial_\nu \psi(x) + m \psi(x) \\
&=A_{\rho\alpha}\gamma_\alpha A_{\rho\nu} \partial_\nu\psi(x) + m\psi(x) \\
&=\delta_{\alpha\nu}\gamma_\alpha \partial_\nu\psi(x) + m\psi(x) \\
&=\gamma_\nu \partial_\nu \psi(x) + m\psi(x) \\
\end{aligned}
$$

可见当波函数 $\psi(x) $ 是一个旋量，服从旋量变换规律时，$x $ 系和 $x' $ 系的 Dirac 方程形式上一致。

### Dirac 共轭方程的协变性

Dirac 共轭方程的协变性就是说，当时空坐标进行**固有 Lorentz 变换**或**空间反射变换**时，Dirac 共轭方程在变换前后的参考系内具有相同的形式。

首先回顾一下共轭旋量的变换规律：

$$
\bar{\psi}'(x')
=k\bar{\psi}(x)\Lambda^{-1},\quad
k=\begin{cases}
+1&,\Lambda=S,P \\
-1&,\Lambda=T
\end{cases}
$$

考虑时空坐标进行固有 Lorentz 变换或空间反射变换，即 $x'_\mu=A_{\mu\nu}x_\nu,A=a,\sigma,\Lambda(a)=S,\Lambda(\sigma)=P $，则此时共轭旋量的变换规律为

$$
\bar{\psi}'(x')
=\bar{\psi}(x) \Lambda^{-1}
$$

$x' $ 系的共轭 Dirac 方程为：

$$
\partial'_\mu \bar{\psi}'(x') \gamma_\mu - m \bar{\psi}'(x')
=0
$$

把 $x' $ 系的物理量用 $x $ 系的物理量表达：

$$
\partial_\rho'
\equiv \frac{\partial }{\partial x'_\rho } 
=\frac{\partial x_\nu}{\partial x'_\rho } \frac{\partial }{\partial x_\nu } 
=A_{\rho\nu}\partial_\nu
$$

因此 $x' $ 系的 Dirac 方程可写为：

$$
\begin{aligned}
0
&=\partial'_\mu \bar{\psi}'(x') \gamma_\mu - m \bar{\psi}'(x') \\
&=A_{\mu\rho}\partial_\rho \bar{\psi}(x) \Lambda^{-1} \gamma_\mu - m \bar{\psi}(x) \Lambda^{-1}
\end{aligned}
$$

上式右乘 $\Lambda $，并利用 $\Lambda^{-1} \gamma_\mu \Lambda = A_{\mu\nu}\gamma_\nu $ 和正交关系 $A_{\mu\rho} A_{\mu\nu}=\delta_{\rho\nu} $ 可得：

$$
\begin{aligned}
0
&=A_{\mu\rho}\partial_\rho \bar{\psi}(x) \Lambda^{-1} \gamma_\mu \Lambda - m \bar{\psi}(x) \Lambda^{-1} \Lambda \\
&=A_{\mu\rho}\partial_\rho \bar{\psi}(x) A_{\mu\nu} \gamma_\nu - m \bar{\psi}(x) \\
&=\delta_{\rho\nu} \partial_\rho \bar{\psi}(x) \gamma_\nu - m\bar{\psi}(x) \\
&=\partial_\nu \bar{\psi}(x) \gamma_\nu - m\bar{\psi}(x)
\end{aligned}
$$

可见当 $\bar{\psi}(x) $ 是一个共轭旋量，服从共轭旋量变换规律时，$x $ 系和 $x' $ 系的 Dirac 共轭方程形式上一致。

### Dirac 方程描写粒子的自旋为 $1/2 $

> 为了方便，下面算符都略去帽子。

轨道角动量算符：

$$
L_i
=\left(\vec{x}\times\vec{p} \right)_i
=\varepsilon_{ijk}x_j p_k
$$

自由旋量粒子哈密顿量算符：

$$
H
=\vec{\alpha}\cdot\vec{p} + \beta m
$$

二者对易关系：

$$
\begin{aligned}
\left[H , L_i \right]
&=\left[\alpha_lp_l+\beta m , \varepsilon_{ijk}x_jp_k \right] \\
&=\varepsilon_{ijk}\alpha_l\left[p_l , x_j p_k \right] \\
&=\varepsilon_{ijk}\alpha_l\left(x_j\left[p_l , p_k \right] + \left[p_l , x_j \right]p_k \right) \\
&=\varepsilon_{ijk}\alpha_l \left(-\mathrm{i}\hbar \delta_{lj} \right) p_k \\
&=-\mathrm{i}\hbar\varepsilon_{ijk}\alpha_j p_k \\
&=-\mathrm{i}\hbar\left(\vec{\alpha}\times\vec{p} \right)_i \\
&=-\mathrm{i}\left(\vec{\alpha}\times\vec{p} \right)_i
\end{aligned}
$$

因此：

$$
\left[H , \vec{L} \right] = -\mathrm{i}\vec{\alpha}\times\vec{p}
$$

这表明，Dirac 方程描述的粒子的轨道角动量不守恒。

定义四阶 $\sigma_i $ 矩阵：

$$
\sigma_i
\equiv \frac{1 }{2\mathrm{i} } \varepsilon_{ijk}\gamma_j\gamma_k
$$

利用

$$
\boxed{
\gamma_i\equiv -\mathrm{i}\beta \alpha_i,\quad i=1,2,3
}
$$

$$
\boxed{
\gamma_4\equiv \beta
}
$$

$$
\boxed{
\alpha_i = \mathrm{i} \gamma_4 \gamma_i
}
$$

$$
\boxed{
\beta
=\gamma_4
}
$$

$$
\gamma_i \gamma_j
=2\delta_{ij} I - \gamma_j \gamma_i
$$

$$
\gamma_4 \gamma_i
=-\gamma_i \gamma_4
$$

$$
\begin{aligned}
\left[\gamma_4 , \gamma_j \gamma_k \right]
&=\gamma_4 \gamma_j \gamma_k - \gamma_j \gamma_k \gamma_4 \\
&=\gamma_4 \gamma_j \gamma_k - \gamma_4 \gamma_j \gamma_k \\
&=0
\end{aligned}
$$

可计算：

$$
\begin{aligned}
\left[H , \frac{\sigma_i }{2 }  \right]
&=\left[\alpha_l p_l + \beta m , \frac{1 }{4\mathrm{i} } \varepsilon_{ijk} \gamma_j \gamma_k \right] \\
&=\frac{1 }{4\mathrm{i} } \varepsilon_{ijk} \left[\mathrm{i} \gamma_4 \gamma_l p_l + \gamma_4 m , \gamma_j \gamma_k \right] \\
&=\frac{1 }{4 } \varepsilon_{ijk} \left[\gamma_4 \gamma_l , \gamma_j \gamma_k \right] p_l \\
&=\frac{1 }{4 } \varepsilon_{ijk}\left(\gamma_4 \gamma_l \gamma_j \gamma_k - \gamma_j \gamma_k \gamma_4 \gamma_l \right) p_l \\
&=\frac{1 }{4 } \varepsilon_{ijk} \left(\gamma_4 \gamma_l \gamma_j \gamma_k - \gamma_4 \gamma_j \gamma_k \gamma_l \right) p_l \\
&=\frac{1 }{4 } \varepsilon_{ijk} \gamma_4 \left(\gamma_l \gamma_j \gamma_k - \gamma_j \gamma_k \gamma_l \right) p_l \\
&=\frac{1 }{4 } \varepsilon_{ijk} \gamma_4 \left(\gamma_l \gamma_j \gamma_k - \gamma_j \left(2\delta_{kl} I - \gamma_l \gamma_k \right) \right) p_l \\
&=\frac{1 }{4 } \varepsilon_{ijk} \gamma_4 \left(\gamma_l \gamma_j \gamma_k + \gamma_j \gamma_l \gamma_k - 2\delta_{kl} \gamma_j \right) p_l \\
&=\frac{1 }{4 } \varepsilon_{ijk} \gamma_4 \left(\gamma_l \gamma_j \gamma_k + \left(2\delta_{jl} I - \gamma_l\gamma_j \right) \gamma_k - 2\delta_{kl} \gamma_j \right) p_l \\
&=\frac{1 }{4 } \varepsilon_{ijk} \gamma_4 \left(2\delta_{jl} \gamma_k - 2\delta_{kl}\gamma_j \right) p_l \\
&=\frac{1 }{2\mathrm{i} } \varepsilon_{ijk}\left(\delta_{jl} \mathrm{i} \gamma_4 \gamma_k - \delta_{kl} \mathrm{i} \gamma_4 \gamma_j\right) p_l \\
&=\frac{1 }{2\mathrm{i} } \varepsilon_{ijk} \left(\delta_{jl} \alpha_k - \delta_{kl} \alpha_j \right) p_l \\
&=\frac{1 }{2\mathrm{i} } \left(\varepsilon_{ilk} \alpha_k - \varepsilon_{ijl} \alpha_j \right) p_l \\
&=\frac{1 }{2\mathrm{i} } \left(\varepsilon_{ilk} \alpha_k + \varepsilon_{ilj} \alpha_j \right) p_l \\
&=\frac{1 }{\mathrm{i} } \varepsilon_{ilk} \alpha_k p_l \\
&=\mathrm{i} \varepsilon_{ikl} \alpha_k p_l \\
&=\mathrm{i}\left(\vec{\alpha}\times\vec{p} \right)_i
\end{aligned}
$$

则：

$$
\begin{aligned}
\left[H , L_i + \frac{\sigma_i }{2 }  \right]
=-\mathrm{i}\left(\vec{\alpha}\times\vec{p} \right)_i + \mathrm{i}\left(\vec{\alpha}\times\vec{p} \right)_i 
=0
\end{aligned}
$$

构造

$$
\vec{J}\equiv \vec{L} + \frac{\vec{\sigma} }{2 } 
$$

则：

$$
\left[H , \vec{J} \right] = 0
$$
这表明，Dirac 方程描述的粒子的总角动量 $\vec{J} $ 守恒。

其中的附加项 $\vec{\sigma}/2 $ 解释为粒子的自旋角动量算符。因此旋量波函数描述的粒子自旋为 $\vec{\sigma}/2 $。这种粒子称为旋量粒子。

### 用 $\sigma_i^0 $ 表达 $\alpha_i,\beta,\gamma_\mu $

### 一些对易关系

$$
\left[\left(\vec{\sigma}\cdot\vec{p} \right) , \left(\vec{\gamma}\cdot\vec{p} \right) \right]
=0
$$

$$
\left[\left(\vec{\sigma}\cdot\vec{p} \right) , \beta
=0 \right]
$$

$$
\left[\hat{H} , \left(\vec{\sigma} \cdot \vec{n} \right) \right]
=0
$$

$$
\left[\hat{H} , \left(\vec{\sigma}\cdot\vec{p} \right) \right]
=0
$$

### 自由旋量粒子的波函数

#### 自旋旋量粒子

若波函数 $\psi(x) $ 满足 Dirac 方程

$$
\left(\gamma_\mu\partial_\mu + m_0 \right)\psi(x)
=0
$$

则由 $\psi(x) $ 描述的粒子称为**自由旋量粒子**。

#### 四维动量算符及其本征方程

四维动量算符 $\hat{p}_\mu $ 定义为：

$$
\hat{p}_\mu
\equiv -\mathrm{i}\partial_\mu
$$

写成 $3+1 $ 形式即：

$$
\hat{p}_\mu
=\left(\hat{\vec{p}} , -\partial_t \right)
=\left(-\mathrm{i}\nabla , -\partial_t \right),\quad
\hat{p}_4 = -\partial_t
$$

考虑四维动量算符的本征方程：

$$
\hat{p}_\mu \psi(x)
\equiv -\mathrm{i}\partial_\mu \psi(x)
=p_\mu\psi(x)
$$

其中，$p_\mu $ 代表本征值，$\psi(x) $ 是本征波函数。容易猜到，上式中波函数 $\psi $ 有平面波解：

$$
\psi_p(x)
=u(p)\mathrm{e}^{\mathrm{i}p x},\quad \forall p_\mu
$$

$$
p x
\equiv p_\mu x_\mu
=\vec{p}\cdot\vec{x} + p_4 x_4
=\vec{p}\cdot\vec{x} + \left(\mathrm{i}p_0 \right) \left(\mathrm{i}t \right)
=\vec{p}\cdot\vec{x} - p_0 t,\quad
$$

很容易验证上面构造的平面波解 $\psi_p(x)=u(p)\mathrm{e}^{\mathrm{i}p x} = u(p) \mathrm{e}^{\mathrm{i}\left(\vec{p}\cdot\vec{x} - p_4 x_4 \right)} $ 是四维动量算符的本征波函数，对应本征值恰为构造平面波解用到的四个连续参数 $\left(\vec{p} , p_4 \right) .$

#### 具有确定四维动量自由旋量粒子动量表象 Dirac 方程

具有确定四维动量自由旋量粒子，其波函数 $\psi(x) $ 应既是四维动量算符本征波函数，又要满足 Dirac 方程。

$\psi(x) $ 首先要满足 $\hat{p}_\mu $ 的本征方程：

$$
\hat{p}_\mu \psi(x)
\equiv -\mathrm{i}\partial_\mu \psi(x)
=p_\mu\psi(x)
$$

上面已经讨论过了，$\psi(x) $ 有平面波解：

$$
\psi_p(x)
=u(p)\mathrm{e}^{\mathrm{i}p x}
$$

$\psi(x) $ 还要满足 Dirac 方程。将 $\psi(x) $ 的平面波解代入自由旋量场 Dirac 方程 $\left(\gamma_\mu\partial_\mu + m \right)\psi(x) = 0$，可得：

$$
\left(\mathrm{i}\gamma_\mu p_\mu + m \right)u(p)\mathrm{e}^{\mathrm{i}p x}
=0
$$

因此，对任意 $p_\mu $，相应 $u(p) $ 要满足：

$$
\boxed{
\left(\mathrm{i}\hat{p}+m \right)u(p)
=0,\quad
\hat{p}\equiv \gamma_\mu p_\mu
}
$$

这是具有确定四维动量自由旋量粒子动量表象 Dirac 方程。

#### 具有确定三维动量的自由旋量粒子的哈密顿算符

回顾一下，对于一个自由旋量粒子，其哈密顿算符为 

$$
\hat{H}
=\vec{\alpha}\cdot\hat{\vec{p}} + \beta m
=\mathrm{i}\gamma_4 \vec{\gamma}\cdot\hat{\vec{p}} + \beta m 
=\beta\left(\mathrm{i}\vec{\gamma}\cdot\hat{\vec{p}} + m \right) 
$$

Somehow，R场论认为，一个具有确定动量（三维动量而非四维动量）的自由旋量粒子的哈密顿算符为：

$$
\hat{H}(\vec{p})
=\beta\left(\mathrm{i}\vec{\gamma}\cdot\vec{p} + m \right)
$$

#### 动量表象 $\hat{H}(\vec{p}) $ 的本征方程

具有确定四维动量自由旋量粒子动量表象 Dirac 方程：

$$
\left(\mathrm{i}\gamma_\mu p_\mu + m \right) u(p)
=0
$$

即：

$$
\left(\mathrm{i}\gamma_i p_i + \mathrm{i}\gamma_4p_4 + m \right)u(p)
=0
$$

左乘 $\beta =\gamma_4$：

$$
\left(\mathrm{i}\beta\vec{\gamma}\cdot\vec{p} + \mathrm{i}p_4 + m\beta \right)u(p)
=0
$$

即：

$$
\beta\left(\mathrm{i}\vec{\gamma}\cdot\vec{p} + m \right)u(p)
=-\mathrm{i}p_4 u(p)
$$

再注意到

$$
\hat{H}(\vec{p})
=\beta\left(\mathrm{i}\vec{\gamma}\cdot\vec{p} + m \right),\quad
p_0 = E,\quad p_4=\mathrm{i}E = \mathrm{i}p_0
$$

因此有动量表象 $\hat{H}(\vec{p}) $ 本征方程：

$$
\hat{H}(\vec{p}) u(p)
=p_0 u(p)
$$

由于 $\hat{H}(\vec{p}) $ 是厄米的，因此

$$
\begin{aligned}
\hat{H}^2(\vec{p})
&=\hat{H}^\dag(\vec{p}) \hat{H}(\vec{p}) \\
&=\left[\beta\left(\mathrm{i}\vec{\gamma}\cdot\vec{p} + m \right) \right]^\dag \left[\beta\left(\mathrm{i}\vec{\gamma}\cdot\vec{p} + m \right) \right] \\
&=\left(-\mathrm{i}\vec{\gamma}\cdot\vec{p} + m \right)\left(\mathrm{i}\vec{\gamma}\cdot\vec{p} + m \right) \\
&=\left(\vec{\gamma}\cdot\vec{p} \right)^2 + m^2 I \\
&=\left(\gamma_i p_i \right)\left(\gamma_j p_j \right) + m^2 I \\
&=\frac{1 }{2 } \left(\gamma_i\gamma_j + \gamma_j\gamma_i \right) p_i p_j + m^2 I \\
&=\delta_{ij}p_ip_j I + m^2 I \\
&=\left(\vec{p}^2 + m^2 \right) I
\end{aligned}
$$

因此由

$$
\hat{H}^2(\vec{p}) u(p) = p_0^2 u(p)
$$

可得：

$$
p_0 = \pm \sqrt{\vec{p}^2 + m^2}\equiv \pm E,\quad E\equiv \sqrt{\vec{p}^2+m^2}
$$

即：

$$
\hat{H}(\vec{p}) u(p) = \pm E u(p)
$$

上式说明，具有确定三维动量自由旋量粒子哈密顿算符 $\hat{H}(\vec{p}) $ 本征值为 $\pm\sqrt{\vec{p}^2+m^2} $，也就是说具有确定三维动量自由旋量粒子有 $+\sqrt{\vec{p}^2+m^2} $ 和 $-\sqrt{\vec{p}^2+m^2} $ 两种能量状态。

#### 具有确定四维动量自由旋量粒子自旋方向

由于

$$
\left[\hat{H}(\vec{p}) , \vec{\sigma}\cdot\vec{n} \right]
=0
$$

因此 $\hat{H}(\vec{p}) $ 的本征函数 $u(p) $ 也是 $\vec{\sigma}\cdot\vec{n} $ 的本征函数，设对应的本征值为 $\lambda $，其本征方程为：

$$
\left(\vec{\sigma}\cdot\vec{n} \right) u(p)
=\lambda u(p)
$$

注意到

$$
\begin{aligned}
\left(\vec{\sigma}\cdot\vec{n} \right)^2
&=\left(\vec{\sigma}\cdot\vec{n} \right)\left(\vec{\sigma}\cdot\vec{n} \right) \\
&=\vec{n}\cdot\vec{n} + \mathrm{i}\vec{\sigma}\cdot\left(\vec{n}\times\vec{n} \right) \\
&=1
\end{aligned}
$$

$\vec{\sigma}\cdot\vec{n} $ 两次作用于 $u(p) $：

$$
\left(\vec{\sigma}\cdot\vec{n} \right)^2 u(p)
=\lambda^2 u(p)
$$

结合 $\left(\vec{\sigma}\cdot\vec{n} \right)^2=1 $ 可得本征值的取值：

$$
\lambda = \pm 1
$$

即

$$
\left(\vec{\sigma}\cdot\vec{n} \right) u(p)
=\pm u(p)
$$

这就是说，具有确定四维动量的自由旋量粒子的自旋方向只可能与粒子运动方向平行或反平行。

#### 具有确定动量自由旋量粒子的四种独立态状态

由于

$$
\left[\hat{H}(\vec{p}) , \left(\vec{\sigma}\cdot\vec{n} \right) \right] = 0
$$

因此二者有共同本征态。上面讨论过，$\hat{H}(\vec{p}) $ 的本征值有 $\pm E $ 两种，$\left(\vec{\sigma}\cdot\vec{n} \right) $ 有 $\pm 1 $ 两种。

根据本征值可将 $\psi(x)=u(p)\mathrm{e}^{\mathrm{i}p x} $ 划分为以下四种态：

$p_0=+E,\lambda=+1 $ 记为 $u_1(\vec{p}) $

$p_0=+E,\lambda=-1 $ 记为 $u_2(\vec{p}) $

$p_0=-E,\lambda=+1 $ 记为 $u_3(\vec{p}) $

$p_0=-E,\lambda=-1 $ 记为 $u_4(\vec{p}) $

即

$$
\left(\vec{\sigma}\cdot\vec{n} \right)u_a(\vec{p})
=\left\{
\begin{aligned}
+ u_a(\vec{p}),a=1,3 \\
- u_a(\vec{p}),a=2,4
\end{aligned}
\right.
$$

$$
\hat{H}(\vec{p})u_a(\vec{p})
=\left\{
\begin{aligned}
+E u_a(\vec{p}),a=1,2 \\
-Eu_a(\vec{p}),a=3,4
\end{aligned}
\right.
$$

注意，本征态 $u_a(\vec{p}) $ 的能量本征值 $p_0 $ 由下标 $a $ 决定：

$$
p_0
=\left\{
\begin{aligned}
+E,a=1,2 \\
-E,a=3,4
\end{aligned}
\right.
$$

### 单位旋量 $u_a(\vec{p}) $ 的空间反射态

当时空坐标进行空间反射变换 $\vec{x}'=-\vec{x},t'=t $ 时，旋量场函数的变换规律为：

$$
\psi'(x')
=P\psi(x)
=\eta_{P}\gamma_4\psi(x),\quad
\eta_P = \pm\mathrm{i},\pm 1
$$

对于具有确定三维动量、能量和自旋状态的波函数

$$
\psi_a(x)
=u_a(\vec{p})\mathrm{e}^{\mathrm{i}(\vec{p}\cdot\vec{x}-p_0 t)}
$$

在空间反射新坐标系中的波函数为

$$
\begin{aligned}
\psi_a'(x')
&=\eta_P \gamma_4 \psi_a(x) \\
&=\eta_P \gamma_4 u_a(\vec{p}) \mathrm{e}^{\mathrm{i}(\vec{p}\cdot\vec{x}-p_0 t)} \\
&=\eta_P \gamma_4 u_a(\vec{p}) \mathrm{e}^{-\mathrm{i}\vec{p}\cdot\vec{x}'-p_0 t'} \\
&=\eta_P \gamma_4 u_a(\vec{p}) \mathrm{e}^{-\mathrm{i}\vec{p}\cdot\vec{x}'-p_0 t'} \\
&=\eta_P \gamma_4 u_a(\vec{p}) \mathrm{e}^{\mathrm{i}\left[\left(-\vec{p} \right)\cdot\vec{x}'-p_0 t' \right]}
\end{aligned}
$$

在新坐标系中，$\psi_a'(x') $ 沿 $\vec{p}'\equiv -\vec{p} $ 方向传播。

$\eta_P\gamma_4 u_a(\vec{p}) $ 称为单位旋量 $u_a(\vec{p}) $ 的空间反射态，记为 $u_a(-\vec{p}) $

$$
\boxed{
u_a(-\vec{p})
\equiv \eta_P \gamma_4 u_a(\vec{p})
}
$$

可以证明，$u_a(-\vec{p}) $ 能量状态与 $u_a(\vec{p}) $ 相同；$u_a(\vec{p}) $ 中自旋与 $\vec{p} $ 的夹角等于 $u_a(-\vec{p}) $ 中自旋与 $\vec{p} $ 的夹角。

### 旋量场的电荷共轭变换（正反粒子变换）

#### 有电磁场存在时的 Dirac 方程

我们知道自由旋量场 Dirac 方程：

$$
\left(\gamma_\mu \partial_\mu + m \right)\psi(x)
=0
$$

当有电磁场存在时，旋量粒子与光子会相互作用，旋量粒子不自由了。为了找到此时的场方程，作如下变换：

$$
p_\mu\to p_\mu-e A_\mu
$$

$$
\partial_\mu\to \partial_\mu-\mathrm{i}e A_\mu\equiv D_\mu
$$

则 Dirac 方程及其共轭方程化为

$$
\left(\gamma_\mu D_\mu + m \right)\psi = 0
$$

$$
D_\mu^\dag\bar{\psi}\gamma_mu - m\bar{\psi} = 0
$$

即得到矢量场合旋量场相互作用场方程：

$$
\left(\gamma_\mu\partial_\mu+m \right)\psi = \mathrm{i}e A_\mu \gamma_\mu \psi
$$

$$
\partial_\mu\bar{\psi}\gamma_\mu - m\bar{\psi} = -\mathrm{i}e A_\mu \bar{\psi}\gamma_\mu
$$

#### 电磁场存在时 Dirac 方程的 Lorentz 协变性

电磁场存在时 $x' $ 系的 Dirac 方程为：

$$
\left(\gamma_\mu\partial'_\mu - \mathrm{i}e A'_\mu \gamma_\mu + m \right)\psi'(x')
=0
$$

时空坐标进行 Lorentz 变换：

$$
x_\mu\to x'_\mu = A_{\mu\nu}x_\nu,\quad
A_{\mu\lambda}x'_\mu
=x_\lambda
$$

$x' $ 系的物理量用 $x $ 系的物理量表达：

$$
\partial'_\mu
\equiv \frac{\partial }{\partial x'_\mu } 
=\frac{\partial x_\nu }{\partial x'_\mu } \frac{\partial }{\partial x_\nu } 
=A_{\mu\nu}\partial_\nu
$$

$$
\psi'(x')
=\Lambda \psi(x)
$$

$$
A'_\mu
=A_{\mu\nu}A_\nu
$$

则 Dirac 方程化为：

$$
\begin{aligned}
0
&=\left(\gamma_\mu\partial'_\mu - \mathrm{i}e A'_\mu \gamma_\mu + m \right)\psi'(x') \\
&=\left(\gamma_\mu A_{\mu\nu}\partial_\nu - \mathrm{i}eA_{\mu\nu}A_\nu\gamma_\mu + m \right)\Lambda \psi(x)
\end{aligned}
$$

左乘 $\Lambda^{-1} $，并利用

$$
\Lambda^{-1}\gamma_\mu \Lambda
=A_{\mu\rho}\gamma_\rho
$$

可得：

$$
\begin{aligned}
0
&=\Lambda^{-1}\left(\gamma_\mu A_{\mu\nu}\partial_\nu - \mathrm{i}eA_{\mu\nu}A_\nu\gamma_\mu + m \right)\Lambda \psi(x) \\
&=\left(A_{\mu\rho}\gamma_\rho A_{\mu\nu}\partial_\nu - \mathrm{i}eA_{\mu\nu} A_\nu A_{\mu\rho}\gamma_\rho + m \right)\psi(x) \\
&=\left(\delta_{\rho\nu}\gamma_\rho\partial_\nu - \mathrm{i}e\delta_{\nu\rho}A_\nu\gamma_\rho + m \right)\psi(x) \\
&=\left(\gamma_\nu \partial_\nu - \mathrm{i} e A_\rho\gamma_\rho + m \right)\psi(x)
\end{aligned}
$$

因此，$x $ 系中的 Dirac 方程为：

$$
\left(\gamma_\mu \partial_\mu - \mathrm{i} e A_\mu \gamma_\mu + m \right)\psi(x)
=0
$$

与 $x' $ 系中的 Dirac 方程

$$
\left(\gamma_\mu\partial'_\mu - \mathrm{i}e A'_\mu \gamma_\mu + m \right)\psi'(x')
=0
$$

对比可知，电磁场存在时 Dirac 方程具有 Lorentz 协变性。

#### 电荷共轭变换

电荷共轭变换把粒子的场函数变为反粒子场函数，把粒子运动方程变为反粒子的运动方程。

经典旋量场的电荷共轭变换定义如下：

$$
\psi^C(x)
\equiv C \bar{\psi}^\mathrm{T}(x),\quad
\bar{\psi}^C(x)
=\left(\psi^C \right)^\dag \gamma_4
=\left[C^{-1}\psi(x) \right]^\mathrm{T}
$$

称为 $\psi(x) $ 和 $\bar{\psi}(x) $ 的电荷共轭函数，其中

$$
C
\equiv \mathrm{i}\gamma_2\gamma_4
=-\begin{bmatrix}
0 &\sigma^0_2 \\
\sigma^0_2 &0
\end{bmatrix}
$$

由

$$
-\gamma_\mu^\mathrm{T}
=C^{-1} \gamma_\mu C,\quad \left|C \right|\ne 0
$$

定义。

#### $\psi^C $ 和 $\bar{\psi}^C $ 满足的方程

$$
\gamma_\mu\partial_\mu \psi^C + m\psi^C
=-\mathrm{i}e A_\mu \gamma_\mu \psi^C
$$

$$
\partial_\mu \bar{\psi}^C \gamma_\mu - m\bar{\psi}^C
=\mathrm{i}e A_\mu \bar{\psi}^C \gamma_\mu
$$

上两式称为 Dirac 方程的电荷共轭方程。与电磁场存在时的 Dirac 方程

$$
\left(\gamma_\mu\partial_\mu + m \right)\psi
=\mathrm{i}e A_\mu \gamma_\mu \psi
$$

$$
\partial_\mu\bar{\psi}\gamma_mu - m\bar{\psi}
=-\mathrm{i}e A_\mu \bar{\psi}\gamma_\mu
$$

比较，可知经过电荷共轭变换后，方程中电荷改变了正负号。

若 $\psi(x) $ 是描写电子的旋量函数，则 $\psi^C(x) $ 是描述正电子的旋量函数。

若 $\bar{\psi}(x) $ 是描写正电子的旋量函数，则 $\bar{\psi}^C(x) $ 是描述电子的旋量函数。

即若 $\psi(x) $ 和 $\bar{\psi}(x) $ 是描写粒子的旋量函数，则 $\psi^C(x) $ 和 $\bar{\psi}^C $ 是描述反粒子的旋量函数。

#### 反粒子单位旋量 $v_b(\vec{p}) $

对于具有确定能量、动量和自旋态的自由电子，其旋量波函数为

$$
\psi_b(x)
=u_b(\vec{p})\mathrm{e}^{\mathrm{i}p x}
$$

相应共轭旋量波函数为

$$
\bar{\psi}_b(x)
\equiv \psi_b^\dag(x) \gamma_4
=u_b^\dag(\vec{p}) \gamma_4 \mathrm{e}^{-\mathrm{i}p x}
\equiv \bar{u}_b(\vec{p})\mathrm{e}^{-\mathrm{i}p x},\quad
\bar{u}_b(\vec{p})
\equiv u_b^\dag(\vec{p})\gamma_4,\quad b=1,2,3,4
$$

$\psi_b(x) $ 的电荷共轭函数为

$$
\psi_b^C(x)
\equiv C\bar{\psi}_b^\mathrm{T}(x)
=C \left(\bar{u}_b(\vec{p})\mathrm{e}^{-\mathrm{i}p x} \right)^{\mathrm{T}}
=C \bar{u}_b^{\mathrm{T}}(\vec{p}) \mathrm{e}^{-\mathrm{i}p x}
\equiv u_b^C(\vec{p})\mathrm{e}^{-\mathrm{i}p\cdot x}
$$

$$
u_b^C(\vec{p})
\equiv C\bar{u}_b^\mathrm{T}(\vec{p})
\equiv C \left(u_b^\dag(\vec{p})\gamma_4 \right)^{\mathrm{T}}
=C \gamma_4^{\mathrm{T}} u_b^*(\vec{p})
$$

把

$$
\psi_b^C(x)
=u_b^C(\vec{p})\mathrm{e}^{-\mathrm{i}p\cdot x}
$$

代入自由旋量粒子电荷共轭 Dirac 方程

$$
\gamma_\mu\partial_\mu\psi^C + m\psi^C
=0
$$

可得 $u_b^C(\vec{p}) $ 满足的动量表象方程：

$$
\boxed{
\left(\mathrm{i}\hat{p}-m \right)u_b^C(\vec{p})
=0
}
$$

$u_b^C(\vec{p})\equiv C\bar{u}_b^\mathrm{T}(\vec{p}) $ 称为**反粒子单位旋量**，通常记为 $v_b(\vec{p}) $，即：

$$
\boxed{
v_b(\vec{p})
\equiv u_b^C(\vec{p})\equiv C\bar{u}_b^\mathrm{T}(\vec{p})
=C \gamma_4^{\mathrm{T}} u_b^*(\vec{p})
}
$$

其满足方程：

$$
\boxed{
\left(\mathrm{i}\hat{p}-m \right) v_b(\vec{p})
=0
}
$$

利用 $u_b(\vec{p}) $ 的正交完备性，可证明 $v_b(\vec{p}) $ 也是正交完备的：

$$
\boxed{
v_a^\dag v_b = \delta_{ab},\quad a=1,2,3,4
}
$$

$$
\boxed{
v_a v_a^\dag = I
}
$$

#### 单位旋量 $u_a(\vec{p}) $ 和 $v_a(\vec{p}) $ 的一些性质

$\left\{u_a(\vec{p}),a=1,2,3,4 \right\} $ 和 $\left\{v_a(\vec{p}),a=1,2,3,4 \right\} $ 构成旋量空间的两组基底。

可选取

$$
u_1(\vec{p}),u_2(\vec{p}),v_1(\vec{p}),v_2(\vec{p})
$$

作为旋量空间的基底，它们满足正反粒子单位旋量动量表象 Dirac 方程：

$$
\left(\mathrm{i}\hat{p} + m \right) u_i(\vec{p})
=0,\quad
\left(\mathrm{i}\hat{p} - m \right) v_i(\vec{p})
=0,\quad
i=1,2
$$

有如下正交关系：

$$
u_i^\dag(\vec{p})u_j(\vec{p}) = \delta_{ij}
$$

$$
v_i^\dag(\vec{p})v_j(\vec{p}) = \delta_{ij}
$$

$$
\bar{u}_i(\vec{p}) u_j(\vec{p})
=\frac{m }{E } \delta_{ij}
$$

$$
\bar{v}_i(\vec{p}) v_j(\vec{p})
=-\frac{m }{E } \delta_{ij}
$$

#### 正反粒子投影算符 $\Lambda_{\pm}(p) $

正反粒子投影算符 $\Lambda_{\pm}(p) $ 定义如下：

$$
\boxed{
\Lambda_\pm(p)
\equiv \pm \frac{1 }{2 m} \left(\mathrm{i}\gamma_\mu p_\mu \pm m \right)
}
$$

有如下的一些性质：

$$
\boxed{
\begin{aligned}
\Lambda_\pm(-p)
&=\Lambda_\mp(p)
\end{aligned}
}
$$

$$
\boxed{
\Lambda_+(p) + \Lambda_-(p) = 1
}
$$

$$
\begin{aligned}
\Lambda_+(p) \Lambda_-(p)
&=\frac{1 }{2m } \left(\mathrm{i}\gamma_\mu p_\mu + m  \right) \frac{-1 }{2m } \left(\mathrm{i}\gamma_\nu p_\nu - m \right) \\
&=\frac{1 }{4m^2 } \left(\gamma_\mu \gamma_\nu p_\mu p_\nu + m^2 \right) \\
&=0
\end{aligned}
$$

$$
\boxed{
\Lambda_+(p) \Lambda_-(p) = \Lambda_-(p) \Lambda_+(p) = 0
}
$$

$$
\boxed{
\Lambda_+^2(p)
=\Lambda_+(p),\quad
\Lambda_-^2(p)
=\Lambda_-(p)
}
$$

考虑到 $\left(\mathrm{i}\gamma_\mu \hat{p}_\mu + m \right) u_i(\vec{p}) = 0,\left(\mathrm{i}\gamma_\mu \hat{p}_\mu - m \right) v_i(\vec{p}) = 0 $ 可得：

$$
\boxed{
\Lambda_-(p) u_j(\vec{p})
=u_j(\vec{p}),\quad
\Lambda_-(p) v_j(\vec{p})
=0
}
$$

$$
\boxed{
\Lambda_+(p) u_j(\vec{p})
=0,\quad
\Lambda_+(p) v_j(\vec{p})
=v_j(\vec{p})
}
$$

可见，$\Lambda_+(p) $ 反粒子单位旋量投影算符；$\Lambda_-(p) $ 正粒子单位旋量投影算符。

可以证明，任何旋量 $f(p) $ 可以用 $u_1(\vec{p}),u_2(\vec{p}),v_1(\vec{p}),v_2(\vec{p}) $ 展开：

$$
f(p)
=a_i u_i(\vec{p}) + b_i v_i(\vec{p})
$$

展开系数为：

$$
a_i = \frac{E }{m } \bar{u}_i(\vec{p}) f(p),\quad
b_i = -\frac{E }{m } \bar{v}_i(\vec{p}) f(p),\quad
i=1,2
$$

投影算符（或动量算符）与单位旋量之间的关系为：

$$
\boxed{
u_i(\vec{p}) \bar{u}_i(\vec{p}) = \frac{m }{E } \Lambda_-(p) = -\frac{1 }{2E } \left(\mathrm{i}\gamma_\mu \hat{p}_\mu - m \right) ,\quad
v_i(\vec{p}) \bar{v}_i(\vec{p}) = -\frac{m }{E } \Lambda_+(p) = -\frac{1 }{2E } \left(\mathrm{i}\gamma_\mu \hat{p}_\mu + m \right)
}
$$

# 6 拉格朗日方程、对称性与守恒律

## 场论中的拉格朗日原理

### 拉格朗日原理与场的运动方程

引入广义场函数 $\phi_A(x) $，其可以是张量场函数，也可以是旋量场函数，也可以是标量场函数。

场的作用量定义如下：

$$
I\left[\phi_A(x) \right]
=\int\limits_{G} \mathcal{L}\left(\phi_A,\partial_\mu\phi_A \right)\mathrm{d}^4x,\quad
\mathrm{d}^4 x
=\mathrm{d}x_0\mathrm{d}x_1\mathrm{d}x_2\mathrm{d}x_3,\quad
x_4
=\mathrm{i}x_0
$$

$G $ 是场在四维时空中存在的范围；$\mathcal{L} $ 是场的拉格朗日密度。

Lagrange 原理就是说，场的真实运动规律使作用量 $I $ 取最小值，即：

$$
\delta I = 0
$$

利用变分法可得场的运动方程（E-L方程）：

$$
\boxed{
\frac{\partial\mathcal{L} }{\partial \phi_A } - \partial_\mu\frac{\partial\mathcal{L} }{\partial \left(\partial_\mu \phi_A \right) } 
=0
}
$$

定义拉格朗日密度对广义场函数的欧拉式 $\left[\mathcal{L} \right]_{\phi_A} $：

$$
\left[\mathcal{L} \right]_{\phi_A}
\equiv \frac{\partial\mathcal{L} }{\partial \phi_A } - \partial_\mu\frac{\partial\mathcal{L} }{\partial \left(\partial_\mu \phi_A \right) } 
$$

则场的运动方程可写为：

$$
\left[\mathcal{L} \right]_{\phi_A}
=0
$$

### 拉格朗日密度满足的条件

（1）$\mathcal{L} $ 是固有洛伦兹变换 $a_{\mu\nu} $ 及其旋量表示 $\Lambda $ 的不变量。这样才能保证场方程对固有洛伦兹变换协变和角动量守恒。

（2）$\mathcal{L} $ 是四维位移变换的不变量，因此 $\mathcal{L} $ 不应显含 $x_\mu $,这样才能保证能量和动量守恒。

（3）$\mathcal{L} $ 必须是 $\phi_A $ 和 $\partial_\mu\phi_A $ 的二次齐式。这样才能保证场的微分方程是线性的，荷守恒定律及电荷数、重子数、轻子数守恒（整体相因子变换下的守恒性）。

（4）$\mathcal{L} $ 是时间反演变换的不变量。在强和电磁作用中还要求 $\mathcal{L} $ 对空间反射变换合电荷共轭变换的不变性。

（5）$\mathcal{L} $ 是规范变换的不变量。整体规范变换的协变性保证荷守恒。局域规范变换的协变性引入相互作用。

### 各种自由场的拉格朗日函数

#### 实标量场

实标量场描述自旋为零、偶宇称、无反粒子的粒子，

$$
\mathcal{L}_0
=-\frac{1 }{2 } \left(\partial_\mu \phi \partial_\mu \phi + m^2\phi^2 \right)
$$

$$
\frac{\partial \mathcal{L}_0 }{\partial \phi } = -m^2\phi,\quad
\frac{\partial \mathcal{L}_0 }{\partial\left(\partial_\mu \phi \right) } = -\partial_\mu\phi
$$

代入E-L方程，得标量场方程：

$$
\left(\square-m^2 \right)\phi = 0
$$

#### 复标量场

复标量场描述自旋为零，存在正、反粒子的粒子。

$$
\mathcal{L}_0
=-\partial_\mu\phi^* \partial_\mu\phi  - m^2\phi^*\phi
$$

分别把 $\phi,\phi^* $ 作为变分量代入 E-L 方程，可得复标量场方程：

$$
\left(\square-m^2 \right)\phi = 0
$$

$$
\left(\square-m^2 \right)\phi^* = 0
$$

#### 赝标量场

赝标量场描述自旋为零、奇宇称的粒子。

$$
\mathcal{L}_0
=-\frac{1 }{2 } \left(\partial_\mu\tilde{\phi} \partial_\mu\tilde{\phi} + m^2\tilde{\phi}^2 \right)
$$

赝标量场方程为：

$$
\left(\square-m^2 \right)\tilde{\phi} = 0
$$

#### 旋量场

旋量场描述自旋为 $1/2 $ 的粒子（自旋为 $1/2 $ 粒子总有反粒子存在）。

$$
\mathcal{L}_0
=-\frac{1 }{2 } \left(\bar{\psi}\gamma_\mu\partial_\mu\psi - \partial_\mu\bar{\psi} \gamma_\mu\psi \right) - m\bar{\psi}\psi
=-\frac{1 }{2 } \bar{\psi}\left(\gamma_\mu\partial_\mu\psi + m\psi \right) + \frac{1 }{2 } \left(\partial_\mu\bar{\psi}\gamma_\mu - m\bar{\psi} \right)\psi
$$

分别把 $\psi,\bar{\psi} $ 作为变分量，代入 E-L 方程可得 Dirac 方程以及共轭 Dirac 方程：

$$
\left(\gamma_\mu\partial_\mu + m \right)\psi = 0
$$

$$
\partial_\mu\bar{\psi}\gamma_\mu - m\bar{\psi} = 0
$$

#### 矢量场

矢量场描述自旋为 $1 $ 的光子。

$$
\mathcal{L}_0
=-\frac{1 }{2 }\partial_\mu A_\nu \partial_\mu A_\nu 
$$

把 $A_\mu $ 作为变分量代入 E-L 方程，的达朗贝尔方程：

$$
\square A_\mu = 0
$$

静止质量不为零的矢量粒子的拉格朗日密度为：

$$
\mathcal{L}_0
=-\frac{1 }{2 } \left(\partial_\mu A_\nu \right)\left(\partial_\mu A_\nu \right) - \frac{1 }{2 } m^2 A_\mu A_\mu
$$

运动方程：

$$
\left(\square - m^2 \right)A_\mu = 0
$$

这破坏规范协变性。

---

若令

$$
\mathcal{L}_0'
=-\frac{1 }{4 } F_{\mu\nu} F_{\mu\nu},\quad
F_{\mu\nu}
=\partial_\mu A_\nu - \partial_\nu A_\mu
$$

则可得：

$$
\partial_\nu F_{\mu\nu}
=0
$$

---

若 $A_\mu $ 满足 Lorenz 条件

$$
\partial_\mu A_\mu
=0
$$

则

$$
\mathcal{L}_0'
=-\frac{1 }{4 } F_{\mu\nu} F_{\mu\nu},\quad
\mathcal{L}_0
=-\frac{1 }{2 }\partial_\mu A_\nu \partial_\mu A_\nu 
$$

等价。

## 对称性与守恒律

### 广义守恒定理1

设 $\theta_{\mu\cdots \nu\lambda}(x) $ 是 $n $ 阶张量函数，且满足：

$$
\theta_{\mu\cdots \nu\lambda}(x)\bigg|_{\vec{x}\to \infty}
=0
$$

若

$$
\partial_{\lambda}\theta_{\mu\cdots \nu\lambda}
=0
$$

则存在一个 $(n-1) $ 阶守恒张量：

$$
T_{\mu\cdots \nu}(x_4)
\equiv \frac{1 }{\mathrm{i} } \int\limits_{\vec{x}\in \R^3} \theta_{\mu\cdots \nu 4}(\vec{x},x_4)\mathrm{d}^3\vec{x}
=\mathrm{const}
$$

即 $T_{\mu\cdots \nu} $ 不随时间改变。

### 广义守恒定理2

若场的作用量

$$
I
=\int\limits_{G} \mathcal{L}\left(\phi_A,\partial_\mu\phi_A \right)\mathrm{d}^4 x
$$

对微量变换

$$
x\to x' = x+\delta x,\quad
\phi_A\to \phi'_A = \phi_A + \delta_0 \phi_A
$$

$$
\phi_A(x)\to \phi_A'(x')
=\phi_A(x) + \delta \phi_A(x)
$$

保持不变，则存在一个矢量

$$
\theta_\mu
=\left(\mathcal{L}\delta_{\mu\nu}-\frac{\partial\mathcal{L} }{\partial\left(\partial_\mu\phi_A \right) } \partial_\nu\phi_A \right)\delta x_\nu + \frac{\partial\mathcal{L} }{\partial\left(\partial_\mu\phi_A \right) } \delta\phi_A
$$

满足关系式：

$$
\partial_\mu\theta_\mu + \left[\mathcal{L} \right]_{\phi_A}\delta_0 \phi_A
=0
$$

### 诺特定理

设坐标和广义场函数的变换依赖于连续变化的参数 $\alpha=\left\{\alpha_{i\cdots k} \right\} $，即

$$
x'=x'(x,\alpha),\quad
\phi'_A(x')=\phi'_A(x,\alpha)\equiv \Phi_A(x,\alpha),\quad
$$

且满足

$$
x'(x,0) = x,\quad
\Phi_A(x,0) = \phi_A(x)
$$

若作用量 $I $ 对这个依赖于连续参数 $\alpha $ 的变换不变，且广义场函数满足欧拉方程 $\left[\mathcal{L} \right]_{\phi_A}=0 $，也即满足最小作用量原理时，则存在守恒定律（连续方程）

$$
\partial_\mu \theta_{i\cdots k \mu}
=0,\quad
\theta_{i\cdots k \mu}
\equiv \left[\mathcal{L}\frac{\partial x'_\mu }{\partial \alpha_{i\cdots k} } - \frac{\partial \mathcal{L} }{\partial\left(\partial_\mu \phi_A \right) } \partial_\nu \phi_A \frac{\partial x'_\nu }{\partial \alpha_{i\cdots k} } + \frac{\partial \mathcal{L} }{\partial\left(\partial_\mu \phi_A \right) } \frac{\partial \Phi_A }{\partial \alpha_{i\cdots k} }  \right]\bigg|_{\alpha=0}
$$

和守恒张量

$$
T_{i\cdots k}
=\frac{1 }{\mathrm{i} } \int \theta_{i\cdots k4}\mathrm{d}V
$$

且 $T_{i\cdots k} $ 的指标与 $\alpha_{i\cdots k} $ 的指标一致。

#### 能量动量张量和能量动量守恒

考虑坐标进行四维时空平移变换：

$$
x'_\mu(x,\alpha) = x_\mu + \alpha_\mu,\quad
\phi_A'(x,\alpha) = \phi_A(x)
$$

根据诺特定理，若场的作用量对四维时空平移变化保持不变，则存在连续方程和守恒张量。下面来找连续方程和守恒张量。

计算变换后坐标对参数的偏导、变换后广义场函数对参数的偏导在参数为零处的取值：

$$
\frac{\partial x'_\mu(x,\alpha) }{\partial \alpha_\nu } \bigg|_{\alpha=0}
=\delta_{\mu\nu},\quad
\frac{\partial \phi'_A(x,\alpha) }{\partial \alpha_\nu } \bigg|_{\alpha=0}
=0
$$

诺特定理中定义的量

$$
\begin{aligned}
\theta_{i\cdots k \mu}
&\equiv \left[\mathcal{L}\frac{\partial x'_\mu }{\partial \alpha_{i\cdots k} } - \frac{\partial \mathcal{L} }{\partial\left(\partial_\mu \phi_A \right) } \partial_\beta \phi_A \frac{\partial x'_\beta }{\partial \alpha_{i\cdots k} } + \frac{\partial \mathcal{L} }{\partial\left(\partial_\mu \phi_A \right) } \frac{\partial \phi_A' }{\partial \alpha_{i\cdots k} }  \right]\bigg|_{\alpha=0} \\
\end{aligned}
$$

在这里（四个参数 $\alpha_\nu $）表现为：

$$
\begin{aligned}
\theta_{\nu \mu}
&=\left[\mathcal{L}\frac{\partial x'_\mu }{\partial \alpha_{\nu} } - \frac{\partial \mathcal{L} }{\partial\left(\partial_\mu \phi_A \right) } \partial_\beta \phi_A \frac{\partial x'_\beta }{\partial \alpha_{\nu} } + \frac{\partial \mathcal{L} }{\partial\left(\partial_\mu \phi_A \right) } \frac{\partial \phi_A' }{\partial \alpha_{\nu} }  \right]\bigg|_{\alpha=0} \\
&=\mathcal{L} \delta_{\mu\nu} - \frac{\partial \mathcal{L} }{\partial\left(\partial_\mu \phi_A \right) } \partial_\nu \phi_A
\end{aligned}
$$

交换 $\mu,\nu $ 指标得到：

$$
\theta_{\mu\nu}
=\mathcal{L} \delta_{\mu\nu} - \frac{\partial \mathcal{L} }{\partial\left(\partial_\nu \phi_A \right) } \partial_\mu \phi_A
$$

定义场的能量动量张量 $T_{\mu\nu} $：

$$
T_{\mu\nu}
\equiv \mathcal{L} \delta_{\mu\nu} - \frac{\partial \mathcal{L} }{\partial\left(\partial_\nu \phi_A \right) } \partial_\mu \phi_A
$$

诺特定理中的连续方程

$$
\partial_\mu \theta_{i\cdots k\mu} = 0
$$

在这里表现为：

$$
\partial_\nu T_{\mu\nu}
=0
$$

诺特定理中的守恒张量

$$
T_{i\cdots k}
=\frac{1 }{\mathrm{i} } \int \theta_{i\cdots k4}\mathrm{d}V
$$

在这里表现为：

$$
p_\mu
\equiv \frac{1 }{\mathrm{i} } \int T_{\mu4}\mathrm{d}V,\quad
\frac{\mathrm{d}p_\mu }{\mathrm{d}t }
=0
$$

$$
p_i
\equiv \frac{1 }{\mathrm{i} } \int T_{i4}\mathrm{d}V,\quad
p_4
\equiv \frac{1 }{\mathrm{i} } \int T_{44}\mathrm{d}V
=\mathrm{i} \frac{E }{c } 
$$

$p_i $ 称为三维空间场的动量，$E $ 称为场的能量。

$$
E
=-\int T_{44} \mathrm{d}V
$$

#### 角动量张量和角动量守恒

考虑坐标进行固有 Lorentz 变换，广义场函数（标量场、矢量场或旋量场）也进行相应变换：

$$
x'_\mu(x,\alpha) = a_{\mu \nu} x_\nu = (\delta_{\mu\nu} + \alpha_{\mu\nu}) x_\nu,\quad
\phi'(x,\alpha) = D(\alpha) \phi(x)
$$

其中，对于标量场，$\phi(x) $ 是标量，$D(\alpha) $ 是 $1 $；对于矢量场，$\phi(x) $ 是矢量场列矢量，$D(\alpha) $ 是固有 Lorentz 变换矩阵；对于旋量场，$\phi(x) $ 是旋量列矢量，$D(\alpha) $ 是固有 Lorentz 变换的旋量表示 $S .$

根据诺特定理，若场的作用量对坐标的固有 Lorentz 变换和广义场函数相应变换保持不变，则存在连续方程和守恒张量。下面来找连续方程和守恒张量。

为简单，考虑坐标和广义场函数的无穷小变换，即：

$$
\alpha_{\mu\nu} \to 0,\quad
x'_\mu(x,\alpha) = (\delta_{\mu\nu} + \alpha_{\mu\nu}) x_\nu = x_\mu + \alpha_{\mu\nu} x_\nu 
$$

$$
\phi'(x,\alpha) = \phi(x) + \frac{1 }{2 } I_{\mu\nu} \alpha_{\mu\nu} \phi(x),\quad
I_{\mu\nu} \equiv \frac{\partial D(\alpha) }{\partial \alpha_{\mu\nu} } \bigg|_{\alpha=0}
$$

$$
\phi_A'(x,\alpha) = \phi_A(x) + \frac{1 }{2 } \left(I_{\mu\nu} \right)_{AB} \alpha_{\mu\nu} \phi_B(x)
$$

容易证明，无穷小变换情况下，$\alpha_{\mu\nu}=-\alpha_{\nu\mu},I_{\mu\nu}=-I_{\nu\mu} $，这就导致了 $1/2 $ 因子。

计算变换后坐标对参数的偏导、变换后广义场函数对参数的偏导在参数为零处的取值：

$$
\frac{\partial x'_\mu(x,\alpha) }{\partial\alpha_{\lambda\rho} } \bigg|_{\alpha=0}
=\left(\delta_{\mu\lambda}\delta_{\nu\rho} - \delta_{\mu\rho}\delta_{\nu\lambda} \right)x_\nu
=\delta_{\mu\lambda}x_\rho - \delta_{\mu\rho}x_\lambda
$$

$$
\frac{\partial \phi'(x,\alpha) }{\partial \alpha_{\lambda\rho} } \bigg|_{\alpha=0}
=I_{\lambda\rho} \phi(x)
\equiv D_{\lambda\rho}
$$

$$
\frac{\partial \phi_A'(x,\alpha) }{\partial \alpha_{\lambda\rho} } \bigg|_{\alpha=0}
=\left(I_{\lambda\rho} \right)_{AB} \phi_B(x)
\equiv \left(D_{\lambda\rho} \right)_A
$$

诺特定理中定义的量

$$
\begin{aligned}
\theta_{i\cdots k \mu}
&\equiv \left[\mathcal{L}\frac{\partial x'_\mu }{\partial \alpha_{i\cdots k} } - \frac{\partial \mathcal{L} }{\partial\left(\partial_\mu \phi_A \right) } \partial_\nu \phi_A \frac{\partial x'_\nu }{\partial \alpha_{i\cdots k} } + \frac{\partial \mathcal{L} }{\partial\left(\partial_\mu \phi_A \right) } \frac{\partial \phi_A' }{\partial \alpha_{i\cdots k} }  \right]\bigg|_{\alpha=0} \\
\end{aligned}
$$

在这里（参数 $\alpha_{\mu\nu} $）表现为：

$$
\begin{aligned}
\theta_{\lambda\rho\mu}
&=\left[\mathcal{L}\frac{\partial x'_\mu }{\partial \alpha_{\lambda\rho} } - \frac{\partial \mathcal{L} }{\partial\left(\partial_\mu \phi_A \right) } \partial_\nu \phi_A \frac{\partial x'_\nu }{\partial \alpha_{\lambda\rho} } + \frac{\partial \mathcal{L} }{\partial\left(\partial_\mu \phi_A \right) } \frac{\partial \phi_A' }{\partial \alpha_{\lambda\rho} }  \right]\bigg|_{\alpha=0} \\
&=\mathcal{L}(\delta_{\mu\lambda}x_\rho - \delta_{\mu\rho}x_\lambda) - \frac{\partial \mathcal{L} }{\partial\left(\partial_\mu \phi_A \right) } \partial_\nu \phi_A(\delta_{\nu\lambda}x_\rho - \delta_{\nu\rho}x_\lambda) + \frac{\partial\mathcal{L} }{\partial\left(\partial_\mu\phi_A \right) } \left(D_{\lambda\rho} \right)_A \\
&=\mathcal{L}(\delta_{\mu\lambda}x_\rho - \delta_{\mu\rho}x_\lambda) - \frac{\partial \mathcal{L} }{\partial\left(\partial_\mu \phi_A \right) } (x_\rho \partial_\lambda \phi_A - x_\lambda \partial_\rho \phi_A) + \frac{\partial\mathcal{L} }{\partial\left(\partial_\mu\phi_A \right) } \left(D_{\lambda\rho} \right)_A \\
&=\left(\mathcal{L}\delta_{\mu\lambda} - \frac{\partial \mathcal{L} }{\partial\left(\partial_\mu \phi_A \right) } \partial_\lambda \phi_A \right) x_\rho - \left(\mathcal{L}\delta_{\mu\rho} - \frac{\partial \mathcal{L} }{\partial\left(\partial_\mu \phi_A \right) } \partial_\rho \phi_A \right) x_\lambda + \frac{\partial\mathcal{L} }{\partial\left(\partial_\mu\phi_A \right) } \left(D_{\lambda\rho} \right)_A \\
&\equiv T_{\lambda\mu} x_\rho - T_{\rho\mu} x_\lambda + \frac{\partial\mathcal{L} }{\partial\left(\partial_\mu\phi_A \right) } \left(D_{\lambda\rho} \right)_A \\
\end{aligned}
$$

换个指标：

$$
\theta_{[\mu\nu]\alpha}
=T_{\mu\alpha} x_\nu - T_{\nu\alpha} x_\mu + \frac{\partial\mathcal{L} }{\partial\left(\partial_\alpha\phi_A \right) } \left(D_{\mu\nu} \right)_A
$$

场的总动量矩张量 $J_{[\mu\nu]\alpha} $ 定义为：

$$
J_{[\mu\nu]\alpha}
\equiv T_{\mu\alpha} x_\nu - T_{\nu\alpha} x_\mu + \frac{\partial\mathcal{L} }{\partial\left(\partial_\alpha\phi_A \right) } \left(D_{\mu\nu} \right)_A
$$

定义场的三阶轨道动量矩张量 $L_{[\mu\nu]\alpha} $：

$$
L_{[\mu\nu]\alpha}
\equiv T_{\mu\alpha} x_\nu - T_{\nu\alpha} x_\mu
$$

定义场的三阶自旋张量 $S_{[\mu\nu]\alpha} $：

$$
S_{[\mu\nu]\alpha}
\equiv \frac{\partial\mathcal{L} }{\partial\left(\partial_\alpha\phi_A \right) } \left(D_{\mu\nu} \right)_A
$$

则：

$$
J_{[\mu\nu]\alpha}
=L_{[\mu\nu]\alpha} + S_{[\mu\nu]\alpha}
$$

诺特定理中的连续方程

$$
\partial_\mu \theta_{i\cdots k\mu} = 0
$$

在这里表现为：

$$
\partial_\alpha J_{[\mu\nu]\alpha}
=0
$$

诺特定理中的守恒张量

$$
T_{i\cdots k}
=\frac{1 }{\mathrm{i} } \int \theta_{i\cdots k4}\mathrm{d}V
$$

在这里表现为：

$$
J_{\mu\nu}
\equiv \frac{1 }{\mathrm{i} } \int J_{[\mu\nu]4}\mathrm{d}V,\quad
\frac{\mathrm{d}J_{\mu\nu } }{\mathrm{d}t } 
=0
$$

其中 $J_{\mu\nu} $ 称为二阶动量矩张量。

定义场的二阶轨道动量矩张量：

$$
L_{\mu\nu}
\equiv \frac{1 }{\mathrm{i} } \int L_{[\mu\nu]4}\mathrm{d}V
$$

定义场的二阶自旋张量：

$$
S_{\mu\nu}
\equiv \frac{1 }{\mathrm{i} } \int S_{[\mu\nu]4}\mathrm{d}V
$$

则守恒量 $J_{\mu\nu} $ 可写为：

$$
J_{\mu\nu}
=L_{\mu\nu} + S_{\mu\nu}
$$

#### 相因子变换、电流密度矢量和电荷守恒

考虑广义场函数进行相因子变换:

$$
x'_\mu(x,\alpha) = x_\mu,\quad
\phi'_A(x,\alpha) = \mathrm{e}^{\mathrm{i}\alpha}\phi_A(x),\quad
\phi_A^{*'}(x,\alpha) = \mathrm{e}^{-\mathrm{i}\alpha} \phi_A^*(x)
$$

根据诺特定理，若场的作用量对相因子变化保持不变，则存在连续方程和守恒张量。下面来找连续方程和守恒张量。

计算变换后坐标对参数的偏导、变换后广义场函数对参数的偏导在参数为零处的取值：

$$
\frac{\partial x'_\mu(x,\alpha) }{\partial\alpha } \bigg|_{\alpha=0}
=0,\quad
\frac{\partial \phi_A'(x,\alpha) }{\partial\alpha } \bigg|_{\alpha=0}
=\mathrm{i}\phi_A(x),\quad
\frac{\partial \phi_A^{*'}(x,\alpha) }{\partial \alpha} \bigg|_{\alpha=0}
=-\mathrm{i}\phi_A^*(x)
$$

诺特定理中定义的量

$$
\begin{aligned}
\theta_{i\cdots k \mu}
&\equiv \left[\mathcal{L}\frac{\partial x'_\mu }{\partial \alpha_{i\cdots k} } - \frac{\partial \mathcal{L} }{\partial\left(\partial_\mu \phi_A \right) } \partial_\nu \phi_A \frac{\partial x'_\nu }{\partial \alpha_{i\cdots k} } + \frac{\partial \mathcal{L} }{\partial\left(\partial_\mu \phi_A \right) } \frac{\partial \phi_A' }{\partial \alpha_{i\cdots k} }  \right]\bigg|_{\alpha=0} \\
\end{aligned}
$$

在这里（一个参数 $\alpha $）表现为：

$$
\begin{aligned}
\theta_{\mu}
&=\left[\mathcal{L}\frac{\partial x'_\mu }{\partial \alpha } - \frac{\partial \mathcal{L} }{\partial\left(\partial_\mu \phi_A \right) } \partial_\nu \phi_A \frac{\partial x'_\nu }{\partial \alpha } + \frac{\partial \mathcal{L} }{\partial\left(\partial_\mu \phi_A \right) } \frac{\partial \phi_A' }{\partial \alpha }  \right]\bigg|_{\alpha=0} \\
&=\left[\frac{\partial\mathcal{L} }{\partial\left(\partial_\mu \phi_A \right) } \frac{\partial \phi_A'(x,\alpha) }{\partial\alpha } + \frac{\partial \phi_A^{*'}(x,\alpha) }{\partial\alpha } \frac{\partial\mathcal{L} }{\partial\left(\partial_\mu \phi_A^* \right) }  \right]\bigg|_{\alpha=0} \\
&=\mathrm{i}\alpha\left[\frac{\partial\mathcal{L} }{\partial\left(\partial_\mu \phi_A \right) } \phi_A - \phi_A^* \frac{\partial\mathcal{L} }{\partial\left(\partial_\mu \phi_A^* \right) } \right]
\end{aligned}
$$

诺特定理中的连续方程

$$
\partial_\mu \theta_{i\cdots k\mu} = 0
$$

在这里表现为：

$$
\partial_\mu \theta_\mu = 0
$$

定义四维电流密度 $j_\mu $：

$$
j_\mu
\equiv -e \theta_\mu
=-\mathrm{i} e \left[\frac{\partial\mathcal{L} }{\partial\left(\partial_\mu\phi_A \right) } \phi_A - \phi_A^*\frac{\partial\mathcal{L} }{\partial\left(\partial_\mu\phi_A^* \right) }  \right],\quad
j_\mu = \left(\vec{j} , \mathrm{i}\rho \right)
$$

则 $j_\mu $ 满足连续方程：

$$
\partial_\mu j_\mu = 0,\quad
\nabla\cdot\vec{j} + \frac{\partial \rho }{\partial t } 
=0
$$

诺特定理中的守恒张量

$$
T_{i\cdots k}
=\frac{1 }{\mathrm{i} } \int \theta_{i\cdots k4}\mathrm{d}V
$$

在这里表现为电荷 $Q $：

$$
Q
=\frac{1 }{\mathrm{i} } \int j_4 \mathrm{d}V
=\int \rho\mathrm{d}V,\quad
\frac{\mathrm{d}Q }{\mathrm{d}t } = 0
$$

# 7 规范场理论

## 规范变换

设 $H $ 是一个以 $\alpha $ 为参数的 $r $ 阶李群，$S(\alpha) $ 是 $H $ 的不可约线性表示，某广义场函数 $\phi $ 为 $S(\alpha) $ 的变换对象。

若 $\alpha $ 是局域的，则变换

$$
\phi'(x)
\equiv S(\alpha(x)) \phi(x)
$$

称为广义场函数 $\phi $ 对于李群 $H $ 的规范变换。

由于 $S(\alpha(x)) $ 是局域的，因此

$$
\partial_\mu \phi'(x)
\ne S(\alpha(x)) \partial_\mu \phi(x)
$$

这就无法保证拉格朗日函数的规范不变性。

假设存在一种微商运算 $\nabla_\mu $，使得 $\nabla_\mu \phi(x) $ 是规范协变量，即：

$$
\nabla'_\mu \phi'(x)
=S(x) \nabla_\mu \phi(x)
$$

设：

$$
\nabla_\mu \phi
=\partial_\mu \phi - \omega_\mu \phi
$$

可以证明，$\omega_\mu $ 的变换规律为：

$$
\omega_\mu'
=S \omega_\mu S^{-1} + \left(\partial_\mu S \right)S^{-1}
$$

矩阵函数 $\omega_\mu $ 称为联络矩阵。

## 伴随协变张量 $F_{\mu\nu} $ 及其性质

设 $F_{\mu\nu} $ 满足

$$
\left(\nabla_\mu \nabla_\nu - \nabla_\nu \nabla_\mu \right)\phi(x)
=-F_{\mu\nu} \phi(x)
$$

可证明

$$
F_{\mu\nu}
=\partial_\mu \omega_\nu - \partial_\nu \omega_\mu - \left[\omega_\mu , \omega_\nu \right]
$$

其变换规律为

$$
F'_{\mu\nu}
=S F_{\mu\nu} S^{-1}
$$

这说明 $F_{\mu\nu} $ 是规范协变量，且

$$
\mathrm{Tr}\left(F'_{\mu\nu} F'_{\mu\nu} \right)
=\mathrm{Tr}\left(F_{\mu\nu} F_{\mu\nu} \right)
$$

是规范不变量，同时也是 Lorentz 不变量，可用于构造规范场的拉格朗日函数。

# 8 自由场二次量子化

## 量子场论基本假设

（1）二次量子化状态由态矢量（状态幅度）$\Psi $ 或 $\Ket{\Psi } $ 完全描述

（2）

$$
\Braket{\alpha_1\Phi_1+\alpha_2\Phi_2|\Psi}
=\alpha_1^*\braket{\Phi_1|\Psi} + \alpha_2^*\braket{\Phi_2|\Psi}
$$

$$
\braket{\Phi|\Psi}^\dag
=\braket{\Psi|\Phi}
$$

$$
\braket{\Psi|\Psi} \geqslant 0
$$

（3）所有经典场的物理量都对应于 Hilbert 空间的一个线性厄米算符 $\hat{T}_{\mu\cdots\nu\lambda} $，其观测平均值为：

$$
\Braket{\Psi|\hat{T}_{\mu\cdots \nu\lambda}|\Psi}
$$

（4）二次量子化中的态矢量 $\Psi $ 满足薛定谔方程

$$
\mathrm{i}\partial_t \Psi
=\hat{H} \Psi
$$

$\hat{H} $ 是经典场的能量算符。

## 二次量子化 SOP

（1）将场函数进行 Fourier 分解（三维积分分解、四维积分分解或级数分解），把场函数算符化为场算符。场算符可表达为无数产生、消灭算符的线性叠加；

（2）把经典场的哈密顿量算符化为哈密顿算符，哈密顿算符可由产生、消灭算符表达。利用海森堡方程求解哈密顿算符与产生、消灭算符对易关系；

（3）给出对易关系和粒子数表象；

（4）给出各种物理量算符的二次量子化结果。

## 实标量场量子化

### 场算符 Fourier 积分分解

$$
\hat{\phi}(x)
=\hat{\phi}^{(+)}(x) + \hat{\phi}^{(-)}(x)
$$

$$
\hat{\phi}^{(+)}(x)
=\left(\frac{1 }{2\pi }  \right)^{3/2} \int \mathrm{e}^{-\mathrm{i}k x}\frac{1 }{\sqrt{2\varepsilon_{\vec{k}}} } \hat{a}^{(+)}\left(\vec{k} \right) \mathrm{d}^3\vec{k}
$$

$$
\hat{\phi}^{(-)}(x)
=\left(\frac{1 }{2\pi }  \right)^{3/2} \int \mathrm{e}^{+\mathrm{i}k x}\frac{1 }{\sqrt{2\varepsilon_{\vec{k}}} } \hat{a}^{(-)}\left(\vec{k} \right) \mathrm{d}^3\vec{k}
$$

### 哈密顿算符表达式

实标量场的能量密度：

$$
W
=\frac{1 }{2 } \left[\left(\nabla\phi \right)\cdot\left(\nabla\phi \right) + \left(\partial_t \phi \right)\left(\partial_t \phi \right) + m^2 \phi^2 \right]
$$

哈密顿算符：


$$
\hat{H}
=\frac{1 }{2 } \int\left[\left(\nabla\hat{\phi} \right)^2 + \left(\frac{\partial\hat{\phi} }{\partial t }  \right)^2 + m^2 \hat{\phi}^2 \right] \mathrm{d}V
$$

最终可得连续形式哈密顿算符：

$$
\boxed{
\begin{aligned}
\hat{H}
=\frac{1 }{2 } \int \varepsilon_{\vec{k}} \left\{\hat{a}^{(+)}\left(\vec{k} \right) , \hat{a}^{(-)}\left(\vec{k} \right) \right\} \mathrm{d}^3\vec{k}
\end{aligned}
}
$$

利用连续形式和分立形式的关系

$$
\int \mathrm{d}^3\vec{k} \cdots
=\frac{(2\pi)^3 }{V } \sum_{\vec{k}} \cdots,\quad
\hat{a}^{(\pm)}\left(\vec{k} \right)
=\frac{\sqrt{V} }{(2\pi)^{3/2} } \hat{a}_{\vec{k}}^{(\pm)}
$$

可得分立形式哈密顿算符：

$$
\boxed{
\hat{H}
=\frac{1 }{2 } \sum_{\vec{k}} \varepsilon_{\vec{k}} \left\{\hat{a}^{(+)}_{\vec{k}} , \hat{a}^{(-)}_{\vec{k}} \right\}
}
$$

### 动量算符表达式

$$
\vec{p}
=-\int \nabla\phi \frac{\partial\phi }{\partial t } \mathrm{d}^3\vec{x}
$$

$$
\hat{\vec{p}}
=-\int \left[\nabla \hat{\phi}^{(+)}\left(\vec{k} \right) + \nabla \hat{\phi}^{(-)}\left(\vec{k} \right) \right]\left[\partial_t \hat{\phi}^{(+)}\left(\vec{k} \right) + \partial_t \hat{\phi}^{(-)}\left(\vec{k} \right) \right] \mathrm{d}^3\vec{r}
$$

最终可得连续形式动量算符：

$$
\boxed{
\hat{\vec{p}}
=\frac{1 }{2 } \int \vec{k} \left\{\hat{a}^{(+)}\left(\vec{k} \right) , \hat{a}^{(-)}\left(\vec{k} \right) \right\} \mathrm{d}^3\vec{k}
}
$$

利用连续形式和分立形式的关系

$$
\int \mathrm{d}^3\vec{k} \cdots
=\frac{(2\pi)^3 }{V } \sum_{\vec{k}} \cdots,\quad
\hat{a}^{(\pm)}\left(\vec{k} \right)
=\frac{\sqrt{V} }{(2\pi)^{3/2} } \hat{a}_{\vec{k}}^{(\pm)}
$$

可得分立形式动量算符：

$$
\boxed{
\hat{\vec{p}}
=\frac{1 }{2 } \sum_{\vec{k}} \vec{k} \left\{\hat{a}^{(+)}_{\vec{k}} , \hat{a}^{(-)}_{\vec{k}} \right\}
}
$$

### 实标量场二次量子化算符的性质

把场算符代入海森堡方程，可得哈密顿算符与产生、消灭算符对易关系：

$$
\left[\hat{H} , \hat{a}^{(-)}\left(\vec{k} \right) \right]
=-\varepsilon_k\hat{a}^{(-)}\left(\vec{k} \right)
$$

$$
\left[\hat{H} , \hat{a}^{(+)}\left(\vec{k} \right) \right]
=\varepsilon_k\hat{a}^{(+)}\left(\vec{k} \right)
$$

把哈密顿算符用产生、消灭算符表示，代入上面两方程，就得到连续形式产生、消灭算符对易关系：

$$
\left[\hat{a}^{(-)}\left(\vec{k}' \right) , \hat{a}^{(+)}\left(\vec{k} \right) \right]
=\delta\left(\vec{k}-\vec{k}' \right)
$$

$$
\left[\hat{a}^{(-)}\left(\vec{k} \right) , \hat{a}^{(-)}\left(\vec{k}' \right) \right]
=\left[\hat{a}^{(+)}\left(\vec{k} \right) , \hat{a}^{(+)}\left(\vec{k}' \right) \right]
=0
$$

利用连续形式和分立形式的关系

$$
\int \mathrm{d}^3\vec{k} \cdots
=\frac{(2\pi)^3 }{V } \sum_{\vec{k}} \cdots,\quad
\hat{a}^{(\pm)}\left(\vec{k} \right)
=\frac{\sqrt{V} }{(2\pi)^{3/2} } \hat{a}_{\vec{k}}^{(\pm)}
$$

可得分立形式产生、消灭算符对易关系：

$$
\left[\hat{a}^{(-)}_{\vec{k}} , \hat{a}^{(+)}_{\vec{k}'} \right]
=\delta_{\vec{k},\vec{k}'}
$$

$$
\left[\hat{a}^{(-)}_{\vec{k}} , \hat{a}^{(-)}_{\vec{k}'} \right]
=\left[\hat{a}^{(+)}_{\vec{k}} , \hat{a}^{(+)}_{\vec{k}'} \right]
=0
$$

此外，计算可得：

$$
\left[\hat{\vec{p}} , \hat{a}^{(+)}\left(\vec{k} \right) \right]
=\vec{k} \hat{a}^{(+)}\left(\vec{k} \right)
$$

$$
\left[\hat{\vec{p}} , \hat{a}^{(-)}\left(\vec{k} \right) \right]
=-\vec{k} \hat{a}^{(-)}\left(\vec{k} \right)
$$

$$
\left[\hat{H} , \hat{\vec{p}} \right]
=0
$$

$\hat{H} , \hat{\vec{p}} $ 二者有共同本征函数，设为 $\Psi_p $

$$
\hat{H} \left(\hat{a}^{(\pm)}\left(\vec{k} \right) \Psi_p \right)
=\left(E \pm \varepsilon_{\vec{k}} \right) \left(\hat{a}^{(\pm)}\left(\vec{k} \right) \Psi_p \right)
$$

$$
\hat{\vec{p}} \left(\hat{a}^{(\pm)}\left(\vec{k} \right) \Psi_p \right)
=\left(\vec{p} \pm \vec{k} \right) \left(\hat{a}^{(\pm)}\left(\vec{k} \right) \Psi_p \right)
$$

$\hat{a}^{(\pm)}\left(\vec{k} \right) \Psi_p $ 仍是能量算符和动量算符的本征态。

$\hat{a}^{(+)}\left(\vec{k} \right) \Psi_p $ 是产生了一个动量为 $\vec{k} $，能量为 $\varepsilon_{\vec{k}} $ 的自由粒子的态。

$\hat{a}^{(-)}\left(\vec{k} \right) \Psi_p $ 是消灭了一个动量为 $\vec{k} $，能量为 $\varepsilon_{\vec{k}} $ 的自由粒子的态。

$\hat{a}^{(\pm)}\left(\vec{k} \right) $ 是标量粒子的产生、消灭算符。

### 场论中的真空态

场论中的真空态，一般指每种场算符的量子化状态中能量最低的那个量子态，通常记为 $\Ket{0 } .$

### 归一化的态矢量

$$
\ket{n_{\vec{k}}}
\equiv \frac{1 }{\sqrt{n_{\vec{k}} !} } \left(\hat{a}^{(+)}_{\vec{k}} \right)^{n_{\vec{k}}} \ket{0}
$$

上式描述的状态是 $n_{\vec{k}} $ 个动量为 $\vec{k} $ 的自由粒子。

$$
\left(\prod_i \frac{1 }{\sqrt{n_{\vec{k}_i}!} } \left(\hat{a}_{\vec{k}_i}^{(+)} \right)^{n_{\vec{k}_i}} \right) \Ket{0 }
$$

上式描述的状态是动量为 $\vec{k}_i $ 的粒子有 $n_{k_i} $ 个的状态。

### 粒子数算符

用 $\ket{n_{\vec{k}}} $ 表示有 $n_{\vec{k}} $ 个动量为 $\vec{k} $ 的粒子的态：

$$
\ket{n_{\vec{k}}}
\equiv \frac{1 }{\sqrt{n_{\vec{k}} !} } \left(\hat{a}^{(+)}_{\vec{k}} \right)^{n_{\vec{k}}} \ket{0}
$$

容易得到：

$$
\hat{a}^{(-)}_{\vec{k}} \hat{a}^{(+)}_{\vec{k}} \ket{n_{\vec{k}} - 1}
=n_{\vec{k}}\ket{n_{\vec{k}} - 1}
$$

$$
\hat{a}^{(+)}_{\vec{k}} \ket{n_{\vec{k}}}
=\sqrt{n_{\vec{k}}+1} \ket{n_{\vec{k}}+1}
$$

$$
\hat{a}^{(-)}_{\vec{k}} \ket{n_{\vec{k}}}
=\sqrt{n_{\vec{k}}} \ket{n_{\vec{k}}-1}
$$

$$
\hat{a}^{(+)}_{\vec{k}} \hat{a}^{(-)}_{\vec{k}} \ket{n_{\vec{k}}}
=n_{\vec{k}} \ket{n_{\vec{k}}}
$$

定义粒子数算符 $\hat{N}_{\vec{k}} $：

$$
\hat{N}_{\vec{k}}
\equiv \hat{a}^{(+)}_{\vec{k}} \hat{a}^{(-)}_{\vec{k}}
$$

满足：

$$
\hat{N}_{\vec{k}}^\dag
=\hat{N}_{\vec{k}}
$$

$$
\hat{N}_{\vec{k}}\ket{n_{\vec{k}}}
=n_{\vec{k}}\ket{n_{\vec{k}}}
$$

$\ket{n_{\vec{k}}} $ 是粒子数算符的本征态，也是 $\hat{\vec{p}},\hat{H} $ 的共同本征态。

### 粒子数表象

$\left\{\ket{n_{\vec{k}}} ,\forall \vec{k}, n_{\vec{k}}=0,1,2,\cdots \right\} $ 组成一组正交完备基。自由标量场的任意量子态可由 $\ket{n_{k_i}} $ 展开，这种描述称为**粒子数表象**。

### $\hat{\vec{p}},\hat{H} $ 粒子数算符表达式

$$
\left\{\hat{a}^{(+)}_{\vec{k}} , \hat{a}^{(+)}_{\vec{k}} \right\}
=2\hat{N}_{\vec{k}} + 1
$$

$$
\hat{H}
=\frac{1 }{2 } \sum_{\vec{k}} \varepsilon_{\vec{k}} \left\{\hat{a}^{(+)}_{\vec{k}} , \hat{a}^{(-)}_{\vec{k}} \right\}
$$

$$
\hat{\vec{p}}
=\frac{1 }{2 } \sum_{\vec{k}} \vec{k} \left\{\hat{a}^{(+)}_{\vec{k}} , \hat{a}^{(-)}_{\vec{k}} \right\}
$$

$$
\hat{H}
=\sum_{\vec{k}} \varepsilon_{\vec{k}} \left(\hat{N}_k + \frac{1 }{2 }  \right)
$$

$$
\hat{\vec{p}}
=\sum_{\vec{k}} \vec{k} \left(\hat{N}_k + \frac{1 }{2 }  \right)
$$

## 矢量场量子化

$$
\hat{A}_\mu(x)
=\hat{A}^{(+)}_\mu(x) + \hat{A}^{(-)}_\mu(x)
$$

傅里叶积分展开

$$
\hat{A}^{(+)}_\mu(x)
=\frac{1 }{\left(2\pi \right)^{3/2} } \int\limits_{k_0=\varepsilon_{\vec{k}}} \mathrm{e}^{-\mathrm{i}kx} \frac{1 }{\sqrt{2\varepsilon_{\vec{k}}} } \hat{C}_\mu^{(+)}\left(\vec{k} \right)\mathrm{d}^3\vec{k}
$$

$$
\hat{A}^{(-)}_\mu(x)
=\frac{1 }{\left(2\pi \right)^{3/2} } \int\limits_{k_0=\varepsilon_{\vec{k}}} \mathrm{e}^{+\mathrm{i}kx} \frac{1 }{\sqrt{2\varepsilon_{\vec{k}}} } \hat{C}_\mu^{(-)}\left(\vec{k} \right)\mathrm{d}^3\vec{k}
$$

分立形式

$$
\hat{A}^{(+)}_\mu(x)
=\frac{1 }{\sqrt{V} } \sum_{\vec{k}} \frac{1 }{\sqrt{2\varepsilon_{\vec{k}}} } \hat{C}_{\mu\vec{k}}^{(+)} \mathrm{e}^{-\mathrm{i}kx}\bigg|_{k_0=\varepsilon_{\vec{k}}}
$$

$$
\hat{A}^{(-)}_\mu(x)
=\frac{1 }{\sqrt{V} } \sum_{\vec{k}} \frac{1 }{\sqrt{2\varepsilon_{\vec{k}}} } \hat{C}_{\mu\vec{k}}^{(-)} \mathrm{e}^{-\mathrm{i}kx}\bigg|_{k_0=\varepsilon_{\vec{k}}}
$$

其中

$$
\varepsilon_{\vec{k}}
\equiv \sqrt{\vec{k}^2}
=\left|\vec{k} \right|
$$

### 算符化

$$
\hat{H}
=\frac{1 }{2 } \int \left[\left(\nabla\hat{A}_\mu \right)\cdot\left(\nabla\hat{A}_\mu \right) + \left(\partial_t\hat{A}_\mu \right)\left(\partial_t\hat{A}_\mu \right) \right]\mathrm{d}^3\vec{x}
$$

$$
\hat{\vec{p}}
=-\int \left(\nabla\hat{A}_\mu \right)\left(\partial_t \hat{A}_\mu \right)\mathrm{d}^3\vec{x}
$$

$$
\hat{\vec{S}}
=\int \hat{\vec{A}}\times\partial_t \hat{\vec{A}} \mathrm{d}^3\vec{x}
$$

最终可得

$$
\hat{H}
=\frac{1 }{2 } \int \varepsilon_{\vec{k}} \left[\hat{C}_\mu^{(+)}\left(\vec{k} \right) \hat{C}_\mu^{(-)}\left(\vec{k} \right) + \hat{C}_\mu^{(-)}\left(\vec{k} \right) \hat{C}_\mu^{(+)}\left(\vec{k} \right) \right] \mathrm{d}^3\vec{k}
$$

$$
\hat{\vec{p}}
=\frac{1 }{2 } \int \vec{k} \left[\hat{C}_\mu^{(+)}\left(\vec{k} \right) \hat{C}_\mu^{(-)}\left(\vec{k} \right) + \hat{C}_\mu^{(-)}\left(\vec{k} \right) \hat{C}_\mu^{(+)}\left(\vec{k} \right) \right] \mathrm{d}^3\vec{k}
$$

$$
\hat{\vec{S}}
=\frac{\mathrm{i} }{2 } \int \left[\hat{\vec{C}}^{(-)}\left(\vec{k} \right) \times \hat{\vec{C}}^{(+)}\left(\vec{k} \right) - \hat{\vec{C}}^{(+)}\left(\vec{k} \right) \times \hat{\vec{C}}^{(-)}\left(\vec{k} \right) \right] \mathrm{d}^3\vec{k}
$$

其中

$$
\hat{\vec{C}}^{(\pm)}\left(\vec{k} \right)
\equiv \left(\hat{C}_1^{(\pm)} , \hat{C}_2^{(\pm)} , \hat{C}_3^{(\pm)} \right)
$$

分立形式

$$
\hat{H}
=\frac{1 }{2 } \sum_{\vec{k}} \varepsilon_{\vec{k}} \left[\hat{C}_{\mu\vec{k}}^{(+)} \hat{C}_{\mu\vec{k}}^{(-)} + \hat{C}_{\mu\vec{k}}^{(-)} \hat{C}_{\mu\vec{k}}^{(+)} \right]
$$

$$
\hat{\vec{p}}
=\frac{1 }{2 } \sum_{\vec{k}} \vec{k} \left[\hat{C}_{\mu\vec{k}}^{(+)} \hat{C}_{\mu\vec{k}}^{(-)} + \hat{C}_{\mu\vec{k}}^{(-)} \hat{C}_{\mu\vec{k}}^{(+)} \right]
$$

$$
\hat{\vec{\vec{S}}}
=\frac{\mathrm{i} }{2 } \sum_{\vec{k}} \vec{k} \left[\hat{\vec{C}}_{\vec{k}}^{(-)} \times \hat{\vec{C}}_{\vec{k}}^{(+)} - \hat{\vec{C}}_{\vec{k}}^{(+)} \times \hat{\vec{C}}_{\vec{k}}^{(-)}\right]
$$

### 算符对易关系

由海森堡运动方程可得

$$
\left[\hat{H} , \hat{C}^{(\pm)}_{\mu}\left(\vec{k} \right) \right]
=\pm \varepsilon_{\vec{k}} \hat{C}^{(\pm)}_{\mu}\left(\vec{k} \right)
$$

$$
\left[\hat{C}_\mu^{(-)}\left(\vec{k} \right) , \hat{C}_\nu^{(+)}\left(\vec{k}' \right) \right]
=\delta_{\mu\nu} \delta\left(\vec{k}-\vec{k}' \right)
$$

$$
\left[\hat{C}_\mu^{(\pm) }\left(\vec{k} \right) , \hat{C}_\nu^{(\pm)}\left(\vec{k}' \right) \right]
=0
$$

分立情况

$$
\left[\hat{C}_{\mu\vec{k}}^{(-)} , \hat{C}_{\nu\vec{k}'}^{(+)} \right]
=\delta_{\mu\nu} \delta_{\vec{k},\vec{k}'}
$$

$$
\left[\hat{C}_{\mu\vec{k}}^{(\pm)} , \hat{C}_{\nu\vec{k}'}^{(\pm)} \right]
=0
$$

以及

$$
\left[\hat{\vec{p}} , \hat{C}_\nu^{(\pm)}\left(\vec{k} \right) \right]
=\pm\vec{k} \hat{C}_\nu^{(\pm)}\left(\vec{k} \right)
$$

$$
\left[\hat{\vec{p}} , \hat{H} \right]
=0
$$

### 光子极化坐标中物理量算符表达式

设四维闵氏时空基矢为 $\vec{e}_i,\vec{e}_4 $，基矢用下标标记。

设光子动量为 $\vec{k} $，设光子极化坐标的空间基矢为

$$
\vec{e}^3 = \vec{k}/\left|\vec{k} \right|,\quad
\mathrm{such} \quad \vec{e}^1,\vec{e}^2 \quad \mathrm{that} \quad \vec{e}^3 = \vec{e}^1 \times \vec{e}^2,\quad
\vec{e}^4 = \vec{e}_4
$$

在原来在坐标下，矢量场写为 $\hat{A}_\mu $；在极化坐标下，矢量场写为 $\hat{A}^\mu .$

极化坐标下 $\hat{A}^1,\hat{A}^2 $ 称为横分量，$\hat{A}^3 $ 称为纵分量，$\hat{A}^4 $ 称为时间分量。



### 场量子化后的 Lorenz 规范条件

> Lorenz 和 Lorentz 是两个人。。。

经典电动力学中，广义 Lorenz 规范条件为：

$$
\partial_\mu A_\mu = 0
$$

把场算符化，并把 $\hat{A}_\mu $ 的 Fourier 展式代入上式，就得到场量子化后的 Lorenz 规范条件：

$$
k_\mu \hat{C}_\mu^{(\pm)}\left(\vec{k} \right)
=0
$$

在光子极化坐标中写为：

$$
k^\mu \hat{C}^{(\pm)\mu}\left(\vec{k} \right)
=0
$$

又在光子极化坐标中，光子四维动量为

$$
\left(k^\mu \right)
=\left(0,0,\left|\vec{k} \right| , \mathrm{i} \left|\vec{k} \right| \right)
$$

因此有：

$$
\left|\vec{k} \right| \hat{C}^{(\pm)3}\left(\vec{k} \right) + \mathrm{i}\left|\vec{k} \right| \hat{C}^{(\pm)4}\left(\vec{k} \right)
=0
$$

即：

$$
\boxed{
\hat{C}^{(\pm)4}\left(\vec{k} \right)
=\mathrm{i} \hat{C}^{(\pm)3}\left(\vec{k} \right)
}
$$

把上式代入光子极化坐标下算符的 Fourier 展式

$$
\hat{H}
=\frac{1 }{2 } \int \varepsilon_{\vec{k}} \left[\hat{C}^{(+)\mu}\left(\vec{k} \right) \hat{C}^{(-)\mu}\left(\vec{k} \right) + \hat{C}^{(-)\mu}\left(\vec{k} \right) \hat{C}^{(+)\mu}\left(\vec{k} \right) \right] \mathrm{d}^3\vec{k}
$$

$$
\hat{\vec{p}}
=\frac{1 }{2 } \int \vec{k} \left[\hat{C}^{(+)\mu}\left(\vec{k} \right) \hat{C}^{(-)\mu}\left(\vec{k} \right) + \hat{C}^{(-)\mu}\left(\vec{k} \right) \hat{C}^{(+)\mu}\left(\vec{k} \right) \right] \mathrm{d}^3\vec{k}
$$

$$
\hat{\vec{S}}
=\frac{\mathrm{i} }{2 } \int \left[\hat{\vec{C}}^{(-)}\left(\vec{k} \right) \times \hat{\vec{C}}^{(+)}\left(\vec{k} \right) - \hat{\vec{C}}^{(+)}\left(\vec{k} \right) \times \hat{\vec{C}}^{(-)}\left(\vec{k} \right) \right] \mathrm{d}^3\vec{k}
$$

容易发现，$\mu=3 $ 和 $\mu=4 $ 项抵消。因此光子极化坐标下，只有横分量 $1,2 $ 有贡献。此时有

$$
\hat{H}
=\frac{1 }{2 } \int \varepsilon_{\vec{k}} \sum_{i=1}^{2} \left\{\hat{C}^{(+)i}\left(\vec{k} \right) , \hat{C}^{(-)i}\left(\vec{k} \right) \right\} \mathrm{d}^3\vec{k}
$$

$$
\hat{\vec{p}}
=\frac{1 }{2 } \int \vec{k} \sum_{i=1}^{2} \left\{\hat{C}^{(+)i}\left(\vec{k} \right) , \hat{C}^{(-)i}\left(\vec{k} \right) \right\} \mathrm{d}^3\vec{k}
$$

自旋的表达式为：

$$
\hat{S}^3
=\mathrm{i}\left[\hat{C}^{(-)1}\left(\vec{k} \right) \hat{C}^{(-)2}\left(\vec{k} \right) - \hat{C}^{(+)1}\left(\vec{k} \right) \hat{C}^{(-)2}\left(\vec{k} \right) \right]
$$

### 粒子数表象

> 怎么写着写着记号还变了呢！这必须坚持使用 R 语言啊！

横光子粒子数算符：

$$
\hat{N}^1_{\vec{k}}
\equiv \hat{C}_{\vec{k}}^{(+)1} \hat{C}_{\vec{k}}^{(-)1},\quad
\hat{N}^2_{\vec{k}}
\equiv \hat{C}_{\vec{k}}^{(+)2} \hat{C}_{\vec{k}}^{(-)2}
$$

利用

$$
\left[\hat{C}^{(-)\mu}\left(\vec{k} \right) , \hat{C}^{(+)\nu}\left(\vec{k}' \right) \right]
=\delta^{\mu\nu}\delta\left(\vec{k}-\vec{k}' \right)
$$

$$
\left[\hat{C}_{\vec{k}}^{(-)\mu} , \hat{C}_{\vec{k}}^{(+)\nu} \right]
=\delta^{\mu\nu} \delta_{\vec{k},\vec{k}'}
$$

可得

$$
\hat{H}
=\sum_{\vec{k}} \varepsilon_{\vec{k}} \left(\hat{N}^1_{\vec{k}} + \hat{N}^2_{\vec{k}} + 1 \right)
$$

$$
\hat{\vec{p}}
=\sum_{\vec{k}} \vec{k} \left(\hat{N}^1_{\vec{k}} + \hat{N}^2_{\vec{k}} + 1 \right)
$$

$$
\hat{S}^3
=\sum_{\vec{k}} \left(\hat{N}^1_{\vec{k}} - \hat{N}^2_{\vec{k}} \right)
$$

$\hat{N}^1_{\vec{k}} $ 为自旋 $S^3=+1 $，动量为 $\vec{k} $ 的光子数算符。

$\hat{N}^2_{\vec{k}} $ 为自旋 $S^3=-1 $，动量为 $\vec{k} $ 的光子数算符。

光子极化坐标中 $\hat{C}_{\vec{k}}^\nu $ 的 $\nu $ 表征自旋，$\nu=3,4 $ 无贡献。

## 旋量场量子化

## 3.7 旋量场量子化

$$
\hat{\psi}(x)
=\hat{\psi}^{(+)}(x) + \hat{\psi}^{(-)}(x)
$$

$$
\hat{\psi}^{(+)}(x)
=\left(\frac{1 }{2\pi } \right)^{3/2} \int\limits_{p_0=E_{\vec{p}}} \mathrm{e}^{-\mathrm{i}p x} \hat{b}_i^{(+)}(\vec{p}) v_i(\vec{p}) \mathrm{d}^3\vec{p}
$$

$$
\hat{\psi}^{(-)}(x)
=\left(\frac{1 }{2\pi }  \right)^{3/2} \int\limits_{p_0=E_{\vec{p}}} \mathrm{e}^{+\mathrm{i}p x} \hat{a}_i^{(-)}(\vec{p}) u_i(\vec{p}) \mathrm{d}^3\vec{p}
$$

$$
\hat{\bar{\psi}}(x)
=\hat{\psi}^\dag \gamma_4,\quad
\hat{\bar{\psi}}(x)
=\hat{\bar{\psi}}^{(+)}(x) + \hat{\bar{\psi}}^{(-)}(x)
$$

$$
\hat{\bar{\psi}}^{(+)}(x)
=\left(\frac{1 }{2\pi } \right)^{3/2} \int\limits_{p_0=E_{\vec{p}}} \mathrm{e}^{-\mathrm{i}p x} \hat{a}_i^{(+)}(\vec{p}) \bar{u}_i(\vec{p}) \mathrm{d}^3\vec{p}
$$

$$
\hat{\bar{\psi}}^{(-)}(x)
=\left(\frac{1 }{2\pi }  \right)^{3/2} \int\limits_{p_0=E_{\vec{p}}} \mathrm{e}^{+\mathrm{i}p x} \hat{b}_i^{(-)}(\vec{p}) \bar{v}_i(\vec{p}) \mathrm{d}^3\vec{p}
$$

定义

$$
\hat{a}_{\vec{p} i}^{(-)}
=\frac{\left(2\pi \right)^{3/2} }{\sqrt{V} } \hat{a}_i^{(-)}(\vec{p}),\quad
\hat{b}_{\vec{p} i}^{(-)}
=\frac{\left(2\pi \right)^{3/2} }{\sqrt{V} } \hat{b}_i^{(-)}(\vec{p})
$$

则有分立表示

$$
\hat{\psi}(x)
=\frac{1 }{\sqrt{V} } \sum_{\vec{p}} \left[ \mathrm{e}^{\mathrm{i}p x} \hat{a}_{\vec{p}i}^{(-)} u_i(\vec{p}) + \mathrm{e}^{-\mathrm{i}p x}\hat{b}_{\vec{p} i}^{(+)} v_i(\vec{p}) \right]
$$

$$
\hat{\bar{\psi}}(x)
=\frac{1 }{\sqrt{V} } \sum_{\vec{p}} \left[ \mathrm{e}^{\mathrm{i}p x} \hat{b}_{\vec{p}i}^{(-)} \bar{v}_i(\vec{p}) + \mathrm{e}^{-\mathrm{i}p x}\hat{a}_{\vec{p} i}^{(+)} \bar{u}_i(\vec{p}) \right]
$$

### 旋量场的二次量子化

$$
\hat{H}
=\int E_{\vec{p}} \left[\hat{a}^{(+)}_i\left(\vec{p} \right) \hat{a}^{(-)}_i\left(\vec{p} \right) - \hat{b}^{(-)}_i\left(\vec{p} \right) \hat{b}^{(+)}_i\left(\vec{p} \right) \right] \mathrm{d}^3\vec{p}
$$

$$
\hat{\vec{p}}
=\int \vec{p} \left[\hat{a}^{(+)}_i\left(\vec{p} \right) \hat{a}^{(-)}_i\left(\vec{p} \right) - \hat{b}^{(-)}_i\left(\vec{p} \right) \hat{b}^{(+)}_i\left(\vec{p} \right) \right] \mathrm{d}^3\vec{p}
$$

$$
\hat{Q}
=-e \int \left[\hat{a}^{(+)}_i\left(\vec{p} \right) \hat{a}^{(-)}_i\left(\vec{p} \right) + \hat{b}^{(-)}_i\left(\vec{p} \right) \hat{b}^{(+)}_i\left(\vec{p} \right) \right] \mathrm{d}^3\vec{p}
$$

$$
\hat{S}_n
=\frac{1 }{2 } \int \left\{\left[\hat{a}_1^{(+)}(\vec{p}) \hat{a}_1^{(-)}(\vec{p}) - \hat{a}_2^{(+)}(\vec{p}) \hat{a}_2^{(-)}(\vec{p}) \right] - \left[\hat{b}_1^{(-)}(\vec{p}) \hat{b}_1^{(+)}(\vec{p}) - \hat{b}_2^{(-)}(\vec{p}) \hat{b}_2^{(+)}(\vec{p}) \right] \right\} \mathrm{d}^3\vec{p}
$$

### 动量表象海森堡方程

$$
\left[\hat{H} , \hat{b}_i^{(\pm)}(\vec{p}) \right]
=\pm E_{\vec{p}} \hat{b}_i^{(\pm)}(\vec{p})
$$

$$
\left[\hat{H} , \hat{a}_i^{(\pm)}(\vec{p}) \right]
=\pm E_{\vec{p}} \hat{a}_i^{(\pm)}(\vec{p})
$$

### 产生、消灭算符反对易关系

$$
\left\{\hat{a}_i^{(-)}\left(\vec{p} \right) , \hat{a}_j^{(+)}\left(\vec{p}' \right) \right\}
=\delta_{ij} \delta\left(\vec{p}-\vec{p}' \right)
$$

$$
\left\{\hat{b}_i^{(-)}\left(\vec{p} \right) , \hat{b}_j^{(+)}\left(\vec{p}' \right) \right\}
=\delta_{ij} \delta\left(\vec{p}-\vec{p}' \right)
$$

其余反对易关系为零。

分立形式

$$
\left\{\hat{a}_{\vec{p}i}^{(-)} , \hat{a}_{\vec{p}'j}^{(+)} \right\}
=\delta_{ij} \delta_{\vec{p},\vec{p}'}
$$

$$
\left\{\hat{b}_{\vec{p}i}^{(-)} , \hat{b}_{\vec{p}'j}^{(+)} \right\}
=\delta_{ij}\delta_{\vec{p},\vec{p'}}
$$

对于自由旋量场 $\hat{\psi},\hat{\bar{\psi}} $，算符 $\hat{H},\hat{\vec{p}},\hat{Q},\hat{S}_n $ 具有共同本征态。

$\hat{a}_1^{(+)}(\vec{p}) $ 代表产生一个 $\vec{p},E_{\vec{p}},-e $，自旋 $1/2 $ 的粒子；

$\hat{a}_1^{(-)}(\vec{p}) $ 代表消灭一个 $\vec{p},E_{\vec{p}},-e $，自旋 $1/2 $ 的粒子；

$\hat{a}_2^{(+)}(\vec{p}) $ 代表产生一个 $\vec{p},E_{\vec{p}},-e $，自旋 $-1/2 $ 的粒子；

$\hat{a}_2^{(-)}(\vec{p}) $ 代表消灭一个 $\vec{p},E_{\vec{p}},-e $，自旋 $-1/2 $ 的粒子；

$\hat{b}_1^{(+)}(\vec{p}) $ 代表产生一个 $\vec{p},E_{\vec{p}},+e $，自旋 $1/2 $ 的反粒子；

$\hat{b}_1^{(-)}(\vec{p}) $ 代表消灭一个 $\vec{p},E_{\vec{p}},+e $，自旋 $1/2 $ 的反粒子；

$\hat{b}_2^{(+)}(\vec{p}) $ 代表产生一个 $\vec{p},E_{\vec{p}},+e $，自旋 $-1/2 $ 的反粒子；

$\hat{b}_2^{(-)}(\vec{p}) $ 代表消灭一个 $\vec{p},E_{\vec{p}},+e $，自旋 $-1/2 $ 的反粒子。

总之：$a,b $ 区分正反粒子（电荷），数字 $1,2 $ 区别自旋 $1/2,-1/2 $，$(\pm) $ 区分产生、消灭。

### 粒子数表象

$$
\hat{N}_{\vec{p}i}^{(+)}
\equiv \hat{a}_{\vec{p}i}^{(+)} \hat{a}_{\vec{p}i}^{(-)},\quad 正粒子
$$

$$
\hat{N}_{\vec{p}i}^{(-)}
\equiv \hat{b}_{\vec{p}i}^{(+)} \hat{b}_{\vec{p}i}^{(-)},\quad 反粒子
$$

以上 $i $ 不求和。

$$
\left(\hat{N}_{\vec{p}i}^{(\pm)} \right)^2
=\hat{N}_{\vec{p}i}^{(\pm)}
$$

因此 $\hat{N}_{\vec{p}i}^{(\pm)} $ 的本征值取 $0,1 $，这对应于费米子要遵循的 Pauli 不相容原理。

$$
\hat{H}
=\sum_{\vec{p}} \sum_{i=1}^{2} E_{\vec{p}} \left(\hat{N}_{\vec{p}i}^{(+)} + \hat{N}_{\vec{p}i}^{(-)} - 1 \right)
$$

$$
\hat{\vec{p}}
=\sum_{\vec{p}} \sum_{i=1}^{2} \vec{p} \left(\hat{N}_{\vec{p}i}^{(+)} + \hat{N}_{\vec{p}i}^{(-)} - 1 \right)
$$

$$
Q
=\sum_{\vec{p}} \sum_{i=1}^{2} (-e) \left(\hat{N}_{\vec{p}i}^{(+)} + \hat{N}_{\vec{p}i}^{(-)} - 1 \right)
$$

$$
\hat{S}_n
=\frac{1 }{2 } \sum_{\vec{p}} \left(\hat{N}_{\vec{p}1}^{(+)} + \hat{N}_{\vec{p}1}^{(-)} - \hat{N}_{\vec{p}2}^{(+)} - \hat{N}_{\vec{p}2}^{(-)} \right)
$$

$\hat{N}_{\vec{p}1}^{(+)} $ 代表电荷 $-e $，自旋 $1/2 $，动量 $\vec{p} $ 的正粒子数算符；

$\hat{N}_{\vec{p}2}^{(+)} $ 代表电荷 $-e $，自旋 $-1/2 $，动量 $\vec{p} $ 的正粒子数算符；

$\hat{N}_{\vec{p}1}^{(-)} $ 代表电荷 $+e $，自旋 $1/2 $，动量 $\vec{p} $ 的反粒子数算符；

$\hat{N}_{\vec{p}2}^{(-)} $ 代表电荷 $+e $，自旋 $-1/2 $，动量 $\vec{p} $ 的反粒子数算符。

# Green 函数、Feynman 函数、N 乘积、P 乘积、T 乘积与耦合

## 场方程的 Green 函数和 Feynman 函数

### 线性偏微分方程的 Green 函数

$$
\hat{L}(x)
=a_0 + a_\mu\partial_\mu + a_{\mu\nu}\partial_\mu\partial_\nu + \cdots
$$

齐次线性微分方程：

$$
\hat{L}(x) \phi(x)
=0
$$

非齐次线性微分方程：

$$
\hat{L}(x) \phi(x)
=-\rho(x)
$$

形式特解：

$$
\phi(x)
=-\hat{L}^{-1}(x) \rho(x)
$$

$\delta $ 函数筛选性质：

$$
\rho(x)
=\int \rho(x') \delta(x-x')\mathrm{d}x'
$$

特解

$$
\phi(x)
=-\int \rho(x') \hat{L}^{-1}(x) \delta(x-x')\mathrm{d}x'
$$

Green 函数：

$$
G(x-x')
\equiv -\hat{L}^{-1}(x) \delta(x-x')
$$

$$
\hat{L}(x) G(x-x')
=-\delta(x-x')
$$

$$
\phi(x)
=\int \rho(x') G(x-x')\mathrm{d}x'
$$

$\hat{L}(x) $ 对 $\mathrm{e}^{\mathrm{i}k(x-x')} $ 的作用：

$$
\hat{L}(x) \mathrm{e}^{\mathrm{i}k(x-x')} 
=\left(a_0 + \mathrm{i}a_\mu k_\mu + \mathrm{i}^2 a_{\mu\nu} k_\mu k_\nu + \cdots \right)\mathrm{e}^{\mathrm{i}k(x-x')}
$$

则

$$
\hat{L}^{-1}(x) \mathrm{e}^{\mathrm{i}k(x-x')}
=\frac{\mathrm{e}^{\mathrm{i}k(x-x')} }{a_0 + \mathrm{i}a_\mu k_\mu + \mathrm{i}^2 a_{\mu\nu} k_\mu k_\nu + \cdots } 
$$

于是：

$$
\begin{aligned}
G(x-x')
&\equiv -\hat{L}^{-1}(x) \delta(x-x') \\
&=-\hat{L}^{-1}(x) \left(\frac{1 }{2\pi }  \right)^n \int \mathrm{e}^{\mathrm{i}k(x-x')} \mathrm{d}^n k \\
&=\frac{-1 }{\left(2\pi \right)^n } \int \mathrm{d}^n k \frac{\mathrm{e}^{\mathrm{i}k(x-x')} }{a_0 + \mathrm{i}a_\mu k_\mu + \mathrm{i}^2 a_{\mu\nu} k_\mu k_\nu + \cdots } 
\end{aligned}
$$

即对于方程 $\hat{L}(x) \phi(x)=-\rho(x) $ 来说，算符 $\hat{L}(x)=a_0 + a_\mu\partial_\mu + a_{\mu\nu}\partial_\mu\partial_\nu + \cdots $ 对应的 Green 函数 $G(x-x') $ 由下式计算：

$$
\boxed{
G(x-x')
\equiv -\hat{L}^{-1}(x) \delta(x-x')
=\frac{-1 }{\left(2\pi \right)^n } \int \mathrm{d}^n k \frac{\mathrm{e}^{\mathrm{i}k(x-x')} }{a_0 + \mathrm{i}a_\mu k_\mu + \mathrm{i}^2 a_{\mu\nu} k_\mu k_\nu + \cdots } 
}
$$

### 各种场的 Green 函数

#### 标量场

非齐次方程

$$
\left(\square - m^2 \right)\phi(x)
=-\rho(x)
$$

$$
\hat{L}
=-m^2 + \partial_\mu \partial_\mu
$$

$$
a_0 = -m^2,\quad
a_\mu = 0,\quad
a_{\mu\nu} = \delta_{\mu\nu},\quad
a_{\mu\nu\lambda} = \cdots = 0
$$

Green 函数：

$$
\begin{aligned}
\Delta^G(x-x')
&=\frac{-1 }{\left(2\pi \right)^n } \int \mathrm{d}^n k \frac{\mathrm{e}^{\mathrm{i}k(x-x')} }{a_0 + \mathrm{i}a_\mu k_\mu + \mathrm{i}^2 a_{\mu\nu} k_\mu k_\nu + \cdots } \\
&=\frac{-1 }{\left(2\pi \right)^4 } \int \mathrm{d}^4 k \frac{\mathrm{e}^{\mathrm{i}k(x-x')} }{-m^2 + \mathrm{i}^2 \delta_{\mu\nu} k_\mu k_\nu } \\
&=\frac{1 }{\left(2\pi \right)^4 } \int \mathrm{d}^4 k \frac{\mathrm{e}^{\mathrm{i}k(x-x')} }{k^2 + m^2 } \\
&\equiv \left(\frac{1 }{2\pi }  \right)^4 \int \Delta^G(k) \mathrm{e}^{\mathrm{i}k(x-x')} \mathrm{d}^4 k
\end{aligned}
$$

其中，

$$
\Delta^G(k)
\equiv \frac{1 }{k^2 + m^2 } 
$$

#### 矢量场

非齐次方程：

$$
\square A_\mu = -j_\mu(x)
$$

$$
\hat{L}
=\partial_\mu \partial_\mu
$$

$$
a_0 = 0,\quad
a_\mu = 0,\quad
a_{\mu\nu} = \delta_{\mu\nu},\quad
a_{\mu\nu\lambda} = \cdots = 0
$$

Green 函数：

$$
\begin{aligned}
D^G(x-x')
&=\frac{-1 }{\left(2\pi \right)^n } \int \mathrm{d}^n k \frac{\mathrm{e}^{\mathrm{i}k(x-x')} }{a_0 + \mathrm{i}a_\mu k_\mu + \mathrm{i}^2 a_{\mu\nu} k_\mu k_\nu + \cdots } \\
&=\frac{-1 }{\left(2\pi \right)^4 } \int \mathrm{d}^4 k \frac{\mathrm{e}^{\mathrm{i}k(x-x')} }{ \mathrm{i}^2 \delta_{\mu\nu} k_\mu k_\nu } \\
&=\frac{1 }{\left(2\pi \right)^4 } \int \mathrm{d}^4 k \frac{\mathrm{e}^{\mathrm{i}k(x-x')} }{k^2} \\
&\equiv \left(\frac{1 }{2\pi }  \right)^4 \int D^G(k) \mathrm{e}^{\mathrm{i}k(x-x')} \mathrm{d}^4 k
\end{aligned}
$$

其中，

$$
D^G(k)
\equiv \frac{1 }{k^2 } 
$$

#### 旋量场

非齐次方程

$$
\left(\gamma_\mu \partial_\mu + m \right)\psi(x)
=-\rho(x)
$$

$$
\hat{L}
=m + \gamma_\mu \partial_\mu
$$

$$
a_0 = m,\quad
a_\mu = \gamma_\mu,\quad
a_{\mu\nu} = \cdots = 0
$$

Green 函数：

$$
\begin{aligned}
S^G(x-x')
&=\frac{-1 }{\left(2\pi \right)^n } \int \mathrm{d}^n p \frac{\mathrm{e}^{\mathrm{i}p(x-x')} }{a_0 + \mathrm{i}a_\mu p_\mu + \mathrm{i}^2 a_{\mu\nu} p_\mu p_\nu + \cdots } \\
&=\frac{-1 }{\left(2\pi \right)^4 } \int \mathrm{d}^4 p \frac{\mathrm{e}^{\mathrm{i}p(x-x')} }{m + \mathrm{i}\gamma_\mu p_\mu } \\
&=\frac{-1 }{\left(2\pi \right)^4 } \int \mathrm{d}^4 p \mathrm{e}^{\mathrm{i}p(x-x')} \frac{m-\mathrm{i}\gamma_\mu p_\mu }{m^2 + \left(\gamma_\mu p_\mu \right)^2 } \\
&=\frac{1 }{\left(2\pi \right)^4 } \int \frac{\mathrm{i}\gamma_\mu p_\mu - m }{ \left(\gamma_\mu p_\mu \right)^2 + m^2 } \mathrm{e}^{\mathrm{i}p(x-x')} \mathrm{d}^4 p \\
&\equiv \left(\frac{1 }{2\pi }  \right)^4 \int S^G(p) \mathrm{e}^{\mathrm{i}p(x-x')} \mathrm{d}^4 p
\end{aligned}
$$

其中，

$$
S^G(k)
\equiv \frac{\mathrm{i}\hat{p} - m }{\hat{p}^2 + m^2 } 
=\frac{\mathrm{i}\gamma_\mu p_\mu - m }{ \left(\gamma_\mu p_\mu \right)^2 + m^2 },\quad
\hat{p}
\equiv \gamma_\mu p_\mu
$$

### Feynman（Green函数）与对易函数的关系

Green 函数 $G(x-x') $ 乘 $-2\mathrm{i} $ 就得到 Feynman 函数 $F(x-x') $：

$$
F(x-x')
=-2\mathrm{i} G(x-x')
$$

$$
\Delta^F(x)
=-2\mathrm{i} \Delta^G(x)
$$

$$
D^F(x)
=-2\mathrm{i} D^G(x)
$$

$$
S^F(x)
=-2\mathrm{i} S^G(x)
$$

Green 函数定义：

$$
G(x-x')
\equiv -\hat{L}(x) \delta(x-x')
$$

$$
\hat{L}(x) G(x)
=-\delta(x)
$$

$$
\hat{L}(x) \left[-2\mathrm{i}G(x) \right]
=2\mathrm{i}\delta(x)
$$

$$
\hat{L}(x) F(x)
=2\mathrm{i}\delta(x)
$$

标量场、矢量场和旋量场的 Feynman 函数分别满足：

$$
\left(\square - m^2 \right)\Delta^F(x) = 2\mathrm{i}\delta(x)
$$

$$
\square D^F(x) = 2\mathrm{i}\delta(x)
$$

$$
\left(\gamma_\mu \partial_\mu + m \right) S^F(x) = 2\mathrm{i}\delta(x)
$$

$$
\Delta^F(x)
=\frac{2\mathrm{i} }{\left(2\pi \right)^4 } \int \mathrm{d}^3\vec{k} \mathrm{e}^{\mathrm{i}\vec{k}\cdot\vec{x}}\int\mathrm{d}k_0 \frac{\mathrm{e}^{-\mathrm{i}k_0 t} }{k_0^2-\varepsilon_{\vec{k}}^2 } 
$$

定义反常积分：

$$
I\left(\vec{k} \right)
\equiv \int \frac{\mathrm{e}^{-\mathrm{i}k_0 t} }{k_0^2-\varepsilon_{\vec{k}}^2 } \mathrm{d}k_0
$$

当 $t>0 $，

$$
\Delta^F(x)
=\frac{1 }{\left(2\pi \right)^2 } \int \mathrm{d}^3\vec{k} \mathrm{e}^{\mathrm{i}\vec{k}\cdot\vec{x}} \frac{\mathrm{e}^{-\mathrm{i}\varepsilon_{\vec{k}} t} }{\varepsilon_{\vec{k}} } 
$$

当 $t<0 $，

$$
\Delta^F(x)
=\frac{1 }{\left(2\pi \right)^2 } \int \mathrm{d}^3\vec{k} \mathrm{e}^{\mathrm{i}\vec{k}\cdot\vec{x}} \frac{\mathrm{e}^{\mathrm{i}\varepsilon_{\vec{k}} t} }{\varepsilon_{\vec{k}} } 
$$

当 $t>0 $，

$$
\Delta^F(x)
=\Delta^{(1)}(x) + \mathrm{i}\Delta(x)
$$

当 $t<0 $，

$$
\Delta^F(x)
=\Delta^{(1)}(x) - \mathrm{i}\Delta(x)
$$

合写为

$$
\Delta^F(x)
=\Delta^{(1)}(x) + \mathrm{i}\varepsilon(t)\Delta(x)
$$

$$
\Delta^F(x)
=2\mathrm{i}\left[\Delta^{(-)}(x)\theta_+(t) - \Delta^{(+)}(x)\theta_-(t) \right]
$$

$$
D^F(x)
=2\mathrm{i}\left[D^{(-)}(x)\theta_+(t) - D^{(+)}(x)\theta_-(t) \right]
$$

$$
S^F(x)
=2\mathrm{i}\left[S^{(-)}(x)\theta_+(t) - S^{(-)}(x)\theta_-(t) \right]
$$

## $N $ 乘积，$P $ 乘积和 $T $ 乘积与耦合

用 $\hat{U}_\alpha^{(\pm)}(x) $ 代表广义场算符

用 $\hat{\bar{U}}_\alpha^{(\pm)}(x) $ 代表广义场算符的共轭

用 $Q_{\alpha\beta}^{(\pm)}(x) $ 代表 $\Delta^{(\pm)}(x),D^{(\pm)}(x)\delta_{\alpha\beta},-S^{(\pm)}_{\alpha\beta}(x) $

用 $Q_{\alpha\beta}(x) $ 代表 $\Delta(x),D(x)\delta_{\alpha\beta}(x),-S_{\alpha\beta}(x) $

用 $Q^{(1)}_{\alpha\beta}(x) $ 代表 $\Delta^{(1)}(x),D^{(1)}(x)\delta_{\alpha\beta},-S^{(1)}_{\alpha\beta}(x) $

用 $Q^F_{\alpha\beta} $ 代表 $\Delta^F(x),D^F(x)\delta_{\alpha\beta},-S^F_{\alpha\beta}(x) $

### $N $ 乘积

产生算符在左，消灭算符在右，再乘系数 $(-1)^p $，其中 $p $ 为原序到 $N $ 乘积顺序所需的费米算符置换次数。

$$
N\left[\hat{U}^{(-)}(x) \hat{U}^{(+)}(x') \right]
=\mp \hat{U}^{(+)}(x') \hat{U}^{(-)}(x)
$$

当 $\hat{U} $ 为费米子场算符时取负号，当 $\hat{U} $ 为玻色子场算符时取正号。

例如：

$$
N\left[\hat{\phi}^{(-)}(x) \hat{\phi}^{(+)}(x') \right]
=\hat{\phi}^{(+)}(x') \hat{\phi}^{(-)}(x)
$$

$$
N\left[\hat{\psi}^{(-)}(x) \hat{\psi}^{(+)}(x') \right]
=-\hat{\psi}^{(+)}(x') \hat{\psi}^{(-)}(x)
$$

$N $ 乘积又称为正规乘积，记为 $:~~ : $

场算符 $N $ 乘积的真空期望值为零，即：

$$
\Braket{0|N\left[\hat{U}(x_1) \cdots \hat{U}(x_n) \right]|0}
=0
$$

若把量子场论中的算符定义为相应经典物理算符化后再取 $N $ 乘积，则可消除所有真空发散项。

### $P $ 乘积

$P $ 乘积又称为编时乘积，算符经其作用后时间 $t $ 小的排在右边，$t $ 大的排在左边。

$$
P\left[\hat{U}\left(x^1 \right) \hat{U}\left(x^2 \right) \cdots \hat{U}\left(x^n \right) \right]
=\hat{U}\left(x^{i_1} \right) \hat{U}\left(x^{i_2} \right) \cdots \hat{U}\left(x^{i_n} \right)
$$

其中 $t^{i_1}\geqslant t^{i_2}\geqslant \cdots t^{i_n} .$

### $T $ 乘积

$T $ 乘积的定义为：

$$
T\left[\hat{U}\left(x^1 \right) \cdots \hat{U}\left(x^n \right) \right]
=(-1)^p P\left[\hat{U}\left(x^1 \right) \hat{U}\left(x^2 \right) \cdots \hat{U}\left(x^n \right) \right]
$$

其中，$p $ 为费米置换次数（玻色场函数的置换不计入 $p $）。

### 收缩（耦合）

定义 $T $ 乘积与 $N $ 乘积之差为收缩（耦合）：

$$
\dot{\hat{U}}_\alpha\left(x^1 \right) \dot{\hat{\bar{U}}}_\beta\left(x^2 \right)
\equiv (T-N) \left[\hat{U}_\alpha\left(x^1 \right) \hat{\bar{U}}\left(x^2 \right) \right]
$$

当 $t^1>t^2 $，

$$
\dot{\hat{U}}_\alpha\left(x^1 \right)\dot{\hat{\bar{U}}}_\beta\left(x^2 \right)
=\left(T-N \right)\left[\hat{U}_\alpha\left(x^1 \right)\hat{\bar{U}}_\beta\left(x^2 \right) \right]
=+\mathrm{i}Q_{\alpha\beta}^{(-)}\left(x^1-x^2 \right),\quad
t^1>t^2
$$

当 $t^1<t^2 $，

$$
\dot{\hat{U}}_\alpha\left(x^1 \right)\dot{\hat{\bar{U}}}_\beta\left(x^2 \right)
=\left(T-N \right)\left[\hat{U}_\alpha\left(x^1 \right)\hat{\bar{U}}_\beta\left(x^2 \right) \right]
=-\mathrm{i}Q_{\alpha\beta}^{(+)}\left(x^1-x^2 \right),\quad
t^1<t^2
$$

统一写为：

$$
\dot{\hat{U}}_\alpha\left(x^1 \right)\dot{\hat{\bar{U}}}_\beta\left(x^2 \right)
=\frac{1 }{2 } Q_{\alpha\beta}^F\left(x^1-x^2 \right)
$$


# 场的相互作用与 S 矩阵

## 场的相互作用拉格朗日函数

在场的相互作用情况下，总拉格朗日函数 $\mathcal{L} $ 应是自由场拉格朗日函数 $\mathcal{L}_0 $ 与相互作用拉格朗日函数 $\mathcal{L}_i $ 之和：

$$
\hat{\mathcal{L}}
=\hat{\mathcal{L}}_0 + \hat{\mathcal{L}_i}
$$

场的相互作用拉格朗日函数 $\mathcal{L}_i $ 也必须是 Lorentz 变换的不变量。因此有场的相互作用的拉格朗日函数广义形式：

$$
\hat{\mathcal{L}}_i
=g \hat{T}^1_{\mu\nu\cdots\lambda}(x) \hat{T}^2_{\mu\nu\cdots\lambda}(x)
$$

常数 $g $ 称为作用常数，代表两种场相互作用的大小。

$\hat{T}^1_{\mu\nu\cdots\lambda}(x) $ 和 $\hat{T}^2_{\mu\nu\cdots\lambda}(x) $ 为两种不同的场函数组成的同级张量。

### 玻色场与费米场的相互作用

#### 标量场与旋量场的作用

$$
?\hat{\bar{\psi}}(x) \hat{\psi}(x) \hat{\phi}(x),\quad
? \hat{\bar{\psi}}(x) \gamma_\mu \hat{\psi}(x) \partial_\mu \hat{\phi}(x)
$$

#### 赝标量场与旋量场的作用

赝标耦合：

$$
? \hat{\bar{\psi}}(x) \gamma_5 \hat{\psi}(x) \hat{\tilde{\phi}}(x)
$$

赝矢耦合：

$$
? \hat{\bar{\psi}}(x) \gamma_5 \gamma_\mu \hat{\psi}(x) \partial_\mu \hat{\tilde{\phi}}(x)
$$

#### 矢量场与旋量场的作用

$$
? \hat{\bar{\psi}}(x) \gamma_\mu \hat{\psi}(x) \hat{A}_\mu(x),\quad
? \hat{\bar{\psi}}(x) \gamma_\mu \gamma_\nu \hat{\psi}(x) \hat{F}_{\mu\nu}
$$

#### $\pi $ 介子与核子的作用

$$
? \hat{\bar{\psi}}(x) \gamma_5 \hat{\psi}(x) \hat{\tilde{\phi}}(x),\quad
? \hat{\bar{\psi}}(x) \gamma_5 \gamma_\mu \hat{\psi}(x) \partial_\mu \hat{\tilde{\phi}}(x)
$$

$$
\hat{\mathcal{L}}_i
=\mathrm{i} G \hat{\bar{\psi}}(x) \gamma_5 \hat{\psi}(x) \hat{\tilde{\phi}}(x) + \mathrm{i} \frac{g }{\mu } \hat{\bar{\psi}}(x) \gamma_5 \gamma_\mu \hat{\psi}(x) \partial_\mu \hat{\tilde{\phi}}(x)
$$

$$
\mu
=\frac{1 }{\lambda } 
=\frac{m c }{h } 
=\frac{m c }{2 \pi \hbar } 
$$

#### 电子与光子的作用

$$
? \hat{\bar{\psi}}(x) \gamma_\mu \hat{\psi}(x) \hat{A}_\mu(x)
$$

$$
\hat{\mathcal{L}}_i
=\mathrm{i} e \hat{\bar{\psi}}(x) \gamma_\mu \hat{\psi}(x) \hat{A}_\mu(x)
$$

#### 费米场与费米场的相互作用

核子 $\beta^- $ 衰变：

$$
n \to p + e^- + \tilde{\nu}_e
$$

$\mu^{\pm} $ 轻子衰变：
$$
\mu^+ \to e^+ + \nu_e + \tilde{\nu}_e,\quad
\mu^- \to e^- + \tilde{\nu}_e + \nu_\mu
$$

五种形式：标量耦合、赝标耦合、矢量耦合、赝矢耦合、张量耦合，合写为：

$$
\hat{\mathcal{L}}_i
=\sum_{i=1}^{5} C_i \left[\hat{\bar{\psi}}(x) O_i \hat{\psi}(x) \right]\left[\hat{\bar{\psi}}(x) O_i \hat{\psi}(x) \right]
$$

Gellmann & Feynman：

$$
\hat{\mathcal{L}}_i
=\frac{C }{\sqrt{2} } \left[\hat{\bar{\psi}}(x) \gamma_\mu(1+\gamma_5) \hat{\psi}(x) \right] \left[\hat{\bar{\psi}}(x) \gamma_\mu(1+\gamma_5) \hat{\psi}(x) \right]
$$

### 玻色场与玻色场的相互作用

$\pi $ 介子与$\pi $ 介子的相互作用：

$$
? \hat{\tilde{\phi}}(x) \hat{\tilde{\phi}}(x) \hat{\tilde{\phi}}(x) \hat{\tilde{\phi}}(x)
$$

光子与 $\pi $ 介子的相互作用：

$$
? \left[\partial_\mu \hat{\tilde{\phi}}^*(x) \hat{\tilde{\phi}}(x) - \hat{\tilde{\phi}}^*(x) \partial_\mu \hat{\tilde{\phi}}(x) \right] \hat{A}_\mu(x)
$$

### 场的作用常数问题

场的作用常数也称为荷。

#### 强作用常数

$$
\frac{G_\pi^2 }{\hbar c } \sim 15
$$

#### 中作用常数

$$
\frac{G_K^2 }{\hbar c } \sim 1
$$

#### 电磁作用常数

$$
\frac{e^2 }{\hbar c } 
=\frac{1 }{137 } 
$$

#### 弱作用常数

$$
G
=\frac{10^{-5} }{M_p^2 } 
$$

## 场的相互作用运动方程荷相互作用哈密顿量

场相互作用情况下总拉格朗日函数：

$$
\hat{\mathcal{L}}
=\hat{\mathcal{L}}_0 + \hat{\mathcal{L}}_i
$$

把 $\hat{\mathcal{L}} $ 代入 E-L 方程就得到场的运动方程：

$$
\frac{\partial \hat{\mathcal{L}} }{\partial \hat{\phi}_A(x) } - \partial_\mu \frac{\partial \hat{\mathcal{L}} }{\partial \left(\partial_\mu \hat{\phi}_A(x) \right) } 
=0
$$

### 电子与电磁场作用的运动方程

总拉格朗日函数：

$$
\begin{aligned}
\mathcal{L}
&=-\frac{1 }{4 } F_{\mu\nu} F_{\mu\nu} \\
&- \frac{1 }{2 } \left[\hat{\bar{\psi}}(x) \gamma_\mu \partial_\mu \hat{\psi}(x) - \partial_\mu \hat{\bar{\psi}}(x) \gamma_\mu \hat{\psi}(x) \right] - m \hat{\bar{\psi}}(x) \hat{\psi}(x) \\
&+ \mathrm{i} e \hat{\bar{\psi}}(x) \gamma_\mu \hat{\psi}(x) \hat{A}_\mu(x)
\end{aligned}
$$

对 $\hat{A}_\mu(x),\hat{\bar{\psi}}(x),\hat{\psi}(x) $ 变分，得场方程：

$$
\partial_\nu F_{\mu\nu} = \mathrm{i} e\hat{\bar{\psi}}(x) \gamma_\mu \hat{\psi}(x)
$$

$$
\left(\gamma_\mu \partial_\mu + m \right) \hat{\psi}(x)
=\mathrm{i} e \hat{A}_\mu(x) \gamma_\mu \hat{\psi}(x)
$$

$$
\partial_\mu(x) \hat{\bar{\psi}} \gamma_\mu - m \hat{\bar{\psi}}(x)
=-\mathrm{i} e \hat{A}_\mu(x) \hat{\bar{\psi}}(x) \gamma_\mu 
$$

四维电流矢量：

$$
j_\mu
=\mathrm{i} e \hat{\bar{\psi}}(x) \gamma_\mu \hat{\psi}(x)
$$

### 核子与介子场作用的运动方程

总拉格朗日函数：

$$
\begin{aligned}
\hat{\mathcal{L}}
&=-\frac{1 }{2 } \left[\partial_\mu \hat{\tilde{\phi}}(x) \partial_\mu \hat{\tilde{\phi}}(x) + m_\pi^2 \hat{\tilde{\phi}}^2(x) \right] \\
&- \frac{1 }{2 } \left[\hat{\bar{\psi}}(x) \gamma_\mu \partial_\mu \hat{\psi}(x) - \partial_\mu \hat{\bar{\psi}}(x) \gamma_\mu \hat{\psi}(x) \right] - M \hat{\bar{\psi}}(x) \hat{\psi}(x) \\
&+ \mathrm{i} G \hat{\bar{\psi}}(x) \gamma_5 \hat{\psi}(x) \hat{\tilde{\phi}}(x)
\end{aligned}
$$

变分得场方程：

$$
\left(\square - m_\pi^2 \right) \hat{\tilde{\phi}}(x)
=-\mathrm{i} G \hat{\bar{\psi}}(x) \gamma_5 \hat{\psi}(x)
$$

$$
\left(\gamma_\mu \partial_\mu + M \right) \hat{\psi}(x)
=\mathrm{i} G \gamma_5 \hat{\psi}(x) \hat{\tilde{\phi}}(x)
$$

$$
\partial_\mu \hat{\bar{\psi}}(x) \gamma_\mu - M \hat{\bar{\psi}}(x)
=-\mathrm{i} G \hat{\tilde{\phi}}(x) \hat{\bar{\psi}}(x) \gamma_5
$$

### 场相互作用的哈密顿量

场的相互作用情况下的能量-动量张量：

$$
\hat{T}_{\mu\nu}
=\hat{\mathcal{L}} \delta_{\mu\nu} - \frac{\partial \hat{\mathcal{L}} }{\partial \left(\partial_\nu \hat{\phi}_A(x) \right) } \partial_\mu \hat{\phi}_A(x)
$$

由于

$$
\hat{\mathcal{L}}
=\hat{\mathcal{L}}_0 + \hat{\mathcal{L}}_i
$$

于是能量-动量张量也可以分为自由部分 $\hat{T}_{\mu\nu}^{(0)} $ 与相互作用部分 $\hat{T}_{\mu\nu}^{(i)} $：

$$
\hat{T}_{\mu\nu}^{(0)}
=\hat{\mathcal{L}}_0 \delta_{\mu\nu} - \frac{\partial \hat{\mathcal{L}}_0 }{\partial \left(\partial_\nu \hat{\phi}_A(x) \right) } \partial_\mu \hat{\phi}_A(x)
$$

$$
\hat{T}_{\mu\nu}^{(i)}
=\hat{\mathcal{L}}_i \delta_{\mu\nu} - \frac{\partial \hat{\mathcal{L}}_i }{\partial \left(\partial_\nu \hat{\phi}_A(x) \right) } \partial_\mu \hat{\phi}_A(x)
$$

$$
\hat{T}_{\mu\nu}
=\hat{T}^{(0)}_{\mu\nu} + \hat{T}^{(i)}_{\mu\nu}
$$

能量密度也同样可分为自由部分 $\hat{\mathcal{H}}_0 $ 和相互作用部分 $\hat{\mathcal{H}}_i $：

$$
\hat{\mathcal{H}}_0
=-\hat{T}^{(0)}_{44}
$$

$$
\hat{\mathcal{H}}_i
=-\hat{T}^{(i)}_{44}
=-\hat{\mathcal{L}}_i + \frac{\partial \hat{\mathcal{L}}_i }{\partial \partial_t \hat{\phi}_A(x) } \partial_t \hat{\phi}_A(x)
$$

$$
\hat{\mathcal{H}}
=-\hat{T}_{44}
=-\hat{T}^{(0)}_{44} -\hat{T}^{(i)}_{44}
=\hat{\mathcal{H}}_0 + \hat{\mathcal{H}}_i
$$

哈密顿算符 $\hat{H} $ 也可分为自由场哈密顿算符 $\hat{H}_0 $ 和场相互作用哈密顿算符 $\hat{H}_i $：

$$
\hat{H}_0
=\int \hat{\mathcal{H}}_0 \mathrm{d}V
$$

$$
\hat{H}_i
=\int \hat{\mathcal{H}}_i \mathrm{d}V
$$

$$
\hat{H}
=\hat{H}_0 + \hat{H}_i
=\int \hat{\mathcal{H}}_0 \mathrm{d}V + \int \hat{\mathcal{H}}_i \mathrm{d}V
$$

#### 电子旋量场与电磁场相互作用哈密顿算符

总拉格朗日函数：

$$
\begin{aligned}
\mathcal{L}
&=-\frac{1 }{4 } F_{\mu\nu} F_{\mu\nu} \\
&- \frac{1 }{2 } \left[\hat{\bar{\psi}}(x) \gamma_\mu \partial_\mu \hat{\psi}(x) - \partial_\mu \hat{\bar{\psi}}(x) \gamma_\mu \hat{\psi}(x) \right] - m \hat{\bar{\psi}}(x) \hat{\psi}(x) \\
&+ \mathrm{i} e \hat{\bar{\psi}}(x) \gamma_\mu \hat{\psi}(x) \hat{A}_\mu(x)
\end{aligned}
$$

相互作用拉格朗日函数：

$$
\hat{\mathcal{L}}_i
=\mathrm{i} e \hat{\bar{\psi}}(x) \gamma_\mu \hat{\psi}(x) \hat{A}_\mu(x)
$$

相互作用能量-动量张量：

$$
\begin{aligned}
\hat{T}_{\mu\nu}^{(i)}
&=\hat{\mathcal{L}}_i \delta_{\mu\nu} - \frac{\partial \hat{\mathcal{L}}_i }{\partial \left(\partial_\nu \hat{\phi}_A(x) \right) } \partial_\mu \hat{\phi}_A(x) \\
&=\delta_{\mu\nu} \mathrm{i} e \hat{\bar{\psi}}(x) \gamma_\alpha \hat{\psi}(x) \hat{A}_\alpha(x)
\end{aligned}
$$

电子旋量场与电磁场相互作用哈密顿算符：

$$
\begin{aligned}
\hat{H}_i
&=-\int \hat{T}^{(i)}_{44} \mathrm{d}V \\
&=-\mathrm{i} e \int \hat{\bar{\psi}}(x) \gamma_\mu \hat{\psi}(x) \hat{A}_\mu(x) \mathrm{d}V
\end{aligned}
$$

#### 核子旋量场与介子场相互作用哈密顿算符

总拉格朗日函数：

$$
\begin{aligned}
\hat{\mathcal{L}}
&=-\frac{1 }{2 } \left[\partial_\mu \hat{\tilde{\phi}}(x) \partial_\mu \hat{\tilde{\phi}}(x) + m_\pi^2 \hat{\tilde{\phi}}^2(x) \right] \\
&- \frac{1 }{2 } \left[\hat{\bar{\psi}}(x) \gamma_\mu \partial_\mu \hat{\psi}(x) - \partial_\mu \hat{\bar{\psi}}(x) \gamma_\mu \hat{\psi}(x) \right] - M \hat{\bar{\psi}}(x) \hat{\psi}(x) \\
&+ \mathrm{i} G \hat{\bar{\psi}}(x) \gamma_5 \hat{\psi}(x) \hat{\tilde{\phi}}(x)
\end{aligned}
$$

相互作用拉格朗日函数：

$$
\hat{\mathcal{L}}_i
=\mathrm{i} G \hat{\bar{\psi}}(x) \gamma_5 \hat{\psi}(x) \hat{\tilde{\phi}}(x)
$$

相互作用能量-动量张量：

$$
\begin{aligned}
\hat{T}_{\mu\nu}^{(i)}
&=\hat{\mathcal{L}}_i \delta_{\mu\nu} - \frac{\partial \hat{\mathcal{L}}_i }{\partial \left(\partial_\nu \hat{\phi}_A(x) \right) } \partial_\mu \hat{\phi}_A(x) \\
&=\delta_{\mu\nu} \mathrm{i} G \hat{\bar{\psi}}(x) \gamma_5 \hat{\psi}(x) \hat{\tilde{\phi}}(x)
\end{aligned}
$$

核子旋量场与介子场相互作用哈密顿算符

$$
\begin{aligned}
\hat{H}_i
&=-\int \hat{T}^{(i)}_{44} \mathrm{d}V \\
&=-\mathrm{i} G \int \hat{\bar{\psi}}(x) \gamma_5 \hat{\psi}(x) \hat{\tilde{\phi}}(x) \mathrm{d}V \\
\end{aligned}
$$

## 相互作用绘景

### 薛定谔绘景

薛定谔绘景中，场相互作用情况下，状态幅度 $\Psi_S $ 随时间的变化规律：

$$
\mathrm{i} \frac{\partial }{\partial t } \Psi_S
=\hat{H}_S \Psi_S
$$

$$
\hat{H}_S
=\hat{H}_{S0} + \hat{H}_{Si}
$$

其中，$\hat{H}_{S0} $ 为薛定谔绘景中自由场哈密顿算符，$\hat{H}_{Si} $ 为场相互作用哈密顿算符。$\hat{H}_{S0} $ 和 $\hat{H}_{Si} $ 都不随时间改变。

### 海森堡绘景

$$
\Psi_H
=\Psi_S(0),\quad
\hat{F}_H
\equiv \mathrm{e}^{\mathrm{i}\hat{H}_S t} \hat{F}_S \mathrm{e}^{-\mathrm{i}\hat{H}_S t}
$$

$$
\hat{H}_H
=\hat{H}_S
\equiv \hat{H}
$$

$$
\frac{\partial \Psi_H }{\partial t } = 0
$$

$$
\frac{\partial \hat{F}_H }{\partial t } = \mathrm{i}\left[\hat{H} , \hat{F}_H \right]
$$

### 相互作用绘景

$$
\Phi_I(t)
\equiv \mathrm{e}^{\mathrm{i}\hat{H}_{S0}t} \Psi_S
$$

相互作用绘景中的算符 $\hat{F}_I $ 定义为：

$$
\hat{F}_I(t)
\equiv \mathrm{e}^{\mathrm{i} \hat{H}_{S0} t} \hat{F}_S \mathrm{e}^{-\mathrm{i} \hat{H}_{S0} t}
$$

$$
\hat{H}_{I}
=\mathrm{e}^{\mathrm{i} \hat{H}_{S0} t} \left(\hat{H}_{S0} + \hat{H}_{Si} \right) \mathrm{e}^{-\mathrm{i} \hat{H}_{S0} t}
=\mathrm{e}^{\mathrm{i} \hat{H}_{S0} t} \hat{H}_{Si}  \mathrm{e}^{-\mathrm{i} \hat{H}_{S0} t}
\equiv \hat{H}_{Ii}
$$

$\Phi_I(t) $ 随时间变化规律为：

$$
\begin{aligned}
\mathrm{i}\frac{\partial \Phi_I(t) }{\partial t } 
&=\mathrm{i} \frac{\partial \hat{V}(t) }{\partial t } \Psi_S(t) + \mathrm{i} \hat{V}(t) \frac{\partial \Psi_S(t) }{\partial t } \\
&=- \hat{V}(t) \hat{H}_{S0} \Psi_S(t) + \hat{V}(t) \hat{H}_{S0} \Psi_S(t) + \hat{V}(t) \hat{H}_{Si} \Psi_S(t) \\
&=\hat{V}(t) \hat{H}_{Si} \Psi_S(t) \\
&=\hat{V}(t) \hat{H}_{Si} \hat{V}^\dag(t) \hat{V}(t) \Psi_S(t) \\
&\equiv \hat{H}_{Ii}(t) \Phi_I(t)
\end{aligned}
$$

$$
\mathrm{i} \frac{\partial  }{\partial t } \Phi_I(t)
=\hat{H}_{Ii}(t) \Phi_I(t)
$$

$\hat{F}_I(t) $ 随时间的变化规律为：

$$
\frac{\partial \hat{F}_I }{\partial t } 
=\mathrm{i}\left[\hat{H}_{I0}(t) , \hat{F}_I(t) \right]
$$

薛定谔绘景：

$$
\boxed{
\hat{H}_S
=\hat{H}_{S0} + \hat{H}_{Si}
}
$$

$$
\boxed{
\mathrm{i}\frac{\partial }{\partial t } \Psi_S
=\hat{H}_S \Psi_S,\quad
\frac{\mathrm{d}\hat{F}_S }{\mathrm{d}t } = 0
}
$$

相互作用绘景：

$$
\boxed{
\Phi_I(t) \equiv \mathrm{e}^{\mathrm{i}\hat{H}_{S0} t} \Phi_S(t),\quad
\hat{F}_I \equiv \mathrm{e}^{\mathrm{i}\hat{H}_{S0} t} \hat{F}_{S} \mathrm{e}^{-\mathrm{i}\hat{H}_{S0} t},\quad
\hat{H}_I = \mathrm{e}^{\mathrm{i}\hat{H}_{S0} t} \hat{H}_{Si} \mathrm{e}^{-\mathrm{i}\hat{H}_{S0} t}
}
$$

$$
\boxed{
\mathrm{i}\frac{\partial }{\partial t } \Phi_I(t)
=\hat{H}_{Ii} \Phi_I(t)
}
$$

$$
\boxed{
\frac{\partial }{\partial t } \hat{F}_I
=\mathrm{i}\left[\hat{H}_{I0} , \hat{F}_I \right]
}
$$

### 积分方程

$$
\Phi_I(t)
=\Phi_I(t_0) - \mathrm{i} \int_{t_0}^{t} \hat{H}_{Ii}(t_1) \Phi_I(t_1) \mathrm{d}t_1
$$

## $\hat{U}(t,t_0) $ 矩阵及其性质

$\hat{U}(t,t_0) $ 把相互作用绘景中 $t_0 $ 时刻的状态幅度 $\Phi_I(t_0) $ 变为 $t $ 时刻的状态幅度 $\Phi_I(t) $：

$$
\Phi_I(t)
=\hat{U}(t,t_0) \Phi_I(t_0)
$$

把上式代入状态幅度满足的积分方程

$$
\Phi_I(t)
=\Phi_I(t_0) - \mathrm{i} \int_{t_0}^{t} \hat{H}_{Ii}(t_1) \Phi_I(t_1) \mathrm{d}t_1
$$

可得：

$$
\hat{U}(t,t_0) \Phi_I(t_0)
=\Phi_I(t_0) - \mathrm{i} \int_{t_0}^{t} \hat{H}_{Ii}(t_1) \hat{U}(t_1,t_0) \Phi_I(t_0) \mathrm{d}t_1
$$

即：

$$
\hat{U}(t,t_0) \Phi_I(t_0)
=\left(I - \mathrm{i} \int_{t_0}^{t} \hat{H}_{Ii}(t_1) \hat{U}(t_1,t_0) \mathrm{d}t_1 \right) \Phi_I(t_0)
$$

对比得 $\hat{U}(t,t_0) $ 满足的积分方程：

$$
\boxed{
\hat{U}(t,t_0)
=I - \mathrm{i} \int_{t_0}^{t} \hat{H}_{Ii}(t_1) \hat{U}(t_1,t_0) \mathrm{d}t_1
}
$$

把

$$
\Phi_I(t)
=\hat{U}(t,t_0) \Phi_I(t_0)
$$

代入

$$
\mathrm{i} \frac{\partial \Phi_I(t) }{\partial t } 
=\hat{H}_{Ii}(t) \Phi_I(t)
$$

得到 $\hat{U}(t,t_0) $ 满足的微分方程：

$$
\boxed{
\mathrm{i} \frac{\partial \hat{U}(t,t_0) }{\partial t } 
=\hat{H}_{Ii}(t) \hat{U}(t,t_0)
}
$$

#### $\hat{U}(t,t_0) $ 的性质

$$
\hat{U}(t,t) = \hat{U}(t_0,t_0) = I
$$

$$
\hat{U}^{-1}(t_1,t_2)
=\hat{U}(t_2,t_1)
$$

$$
\hat{U}^\dag(t_1,t_2) \hat{U}(t_1,t_2)
=\hat{U}(t_1,t_2) \hat{U}^\dag(t_1,t_2)
=I
$$

$$
\hat{U}(t_1,t_3)
=\hat{U}(t_1,t_2) \hat{U}(t_2,t_3)
$$

### $\hat{U}(t,t_0) $ 矩阵级数解

$$
\begin{aligned}
\hat{U}(t,t_0)
&=I \\
&+\frac{\left(-\mathrm{i} \right) }{1! } \int_{t_0}^{t} \mathrm{d}t_1 P\left[\hat{H}_{Ii}(t_1) \right] \\
&+\frac{\left(-\mathrm{i} \right)^2 }{2! } \int_{t_0}^{t} \mathrm{d}t_1 \int_{t_0}^{t} \mathrm{d}t_2 P\left[\hat{H}_{Ii}(t_1) \hat{H}_{Ii}(t_2) \right] \\
&+\cdots \\
\end{aligned}
$$

或简写为：

$$
\hat{U}(t,t_0)
=P\left[\mathrm{e}^{-\mathrm{i} \int_{t_0}^{t} \mathrm{d}t' \hat{H}_{Ii}(t')} \right]
$$

## $S $ 矩阵及其在 QED 中的形式

假设相互作用发生在 $t=0 $ 附近的一段时间。用 $\Phi_i $ 表示初态状态幅度，用 $\Phi_f $ 表示终态状态幅度，则：

$$
\Phi_i
=\Phi_I(-\infty)
$$

$$
\Phi_f
=\Phi_I(+\infty)
$$

另一方面，

$$
\Phi_I(t_2)
=\hat{U}(t_2,t_1) \Phi_I(t_1)
$$

所以：

$$
\Phi_f 
=\hat{U}(+\infty,-\infty) \Phi_i
$$

$S $ 矩阵就定义为使基本粒子系统的状态幅度由初态到终态的演化算符，即：

$$
\boxed{
\hat{S}
\equiv \hat{U}(+\infty,-\infty)
}
$$

$$
\boxed{
\Phi_f
=\hat{S} \Phi_i
}
$$

由于 $\hat{U} $ 是幺正的，因此 $\hat{S} $ 也是幺正的：

$$
\hat{S}^\dag \hat{S} = \hat{S} \hat{S}^\dag = I
$$

把 $\hat{U}(t,t_0) $ 的级数表达式

$$
\begin{aligned}
\hat{U}(t,t_0)
&=I \\
&+\frac{\left(-\mathrm{i} \right) }{1! } \int_{t_0}^{t} \mathrm{d}t_1 P\left[\hat{H}_{Ii}(t_1) \right] \\
&+\frac{\left(-\mathrm{i} \right)^2 }{2! } \int_{t_0}^{t} \mathrm{d}t_1 \int_{t_0}^{t} \mathrm{d}t_2 P\left[\hat{H}_{Ii}(t_1) \hat{H}_{Ii}(t_2) \right] \\
&+\cdots \\
\end{aligned}
$$

中的 $t_0 $ 替换为 $-\infty $，$t $ 替换为 $+\infty $，则得到 $S $ 矩阵的级数表达式：

$$
\begin{aligned}
\hat{S}
&=I \\
&+\frac{\left(-\mathrm{i} \right) }{1! } \int_{-\infty}^{+\infty} \mathrm{d}t_1 P\left[\hat{H}_{Ii}(t_1) \right] \\
&+\frac{\left(-\mathrm{i} \right)^2 }{2! } \int_{-\infty}^{+\infty} \mathrm{d}t_1 \int_{-\infty}^{+\infty} \mathrm{d}t_2 P\left[\hat{H}_{Ii}(t_1) \hat{H}_{Ii}(t_2) \right] \\
&+\cdots \\
\end{aligned}
$$

或简写为：

$$
\hat{S}
=P\left[\mathrm{e}^{-\mathrm{i} \int_{-\infty}^{+\infty} \mathrm{d}t' \hat{H}_{Ii}(t')} \right]
$$

为了计算方便，定义各级 $S $ 矩阵：

$$
\hat{S}
=\sum_{n=0}^{\infty} \hat{S}_n
$$

$$
\hat{S}_0
\equiv I
$$

$$
\hat{S}_n
\equiv \frac{(-\mathrm{i})^n }{n! } \int_{-\infty}^{+\infty} \mathrm{d}t_1 \mathrm{d}t_2 \cdots \mathrm{d}t_n P\left[\hat{H}_{Ii}(t_1) \hat{H}_{Ii}(t_2) \cdots \hat{H}_{Ii}(t_n) \right]
$$

$\hat{S}_n $ 称为第 $n $ 级 $\hat{S} $ 矩阵。

各阶 $S $ 矩阵都是 Lorentz 协变的，也都满足规范变换的协变性。

### 量子电动力学中的 $S $ 矩阵

电子或正电子与光子相互作用哈密顿算符：

$$
\hat{H}_{Ii}(t)
=-\mathrm{i} e \int \hat{\bar{\psi}}(x) \gamma_\mu \hat{\psi}(x) \hat{A}_\mu(x) \mathrm{d}V
$$

设

$$
\hat{A}(x)
\equiv \gamma_\mu \hat{A}_\mu(x)
$$

则可证明：

$$
\hat{H}_{Ii}(t)
=-\mathrm{i} e \int \hat{\bar{\psi}}(x) \hat{A}(x) \hat{\psi}(x)  \mathrm{d}V
$$

量子电动力学中的 $S $ 矩阵：

$$
\begin{aligned}
\hat{S}_n
&=\frac{\left(-\mathrm{i} \right)^n }{n! } \int_{-\infty}^{+\infty} \mathrm{d}t_1 \cdots \int_{-\infty}^{+\infty} \mathrm{d}t_n P\left[\hat{H}_{Ii}(t_1) \cdots \hat{H}_{Ii}(t_n) \right] \\
&=\frac{\left(-e \right)^n }{n! } \int_{-\infty}^{+\infty} \mathrm{d}x^1 \cdots \int_{-\infty}^{+\infty} \mathrm{d}x^n P\left[\hat{\bar{\psi}}\left(x^1\right) \hat{A}\left(x^1\right) \hat{\psi}\left(x^1\right) \cdots \hat{\bar{\psi}}\left(x^n\right) \hat{A}\left(x^n\right) \hat{\psi}\left(x^n\right) \right]
\end{aligned}
$$

由于积分中 $P $ 乘积中同一个时间坐标的费米场函数是成对的，因此积分中 $P $ 乘积与 $T $ 乘积是等价的。

$$
\boxed{
\begin{aligned}
\hat{S}_n
=\frac{\left(-e \right)^n }{n! } \int_{-\infty}^{+\infty} \mathrm{d}x^1 \cdots \int_{-\infty}^{+\infty} \mathrm{d}x^n T\left[\hat{\bar{\psi}}\left(x^1\right) \hat{A}\left(x^1\right) \hat{\psi}\left(x^1\right) \cdots \hat{\bar{\psi}}\left(x^n\right) \hat{A}\left(x^n\right) \hat{\psi}\left(x^n\right) \right]
\end{aligned}
}
$$

## $T $ 乘积展开的 Wick 定理

量子电动力学中 $\hat{S} $ 矩阵的具体形式为：

$$
\hat{S}
=\sum_{n=0}^{\infty} \hat{S}_n,\quad \hat{S}_0 = I
$$

$$
\begin{aligned}
\hat{S}_n
=\frac{\left(-e \right)^n }{n! } \int_{-\infty}^{+\infty} \mathrm{d}x^1 \cdots \int_{-\infty}^{+\infty} \mathrm{d}x^n T\left[\hat{\bar{\psi}}\left(x^1\right) \hat{A}\left(x^1\right) \hat{\psi}\left(x^1\right) \cdots \hat{\bar{\psi}}\left(x^n\right) \hat{A}\left(x^n\right) \hat{\psi}\left(x^n\right) \right]
\end{aligned}
$$

要计算 $n $ 阶 $S $ 矩阵 $\hat{S}_n $，则必须要算出积分中的 $T $ 乘积。

### $T $ 乘积展开的 Wick 定理

$n $ 个场算符的 $T $ 乘积，等于这 $n $ 个场算符的 $N $ 乘积与包括了所有可能的各种耦合的 $N $ 乘积之和。

$$
\begin{aligned}
T\left[\hat{U}_1 \hat{U}_2 \cdots \hat{U}_n \right]
&=N\left[\hat{U}_1 \hat{U}_2 \cdots \hat{U}_n \right] \\
&+\sum_{i\ne j} N\left[\hat{U}_1 \cdots \dot{\hat{U}}_i \cdots \dot{\hat{U}}_j \cdots \hat{U}_n \right] \\
&+\sum_{i,j,l,m\ne} N\left[\hat{U}_1 \cdots \dot{\hat{U}}_i \cdots \dot{\hat{U}}_j \cdots \ddot{\hat{U}}_l \cdots \ddot{\hat{U}}_m \cdots \hat{U}_n \right] \\
&+\cdots
\end{aligned}
$$

其中，$\hat{U} $ 代表任何一种场函数的产生或消灭算符。

$$
N\left[\hat{U}_1 \cdots \dot{\hat{U}}_i \cdots \dot{\hat{U}}_j \cdots \hat{U}_n \right]
\equiv \left(-1 \right)^{\varepsilon_{ij}} \dot{\hat{U}}_i \dot{\hat{U}}_j N\left[\hat{U}_1 \cdots \hat{U}_{i-1} \hat{U}_{i+1} \cdots \hat{U}_{j-1} \hat{U}_{j+1} \cdots \hat{U}_n \right]
$$

$\varepsilon_{ij} $ 表示将算符 $\hat{U}_i,\hat{U}_j $ 依次置换到所有算符最左边时，所需的费米置换次数。

### QED中的 $\hat{S} $ 矩阵和耦合式

$$
\dot{\hat{A}}_\mu\left(x^1 \right) \dot{\hat{A}}_\nu\left(x^2 \right)
=\frac{1 }{2 } D^F\left(x^1-x^2 \right) \delta_{\mu\nu}
$$

$$
\dot{\hat{\psi}}_\alpha\left(x^1 \right) \dot{\hat{\bar{\psi}}}_\beta\left(x^2 \right)
=-\frac{1 }{2 } S^F_{\alpha\beta} \left(x^1-x^2 \right)
$$

$$
\dot{\hat{\bar{\psi}}}_\alpha\left(x^1 \right) \dot{\hat{\psi}}_\beta\left(x^2 \right)
=\frac{1 }{2 } S^F_{\beta\alpha} \left(x^2-x^1 \right)
$$

$$
\dot{\hat{\psi}}_\alpha\left(x^1 \right) \dot{\hat{\psi}}_\beta\left(x^2 \right)
=\dot{\hat{\bar{\psi}}}_\alpha\left(x^1 \right) \dot{\hat{\bar{\psi}}}_\beta\left(x^2 \right)
=0
$$

$$
\dot{\hat{\psi}}_\alpha\left(x^1 \right) \dot{A}_\mu\left(x^2 \right)
=\dot{\hat{\bar{\psi}}}_\alpha.\left(x^1 \right) \dot{\hat{A}}_\mu\left(x^2 \right)
=0
$$

在 QED 中 $\hat{S} $ 矩阵耦合式只需计算以下三种**非零耦合**情况：

$$
\dot{\hat{A}}_\mu\left(x^1 \right) \dot{\hat{A}}_\nu\left(x^2 \right)
=\frac{1 }{2 } D^F\left(x^1-x^2 \right) \delta_{\mu\nu}
$$

$$
\dot{\hat{\psi}}_\alpha\left(x^1 \right) \dot{\hat{\bar{\psi}}}_\beta\left(x^2 \right)
=-\frac{1 }{2 } S^F_{\alpha\beta} \left(x^1-x^2 \right)
$$

$$
\dot{\hat{\bar{\psi}}}_\alpha\left(x^1 \right) \dot{\hat{\psi}}_\beta\left(x^2 \right)
=\frac{1 }{2 } S^F_{\beta\alpha} \left(x^2-x^1 \right)
$$

另外，在计算 $\hat{S} $ 矩阵时，没必要计算

$$
\dot{\hat{\bar{\psi}}}_\alpha(x) \dot{\hat{\psi}}_\beta(x)
=\infty
$$

这样同一时空点的旋量场的耦合式。

也就是说，$\hat{S} $ 矩阵中四维时空坐标相同的 $\hat{\bar{\psi}}_\alpha(x) $ 和 $\hat{\psi}_\beta(x) $ 可以不考虑。

### QED中 $\hat{S} $ 矩阵的 Wick 展开式

$$
\dot{\hat{A}}_\mu\left(x^1 \right) \dot{\hat{A}}_\nu\left(x^2 \right)
=\frac{1 }{2 } D^F\left(x^1-x^2 \right) \delta_{\mu\nu}
$$

$$
\dot{\hat{\psi}}_\alpha\left(x^1 \right) \dot{\hat{\bar{\psi}}}_\beta\left(x^2 \right)
=-\frac{1 }{2 } S^F_{\alpha\beta} \left(x^1-x^2 \right)
$$

$$
\dot{\hat{\bar{\psi}}}_\alpha\left(x^1 \right) \dot{\hat{\psi}}_\beta\left(x^2 \right)
=\frac{1 }{2 } S^F_{\beta\alpha} \left(x^2-x^1 \right)
$$

除上面之外的耦合式全为零。

$$
\hat{S}_n
=\frac{\left(-e \right)^n }{n! } \int_{-\infty}^{+\infty} \mathrm{d}x^1 \cdots \int_{-\infty}^{+\infty} \mathrm{d}x^n T\left[\hat{\bar{\psi}}\left(x^1 \right) \hat{A}\left(x^1 \right) \hat{\psi}\left(x^1 \right) \cdots \hat{\bar{\psi}}\left(x^n \right) \hat{A}\left(x^n \right) \hat{\psi}\left(x^n \right) \right]
$$

#### 计算 $\hat{S}_0 $

$$
\hat{S}_0
=I
$$

#### 计算 $\hat{S}_1 $

$$
\begin{aligned}
T\left[\hat{\bar{\psi}}\left(x^1 \right) \hat{A}\left(x^1 \right) \hat{\psi}\left(x^1 \right) \right]
&=N\left[\hat{\bar{\psi}}\left(x^1 \right) \hat{A}\left(x^1 \right) \hat{\psi}\left(x^1 \right) \right] \\
&+\left(-1 \right)^{\varepsilon_{12}} \dot{\hat{\bar{\psi}}}\left(x^1 \right)\dot{\hat{A}}\left(x^1 \right) N\left[\hat{\psi}\left(x^1 \right) \right] \\
&+\left(-1 \right)^{\varepsilon_{13}} \dot{\hat{\bar{\psi}}}\left(x^1 \right)\dot{\hat{\psi}}\left(x^1 \right) N\left[\hat{A}\left(x^1 \right) \right] \\
&+\left(-1 \right)^{\varepsilon_{13}} \dot{\hat{A}}\left(x^1 \right)\dot{\hat{\psi}}\left(x^1 \right) N\left[\hat{\bar{\psi}}\left(x^1 \right) \right] \\
&=N\left[\hat{\bar{\psi}}\left(x^1 \right) \hat{A}\left(x^1 \right) \hat{\psi}\left(x^1 \right) \right]
\end{aligned}
$$

$$
\begin{aligned}
\hat{S}_1
&=-e\int_{-\infty}^{+\infty} \mathrm{d}x^1 T\left[\hat{\bar{\psi}}\left(x^1 \right) \hat{A}\left(x^1 \right) \hat{\psi}\left(x^1 \right) \right] \\
&=-e\int_{-\infty}^{+\infty} \mathrm{d}x^1 N\left[\hat{\bar{\psi}}\left(x^1 \right) \hat{A}\left(x^1 \right) \hat{\psi}\left(x^1 \right) \right]
\end{aligned}
$$

#### 计算 $\hat{S}_2 $

$$
\hat{S}_2
=\frac{e^2 }{2 } \int_{-\infty}^{+\infty} \mathrm{d}x^1 \int_{-\infty}^{+\infty} \mathrm{d}x^2 T\left[\hat{\bar{\psi}}\left(x^1 \right) \hat{A}\left(x^1 \right) \hat{\psi}\left(x^1 \right) \hat{\bar{\psi}}\left(x^2 \right) \hat{A}\left(x^2 \right) \hat{\psi}\left(x^2 \right) \right]
$$

> QED Wick 定理不考虑同一时空点的耦合 and 旋量旋量耦合、共轭旋量共轭旋量耦合为零。下面用 Wick 定理计算 $T $ 乘积时就不写耦合为零的项了。

$$
\begin{aligned}
&T\left[\hat{\bar{\psi}}\left(x^1 \right) \hat{A}\left(x^1 \right) \hat{\psi}\left(x^1 \right) \hat{\bar{\psi}}\left(x^2 \right) \hat{A}\left(x^2 \right) \hat{\psi}\left(x^2 \right) \right] \\
=&T\left[\hat{\bar{\psi}}_\alpha\left(x^1 \right) \left(\gamma_\mu \right)_{\alpha\beta} \hat{\psi}_\beta\left(x^1 \right) \hat{A}_\mu\left(x_1 \right) \hat{\bar{\psi}}_\rho\left(x^2 \right) \left(\gamma_\nu \right)_{\rho\lambda} \hat{\psi}_\lambda\left(x^2 \right) \hat{A}_\nu\left(x_2 \right) \right] \\
=&N\left[\hat{\bar{\psi}}_\alpha\left(x^1 \right) \left(\gamma_\mu \right)_{\alpha\beta} \hat{\psi}_\beta\left(x^1 \right) \hat{A}_\mu\left(x_1 \right) \hat{\bar{\psi}}_\rho\left(x^2 \right) \left(\gamma_\nu \right)_{\rho\lambda} \hat{\psi}_\lambda\left(x^2 \right) \hat{A}_\nu\left(x_2 \right) \right] \\
+&N\left[\hat{\bar{\psi}}_\alpha\left(x^1 \right) \left(\gamma_\mu \right)_{\alpha\beta} \hat{\psi}_\beta\left(x^1 \right) \dot{\hat{A}}_\mu\left(x_1 \right) \hat{\bar{\psi}}_\rho\left(x^2 \right) \left(\gamma_\nu \right)_{\rho\lambda} \hat{\psi}_\lambda\left(x^2 \right) \dot{\hat{A}}_\nu\left(x_2 \right) \right] \\
+&N\left[\hat{\bar{\psi}}_\alpha\left(x^1 \right) \left(\gamma_\mu \right)_{\alpha\beta} \dot{\hat{\psi}}_\beta\left(x^1 \right) \hat{A}_\mu\left(x_1 \right) \dot{\hat{\bar{\psi}}}_\rho\left(x^2 \right) \left(\gamma_\nu \right)_{\rho\lambda} \hat{\psi}_\lambda\left(x^2 \right) \hat{A}_\nu\left(x_2 \right) \right] \\
+&N\left[\dot{\hat{\bar{\psi}}}_\alpha\left(x^1 \right) \left(\gamma_\mu \right)_{\alpha\beta} \hat{\psi}_\beta\left(x^1 \right) \hat{A}_\mu\left(x_1 \right) \hat{\bar{\psi}}_\rho\left(x^2 \right) \left(\gamma_\nu \right)_{\rho\lambda} \dot{\hat{\psi}}_\lambda\left(x^2 \right) \hat{A}_\nu\left(x_2 \right) \right] \\
+&N\left[\dot{\hat{\bar{\psi}}}_\alpha\left(x^1 \right) \left(\gamma_\mu \right)_{\alpha\beta} \ddot{\hat{\psi}}_\beta\left(x^1 \right) \hat{A}_\mu\left(x_1 \right) \ddot{\hat{\bar{\psi}}}_\rho\left(x^2 \right) \left(\gamma_\nu \right)_{\rho\lambda} \dot{\hat{\psi}}_\lambda\left(x^2 \right) \hat{A}_\nu\left(x_2 \right) \right] \\
+&N\left[\hat{\bar{\psi}}_\alpha\left(x^1 \right) \left(\gamma_\mu \right)_{\alpha\beta} \dot{\hat{\psi}}_\beta\left(x^1 \right) \ddot{\hat{A}}_\mu\left(x_1 \right) \dot{\hat{\bar{\psi}}}_\rho\left(x^2 \right) \left(\gamma_\nu \right)_{\rho\lambda} \hat{\psi}_\lambda\left(x^2 \right) \ddot{\hat{A}}_\nu\left(x_2 \right) \right] \\
+&N\left[\dot{\hat{\bar{\psi}}}_\alpha\left(x^1 \right) \left(\gamma_\mu \right)_{\alpha\beta} \hat{\psi}_\beta\left(x^1 \right) \ddot{\hat{A}}_\mu\left(x_1 \right) \hat{\bar{\psi}}_\rho\left(x^2 \right) \left(\gamma_\nu \right)_{\rho\lambda} \dot{\hat{\psi}}_\lambda\left(x^2 \right) \ddot{\hat{A}}_\nu\left(x_2 \right) \right] \\
+&N\left[\dot{\hat{\bar{\psi}}}_\alpha\left(x^1 \right) \left(\gamma_\mu \right)_{\alpha\beta} \dddot{\hat{\psi}}_\beta\left(x^1 \right) \ddot{\hat{A}}_\mu\left(x_1 \right) \dddot{\hat{\bar{\psi}}}_\rho\left(x^2 \right) \left(\gamma_\nu \right)_{\rho\lambda} \dot{\hat{\psi}}_\lambda\left(x^2 \right) \ddot{\hat{A}}_\nu\left(x_2 \right) \right] \\
\end{aligned}
$$

接下来利用

$$
N\left[\hat{U}_1 \cdots \dot{\hat{U}}_i \cdots \dot{\hat{U}}_j \cdots \hat{U}_n \right]
\equiv \left(-1 \right)^{\varepsilon_{ij}} \dot{\hat{U}}_i \dot{\hat{U}}_j N\left[\hat{U}_1 \cdots \hat{U}_{i-1} \hat{U}_{i+1} \cdots \hat{U}_{j-1} \hat{U}_{j+1} \cdots \hat{U}_n \right]
$$

$$
\dot{\hat{A}}_\mu\left(x^1 \right) \dot{\hat{A}}_\nu\left(x^2 \right)
=\frac{1 }{2 } D^F\left(x^1-x^2 \right) \delta_{\mu\nu}
$$

$$
\dot{\hat{\psi}}_\alpha\left(x^1 \right) \dot{\hat{\bar{\psi}}}_\beta\left(x^2 \right)
=-\frac{1 }{2 } S^F_{\alpha\beta} \left(x^1-x^2 \right)
$$

$$
\dot{\hat{\bar{\psi}}}_\alpha\left(x^1 \right) \dot{\hat{\psi}}_\beta\left(x^2 \right)
=\frac{1 }{2 } S^F_{\beta\alpha} \left(x^2-x^1 \right)
$$

可进一步计算 $T $ 乘积：

$$
\begin{aligned}
&T\left[\hat{\bar{\psi}}\left(x^1 \right) \hat{A}\left(x^1 \right) \hat{\psi}\left(x^1 \right) \hat{\bar{\psi}}\left(x^2 \right) \hat{A}\left(x^2 \right) \hat{\psi}\left(x^2 \right) \right] \\
=&N\left[\hat{\bar{\psi}}_\alpha\left(x^1 \right) \left(\gamma_\mu \right)_{\alpha\beta} \hat{\psi}_\beta\left(x^1 \right) \hat{A}_\mu\left(x_1 \right) \hat{\bar{\psi}}_\rho\left(x^2 \right) \left(\gamma_\nu \right)_{\rho\lambda} \hat{\psi}_\lambda\left(x^2 \right) \hat{A}_\nu\left(x_2 \right) \right] \\
+&\frac{1 }{2 } D^F\left(x^1-x^2 \right) \delta_{\mu\nu} N\left[\hat{\bar{\psi}}_\alpha\left(x^1 \right) \left(\gamma_\mu \right)_{\alpha\beta} \hat{\psi}_\beta\left(x^1 \right) \hat{\bar{\psi}}_\rho\left(x^2 \right) \left(\gamma_\nu \right)_{\rho\lambda} \hat{\psi}_\lambda\left(x^2 \right) \right] \\
-&\frac{1 }{2 } S_{\beta\rho}^F\left(x^1-x^2 \right) N\left[\hat{\bar{\psi}}_\alpha\left(x^1 \right) \left(\gamma_\mu \right)_{\alpha\beta} \hat{A}_\mu\left(x_1 \right) \left(\gamma_\nu \right)_{\rho\lambda} \hat{\psi}_\lambda\left(x^2 \right) \hat{A}_\nu\left(x_2 \right) \right] \\
+&\cdots
\end{aligned}
$$

## $S $ 矩阵的 Feynman 图解

$\hat{S} $ 矩阵是各级 $\hat{S}_n $ 矩阵之和，而由 Wick 定理，每个 $\hat{S}_n $ 可展开成场算符各种可能的耦合叠加，其中每一项应当有一定的物理意义。

具体来说，某种特定耦合方式代表基本粒子相互作用的某种反应。在 QED 中，某种特定耦合方式代表正负电子和光子相互作用的某种反应。

### QED Feynman 图形规则

$$
\hat{A}^{(+)}_\mu(x)
=\frac{1 }{\left(2\pi \right)^{3/2} } \int\limits_{k_0=\varepsilon_{\vec{k}}} \mathrm{e}^{-\mathrm{i}kx} \frac{1 }{\sqrt{2\varepsilon_{\vec{k}}} } \hat{C}_\mu^{(+)}\left(\vec{k} \right)\mathrm{d}^3\vec{k}
$$

$$
\hat{A}^{(-)}_\mu(x)
=\frac{1 }{\left(2\pi \right)^{3/2} } \int\limits_{k_0=\varepsilon_{\vec{k}}} \mathrm{e}^{+\mathrm{i}kx} \frac{1 }{\sqrt{2\varepsilon_{\vec{k}}} } \hat{C}_\mu^{(-)}\left(\vec{k} \right)\mathrm{d}^3\vec{k}
$$

$$
\hat{\psi}^{(+)}(x)
=\left(\frac{1 }{2\pi } \right)^{3/2} \int\limits_{p_0=E_{\vec{p}}} \mathrm{e}^{-\mathrm{i}p x} \hat{b}_i^{(+)}(\vec{p}) v_i(\vec{p}) \mathrm{d}^3\vec{p}
$$

$$
\hat{\psi}^{(-)}(x)
=\left(\frac{1 }{2\pi }  \right)^{3/2} \int\limits_{p_0=E_{\vec{p}}} \mathrm{e}^{+\mathrm{i}p x} \hat{a}_i^{(-)}(\vec{p}) u_i(\vec{p}) \mathrm{d}^3\vec{p}
$$

$$
\hat{\bar{\psi}}^{(+)}(x)
=\left(\frac{1 }{2\pi } \right)^{3/2} \int\limits_{p_0=E_{\vec{p}}} \mathrm{e}^{-\mathrm{i}p x} \hat{a}_i^{(+)}(\vec{p}) \bar{u}_i(\vec{p}) \mathrm{d}^3\vec{p}
$$

$$
\hat{\bar{\psi}}^{(-)}(x)
=\left(\frac{1 }{2\pi }  \right)^{3/2} \int\limits_{p_0=E_{\vec{p}}} \mathrm{e}^{+\mathrm{i}p x} \hat{b}_i^{(-)}(\vec{p}) \bar{v}_i(\vec{p}) \mathrm{d}^3\vec{p}
$$

注意到：

$\hat{\psi}^{(+)}(x) $ 对应 $\hat{b}_i^{(+)}(\vec{p}) $，即对应产生正电子算符；

$\hat{\psi}^{(-)}(x) $ 对应 $\hat{a}_i^{(-)}(\vec{p}) $，即对应消灭负电子算符；

$\hat{\bar{\psi}}^{(+)}(x) $ 对应 $\hat{a}_i^{(+)}(\vec{p}) $，即对应产生负电子算符；

$\hat{\bar{\psi}}^{(-)}(x) $ 对应 $\hat{b}_i^{(-)}(\vec{p}) $，即对应消灭正电子算符。

用实线代表电子或正电子的运动；

用虚线代表光子的运动；

$\hat{\psi}(x_1) $ 即 $\hat{\psi}^{(+)}(x) $ 或 $\hat{\psi}^{(-)}(x) $ 代表产生正电子或消灭负电子，用入向电子外线表示

$\hat{\bar{\psi}}(x_1) $ 即 $\hat{\bar{\psi}}^{(+)}(x) $ 或 $\hat{\bar{\psi}}^{(-)}(x) $ 代表产生负电子或消灭正电子，用出向电子外线表示；

$A_\mu(x_1) $ 代表光子的放出或吸收，用光子外线表示；

耦合式 $\dot{\hat{\psi}}_\alpha(x_1) \dot{\hat{\bar{\psi}}}_\beta(x_2) = -\frac{1 }{2 } \hat{S}_{\alpha\beta}^F (x_1-x_2) $ 代表中间态的正负电子，用电子内线表示；

耦合式 $\dot{\hat{A}}_\alpha(x_1) \dot{\hat{A}}_\beta(x_2)=\frac{1 }{2 } D^(x_1-x_2)\delta_{\alpha\beta} $ 代表中间态的光子或虚光子，用光子内线表示；

$\gamma_i $ 矩阵代表正负电子和光子有一次作用，用顶点图形表示。

### QED 中的 Feynman 图

一般在 Wick 定理展开式中，有两种或两种以上展开项对应同一种 Feynman 图解。

用 $r $ 代表同一 Feynman 图解所对应的不同形式的 $\hat{S}_n $ 矩阵的展开式的数目。$r $ 称为 Feynman 图解的等值数。

#### $\hat{S}_1 $ 的 Feynman 图解

$$
\hat{S}_1
=
$$

#### $\hat{S}_2 $ 的 Feynman 图解

$\hat{S}_2 $

### $\hat{S}_3 $ 的 Feynman 图解



## 4.8 Furry 关于电子封闭内线的定理

奇数个电子封闭内线的 Feynman 图对 $\hat{S} $ 矩阵没有任何贡献。

# 10 




