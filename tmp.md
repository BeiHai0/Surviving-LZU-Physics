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