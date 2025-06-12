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

# 1 广义洛伦兹变换

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

# 2 张量、赝张量及其变换规律

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

# 3 Clifford 代数、$\gamma $ 矩阵、旋量表示、旋量与 Dirac 方程

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



