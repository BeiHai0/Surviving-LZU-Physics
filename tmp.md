### 数学准备

#### Levi-Civita 符号

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

$$
\varepsilon_{i_1i_2\cdots i_n}\varepsilon_{i_1i_2\cdots i_n}
=n!
$$

两个 $n $ 阶 Levi-Civita 符号中 $m(m\leqslant n) $ 个指标缩并的规律：

$$
\varepsilon_{\red{k_1\cdots k_m} i_{1\cdots } \cdots i_{n-m}} \varepsilon_{\red{k_1\cdots k_m} j_{1\cdots } \cdots j_{n-m}}
=m! \left(\varepsilon_{l_1 \cdots l_{n-m}} \delta_{i_1 j_{l_1}} \cdots \delta_{i_{n-m} j_{l_{n-m}}} \right)
$$

两个 $4 $ 阶 Levi-Civita 符号中 $4 $ 个指标缩并：

$$
\begin{aligned}
\varepsilon_{\mu\nu\lambda\rho} \varepsilon_{\mu\nu\lambda\rho}
&=4!
\end{aligned}
$$

两个 $4 $ 阶 Levi-Civita 符号中 $3 $ 个指标缩并：

$$
\begin{aligned}
\varepsilon_{\mu\nu\lambda \alpha_1} \varepsilon_{\mu\nu\lambda \beta_1}
&=3!\left(\varepsilon_{\rho_1} \delta_{\alpha_1 \beta_{\rho_1}} \right) \\
&=3! \delta_{\alpha_1 \beta_1}
\end{aligned}
$$

> 注意，$\varepsilon_{\rho_1} $ 是 $1 $ 阶 Levi-Civita 符号，$\rho_1 $ 的爱因斯坦求和只能取 $\rho_1=1 .$

两个 $4 $ 阶 Levi-Civita 符号中 $2 $ 个指标缩并：

$$
\begin{aligned}
\varepsilon_{\mu \nu \alpha_1 \alpha_2} \varepsilon_{\mu \nu \beta_1 \beta_2}
&=2!\left(\varepsilon_{\rho_1 \rho_2} \delta_{\alpha_1 \beta_{\rho_1}} \delta_{\alpha_2 \beta_{\rho_2}} \right) \\
&=2!\left(\delta_{\alpha_1 \beta_1} \delta_{\alpha_2 \beta_2} - \delta_{\alpha_1 \beta_2} \delta_{\alpha_2 \beta_1} \right)
\end{aligned}
$$

> 注意，$\varepsilon_{\rho_1 \rho_2} $ 是 $2 $ 阶 Levi-Civita 符号，$\rho_1,\rho_2 $ 的爱因斯坦求和只能取 $\rho_1,\rho_2\in \left\{1,2 \right\} .$

两个 $4 $ 阶 Levi-Civita 符号中 $1 $ 个指标缩并：

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

#### 行列式

$$
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
$$

**重要结论**：

$$
\begin{aligned}
\varepsilon_{i_1i_2\cdots i_n}\mathrm{det}(A)
&=\varepsilon_{i_1i_2\cdots i_n}\varepsilon_{j_1j_2\cdots j_n}A_{1j_1}A_{2j_2}\cdots A_{nj_n} \\
&=\varepsilon_{j_1j_2\cdots j_n}A_{i_1j_1}A_{i_2j_2}\cdots A_{i_nj_n}
\end{aligned}
$$

证明：

当 $i_1,i_2,\cdots,i_n $ 中至少有两个相等，不妨设为 $i_\alpha=i_\beta,\alpha\ne \beta $，则由 Levi-Civita 张量定义，等式左边：

$$
\varepsilon_{i_1i_2\cdots i_n}\mathrm{det}(A)
=0
$$

等式右边：

$$
\begin{aligned}
\red{\varepsilon_{j_1j_2\cdots j_n}A_{i_1j_1}A_{i_2j_2}\cdots A_{i_nj_n}}
&=\varepsilon_{j_1j_2\cdots j_n}A_{i_1j_1}\cdots A_{i_\alpha j_\alpha}\cdots A_{i_\beta j_\beta}\cdots A_{i_nj_n} \\
&=\varepsilon_{j_1\cdots j_\alpha\cdots j_\beta\cdots j_n}A_{i_1j_1}\cdots A_{i_\alpha j_\alpha}\cdots A_{i_\beta j_\beta}\cdots A_{i_nj_n} \\
&=-\varepsilon_{j_1\cdots j_\beta\cdots j_\alpha\cdots j_n}A_{i_1j_1}\cdots A_{i_\alpha j_\alpha}\cdots A_{i_\beta j_\beta}\cdots A_{i_nj_n} \\
&=-\varepsilon_{j_1\cdots j_\beta\cdots j_\alpha\cdots j_n}A_{i_1j_1}\cdots A_{i_\beta j_\alpha}\cdots A_{i_\alpha j_\beta}\cdots A_{i_nj_n} \\
(j_\alpha,j_\beta是哑标,二者交换是恒等变形)&=-\varepsilon_{j_1\cdots j_\alpha\cdots j_\beta\cdots j_n}A_{i_1j_1}\cdots A_{i_\beta j_\beta}\cdots A_{i_\alpha j_\alpha}\cdots A_{i_nj_n} \\
&=-\red{\varepsilon_{j_1\cdots j_\alpha\cdots j_\beta\cdots j_n}A_{i_1j_1}\cdots A_{i_\alpha j_\alpha}\cdots A_{i_\beta j_\beta}\cdots A_{i_nj_n}} \\
\end{aligned}
$$

即：

$$
\varepsilon_{j_1j_2\cdots j_n}A_{i_1j_1}A_{i_2j_2}\cdots A_{i_nj_n}
=0
$$

因此当 $i_1,i_2,\cdots,i_n $ 中至少有两个相等时原式成立。

当 $i_1,i_2,\cdots,i_n $ 各不相等时，$(i_1,i_2,\cdots,i_n) $ 是 $(1,2,\cdots,n) $ 的一个排列，设此排列的逆序对的个数为 $m $，则等式左边：

$$
\begin{aligned}
\varepsilon_{i_1i_2\cdots i_n}\varepsilon_{j_1j_2\cdots j_n}A_{1j_1}A_{2j_2}\cdots A_{nj_n}
&=(-1)^m\varepsilon_{j_1j_2\cdots j_n}A_{1j_1}A_{2j_2}\cdots A_{nj_n}
\end{aligned}
$$

等式右边：

$$
\begin{aligned}
\varepsilon_{j_1j_2\cdots j_n}A_{i_1j_1}A_{i_2j_2}\cdots A_{i_nj_n}
&=
\end{aligned}
$$

$$
\mathrm{det}(A)\varepsilon_{i_1i_2\cdots i_n}\varepsilon_{j_1j_2\cdots j_n}
=\begin{vmatrix}
A_{i_1j_1} &\cdots &A_{i_1j_n} \\
\vdots &\ddots &\vdots \\
A_{i_nj_1} &\cdots &A_{i_nj_n}
\end{vmatrix}
$$

$$
\mathrm{det}(I)\varepsilon_{i_1i_2\cdots i_n}\varepsilon_{j_1j_2\cdots j_n}
=\begin{vmatrix}
\delta_{i_1j_1} &\cdots &\delta_{i_1j_n} \\
\vdots &\ddots &\vdots \\
\delta_{i_nj_1} &\cdots &\delta_{i_nj_n}
\end{vmatrix}
$$

---

## Clifford 代数

设有域 $\mathbb{F} $ 上的向量空间 $V $，且其上配有二次型

$$
Q : V \to \mathbb{F} 
$$

Clifford 代数 $\mathrm{Cl}(V,Q) $ 定义为 $V $ 生成的、满足以下条件的单位结合代数：

$$
\forall v\in V,\quad
v^2 = Q(v) \bold{1}
$$

其中，$v^2\equiv v v $ 代表单位结合代数的乘法；$\bold{1} $ 代表单位结合代数中的乘法单位元，满足：

$$

$$

---

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

#### $C_n(V) $ 中元素的一般形式

$C_n(V) $ 中的元素 $A\in C_n(V) $ 一般可写为：

$$
A
=a + a_\mu e_\mu + \frac{1 }{2! } a_{\mu_1\mu_2} e_{\mu_1} \wedge e_{\mu_2} + \cdots + \frac{1 }{n! } a_{\mu_1\mu_2\cdots \mu_n} e_{\mu_1} \wedge e_{\mu_2} \wedge \cdots \wedge e_{\mu_n}
$$

#### Clifford 代数的代数表示

$$
\Gamma : C_n(V) \to \mathrm{End}(W),\quad
\mathrm{dim}~V = n,\quad
\mathrm{dim}~W = d
$$

其中 $W $ 为复向量空间，$\mathrm{End}(W) $ 为 $W $ 上所有线性变换的全体，满足：

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
\Gamma(e_\mu) \Gamma(e_\nu) + \Gamma(e_\nu) e(e_\mu) = 2\delta_{\mu\nu} \Gamma(\bold{1})
$$

$$
\boxed{
\gamma_\mu \gamma_\nu + \gamma_\nu \gamma_\mu
=2\delta_{\mu\nu} I
}
$$

且

$$
\gamma_\mu^2
=I
$$

注意到

$$
\gamma_\mu^\dag \gamma_\nu^\dag + \gamma_\nu^\dag \gamma_\mu^\dag
=2\delta_{\mu\nu} I
$$

因此可人为约定 $\gamma $ 矩阵还满足

$$
\gamma_\mu^\dag
=\gamma_\mu
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

---

$$
\gamma_5
\equiv \gamma_1 \gamma_2 \gamma_3 \gamma_4
$$

$$
\gamma_5
=\frac{1 }{4! } \varepsilon_{\mu\nu\lambda\rho}  \gamma_\mu \gamma_\nu \gamma_\lambda \gamma_\rho
$$

$$
\gamma_5 \gamma_\mu + \gamma_\mu \gamma_5 = 0,\quad \mu=1,2,3,4
$$

$$
\gamma_5^2 = I
$$

$$
\gamma_5 \gamma_\mu \gamma_5^{-1}
=-\gamma_\mu
$$

$$
\gamma_5 \gamma_\mu \gamma_\nu \gamma_5^{-1}
=\gamma_\mu \gamma_\nu
$$

$$
\gamma_5 \gamma_{\mu_1}\cdots\gamma_{\mu_n} \gamma_5^{-1}
=(-1)^n \gamma_{\mu_1} \cdots \gamma_{\mu_n}
$$

$$
\mathrm{Tr}\left(\gamma_{\mu_1} \cdots \gamma_{\mu_n} \right)
=(-1)^n \mathrm{Tr}\left(\gamma_{\mu_1} \cdots \gamma_{\mu_n} \right)
$$

奇数个 $\gamma_\mu $ 矩阵的迹为零。

偶数个 $\gamma_\mu $ 矩阵的迹：

$$
\mathrm{Tr}\left(\gamma_{\mu_1} \cdots \gamma_{\mu_n} \right)
=4 \sum_p \delta_p \delta_{\nu_1\nu_2} \delta_{\nu_3\nu_4} \cdots \delta_{\nu_{n-1}\nu_n}
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

$$
\mathrm{Tr}\left(\gamma_\mu\gamma_\nu \right)
=4\delta_{\mu\nu}
$$

$$
\mathrm{Tr}\left(\gamma_\mu\gamma_\nu\gamma_\lambda\gamma_\rho \right)
=4\left(\delta_{\mu\nu}\delta_{\lambda\rho} - \delta_{\mu\lambda}\delta_{\rho\nu} + \delta_{\mu\rho}\delta_{\nu\lambda} \right)
$$

### 旋量表示

$$
\gamma_\mu \gamma_\nu + \gamma_\nu \gamma_\mu
=2\delta_{\mu\nu} I
$$

$$
\gamma'_\mu
=A_{\mu\nu} \gamma_\nu
$$

$$
\gamma'_\mu \gamma'_\nu + \gamma'_\nu \gamma'_\mu
=2\delta_{\mu\nu} I
$$

则定理保证 $\gamma'_\mu $ 与 $\gamma_\mu $ 相似，即存在 $\Lambda $ 使得 $\gamma'_\mu=A_{\mu\nu} \gamma_\nu = \Lambda \gamma_\mu \Lambda^{-1} $

---

$$
\begin{aligned}
0
&=A_{\mu\rho}\partial_\rho \bar{\psi}(x) \Lambda^{-1} \gamma_\mu \Lambda - m \bar{\psi}(x) \Lambda^{-1} \Lambda \\
&=A_{\mu\rho}\partial_\rho \bar{\psi}(x) A_{\mu\nu} \gamma_\nu - m \bar{\psi}(x) \\
&=\delta_{\rho\nu} \partial_\rho \bar{\psi}(x) \gamma_\nu - m\bar{\psi}(x) \\
&=\partial_\nu \bar{\psi}(x) \gamma_\nu - m\bar{\psi}(x)
\end{aligned}
$$

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

$\mathcal{L} $ 是固有洛伦兹变换 $a_{\mu\nu} $ 及其旋量表示 $\Lambda $ 的不变量。这样才能保证场方程对固有洛伦兹变换协变和角动量守恒。

$\mathcal{L} $ 是四维位移变换的不变量，因此 $\mathcal{L} $ 不应显含 $x_\mu $,这样才能保证能量和动量守恒。

$\mathcal{L} $ 必须是 $\phi_A(x) $ 和 $\partial_\mu\phi_A $ 的二次齐式。这样才能保证场的微分方程是线性的，荷守恒定律及电荷数、重子数、轻子数守恒（整体相因子变换下的守恒性）。

$\mathcal{L} $ 是时间反演变换的不变量。在强和电磁作用中还要求 $\mathcal{L} $ 对空间反射变换合电荷共轭变换的不变性。

$\mathcal{L} $ 是规范变换的不变量。整体规范变换的协变性保证荷守恒。局域规范变换的协变性引入相互作用。

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

## 2.11 经典场论中的广义守恒定理和诺特定理

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

证明：

由于

$$
\theta_{\mu\cdots \nu\lambda}(x)\bigg|_{\vec{x}\to \infty}
=0,\quad
\partial_{\lambda}\theta_{\mu\cdots \nu\lambda}
=0
$$

于是高斯定理给出：

> 怎么用文字描述 $G $

$$
\begin{aligned}
0
&=\int\limits_{G} \partial_\lambda \theta_{\mu\cdots\nu\lambda}\mathrm{d}^4 x \\
&=\int\limits_{\partial G} \theta_{\mu\cdots\nu\lambda} \mathrm{d}\sigma_\lambda \\
&=\left(\int\limits_{\Sigma_1}-\int\limits_{\Sigma_2} \right)\theta_{\mu\cdots\nu\lambda}\mathrm{d}\sigma_\lambda
\end{aligned}
$$

即：

$$
\int\limits_{\Sigma_1} \theta_{\mu\cdots\nu\lambda}\mathrm{d}\sigma_\lambda
=\int\limits_{\Sigma_2} \theta_{\mu\cdots\nu\lambda}\mathrm{d}\sigma_\lambda
$$

由于 $\Sigma_1,\Sigma_2 $ 是任意选取的，因此

$$
\int\limits_{\Sigma}\theta_{\mu\cdots\nu\lambda}\mathrm{d}\sigma_\lambda
=\mathrm{const}
$$

其中，

$$
\mathrm{d}\sigma_1
\equiv\mathrm{d}x_2\mathrm{d}x_3\mathrm{d}x_4
$$

$$
\mathrm{d}\sigma_2
\equiv\mathrm{d}x_1\mathrm{d}x_3\mathrm{d}x_4
$$

$$
\mathrm{d}\sigma_3
\equiv\mathrm{d}x_1\mathrm{d}x_2\mathrm{d}x_4
$$

$$
\mathrm{d}\sigma_4
\equiv\mathrm{d}x_1\mathrm{d}x_2\mathrm{d}x_3
$$

且选取的 $\Sigma $ 要保证其边界 $\partial\Sigma $ 是三维空间的无穷远面。

特别地，若取 $\Sigma $ 为与 $x_4=\mathrm{i}ct $ 垂直的超平面 $\Sigma^\perp $，且这个超平面与 $x_4 $ 轴的交点为 $x_4 $，即 $\Sigma^\perp $ 是 $t $ 时刻的全空间 $\R^3 $，则在 $\Sigma^\perp $ 上有：

$$
\mathrm{d}x_4 = 0
\Longrightarrow
\mathrm{d}\sigma_1=\mathrm{d}\sigma_2=\mathrm{d}\sigma_3 = 0
$$

因此有：

$$
\begin{aligned}
\mathrm{const}
&=\int\limits_{\Sigma}\theta_{\mu\cdots\nu\lambda}\mathrm{d}\sigma_\lambda \\
&=\int\limits_{\Sigma^\perp} \theta_{\mu\cdots\nu\lambda}\mathrm{d}\sigma_\lambda \\
&=\int\limits_{\Sigma^\perp} \theta_{\mu\cdots \nu 4}\mathrm{d}\sigma_4 \\
&=\int\limits_{\vec{x}\in \R^3} \theta_{\mu\cdots \nu 4}(\vec{x},x_4) \mathrm{d}x_1\mathrm{d}x_2\mathrm{d}x_3 \\
&=\int\limits_{\vec{x}\in \R^3} \theta_{\mu\cdots \nu 4}(\vec{x},x_4)\mathrm{d}^3\vec{x}
\end{aligned}
$$

于是：

$$
\begin{aligned}
T_{\mu\cdots\nu}(x_4)
\equiv \frac{1 }{\mathrm{i} } \int\limits_{\vec{x}\in \R^3} \theta_{\mu\cdots \nu 4}(\vec{x},x_4)\mathrm{d}^3\vec{x}
=\mathrm{const}
\end{aligned}
$$


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


# 第4章 场的相互作用和S矩阵

## 4.1 场的相互作用拉格朗日函数

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

## 4.2 场的相互作用运动方程荷相互作用哈密顿量

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

## 4.3 相互作用绘景

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

## 4.4 $\hat{U}(t,t_0) $ 矩阵及其性质

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

## 4.5 $S $ 矩阵

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

## 4.6 $T $ 乘积展开的 Wick 定理

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

## 4.7 $S $ 矩阵的 Feynman 图解

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
 
## 4.9 $\hat{S} $ 矩阵的矩阵元

为了研究基本粒子反应，采用相互作用绘景的粒子数表象。

QED 中，$\alpha $ 个动量为 $\vec{p}_1,\cdots,\vec{p}_\alpha $，自旋为 $i_1,\cdots,i_\alpha $ 的正负电子和 $r $ 个动量为 $\vec{k}_1,\cdots\vec{k}_r $，极化为 $\mu_1,\cdots,\mu_r $ 的光子系统，在相互作用绘景粒子数表象中的状态幅度可记为：

$$
\Phi_{\vec{p}_1 i_1,\cdots,\vec{p}_\alpha i_\alpha ;\vec{k}_1 \mu_1 \cdots \vec{k}_r \mu_r }
=\hat{a}_{\vec{p}_1 i_1}^{(+)} \cdots \hat{b}_{\vec{p}_\alpha i_\alpha}^{(+)} \hat{C}_{\vec{k}_1}^{\mu_1 (+)} \cdots \hat{C}_{\vec{k}_r}^{\mu_r (+)} \Phi_0
$$

其中，$\hat{a}_{\vec{p} i}^{(+)} $ 是产生动量为 $\vec{p} $，自旋为 $i $ 的电子的算符；$\hat{b}_{\vec{p} i}^{(+)} $ 是产生动量为 $\vec{p} $，自旋为 $i $ 的正电子的算符；$\hat{C}_{\vec{k}}^{\mu(+)} $ 是产生动量为 $\vec{k} $，极化为 $\mu $ 的光子的算符。

为简便，记：

$$
\Phi_{\vec{p}_1 i_1,\cdots,\vec{p}_\alpha i_\alpha ;\vec{k}_1 \mu_1 \cdots \vec{k}_r \mu_r }
\equiv \Phi_\beta
$$

对于基本粒子反应，初态 $\Phi_i $ 应是粒子数表象的某个本征态 $\Phi_\alpha $，即

$$
\Phi_i = \Phi_\alpha
$$

$\hat{S} $ 矩阵给出了末态 $\Phi_f $：

$$
\Phi_f 
=\hat{S} \Phi_i
=\hat{S} \Phi_\alpha
$$

一般来说，末态 $\Phi_f $ 不是粒子数表象的本征态，而是粒子数表象本征态的某种混合。假设 $\Phi_f $ 可按粒子数表象本征态 $\left\{\Phi_\beta \right\} $ 展开：

$$
\Phi_f
=\hat{S} \Phi_i
=\hat{S} \Phi_\alpha
=\sum_\beta C_{\alpha\beta} \Phi_\beta
$$

根据量子力学基本原理，展开系数模方 $\left|C_{\alpha\beta} \right|^2 $ 就代表了初态为粒子数表象本征态 $\Phi_\alpha $  时，系统随时间演化直至末态，对末态进行测量，测得末态为粒子数表象本征态 $\Phi_\beta $ 的概率。

为了计算展开系数，上式左乘 $\Phi_{\beta'}^\dag $，并利用正交关系 $\Phi_{\beta'}^\dag \Phi_\beta=\delta_{\beta\beta'} $ 可得：

$$
C_{\alpha\beta'}
=\Phi_{\beta'}^\dag \hat{S} \Phi_\alpha
$$

用 Dirac 符号来说，假设 $\Ket{\alpha },\Ket{\beta } $ 都是粒子数表象的本征态，那么矩阵元 $\Braket{\beta|\hat{S}|\alpha } $ 就是初态 $\alpha $ 到末态 $\beta $ 的跃迁振幅，$\left|\Braket{\beta|\hat{S}|\alpha } \right|^2 $ 就是初态为粒子数表象本征态 $\Ket{\alpha } $  时，系统随时间演化直至末态，对末态进行测量，测得末态为粒子数表象本征态 $\Ket{\beta } $ 的概率。

### 产生、消灭粒子算符对状态幅度的作用

$$
\hat{a}_{\vec{p}i}^{(-)} \Phi_{\vec{p}'i'}
=\delta_{\vec{p}\vec{p}'}\delta_{i i'} \Phi_0
$$

$$
\hat{b}_{\vec{p} i}^{(-)} \Phi_{\vec{p}' i'}
=\delta_{\vec{p}\vec{p}'}\delta_{i i'} \Phi_0
$$

$$
\hat{C}_{\vec{k}}^{\mu(-)} \Phi_{\vec{k}' \mu'}
=\delta_{\vec{k} \vec{k}'} \delta_{\mu \mu'} \Phi_0
$$

取厄米共轭有：

$$
\Phi_{\vec{p}' i'}^\dag \hat{a}_{\vec{p} i}^{(+)} 
=\delta_{\vec{p}\vec{p}'}\delta_{i i'} \Phi_0^\dag
$$

$$
\Phi_{\vec{p}' i'}^\dag \hat{b}_{\vec{p} i}^{(+)} 
=\delta_{\vec{p}\vec{p}'}\delta_{i i'} \Phi_0^\dag
$$

$$
\Phi_{\vec{k}' \mu'}^\dag \hat{C}_{\vec{k}}^{\mu(+)} 
=\delta_{\vec{k}\vec{k}'}\delta_{\mu \mu'} \Phi_0^\dag
$$


可以推广到 $\alpha $ 个正负电子和 $r $ 个光子系统的情况也类似。

### 场算符 $N $ 乘积对本征态矢量的作用

要研究 $\hat{S} $ 在粒子数表象中的矩阵元，就必须讨论场算符的 $N $ 乘积对本征态矢量的作用。

已知

$$
\hat{A}_\mu^{(+)}(x)
=\frac{1 }{\sqrt{V} } \sum_{\vec{k},\nu} \frac{1 }{\sqrt{2\varepsilon_{\vec{k}}} } e_\mu^\nu \hat{C}_{\vec{k}}^{\nu(+)} \mathrm{e}^{-\mathrm{i}k x}
$$

$$
\hat{A}_\mu^{(-)}(x)
=\frac{1 }{\sqrt{V} } \sum_{\vec{k},\nu} \frac{1 }{\sqrt{2\varepsilon_{\vec{k}}} } e_\mu^\nu \hat{C}_{\vec{k}}^{\nu(-)} \mathrm{e}^{+\mathrm{i}k x}
$$

$$
\hat{\psi}^{(+)}(x)
=\frac{1 }{\sqrt{V} } \sum_{\vec{p},i} \hat{b}_{\vec{p} i}^{(+)} v_i(\vec{p}) \mathrm{e}^{-\mathrm{i}px}
$$

$$
\hat{\psi}^{(-)}(x)
=\frac{1 }{\sqrt{V} } \sum_{\vec{p},i} \hat{a}_{\vec{p}i}^{(-)} u_i(\vec{p}) \mathrm{e}^{\mathrm{i}p x}
$$

$$
\hat{\bar{\psi}}^{(+)}(x)
=\frac{1 }{\sqrt{V} } \sum_{\vec{p},i} \hat{a}_{\vec{p} i}^{(+)} \bar{u}_i(\vec{p}) \mathrm{e}^{-\mathrm{i}p x}
$$

$$
\hat{\bar{\psi}}^{(-)}(x)
=\frac{1 }{\sqrt{V} } \sum_{\vec{p},i} \hat{b}_{\vec{p}i}^{(-)} \bar{v}_i(\vec{p}) \mathrm{e}^{\mathrm{i}p x}
$$

我们需要的是 $\hat{A}_\mu^{(-)}(x) , \hat{\psi}^{(-)}(x) , \hat{\bar{\psi}}^{(-)}(x) $ 从左边作用于粒子数表象单粒子本征态的结果。

注意到：

$$
\begin{aligned}
\hat{A}_\mu^{(+)}(x) \Phi_{\vec{k} \nu}
&=\left(\frac{1 }{\sqrt{V} } \sum_{\vec{k}',\nu'} \frac{1 }{\sqrt{2\varepsilon_{\vec{k}'}} } e_\mu^{\nu'} \hat{C}_{\vec{k}'}^{\nu'(-)} \mathrm{e}^{+\mathrm{i}k' x} \right) \Phi_{\vec{k} \nu} \\
&=\left(\frac{1 }{\sqrt{V} } \sum_{\vec{k}',\nu'} \frac{1 }{\sqrt{2\varepsilon_{\vec{k}'}} } e_\mu^{\nu'} \delta_{\vec{k},\vec{k}'} \delta_{\nu,\nu'} \mathrm{e}^{+\mathrm{i}k' x} \right) \Phi_{0} \\
&=\frac{1 }{\sqrt{V} } \frac{1 }{\sqrt{2\varepsilon_{\vec{k}}} } e_\mu^\nu \mathrm{e}^{+\mathrm{i}k x} \Phi_0
\end{aligned}
$$

$$
\begin{aligned}
\hat{\psi}^{(-)}(x) \Phi_{\vec{p} i}
&=\left(\frac{1 }{\sqrt{V} } \sum_{\vec{p}',i'} \hat{a}_{\vec{p}'i'}^{(-)} u_{i'}(\vec{p}') \mathrm{e}^{\mathrm{i}p' x} \right) \Phi_{\vec{p} i} \\
&=\left(\frac{1 }{\sqrt{V} } \sum_{\vec{p}',i'} \delta_{\vec{p},\vec{p}'} \delta_{i,i'} u_{i'}(\vec{p}') \mathrm{e}^{\mathrm{i}p' x} \right) \Phi_{0} \\
&=\frac{1 }{\sqrt{V} } u_i(\vec{p}) \mathrm{e}^{\mathrm{i}p x} \Phi_0
\end{aligned}
$$

$$
\begin{aligned}
\hat{\bar{\psi}}^{(-)}(x) \Phi_{\vec{p} i}
&=\left(\frac{1 }{\sqrt{V} } \sum_{\vec{p}',i'} \hat{b}_{\vec{p}'i'}^{(-)} \bar{v}_{i'}(\vec{p}) \mathrm{e}^{\mathrm{i}p' x} \right) \Phi_{\vec{p} i} \\
&=\left(\frac{1 }{\sqrt{V} } \sum_{\vec{p}',i'}\delta_{\vec{p},\vec{p}'} \delta_{i,i'} \bar{v}_{i'}(\vec{p}) \mathrm{e}^{\mathrm{i}p' x} \right) \Phi_{0} \\
&=\frac{1 }{\sqrt{V} } \bar{v}_i(\vec{p}) \mathrm{e}^{\mathrm{i}p x}
\end{aligned}
$$

总之：

$$
\hat{A}_\mu^{(-)}(x) \Phi_{\vec{k} \nu}
=\frac{1 }{\sqrt{V} } \frac{1 }{\sqrt{2\varepsilon_{\vec{k}}} } e^{\nu}_{\mu} \mathrm{e}^{\mathrm{i}k x} \Phi_0
$$

$$
\hat{\psi}^{(-)}(x) \Phi_{\vec{p} i}
=\frac{1 }{\sqrt{V} } u_i\left(\vec{p} \right) \mathrm{e}^{\mathrm{i} p x} \Phi_0
$$

$$
\hat{\bar{\psi}}^{(-)}(x) \Phi_{\vec{p} i}
=\frac{1 }{\sqrt{V} } \bar{v}_i\left(\vec{p} \right) \mathrm{e}^{\mathrm{i} p x} \Phi_0
$$

取厄米共轭得：

$$
\Phi_{\vec{k} \nu}^\dag \hat{A}_\mu^{(+)}(x)
=\frac{1 }{\sqrt{V} } \frac{1 }{\sqrt{2\varepsilon_{\vec{k}}} } e^{\nu}_{\mu} \mathrm{e}^{-\mathrm{i}k x} \Phi_0^\dag
$$

$$
\Phi_{\vec{p} i}^\dag \hat{\psi}^{(+)}(x)
=\frac{1 }{\sqrt{V} } v_i(\vec{p}) \mathrm{e}^{-\mathrm{i}p x}\Phi_0^\dag
$$

$$
\Phi_{\vec{p} i}^\dag \hat{\bar{\psi}}^{(+)}(x)
=\frac{1 }{\sqrt{V} } \bar{u}_i(\vec{p}) \mathrm{e}^{-\mathrm{i}p x}\Phi_0^\dag
$$

令 $\hat{O} $ 为产生和消灭算符的 $N $ 乘积，粒子数表象下 $\hat{O} $ 算符由确定初态向确定终态跃迁的矩阵元定义为：

$$
\Phi_f^\dag \hat{O} \Phi_i
=\Braket{f|\hat{O}|i}
$$

其中 $\ket{i},\ket{f} $ 都是粒子数算符本征态。

只有当 $\hat{O} $ 中消灭粒子算符的数目和种类与初态 $\Phi_i $ 的完全相同，且 $\hat{O} $ 中产生粒子算符的数目和种类与终态 $\Phi_f $ 的完全相同，$\Braket{f|\hat{O}|i} $ 才可能不为零。

### $S $ 矩阵的矩阵元

$S $ 矩阵可分解为 $\hat{S}_n $ 矩阵之和，而 $\hat{S}_n $ 矩阵又可用 Wick 定理展开成数项场算符的 $N $ 乘积对时空坐标的积分。

这些项中，有 $r $ 项可以用同一 Feynman 图解表示。

$\hat{S}_n $ 中可以用同一 Feynman 图解表达的项记为 $\hat{M}^n $，则：

$$
\hat{S}_n
=\sum_{\hat{M}^n} \hat{M}^n
$$

其中，求和对不同的 Feynman 图进行。

$$
\begin{aligned}
\hat{M}^n
&=\frac{r\left(-e \right)^n }{n! } \int \mathrm{d}x^1 \cdots \mathrm{d}x^n N\left[F\left(\hat{A}_\mu(x),\hat{\bar{\psi}}(x),\hat{\psi}(x),D^F,S^F \right) \right] \\
&=\frac{r\left(-e \right)^n }{n! } \int \mathrm{d}x^1 \cdots \mathrm{d}x^n \hat{F}_f\left(\hat{A}_\mu^{(+)}(x),\hat{\bar{\psi}}^{(+)},\hat{\psi}^{(+)} \right) \hat{F}_m\left(D_{\mu\nu}^F,S_{\alpha\beta}^F \right) \hat{F}_i\left(\hat{A}_\mu^{(-)}(x),\hat{\bar{\psi}}^{(-)},\hat{\psi}^{(-)} \right)
\end{aligned}
$$

设 $\hat{F}_i $ 中消灭正负电子的算符数为 $\alpha_i' $，消灭光子的算符数为 $r_i' $；$\hat{F}_f $ 中产生正负电子的算符数为 $\alpha_f' $，产生光子的算符数为 $r_f'$，则 $\hat{M}^n $ 可写为：

$$
\hat{M}^n
=\hat{M}^n \left(\alpha_f',r_f';\alpha_i',r_i' \right)
$$

为了计算粒子数表象 $\hat{S} $ 矩阵元，假设要研究的基本粒子反应的初态为 $\alpha_i $ 个正负电子和 $r_i $ 个光子，终态为 $\alpha_f $ 个正负电子和 $r_f $ 个光子。

$$
\Phi_f^\dag \hat{S} \Phi_i
=\sum_{n} \Phi_f^\dag \hat{S}_n \Phi_i
=\sum_{n} \Phi_f^\dag \sum_{\hat{M}^n} \hat{M}^n \Phi_i
$$

$$
\Phi_i
=\Phi_{\alpha_i r_i},\quad
\Phi_f
=\Phi_{\alpha_f r_f}
$$

可以知道，只有当 $\alpha_f'=\alpha_f,r_f'=r_f,\alpha_i'=\alpha_i,r_i'=r_i $ 时 $\Phi_{\alpha_f r_f}^\dag \hat{M}^n\left(\alpha_f',r_f';\alpha_i',r_i' \right) \Phi_{\alpha_i r_i} $ 才可能不为零。

设 $\hat{M}(\alpha_f,r_f;\alpha_i,r_i) $ 为所有不同级的 $\hat{S}_n $ 矩阵的展开式中具有初态为 $(\alpha_i,r_i) $ 且终态为 $(\alpha_f,r_f) $ 的各项 $\hat{M}^n(\alpha_f,r_f;\alpha_i,r_i) $ 之和，即：

$$
\hat{M}(\alpha_f,r_f;\alpha_i,r_i)
=\sum_{n=l}^{\infty} \hat{M}^n(\alpha_f,r_f;\alpha_i,r_i)
$$

其中，$l $ 代表可能发生上述基本粒子反应的最低阶 $\hat{S}_n $ 矩阵的阶数。

则 $\hat{S} $ 矩阵元可写为：

$$
\Phi_f^\dag \hat{S} \Phi_i
=\Phi_{\alpha_f r_f}^\dag \hat{M}(\alpha_f,r_f;\alpha_i,r_i) \Phi_{\alpha_i r_i}
$$

在计算有固定动量和自旋的初态和终态的 $\hat{S} $ 矩阵矩阵元时，只要作替换：

$$

$$

## 4.10 动量表象 S 矩阵元

假设所研究的正负电子和光子反应的 Feynman 图中有：$n $ 个顶点（即 $n $ 阶 S 矩阵）、$E_e $ 个正负电子外线、$E_\gamma $ 个光子外线、$I_e $ 个正负电子内线、$I_\gamma $ 个光子外线、$S $ 个电磁场外线，则：

外线总数 $E=E_e+E_\gamma $

内线总数 $I=I_e+I_\gamma $

## 4.11 基本粒子反应几率和截面

### $\left|\Braket{f|S|i} \right|^2 $ 的意义

$\left|\Braket{f|S|i} \right|^2\equiv M_{i-f} $ 表示初终态之间的跃迁几率，即基本粒子衰变或反应几率。不同的 $\bra{f} $ 代表不同的反应道。

### 单位时间、单位空间基本粒子反应跃迁几率

单位时空体积初终态跃迁几率为：

$$
\mathrm{d}\omega
=\left(\frac{1 }{2\pi }  \right)^4 \left(\prod_i n_i \right) \left|M\left(p^i , p^f \right) \right|^2 \delta\left(p^f - p^i \right) \prod_f \frac{\mathrm{d}^3\vec{p}_f }{\left(2\pi \right)^3 } 
$$

其中，$n_i $ 为某一种初态粒子单位体积的粒子数 $n_i\equiv N_i/V $

### 基本粒子的反应截面

基本粒子的反应**微分**截面 $\mathrm{d}\sigma$ 定义为单位时间单位体积基本粒子（群）反应的几率除以初态粒子流的强度。

$$
\mathrm{d}\sigma
\equiv \frac{\mathrm{d}\omega }{J } 
$$

在一半的基本粒子反应中，初态只有两种粒子

$$
J
=n_1 n_2 v_{12}
$$

$v_{12} $ 是两种基本粒子相对运动速度。

$$
\mathrm{d}\sigma
=\left(\frac{1 }{2\pi }  \right)^4\frac{1 }{v_{12} }  \left|M\left(p^i , p^f \right) \right|^2 \delta\left(p^f - p^i \right) \prod_f \frac{\mathrm{d}^3\vec{p}_f }{\left(2\pi \right)^3 } 
$$

两个初态粒子相对运动公式：

$$
v_{12}
=\frac{1 }{\varepsilon_1 \varepsilon_2 } \sqrt{\left(p^1_\mu p^2_\mu \right)^2 - m_1^2m_2^2}
$$

初态有两种基本粒子反应的微分截面公式：

$$
\mathrm{d}\sigma
=\left(\frac{1 }{2\pi }  \right)^4 \frac{\varepsilon_1 \varepsilon_2 }{F }  \left|M\left(p^i , p^f \right) \right|^2 \delta\left(p^f - p^i \right) \prod_f \frac{\mathrm{d}^3\vec{p}_f }{\left(2\pi \right)^3 } ,\quad
F
\equiv \sqrt{\left(p^1_\mu p^2_\mu \right)^2 - m_1^2m_2^2}
$$

总反应截面公式：

$$
\begin{aligned}
\sigma
=\int \mathrm{d}\sigma
=\left(\frac{1 }{2\pi }  \right)^4 \int \cdots \int \frac{\varepsilon_1 \varepsilon_2 }{F }  \left|M\left(p^i , p^f \right) \right|^2 \delta\left(p^f - p^i \right) \prod_f \frac{\mathrm{d}^3\vec{p}_f }{\left(2\pi \right)^3 }
\end{aligned}
$$

反应的微分截面 $\mathrm{d}\sigma $ 的两个特点：

- $\mathrm{d}\sigma $ 和 $\sigma $ 的量纲为面积；

- $\mathrm{d}\sigma $ 表达式与初态粒子数密度无关。

- 总截面代表反应几率。

### 不稳定基本粒子衰变的平均寿命

单位时间 $1 $ 个基本粒子衰变几率为：

$$
\lambda
=\left(\frac{1 }{2\pi }  \right)^4 \left|M\left(p^i , p^f \right) \right|^2 \delta\left(p^f - p^i \right) \prod_f \frac{\mathrm{d}^3\vec{p}_f }{\left(2\pi \right)^3 }
$$

$\lambda $ 又称为基本粒子的衰变宽度，其倒数称为衰变寿命 $\tau $，即：

$$
\tau
\equiv \frac{1 }{\lambda } 
$$

### 单位时间基本粒子反应的几率

### 在外场作用下基本粒子反应的截面

$$
\mathrm{d}\sigma
=\frac{1 }{2\pi } \frac{1 }{s } V^{E_f} \left|M_{i-f}^{(e)} \left(p^f , p^i \right) \right|^2 \delta\left(\varepsilon^f - \varepsilon^i \right) \prod_f \frac{\mathrm{d}^3\vec{p}_f }{\left(2\pi \right)^3 } 
$$

## 4.12 光子或电子的自旋状态的求和与平均的公式

一般的基本粒子反应中，初态或终态同类的基本粒子的自旋是平均分布的，称为非极化的。

### 对电子和正电子终态的自旋求和

初态有两种基本粒子反应的微分截面公式：

$$
\mathrm{d}\sigma
=\left(\frac{1 }{2\pi }  \right)^4 \frac{\varepsilon_1 \varepsilon_2 }{F }  \left|M\left(p^i , p^f \right) \right|^2 \delta\left(p^f - p^i \right) \prod_f \frac{\mathrm{d}^3\vec{p}_f }{\left(2\pi \right)^3 } ,\quad
F
\equiv \sqrt{\left(p^1_\mu p^2_\mu \right)^2 - m_1^2m_2^2}
$$

总反应截面公式：

$$
\begin{aligned}
\sigma
=\int \mathrm{d}\sigma
=\left(\frac{1 }{2\pi }  \right)^4 \int \cdots \int \frac{\varepsilon_1 \varepsilon_2 }{F }  \left|M\left(p^i , p^f \right) \right|^2 \delta\left(p^f - p^i \right) \prod_f \frac{\mathrm{d}^3\vec{p}_f }{\left(2\pi \right)^3 }
\end{aligned}
$$

通常反应中，首先以初、终态各为一电子的情形为例，此时

$$
M\left(p^i , p^f \right)
=\bar{u}_f\left(\vec{p}_1 \right) \hat{O} u_i\left(\vec{p}_2 \right)
$$

其中 $\hat{O} $ 是矩阵函数。

$$
\begin{aligned}
M^\dag\left(p^i,p^f \right)
&=M^*\left(p^i,p^f \right)
\end{aligned}
$$

设

$$
\hat{\bar{O}}
=\gamma_4 \hat{O}^\dag \gamma_4
$$

则

$$
\begin{aligned}
\left|M\left(p^i,p^f \right) \right|^2
&=\bar{u}_i\left(\vec{p}_2 \right) \hat{\bar{O}} u_f\left(\vec{p}_1 \right) \bar{u}_f\left(\vec{p}_1 \right) \hat{O} u_i\left(\vec{p}_2 \right),\quad i,f 不求和
\end{aligned}
$$

对终态自旋求和

$$
\sum_{f=1}^{2} \left|M\left(p^i,p^f \right) \right|^2
=\sum_{f=1}^{2} \bar{u}_i\left(\vec{p}_2 \right) \hat{\bar{O}} u_f\left(\vec{p}_1 \right) \bar{u}_f\left(\vec{p}_1 \right) \hat{O} u_i\left(\vec{p}_2 \right)
$$

又由

$$
\sum_{f=1}^{2} u_f\left(\vec{p}_1 \right) \bar{u}_f\left(\vec{p}_1 \right)
=\frac{m }{E_1 } \Lambda_-\left(p_1 \right) 
=-\frac{1 }{2E_1 } \left(\mathrm{i}\hat{p}_1 - m \right)
$$

则终态求和为

$$
\sum_{f=1}^{2} \left|M\left(p^i,p^f \right) \right|^2
=\frac{m }{E_1 } \bar{u}_i \left(\vec{p}_2 \right) \hat{\bar{O}} \Lambda_-\left(p_1 \right) \hat{O} u_i\left(\vec{p}_2 \right)
$$

### 对电子或正电子终态自旋求和并对初态自旋平均

### 对光子的极化求和

### 例子

求 $B\to f + \tilde{f} $ 寿命。已知：$B $ 是自旋为零、质量为 $M $ 的玻色子；$f,\tilde{f} $ 是自旋为 $1/2 $、质量为 $m $ 的正反费米子。相互作用哈密顿量为

$$
\hat{\mathcal{H}}_i
=\mathrm{i} g \hat{\phi}(x) \hat{\bar{\psi}}(x) \hat{\psi}(x)
$$

求 $B $ 粒子衰变为正反费米子 $f,\tilde{f} $ 的寿命。

（1）根据反应式画出相应费曼图（仅考虑一阶图），写出 $\lambda $ 表达式。

$$
\hat{S}_1
=-\mathrm{i}\int \mathrm{d}^4 x N\left[\hat{\mathcal{H}}_I(x) \right]
=g \int \mathrm{d}^4 x N\left[\hat{\bar{\psi}}(x) \hat{\psi}(x) \phi(x) \right]
$$

衰变初、终态

$$
\Ket{B }
=\Ket{\vec{k} },\quad
\Ket{f,\tilde{f} }
=\Ket{\vec{p}_1 , i ; \vec{p}_2 , j }
$$

相应 $\hat{M}_{i-f}^{(1)} $ 为

$$
\hat{M}_{i-f}^{(1)}
=g \int \mathrm{d}^4 x \Braket{f , \tilde{f} | \hat{\bar{\psi}}^{(+)}(x) \hat{\psi}^{(+)}(x) \hat{\phi}^{(-)}(x) | B }
$$

$$
\hat{\phi}^{(-)}(x)
\to \frac{1 }{\sqrt{V} } \frac{1 }{\sqrt{2 \varepsilon_{\vec{k}}} } \mathrm{e}^{\mathrm{i}kx},\quad
\hat{\bar{\psi}}^{(+)}(x)
\to \frac{1 }{\sqrt{V} } \bar{u}_i\left(\vec{p}_1 \right) \mathrm{e}^{-\mathrm{i}p_1 x},\quad
\hat{\psi}^{(+)}(x)
\to \frac{1 }{\sqrt{V} } v_j\left(\vec{p}_2 \right) \mathrm{e}^{-\mathrm{i}p_2 x}
$$

代入得

$$
\begin{aligned}
\hat{M}_{i-f}^{(1)}
=g \left(2\pi \right)^4 \delta\left(p_1+p_2-k \right) \left(\frac{1 }{\sqrt{V} }  \right)^3 \frac{1 }{\sqrt{2 \varepsilon_{\vec{k}}} } \bar{u}_i(\vec{p}_1) v_j(\vec{p}_2)
\end{aligned}
$$

$$
M\left(p^i , p^f \right)
=\left(2\pi \right)^4 g \frac{1 }{\sqrt{2\varepsilon_{\vec{k}}} } \bar{u}_i(\vec{p}_1) v_j(\vec{p}_2)
$$

代入

$$
\lambda
=\left(\frac{1 }{2\pi }  \right)^4 \left|M\left(p^i , p^f \right) \right|^2 \delta\left(p^f - p^i \right) \prod_f \frac{\mathrm{d}^3\vec{p}_f }{\left(2\pi \right)^3 }
$$

得到极化态衰变宽度

$$
\begin{aligned}
\lambda
=\left(\frac{g }{2\pi }  \right)^2 \int \frac{1 }{2\varepsilon_{\vec{k}} } \left|\bar{u}_i(\vec{p}_1) v_j(\vec{p}_2) \right|^2 \delta(p_1+p_2-k) \mathrm{d}^3\vec{p}_1 \mathrm{d}^3\vec{p}_2
\end{aligned}
$$

（2）终态自旋求和

$$
\begin{aligned}
\sum_{i=1}^{2} \sum_{j=1}^{2} \left|\bar{u}_i(\vec{p}_1) v_j(\vec{p}_2) \right|^2
&=\sum_{i,j} \mathrm{Tr}\left[u_i(\vec{p}_1) \bar{u}_i(\vec{p}_1) v_j(\vec{p}_2) \bar{v}_j(\vec{p}_2) \right] \\
&=-\frac{1 }{E_1 E_2 } \left[\left(p_1 p_2 \right) + m^2 \right]
\end{aligned}
$$

$$
\begin{aligned}
\lambda
=-\left(\frac{g }{2\pi }  \right)^2 \int \frac{m^2 + \left(p_1 p_2 \right) }{2 \varepsilon_{\vec{k}} E_1 E_2 } \delta(p_1+p_2-k) \mathrm{d}^3\vec{p}_1 \mathrm{d}^3\vec{p}_2
\end{aligned}
$$

（3）对终态动量积分

取初态为质心系

$$
\vec{k} = 0,\quad \varepsilon_{\vec{k}} = M
$$

$$
\delta(p_1 + p_2 - k)
=\delta(\vec{p}_1 + \vec{p}_2) \delta(E_1+E_2-M)
$$

对 $\vec{p}_1 $ 积分，考虑到 $\delta(\vec{p}_1+\vec{p}_2) $ 函数，只需要把被积函数中除 $\delta(\vec{p}_1+\vec{p}_2) $ 函数外的项中 $\vec{p}_1 $ 全替换成 $-\vec{p}_2 $ 即可：

$$
\vec{p}_1 \to -\vec{p}_2,\quad
E_1 = \sqrt{\vec{p}_1^2 + m^2} \to \sqrt{\vec{p}_2^2 + m^2} = E_2 \equiv E,\quad
\left(p_1 p_2 \right) = \vec{p}_1 \cdot \vec{p}_2 - E_1 E_2 \to -\vec{p}_2^2 - E^2 = m^2 - 2E^2
$$

$$
\begin{aligned}
\lambda
&=-\left(\frac{g }{2\pi }  \right)^2 \int \frac{m^2 + \left(p_1 p_2 \right) }{2 \varepsilon_{\vec{k}} E_1 E_2 } \delta(p_1+p_2-k) \mathrm{d}^3\vec{p}_1 \mathrm{d}^3\vec{p}_2 \\
&=-\left(\frac{g }{2\pi }  \right)^2 \int \frac{m^2 - E^2 }{M E^2 } \delta(2E-M) \mathrm{d}^3\vec{p}_2 \\
\end{aligned}
$$

再考虑对 $\vec{p}_2 $ 的积分，利用球坐标

$$
E^2 = \left|\vec{p}_2 \right|^2 + m^2\quad
2 E \mathrm{d}E = 2\left|\vec{p}_2 \right|\mathrm{d}\left|\vec{p}_2 \right|,\quad
\left|\vec{p}_2 \right|^2\mathrm{d}\left|\vec{p}_2 \right|
=\left|\vec{p}_2 \right| E \mathrm{d}E
=\sqrt{E^2-m^2} E\mathrm{d}E
$$

$$
\begin{aligned}
\mathrm{d}^3\vec{p}_2
=\left|\vec{p}_2  \right|^2 \mathrm{d}\left|\vec{p}_2 \right|\mathrm{d}\Omega
=\sqrt{E^2-m^2} E \mathrm{d}E \mathrm{d}\Omega
\end{aligned}
$$

$$
\begin{aligned}
\lambda
&=-\left(\frac{g }{2\pi }  \right)^2 \int \frac{m^2 - E^2 }{M E^2 } \delta(2E-M) \mathrm{d}^3\vec{p}_2 \\
&=-\left(\frac{g }{2\pi }  \right)^2 \int \frac{m^2 - E^2 }{M E^2 } \cdot \frac{1 }{2 }  \delta(E-M/2) \sqrt{E^2-m^2} E\mathrm{d}E \\
&=\frac{g^2 }{8\pi M^2 } \left(M^2 - 4m^2 \right)^{3/2}
\end{aligned}
$$

对应衰变寿命为

$$
\tau
=\frac{8\pi M^2 }{g^2 } \left(M^2-4m^2 \right)^{-3/2}
$$





## 4.13 非相对论情况下 Rutherford 散射问题

## 4.14 光子和电子的散射（Compton 效应）

设动量为 $h\nu_0/c $ 的光子与质量为 $m $ 的静止于 $O $ 点质量为 $m $ 的电子相撞，其结果：电子以速度 $v $ 向 $\varphi $ 角方向运动，光子以动量 $h\nu/c $ 向 $\theta $ 方向偏转。

### Compton 效应的 $M_{i-f}^{(2)} $ 矩阵元素

反应式：

$$
e^- + \gamma \to e^- + \gamma
$$

最低阶费曼图有两张。

### 截面

### 光子角分布公式

### 总截面



## 4.15 正负电子对湮灭为两个光子

$$
e^+ + e^- \to \gamma + \gamma'
$$



## 4.16 高能电子对撞

## 4.17 $\mu $ 粒子衰变

$$
\mu^- \to e^- + \nu_\mu + \bar{\nu}_e,\quad
\mu^+ \to e^+ + \nu_e + \bar{\nu}_\mu
$$

### 弱相互作用哈密顿量和 $\lambda $ 的计算公式

### 平均求和

### 终态动量积分




