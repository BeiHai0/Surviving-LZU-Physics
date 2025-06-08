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

# 3 Clifford代数与 $\gamma $ 矩阵

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



