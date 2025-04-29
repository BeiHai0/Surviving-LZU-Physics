约定度规 $(-,+,+,+) $

约定公式采用几何单位制 $G=c=1 $ 表述。

# 1

## 非线性电动力学模型和场方程

### 麦克斯韦的拉氏量

$$
F
=\frac{1 }{2 } (B^2-E^2)
$$

$$
L_{\mathrm{maxwell}}
=-F \tag{1}
$$

### BI 模型的拉氏量

$$
L_{\mathrm{BI}}
=\frac{2 }{\beta } \left(1-\sqrt{1+\beta F} \right) \tag{2}
$$

$\beta $ 是任意常数。

弱场极限 $\beta F\ll 1 $ 下，BI 模型的拉氏量可近似为：

$$
L_{\mathrm{BI}}
=\frac{2 }{\beta } \left(1-\sqrt{1+\beta F} \right)
\approx -F + \frac{1 }{4 } \beta F^2 - \frac{1 }{8 } \beta^2 F^3 +\mathcal{O}\left(\beta^3 F^4 \right) \tag{3}
$$

当 $\beta\to 0 $，BI 模型的拉氏量与线性麦克斯韦的拉氏量相同。

### novel NLE 模型的拉氏量

$$
L_{\mathrm{general}}(F)
=-\frac{\left(aF+1 \right)^m }{\delta(bF+1)^n } \left(\beta F \right)^p \tag{4}
$$

$m,n,p $ 是无量纲常数，$a,b,\beta,\delta $ 是长度平方量纲的任意常数。

在弱场极限下，拉氏量可近似为：

$$
L_{\mathrm{general}}(F)
=-\frac{\left(aF+1 \right)^m }{\delta(bF+1)^n } \left(\beta F \right)^p
\approx -c\left[F^p + c_1 F^{p+1} +c_2 F^{p+2}  + \mathcal{O}\left(c_3 F^{p+3} \right) \right] \tag{5}
$$

$p=1 $ 时得到麦克斯韦的拉氏量。

通过分析取 $m=1,n=m+1,a=-3b $

得到含有两个参数的拉氏量且遵守麦克斯韦极限的拉氏量：

$$
L(F)
=\frac{\gamma(3\eta F - 1 )F }{(1+\eta F)^2 } \tag{6}
$$

其中，$\gamma=\beta/\delta $ 和 $\eta $ 是任意参数。

当 $\eta F\ll 1 $，即弱场极限下，拉氏量近似为：

$$
L(F)
=\frac{\gamma(3\eta F - 1 )F }{(1+\eta F)^2 } 
\approx -\gamma F + 5\gamma \eta F^2 -9\gamma \eta^2 F^3 + \gamma\mathcal{O}\left(\eta^3F^4 \right) \tag{7}
$$

平坦时空中 (6) 式给出的拉氏量给出的 E-L 运动方程：

$$
\partial_\mu\left(L_F F^{\mu\nu} \right) = 0 \tag{8}
$$

其中，

$$
L_F
\equiv \frac{\partial L }{\partial F } 
=\frac{\gamma(-1+7\eta F) }{(1+\eta F)^3 } \tag{9}
$$

$F^{\mu \nu} $ 是麦克斯韦场强张量。

利用电位移矢量 $\vec{D} $ 与 $\vec{E} $ 的关系 $\vec{D}=\partial L/\partial \vec{E} $，可从 (6) 式得到：

$$
\vec{D}
=\gamma\frac{1-7\eta F }{(1+\eta F)^3 } \vec{E} \tag{10}
$$

(10) $D_i = \varepsilon_i^{~~ j } E_j $

$$
\varepsilon_{ij} = \gamma \frac{1-7\eta F }{(1+\eta F)^3 }\delta_{ij} \tag{11}
$$

磁场 $\vec{H}=-\partial L/\partial \vec{B} $ 结合 (6) 中拉氏量

$$
\vec{H}
=\gamma \frac{1-7\eta F }{(1+\eta F)^3 } \vec{B} \tag{12}
$$

磁感应强度 $B_i=\mu_i^{~~j}H_j $

磁导率张量的逆 $\left(\mu^{-1} \right)_{ij} $

$$
\left(\mu^{-1} \right)_{ij}
=\gamma \frac{1-7\eta F }{(1+\eta F)^3 } \delta_{ij} \tag{13}
$$

无源麦克斯韦方程：

$$
\nabla\cdot\vec{D} = 0,\quad
\frac{\partial \vec{D} }{\partial t } - \nabla\times\vec{H}= \vec{0} \tag{14}
$$

Bianchi identity $\partial_\mu \tilde{F}^{\mu \nu}=0 $，$\tilde{F}^{\mu\nu} $ 是场强张量的对偶。

$$
\nabla\cdot\vec{B} = \vec{0},\quad 
\frac{\partial \vec{B} }{\partial t } + \nabla\times\vec{E} = \vec{0} \tag{15}
$$

静电极限(electrostatic limit)：$\vec{B}=\vec{H}=\vec{0} $

对点电荷

$$
\nabla\cdot\vec{D} = e\delta(\vec{r}) \tag{16}
$$

解：

$$
\vec{D}
=\frac{e }{4\pi r^3 } \vec{r} \tag{17}
$$

结合 (10) 结合 $F=-E^2/2 $

$$
E+\frac{7 }{2 } \eta E^3
=\frac{e }{4\gamma \pi r^2 } \left(1-\frac{\eta  }{2 } E^2 \right)^3 \tag{18}
$$

上式限制 $F>-1/\eta $

弱场极限 $\eta F\ll 1 $，$E(r) $ 可按 $\eta $ 展开

$$
E
=E_{(0)} + \eta E_{(1)} + \eta^2 E_{(3)} + \mathcal{O}\left(\eta^3 \right) \tag{19}
$$

$E_{(1)},E_{(2)} $ 分别代表对电场 $E_{(0)} $ 的一阶和二阶修正。

$E_{(0)} $ 的单位是长度的倒数，$E_{(1)} $ 的单位是长度平方的倒数，

比较系数

$$
E_{(0)}
=\frac{e }{4\pi\gamma r^2 } \tag{20}
$$

$$
E_{(1)} 
=-\frac{7 }{2 } E_{(0)}^3 - \frac{e }{4\pi \gamma r^2 } E_{(0)}^2 \tag{21}
$$

$$
E_{(2)}
=-\frac{21 }{2 } E_{(0)}^2 E_{(1)} + \frac{e }{4\pi\gamma r^2 } \left(-3E_{(0)}E_{(1)} + \frac{3 }{4 } E_{(0)}^4 \right) \tag{22}
$$

弱场极限

$$
E
\approx \frac{e }{4\pi\gamma r^2 } - 5\eta\left(\frac{e }{4\pi\gamma r^2 }  \right)^3 + \frac{273 }{4 } \eta^2\left(\frac{e }{4\pi\gamma r^2 }  \right)^5 + \mathcal{O}\left(\eta^3 \right) \tag{23}
$$

电场最大值

$$
E_{\max}
=\sqrt{\frac{2 }{\eta } } \tag{24}
$$

NLE 模型中电场有限。

当 $\eta\to 0 $，电场发散。

### 点电荷能量

希尔伯特应力-能量张量(Hilbert stress-energy tensor)

$$
T_{\mu\nu}^H
\equiv -\frac{2 }{\sqrt{-g} } \left(\frac{\partial \left(\sqrt{-g}L(F) \right) }{\partial g^{\mu\nu} }  \right)\bigg|_{g=\eta} \tag{25}
$$

可得

$$
T_{\mu\nu}^H
=\eta_{\mu\nu}L(F) - L_FF_\mu^\alpha F_{\nu\alpha} \tag{26}
$$

电能密度

$$
\rho
=-T_t^t
=-L_FE^2-L(F)
=\frac{\gamma E^2\left[1+\frac{3 }{2 } \eta E^2 \left(4+\frac{\eta }{2 } E^2 \right) \right] }{2\left(1-\frac{\eta }{2 } E^2 \right)^3 } \tag{27}
$$

总电能

$$
\epsilon
=4\pi\int_{0}^{+\infty} \rho(r)r^2\mathrm{d}r \tag{28}
$$

转化为对 $E $ 的积分

$$
\epsilon
=\frac{e^{3/2} }{\sqrt{4\pi\gamma} } \int_{0}^{\sqrt{\frac{2 }{\eta  } }} \frac{\sqrt{\left(2-\eta E^2 \right)\left[4+3\eta E^2\left(8+\eta E^2 \right) \right]\left[4+\eta E^2\left(52+21\eta E^2 \right) \right]} }{16\sqrt{E}\left(2+7\eta E^2 \right)^{5/2} } \mathrm{d}E \tag{29}
$$

总能量有限。

### 真空双折射(vacuum birefringence)

考虑平面电磁波 $(\vec{e},\vec{b}) $ 沿 $z $ 轴在两片平行电容板间传播，$x $ 轴方向有匀强电场。外电场 $\bar{\vec{E}}=(\bar{E},0,0) $，总电场 $\vec{E}=\vec{e}+\bar{\vec{E}},\vec{B}=\vec{b} $，设 $\vec{e} $ 远小于 $\bar{\vec{E}} $，(6) 拉氏量

$$
L\left(\vec{e}+\bar{\vec{E}},\vec{b} \right)
=\gamma\frac{\left\{\frac{3 }{2 } \eta\left[\vec{b}^2-\left(\vec{e}+\bar{\vec{E}} \right)^2 \right] - 1 \right\}\left[\vec{b}^2-\left(\vec{e}+\bar{\vec{E}} \right)^2 \right] }{2\left\{1+\frac{\eta }{2 } \left[\vec{b}^2-\left(\vec{e} + \bar{\vec{E}}^2 \right) \right] \right\}^2 } \tag{30}
$$

忽略高阶项

$$
L^{(2)}(\vec{e}+\bar{\vec{E}},\vec{b})
=\frac{\gamma\eta\left(5+\frac{7 }{2 } \eta \bar{\vec{E}}^2 \right) }{\left(1-\frac{\eta }{2 } \bar{\vec{E}}^2 \right)^4 }\left(\vec{e}\cdot\bar{\vec{E}} \right)^2 - \frac{1 }{2 } \gamma \frac{\left(1+\frac{7 }{2 } \eta \bar{\vec{E}}^2 \right) }{\left(1-\frac{\eta }{2 } \bar{\vec{E}}^2 \right)^3 }\left(\vec{b}^2-\vec{e}^2 \right) \tag{31}
$$

电位移矢量和磁场强度

$$
d_i = \frac{\partial L^{(2)} }{\partial e_i } = \left(\alpha\delta_i^j+\beta\bar{E}_i\bar{E}^j \right)e_j,\quad
h_i
=-\frac{\partial L^{(2)} }{\partial b_i } 
=\alpha\delta_i^j b_j \tag{32}
$$

$$
\beta = \frac{2\gamma \eta\left(5+\frac{7 }{2 } \eta \bar{\vec{E}}^2 \right) }{\left(1-\frac{\eta }{2 } \bar{\vec{E}}^2 \right)^4 },\quad 
\alpha = \gamma \frac{\left(1+\frac{7 }{2 }\eta\bar{\vec{E}}^2 \right)  }{\left(1-\frac{\eta }{2 } \bar{\vec{E}}^2 \right)^3 } \tag{33}
$$

关系 $d_i=\varepsilon_i^j e_j,h_i=\left(\mu^{-1} \right)_i^j b_j $

$$
\varepsilon_{ij} = \alpha\delta_{ij} + \beta\bar{E}_i\bar{E}_j ,\quad
\left(\mu^{-1} \right)_{ij} = \alpha\delta_{ij} \tag{34}
$$

平面波麦克斯韦方程

$$
k_i d^i = k_i b^i = 0,\quad
\vec{k}\times\vec{e} = \omega\vec{b},\quad
\vec{k}\times\vec{h} = -\omega\vec{d} \tag{35}
$$


$$
\left\{\varepsilon^{ijk}\varepsilon_{lmn} \left(\mu^{-1} \right)_k^l k_j k^m+\omega^2\epsilon_n^i \right\}e^n = 0
$$

$\varepsilon_{ijk} $ 是反对称张量。

矩阵形式

$$
\Lambda \vec{e} = 0 \tag{37}
$$

$$
\Lambda
\equiv \begin{bmatrix}
-k^2 \alpha+\omega^2\left(\alpha+\beta\bar{E} \right) &0 &0 \\
0 &-k^2\alpha+\omega^2\alpha &0 \\
0 &0 &\omega^2\alpha
\end{bmatrix} \tag{38}
$$

由 $\mathrm{det}(\Lambda)=0 $ 可知电场有两种模式。两种模式定义了色散关系。折射率定义为 $n\equiv k/\omega $，因此有两种不同的折射率：

$$
n_\parallel = \sqrt{1+\frac{\beta }{\alpha } \bar{E}^2},\quad
n_\perp = 1 \tag{39}
$$

不同偏振的电磁波有不同的速度 $v_\parallel=n_\parallel^{-1},v_\perp=1 $

### 拉格朗日函数的因果性和单一性条件

若拉氏量满足不等式：

$$
L_F \leqslant 0,
L_{FF}\geqslant 0,
L_F + 2F L_{FF} \leqslant 0\tag{40}
$$

则群速度不超过真空光速，且动能非负。

$$
L_F
= ,
L_{FF}
= \tag{41}
$$

#### 电场部分

取 $B=0 $，拉氏量 $\displaystyle{L(F)=-\frac{\left(aF+1 \right)^m }{\delta(bF+1)^n } \left(\beta F \right)^p }$ ，前两个不等式给出

$$
n\geqslant m+1,a\leqslant 0,b\geqslant 0\tag{42}
$$

在此基础上，第三个不等式自动满足。

#### 磁场部分

取 $E=0 $，类似可得

$$
n\geqslant m+1,a\geqslant 0,b\leqslant 0\tag{43}
$$

#### $n=m+1,a=-3b $ 时的因果性和单一性条件

$$
L_F
=\frac{\gamma\left(-1+7\eta F \right) }{\left(1+\eta F \right)^3 },
L_{FF}
=\frac{2\gamma \eta\left(5-7\eta F \right) }{\left(1+\eta F \right)^4 } \tag{44} 
$$

$$
L_F + 2FL_{FF} 
=\gamma \frac{-\eta F\left(26-21\eta F \right) }{\left(1+\eta F \right)^4 } \tag{45}
$$

仅电场部分，取 $B=0 $，因果性和单一性条件三个不等式给出

$$
-\frac{2+7\eta E^2 }{\left(2-\eta E^2 \right)^3 } \leqslant 0,
\frac{10+7\eta E^2 }{\left(2-\eta E^2 \right)^4 } \geqslant 0,
\frac{-4-\eta E^2\left(521\eta E^2 \right) }{\left(2-\eta E^2 \right)^4 } \leqslant 0 \tag{46}
$$


所有情况都有 $E<\sqrt{2/\eta} $，$E_{\max}=\sqrt{\eta/2} $

分析磁场，取 $E=0 $，前两个不等式给出

$$
\left(-1+\frac{7 }{2 } \eta B^2 \right)\leqslant 0,
\left(5-\frac{7 }{2 } \eta B^2 \right)\geqslant 0 \tag{47}
$$

可以得到 $F<1/7\eta $

第三不等式给出

$$
-2+\eta B^2\left(26-\frac{21 }{2 } \eta B^2 \right)\leqslant 0\tag{48}
$$

得到 $(13-2\sqrt{37})/21<\eta F<(13+2\sqrt{37})/21 $

### 新 NLE 模型与 GR 耦合

通过作用量把拉氏量 $L(F) $ 与引力进行最小耦合

$$
I
=\int \mathrm{d}^4 x\sqrt{-g}\left(\frac{R }{\kappa } + L(F) \right) \tag{49}
$$

其中 $R $ 为里奇标量。变分可得运动方程

$$
\nabla_\mu\left(\frac{\partial L }{\partial F } F^{\mu\nu} \right)
=0 \tag{50}
$$

$$
R_{\mu\nu} - \frac{1 }{2 } g_{\mu\nu} R
=\kappa T_{\mu\nu} \tag{51}
$$

其中 $R_{\mu\nu} $ 为里奇张量，$T_{\mu\nu} $ 为 Hilbert 能量-动量张量，在弯曲时空表达为

$$
T_\mu^\nu
=L\delta_\mu^\nu - L_F F_{\mu\lambda} F^{\nu \lambda} \tag{52}
$$

考虑球对称静态时空，线元

$$
\mathrm{d}s^2
=-f(r)\mathrm{d}t^2 + \frac{1 }{f(r) } \mathrm{d}r^2 + r^2\left(\mathrm{d}\theta^2+\sin^2\theta\mathrm{d}\phi^2 \right) \tag{53}
$$

假设 $F_{tr},F_{\theta\phi} $ 在 $F_{\mu\nu} $ 非零，$F_{tr}=-F_{rt} $ 代表径向电场，$F_{\theta\phi}=-F_{\phi\theta} $ 代表径向磁场。应力能动-张量非零分量

$$
T_t^t = T_r^r
=L(F) - L_F F_{tr}F^{tr},
T_\theta^\theta
=T_\phi^\phi
=L(F) - L_F F_{\theta\phi}F^{\theta\phi} \tag{54}
$$

只关注纯磁场解和纯电场解。

#### the magnetic regular black hole solution

纯磁场解来自 $F_{tr=0} $，非零麦克斯韦张量分量 $F_{\theta\phi}=-q_m \sin\theta $，$q_m $ 为常数，可理解为一个磁单极子的总荷量，导致径向磁场 $B_r=q_m/r^2 $，麦克斯韦不变量 $F=q_m^2/2r^4 $；$r=0 $ 处奇异

magnetic monopole 能动张量

$$
T_t^t
=T_r^r
=\frac{\gamma q_m^2\left(3\eta q_m^2-2r^4 \right) }{\left(2r^4+\eta q_m^2 \right)^2 } \tag{55}
$$

$$
T_\theta^\theta
=T_\phi^\phi
=\frac{\gamma q_m^2\left(4 r^8-2\eta q_m^2 r^4+3\eta^2q_m^4 \right) }{\left(2r^4+\eta q_m^2 \right)^3 } \tag{56}
$$

由线元可得爱因斯坦张量

$$
G_\mu^\nu
=\mathrm{diag}\left[\frac{f' }{r } + \frac{f-1 }{r^2 } ,\frac{f' }{r } + \frac{f-1 }{r^2 } , \frac{f'' }{2 } + \frac{f' }{r } , \frac{f'' }{2 } + \frac{f' }{r }  \right] \tag{57}
$$

$' $ 代表度规函数 $f(r) $ 的径向微分。爱因斯坦非线性麦克斯韦方程 $tt $ 或 $rr $ 分量简化为

$$
\frac{f' }{r } + \frac{f-1 }{r^2 } 
=\kappa \frac{\gamma q_m^2\left(3\eta q_m^2-2r^4 \right) }{\left(2r^4+\eta q_m^2 \right)^2 } \tag{58}
$$

解上面方程可得度规函数

$$
f(r)
=1+\frac{c_0 }{r } + \frac{\kappa \gamma q_m^2 r^2 }{2r^4+\eta q_m^2 } \tag{59}
$$

$c_0 $ 是积分常数。

选择

$$
c_0=0,
\gamma=-\frac{2b_0^2 }{\kappa q_m^2} ,
\eta=\frac{2g^4 }{q_m^2 } \tag{60}
$$

$b_0,g $ 是长度量纲常数。

线元可改写为

$$
\mathrm{d}s^2
=-\left(1-\frac{b_0^2r^2 }{r^4+g^4 }  \right)\mathrm{d}t^2 + \left(1-\frac{b_0^2r^2 }{r^4+g^4 }  \right)^{-1}\mathrm{d}r^2 + r^2\left(\mathrm{d}\theta^2+\sin^2\theta \mathrm{d}\phi^2 \right) \tag{61}
$$

当 $r$ 趋于无穷大，时空度规渐近平坦

$$
g_{tt}\to -1,g_{rr}\to 1 \quad \mathrm{as}\quad r\to\infty
$$

对于很小的 $r$，其行为与 de-Sitter 时空相似

$$
g_{tt}\to -\left(1-c^2r^2 \right),\quad g^{rr} \to \left(1-c^2r^2 \right)\quad \mathrm{as}\quad r\to 0
$$

其中，$c $ 是常数。

$g_{tt}=0$ 给出无限红移面的位置。若度规参数满足 $0<g<0.5 b_0^2 $，则上面几何代表一系列双视界黑洞；当 $g^2=0.5b_0^2$，得到单视界黑洞；若 $g^2>0.5b_0^2$，则黑洞没有视界。特别地，当 $g^2=0$，黑洞有一个视界。

#### 曲率张量和不变量的正则性

可通过黎曼和里奇张量各分量是否发散来判断时空的正则性、奇异性。坐标基底，非零黎曼曲率张量分量

$$
R^0_{~~ 110} 
=-\frac{b_0^2\left(3r^8 - 12 g^4 r^4 + g^8 \right) }{\left(r^4+g^4 \right)^3 } 
$$

$$
R^0_{~~220} = R^0_{~~330} = R^2_{~~112} = R^3_{~~113}
=\frac{b_0^2\left(r^4-g^4 \right) }{\left(r^4+g^4 \right)^2 } \tag{62}
$$

$$
R^3_{~~223}
=-\frac{b_0^2 }{r^4+g^4 } 
$$

非零 Ricci 张量分量

$$
R_{00} = -R_{11} = -\frac{b_0^2\left(r^8-12g^4r^4+3g^8 \right) }{\left(r^4+g^4 \right)^3 } 
$$

$$
R_{22} = R_{33} = \frac{b_0^2 \left(3g^4-r^4 \right) }{\left(r^4+g^4 \right)^2 } \tag{63}
$$

当 $r\to 0 $，两个张量的分量都有限；当 $r\to \infty $，所有分量趋于零。

三个标量不变量：

Ricci 张量

$$
R = g^{\mu\nu}R_{\mu\nu}
=\frac{4b_0^2\left(3g^8-5g^4r^4 \right) }{\left(r^4+g^4 \right)^3 } \tag{64}
$$

Ricci contraction

$$
R_{\mu\nu} R^{\mu\nu}
=\frac{4b_0^2 \left(r^{16}-14g^4r^{12}+74g^8r^8-30g^{12}r^4+9g^{16} \right) }{\left(r^4+g^4 \right)^6 } \tag{65}
$$

Kretschmann scalar

$$
K
=R_{\mu\nu\lambda\delta} R^{\mu\nu\lambda\delta}
=\frac{8\left(3g^{16}-10g^{12}r^4+74 g^8 r^8-34g^4r^{12}+7r^{16} \right)b_0^4 }{\left(r^4+g^4 \right)^6 } \tag{66}
$$

在 $r\to 0$ 时，三个不变量也都有限。 

#### 能量情况

定义 $\rho=-T_t^t,\tau=t_r^r,p=T_\theta^\theta=T_\phi^\phi $，利用 (55)(56)(60)

$$
\rho=-\tau
=\frac{b_0^2\left(3g^4-r^4 \right) }{\kappa \left(r^4+g^4 \right)^2 } 
$$

$$
p
=-\frac{b_0^2\left(3g^8-12g^4r^4+r^8 \right) }{\kappa \left(r^4+g^4 \right)^3 } \tag{67}
$$

NEC (Null Energy Condition) $\rho+\tau \geqslant 0,\rho+p\geqslant 0 $，第一个在 $\rho+\tau=0 $ 时自动满足；

$$
\rho+p
=\frac{2b_0^2 r^4\left(r^4-7g^4 \right) }{\kappa \left(r^4+g^4 \right)^3 } \tag{68}
$$

第二个满足，只能 $r^4\leqslant 7g^4 $


#### electric naked sigularity solution

纯电解 $F_{\theta\phi=0} $

能动张量


$$
T_t^t = T_r^r = L(F)-2F L_F
=\frac{\gamma E^2\left[4+3\eta E^2\left(8+\eta E^2 \right) \right] }{\left(-2+\eta E^2 \right)^3 } \tag{69}
$$


$$
T_\theta^\theta
=T_\phi^\phi
=L(F)
=\frac{\gamma E^2\left(2+3\eta E^2 \right) }{\left(-2+\eta E^2 \right)^2 } \tag{70}
$$

替换 $F=-E^2/2 $

爱因斯方程给出度规函数满足的方程

$$
\frac{f' }{r } + \frac{f-1 }{r^2 }
=\frac{\gamma \kappa E^2\left[4+3\eta E^2\left(8+\eta E^2 \right) \right] }{\left(-2+\eta E^2 \right)^3 } 
$$

$$
\frac{f'' }{2 } + \frac{f' }{2 } = \frac{\gamma \kappa E^2\left(2+3\eta E^2 \right) }{\left(-2+\eta E^2 \right)^2 } \tag{71}
$$

电场是 $r $ 的函数

弱场极限 $\eta F\ll 1 $，展开

$$
f(r)
=1+\frac{c }{r } \eta^0 f_{(0)} + \eta f_{(1)} + \eta^2 f_{(2)} + \mathcal{O}\left(\eta^3 \right) \tag{72}
$$

$1+c/r $ 是爱因斯坦方程的真空解。

$$
\frac{f''_{(0)} }{2 } + \frac{f'_{(0)} }{r } = \frac{\gamma \kappa }{2 } E_{(0)}^{2} \tag{73}
$$

$$
\frac{f_{(1)}'' }{2 }  + \frac{f_{(1)}' }{r } = \frac{\gamma \kappa  }{2 } \left(2E_{(0)} E_{(1)} +\frac{5 }{2 } E_{(0)}^4 \right) \tag{74}
$$

$$
\frac{f_{(2)}'' }{2 }  + \frac{f_{(2)}' }{r } = \frac{\gamma \kappa  }{2 }\left(E_{(1)}^2 + 10 E_{(0)}^3 E_{(1)} +2 E_{(0)}E_{(2)} + \frac{9 }{4 } E_{(0)}^6 \right) \tag{75}
$$

度规函数可表达

$$
f(r)
=1+\frac{c }{r } + c_{(0)} \eta^0 \frac{e^2 }{r^2  } + c_{(1)} \eta \frac{e^4 }{r^8 } + c_{(2)} \eta^2 \frac{e^6 }{r^{10} } + \mathcal{O}\left(\eta^3 \right) \tag{76}
$$

$E^2\to \tilde{E} $

$$
r\frac{\mathrm{d}f(r) }{\mathrm{d}r } + f(r)-1
=r^2 \frac{\gamma \kappa \tilde{E}\left[4+3\eta \tilde{E}\left(8+\eta \tilde{E} \right) \right] }{\left(-2+\eta \tilde{E} \right)^3 } \tag{78}
$$

$\tilde{E}\in \left[2/\eta ,0 \right] $

$$
\frac{4\tilde{E}\left(-2+\eta \tilde{E} \right)\left(2+7\eta\tilde{E} \right) }{4+\eta \tilde{E}\left(52+21\eta\tilde{E} \right) } \frac{\mathrm{d}f }{\mathrm{d}\tilde{E} } + f\left(\tilde{E} \right) - 1
=-\frac{e\kappa \sqrt{\tilde{E}} \left[4+3\eta \tilde{E}\left(8+\eta\tilde{E} \right) \right] }{16\pi\left(2+7\eta\tilde{E} \right) } \tag{79}
$$

Ricci  标量



$$
R
=g_{\mu\nu} R^{\mu\nu}
=\frac{4 }{r^2 } - \frac{4f(r) }{r^2 } - \frac{8f'(r) }{r } - 2f''(r) \tag{80}
$$

$$
R
=-8\kappa \left(L-FL_F \right)
=-\frac{8\gamma\kappa \eta\tilde{E}^2\left(10+3\eta\tilde{E} \right) }{\left(-2+\eta\tilde{E} \right)^3 } \tag{81}
$$

Ricci contraction

$$
R_{\mu\nu} R^{\mu\nu}
=8\left[\frac{f'(r) }{r } + \frac{f(r)-1 }{r^2 }  \right]^2 + 8 \left[\frac{f'(r) }{r } + \frac{f''(r) }{2 }  \right]^2 \tag{82}
$$

$$
R_{\mu\nu} R^{\mu\nu}
=8\kappa\left[\left(L - 2FL_F \right)^2 + L^2 \right]
=\frac{16\kappa \gamma^2 \tilde{E}^2 \left\{16+\eta \tilde{E}\left[112+\eta\tilde{E}\left(296+3\eta \tilde{E}\left(20+3\eta\tilde{E} \right) \right) \right] \right\} }{\left(-2+\eta\tilde{E} \right)^6 } \tag{83}
$$

# 2 Nonlinear electrodynamics and black holes

## NLED formalism

$$
F_{\mu\nu}
=2A_{[\mu,\nu]} \tag{1}
$$

$$
F = \frac{1 }{4 } F_{\alpha\beta}F^{\alpha\beta},\quad
\tilde{G} = \frac{1 }{4 } F_{\alpha\beta} \tilde{F}^{\alpha\beta} \tag{2}
$$

$F_{\mu\nu} $ 有一个独立的不变量和一个独立的伪不变量（pseudoinvariant）

$\tilde{F}^{\alpha\beta}=\left(\mathrm{i}/2\sqrt{-g} \right) \varepsilon^{\alpha\beta\gamma\delta}F_{\gamma\delta} $ 是 $F^{\alpha\beta} $ 的对偶

### $(F,\tilde{G}) $ and $(P,\tilde{Q}) $ frameworks

$$
P^{\alpha\beta}
=2\frac{\partial L }{\partial F_{\alpha\beta} } 
=\frac{\partial L }{\partial F } F^{\alpha\beta} + \frac{\partial L }{\partial \tilde{G} } \tilde{F}^{\alpha\beta} \tag{3}
$$

$$
H
=\frac{1 }{2 } P^{\alpha\beta} F_{\alpha\beta} - L\left(F,G^2 \right) \tag{4}
$$

与 $P^{\alpha\beta} $ 有关的不变量：

$$
P = \frac{1 }{4 } P_{\alpha\beta} P^{\alpha\beta},\quad
\tilde{Q} = \frac{1 }{4 } P_{\alpha\beta}\tilde{P}^{\alpha\beta} \tag{5}
$$

哈密顿方程

$$
F^{\alpha\beta}
=2\frac{\partial H }{\partial P_{\alpha\beta} } 
=\frac{\partial H }{\partial P } P^{\alpha\beta} + \frac{\partial H }{\partial Q } \tilde{P}^{\alpha\beta} \tag{6}
$$

NLED 与引力耦合作用量：

$$
S
=\int \mathrm{d}^4 x\sqrt{-g} \left\{R(16\pi)^{-1}-L \right\} \tag{7}
$$

$R $ 是曲率标量；$g:=\mathrm{det}\left|g_{\mu\nu} \right| $

$$
L
=\frac{1 }{2 } P^{\mu\nu}P_{\mu\nu} - H\left(P,\tilde{Q} \right) \tag{8}
$$

能动张量和曲率标量

$$
4\pi T_{\mu\nu}
=H_{,P} P_{\mu\alpha} P_\nu^\alpha - g_{\mu\nu}\left(2P H_{,P} + \tilde{Q} H_{,\tilde{Q}} - H \right) \\
R
=8\left(P H_{,P} + \tilde{Q} H_{,\tilde{Q}} - H \right) \tag{9}
$$

其中，$\partial H/\partial P = H_{,P} $ 

Born-Infeld NE 由结构函数 $H(P,\tilde{Q}) $ 给出：

$$
H = b^2\left(1-\sqrt{1-2P/b^2+\tilde{Q}^2/b^4} \right) \tag{10}
$$

其中，$b $ 是最大场强，是 BI 理论中的参数。

### NLED energy conditions

类时矢量 $V^\alpha,V_\alpha V^\alpha<1 $ ，local energy density 非负 $T_{\mu\nu}V^\mu V^\nu\geqslant 0 $；local energy flow 矢量是非类空的要求 $T_{\alpha\beta}T_\gamma^\alpha V^\beta V^\gamma\leqslant 0 $

$$
H_{,P}>0,\quad
\left(P H_{,P} + \tilde{Q} H_{,\tilde{Q}} - H \right) \geqslant 0 \tag{11}
$$

strong energy condition(SEC) $R_{\mu\nu}V^\nu V^\nu\geqslant 0 $，结合爱因斯坦方程

$$
R_{\mu\nu}V^\mu V^\nu 
=8\left(T_{\mu\nu} V^\mu V^\nu + \frac{T }{2 }  \right) \geqslant 0\tag{12}
$$

## NLED Black holes

SSS 线元

$$
\mathrm{d}s^2 = -\psi\mathrm{d}t^2 + \psi^{-1} \mathrm{d}r^2 + r^2\left(\mathrm{d}\theta^2+\sin^2\theta\mathrm{d}\phi^2 \right) \tag{13}
$$

一种解为

$$
\psi
=1-\frac{8\pi }{r } \int_{0}^{r} \left(\sqrt{r^4+1} - r^2 \right)\mathrm{d}r \tag{14}
$$

上面的解有正则奇点；另一个正则解 $D_{,r}=1/r,E_{,r}=r^2/\left(r^4+1 \right) $

度规函数

$$
\psi_{HI}
=1-\frac{k }{r } + \frac{8\pi\gamma }{r } \int_{0}^{r} \left[r^2\ln\left(\frac{r^4 }{1+r^4 }  \right) \right] \mathrm{d}r \tag{15}
$$

SSS 线元 PT

$$
\psi_{PT}
=1-\frac{d }{r } + \frac{8\pi }{r } \int_{0}^{r} H(x) x^2\mathrm{d}x \tag{16}
$$

$$
F_{\mu\nu}
=-\frac{e }{r^2 } \frac{\partial H(P,0) }{\partial P } 2\delta_\mu^{[0}\delta_{\nu}^{r]}
$$

$P=-e^2/4r^2 $

$$
H(P)
=P\frac{1-3\Pi }{\left(1+\Pi \right)^3 } + \frac{6 }{q^2 s } \left(\frac{\Pi }{1+\Pi }  \right)^{5/2 } \tag{18}
$$

$$
H(P)
=P/\cosh^2\left(\sqrt{\Pi} \right) \tag{19}
$$

$$
H(P)
=P\frac{\exp\left(-s\sqrt{\Pi} \right) }{\left(1+\Pi \right)^{5/2} } \left(1+\frac{3\Pi }{s } + \Pi \right) \tag{20}
$$

### Type-D solutions with EBI

### 3.2 Born-Infeld black hole and EBIon

$$
\Psi_{BI}(r)
=1-\frac{2m }{r } + \frac{2 }{3 } b^2\left(r^2-\sqrt{r^4+a^4} \right) + \frac{4g^2 }{3r } G(r) \tag{21}
$$

$$
G'(r)
=-\left(r^4+a^4 \right)^{-1/2} \tag{22}
$$

$$
F_{rt}
=g\left(r^4+a^4 \right)^{-1/2},\quad
P_{rt}
=\frac{g }{r^2 } \tag{23}
$$

$$
G(r)
=\int_{r}^{\infty} \frac{\mathrm{d}s }{\sqrt{s^4+a^4} } 
=\frac{1 }{2a } \mathbb{F} \left[\arccos\left(\frac{r^2-a^2 }{r^2+a^2 }  \right) , \frac{1 }{\sqrt{2} }  \right] \tag{24}
$$

$$
G(r)
=\int_{0}^{r} \frac{-\mathrm{d}s }{\sqrt{s^4+a^4} } 
=-\frac{1 }{2a } \mathbb{F}\left[\arccos\left(\frac{a^2-r^2 }{a^2+r^2 } , \frac{1 }{\sqrt{2} }  \right) \right] \tag{25}
$$

$$
\int_r ^{\infty} \frac{\mathrm{d}s }{\sqrt{s^4+a^4} } + \int_0^r \frac{\mathrm{d}s }{\sqrt{s^4+a^4} } 
=\frac{1 }{a } \mathrm{K}\left[\frac{1 }{2 }  \right] \tag{26}
$$

$$
\Psi_2
=\frac{m }{r^3 } - \frac{g^2 r^3 }{6 } \partial_{,rr} \left(\frac{1 }{r^2 } \int_r^\infty \frac{\mathrm{d}s }{s^2+\sqrt{s^4+a^4} }  \right) \tag{27}
$$

### Trajectories of test particles in BI black hole

#### Massive particals

$$
\frac{\mathrm{d}^2 x^\nu }{\mathrm{d}\tau^2 } + \Gamma_{\alpha\beta}^\nu \frac{\mathrm{d}x^\alpha }{\mathrm{d}\tau } \frac{\mathrm{d}x^\beta }{\mathrm{d}\tau } 
=-\frac{\varepsilon }{\mu } F_{\sigma}^{\nu} \mathrm{d}x^\sigma \mathrm{d}\tau \tag{28}
$$

$$
\dot{t} \Psi_{BI}
=E + \frac{\varepsilon g }{\mu } \sqrt{\frac{b }{4g } } \mathbb{F} \left[\arccos\left(\frac{r^2-g/b }{r^2+g/b }  , \frac{1 }{\sqrt{2} }  \right) \right] \tag{29}
$$ 

$$
1 = \psi\dot{t}^2 - \psi^{-1} \dot{r}^2 - r^2\dot{\phi}^2 \tag{30}
$$

$$
\dot{r}^2 + \psi\left(\frac{l^2 }{r^2 } + 1 \right) - \left\{E+\frac{\varepsilon g }{\mu } \sqrt{\frac{b }{4g } } \mathbb{F} \left[\arccos\left(\frac{r^2-g/b }{r^2+g/b }  , \frac{1 }{\sqrt{2} }  \right) \right] \right\}^2 \tag{31}
$$

#### 3.3.2

$$
g^{\mu\nu} S_{,\mu} S_\nu = 0\tag{32}
$$

$$
\left(g^{\mu\nu} + \frac{4\pi }{b^2 } T_{\mathrm{NLED}}^{\mu\nu} \right) S_{,\mu} S_\nu
=\gamma^{\mu\nu} S_{,\mu} S_\nu
=0 \tag{33}
$$

$$
\dot{r} = \sqrt{E^2-\frac{\psi_{BI} l^2 }{r^2 } } \tag{34}
$$

$$
\dot{r}_{ph}
=\sqrt{E^2 - \frac{\Psi_{BI} l^2 }{r^2 } \left(1+\frac{a^4 }{r^4 }  \right)^{-1}} \tag{35}
$$

## NLED black hole thermodynamics

$$
\delta M_{\Delta} = \frac{\kappa }{8\pi } \delta a_{\Delta} + \Phi_\Delta \delta Q_\Delta \tag{36}
$$

$$
M_\Delta = \frac{\kappa a_\Delta }{4\pi } + \Phi_\Delta Q_\Delta \tag{37}
$$

$$
M_\Delta = \frac{\kappa a_\Delta }{4\pi } + \Phi_\Delta Q_\Delta + V\left(a_\Delta , Q_\Delta , P_\Delta \right) \tag{38}
$$

$$
a_\Delta \frac{\partial \psi }{\partial a_\Delta } + 8\pi r_\Delta Q_\Delta\frac{\partial\Phi }{\partial a_\Delta } + 8\pi r_\Delta \frac{\partial V }{\partial a_\Delta } = 0 \\
\frac{r_\Delta }{2 } \frac{\partial \psi }{\partial Q_\Delta } + Q_\Delta \frac{\partial \Phi }{\partial Q_\Delta } + \frac{\partial V }{\partial Q_{\Delta} } = 0\tag{39}
$$

### Smarr

$$
\mathcal{L}(F)
=\frac{2 }{2 sg^2 } \left(\frac{2g^2 F }{1+\sqrt{2g^2 F} }  \right)^{5/2} \tag{40}
$$

$$
\psi_B
=1-\frac{2 m(r) }{r } 
=1-\frac{2mr^2 }{\left(r^2+g^2 \right)^{3/2} } \tag{41}
$$

$$
M_\Delta
=\frac{1 }{8\pi } \int\kappa \mathrm{d}a
=\int \left(1-m' \right)\mathrm{d}r \tag{42}
$$

$$
V = m r^3 \frac{2g^2 - r^2 }{\left(g^2 + r^2 \right)^{3/2} } \tag{43}
$$

$$
M_\Delta = \frac{r }{2 } - \frac{m r^3 }{\left(r^2+g^2 \right)^{3/2} } \tag{44}
$$

## 5

$$
M_{\mathrm{sol}}^{(n)} = M_{\mathrm{ADM}}^{(n)} - M_\Delta^{(n)} \tag{45}
$$

$$
M_\Delta^{(b)}(r_\Delta)
=\frac{r_\Delta }{2 } + \frac{b^2 r_\Delta }{3 } \left(r_\Delta^2 - \sqrt{r_\Delta^4 + a^4} \right) - \frac{2g^2 }{3 } \int_0^{r_\Delta} \frac{\mathrm{d}s }{\sqrt{a^4+s^4} } \tag{46}
$$

$$
M_{\mathrm{ADM}}^{(b)}(r_\Delta)
=\frac{r_\Delta }{2 } + \frac{b^2 r_\Delta }{3 } \left(r_\Delta^2 - \sqrt{r_\Delta^4 + a^4} \right) + \frac{2g^2 }{3 } \int_{r_\Delta}^{\infty} \frac{\mathrm{d}s }{\sqrt{a^4+s^4} } \tag{46}
$$

## 6

$$
L(y)>0,\quad
L(y)_{,y}>0,\quad
L(y)_{,yy}>0 \tag{48}
$$

$$
f(y)
\equiv yL_{,yy} / L_{,y} > 0,\quad
f(y) N(y) < 3\tag{49}
$$

$$
L(y)
=b^2\left(\sqrt{1+\frac{y^2 }{b^2 g^2 } } - 1 \right) > 0 \tag{50}
$$

$$
L_{,y} = \frac{y }{g^2 } \left(1 + \frac{y^2 }{b^2 g^2 }  \right)^{-1/2} > 0 \\
L_{,yy} = \frac{1 }{g^2 } \left(1 + \frac{y^2 }{b^2 g^2 }  \right)^{-3/2} > 0 \\
f(y) = y\frac{L_{,yy} }{L_{,y} } = \left(1 + \frac{y^2 }{b^2 g^2 }  \right)^{-1} > 0\tag{51}
$$ 

$$
\psi_{BI}(y)
=1-\frac{2m\sqrt{y} }{g } + \frac{2b^2 g^2 }{3y } \left(1-\sqrt{1+\frac{y^2 }{b^2 g^2 } } \right) + \frac{2\sqrt{gby} }{3 } \mathbb{F}\left[\arccos\left(\frac{gb-y }{gb+y } , \frac{1 }{\sqrt{2} }  \right) \right] \tag{52}
$$

$$
\psi_{BI}(y)
=1-\frac{2m\sqrt{y} }{g } + \frac{2b^2 g^2 }{3y } \left(1-\sqrt{1+\frac{y^2 }{b^2 g^2 } } \right) - \frac{2\sqrt{gby} }{3 } \mathbb{F}\left[\arccos\left(\frac{y-gb }{gb+y } , \frac{1 }{\sqrt{2} }  \right) \right] \tag{53}
$$

$$
E_{\mathrm{avail}}^{(n)}
=M_{\mathrm{ADM}}^{(n)} - M_{\mathrm{ADM}}^{(0)} \tag{54}
$$

$$
M_{\mathrm{ADM}}^{(b)}(r_\Delta) - \frac{r_\Delta }{2 } 
=\frac{b^2 }{3 } \left\{r_\Delta^3\left(1-\sqrt{1+\frac{a^4 }{r_\Delta^4 } } \right) + a^3 \mathbb{F} \left[\arccos\left(\frac{r_\Delta^2 - a^2 }{r_\Delta^2 + a^2 }  \right) , \frac{1 }{\sqrt{2} }  \right] \right\} \tag{55}
$$

# 3

## 1 intro

## 2

### 2.1

$$
\begin{align}
h_\mu^a h_b^\mu = \delta_b^a,\quad
h_\mu^a h_a^\nu = \delta_\mu^\nu.
\end{align}
$$

$$
\begin{align}
T^{\lambda}_{~~\nu\mu} = \Gamma^\lambda_{~~\nu\mu} - \Gamma^\lambda_{~~\mu\nu} = h_a^\lambda\left(\partial_\nu h_\mu^a - \partial_\mu h_\nu^a \right),
\end{align}
$$

$$
\begin{align}
S_\rho^{~~\mu\nu} = \frac{1 }{2 } \left(K^{\mu\nu}_{~~~~\rho} + \delta_\rho^\mu T^{\theta\nu}_{~~~~\theta} - \delta_\rho^\nu T^{\theta\mu}_{~~~~\theta} \right),
\end{align}
$$

$$
\begin{align}
S
=\frac{1 }{2\kappa^2 } \int\mathrm{d}^4 x\left[e f(T) + L_m \right],
\end{align}
$$

$$
\begin{align}
\left[e^{-1}\partial_\mu \left(e S_a^{~~\mu\nu} + h_a^\lambda T^\rho_{~~\mu\lambda} S_\rho^{~~\nu\mu} \right) \right] f_T + S_a^{~~\mu\nu} \partial_\mu(T) f_{TT} + \frac{1 }{4 } h_a^\nu f
=\frac{1 }{2 } \kappa^2 h_a^\rho T_\rho^\nu
\end{align}
$$

$$
\begin{align}
\mathrm{d}s^2
=\mathrm{d}t^2 - a^2(t)\left(\mathrm{d}x^2+\mathrm{d}y^2+\mathrm{d}z^2 \right),
\end{align}
$$

$$
\begin{align}
12 H^2 f_T + f = 2\kappa^2 \rho_t,
\end{align}
$$

$$
\begin{align}
48H^2\dot{H} f_{TT} - \left(12 H^2 + 4\dot{H} \right) f_T - f
= 2\kappa^2 \rho_t,
\end{align}
$$

### 2.2

$$
\begin{align}
\bar{Y}
=\lim_{V\to V_0} \frac{1 }{V } \int Y\sqrt{-g} \mathrm{d}^3 x,
\end{align}
$$

$$
\begin{align}
\bar{E}_i = 0,\quad
\bar{B}_i = 0,\quad
\overline{E_i B_i} = 0,\quad
\overline{E_i E_j} = -\frac{1 }{3 } E^2 g_{ij},\quad
\overline{B_i B_j} = -\frac{1 }{3 } B^2 g_{ij},
\end{align}
$$

$$
\begin{align}
\mathcal{L}
=-\frac{1 }{4 } F + \omega F^2 + \eta_0 F^{*2},
\end{align}
$$

$$
\begin{align}
T_{\mu\nu}
=-4\mathcal{L}_F F_\mu^{~~\alpha} F_{\alpha\nu} + \left(F^* \mathcal{L}_{F^*} - \mathcal{L} \right) g_{\mu\nu},
\end{align}
$$

$$
\begin{align}
\rho = -\mathcal{L} - 4E^2 \mathcal{L}_F,
\end{align}
$$

$$
\begin{align}
p = \mathcal{L} + \frac{4 }{3 } \left(E^2-2B^2 \right)\mathcal{L}_F,
\end{align}
$$

$$
\begin{align}
\rho_B = \frac{1 }{2 } B^2\left(1-8\omega B^2 \right),
\end{align}
$$

$$
\begin{align}
p_B = \frac{1 }{6 } B^2 \left(1-40\omega_0 B^2 \right),
\end{align}
$$

$$
\begin{align}
\mathcal{L} = -\frac{1 }{4 } F,\quad
T_{\mu\nu} = F_\mu^{~~\alpha} F_{\alpha\nu} + \frac{1 }{4 } F g_{\mu\nu}.
\end{align}
$$

$$
\begin{align}
\rho = 3p = \frac{1 }{2 } \left(E^2 + B^2 \right),
\end{align}
$$

## 3

$$
\begin{align}
\frac{3 H^2 }{\kappa^2 } = \rho_t,\quad
-\frac{2\dot{H} }{\kappa^2 }  = \rho_t + p_t,
\end{align}
$$

$$
\begin{align}
\rho_T = \frac{1 }{2\kappa^2 } \left(-12 H^2 f_T - f + 6H^2 \right),
\end{align}
$$

$$
\begin{align}
p_T = -\frac{1 }{2\kappa^2 } \left[48\dot{H}H^2 f_{TT} - \left(12 H^2 + 4\dot{H} \right) f_T - f + 6 H^2 + 4\dot{H} \right],
\end{align}
$$

$$
\begin{align}
\dot{\rho}_m + 3H \rho_m = 0,
\end{align}
$$

$$
\begin{align}
\dot{\rho}_B + 3H\left(\rho_B + p_B \right) = 0,
\end{align}
$$

$$
\begin{align}
\dot{\rho}_T + 3H\left(\rho_T + p_T \right) = 0,
\end{align}
$$

$$
\begin{aligned}
\omega_t
&=\left\{-\frac{1 }{\kappa^2 } \left[48\dot{H}H^2 f_{TT} - \left(12 H^2 + 4\dot{H} \right) f_T - f + 6 H^2 + 4\dot{H} \right] + \frac{B^2 }{6 } \left(1-40\omega_0 B^2 \right) \right\} \\
&\times \left\{\rho_{m0} a^{-3} + \frac{1 }{2\kappa^2 } \left[6 H^2 - f-12 H^2 f_T \right] + \frac{B^2 }{2 } \left[1-8\omega_0 B^2 \right] \right\}^{-1} \tag{25}
\end{aligned}
$$

$$
\begin{aligned}
q = -1 - \frac{\dot{H} }{H^2 } .\tag{26}
\end{aligned}
$$

$$
\begin{aligned}
2q_t
&=1 + 3\left[-\frac{1 }{\kappa^2 } \left(48\dot{H} H^2 f_{TT} - \left(12 H^2 + 4\dot{H} \right) f_T - f + 6H^2 + 4\dot{H} \right) + \frac{B^2 }{6 } \left(1-40\omega_0 B^2 \right) \right] \\
&\times \left[\rho_{m0}a^{-3} + \frac{1 }{2 } \left(6H^2-f-12H^2 f_T \right) + \frac{B^2 }{2 } \left(1-8\omega_0 B^2 \right) \right]^{-1} \tag{27}
\end{aligned}
$$

$$
\begin{aligned}
\frac{\mathrm{d}S_X }{\mathrm{d}t } + \frac{\mathrm{d}S_P }{\mathrm{d}t } = \frac{\pi R_X }{G } \left(2\dot{R}_X f_T + R_X\dot{T} f_{TT} \right).\tag{28}
\end{aligned}
$$

$$
\begin{aligned}
\frac{\mathrm{d}S_I }{\mathrm{d}t } 
=\frac{1 }{T_X } \left(\frac{\mathrm{d}E_I }{\mathrm{d}t } + p_t\frac{\mathrm{d}V }{\mathrm{d}t }  \right),\tag{29}
\end{aligned}
$$

$$
\begin{aligned}
\frac{\mathrm{d}S_I }{\mathrm{d}t } 
=\frac{4\pi R_X^2 }{T_X } \left(\dot{R}_X - H R_X \right)\left(\rho_t+p_t \right).\tag{30}
\end{aligned}
$$

$$
\begin{aligned}
\frac{\mathrm{d}S_X }{\mathrm{d}t } + \frac{\mathrm{d}S_P }{\mathrm{d}t } + \frac{\mathrm{d}S_I }{\mathrm{d}t } 
&=\frac{\pi R_X }{G } \left\{2\dot{R}_X f_T + R_X\dot{T}f_{TT} + 8\pi G R_X^2 \left[\rho_{m0}a^{-3} + \frac{1 }{\kappa^2 } \left(4\dot{H} T f_{TT} + 2\dot{H}\left(f_T-1 \right) \right) + \frac{2B_0^2 }{3a^4 } \left(1-\frac{16\omega_0 B_0^2 }{a^4 }  \right) \right]\times \left[\dot{R}_X - H R_X \right] \right\}.\tag{31}
\end{aligned}
$$

$$
\begin{aligned}
R_H = \frac{1 }{H } ,\quad
\dot{R}_H = -\frac{\dot{H} }{H^2 } .\tag{32}
\end{aligned}
$$

$$
\begin{aligned}
\frac{\mathrm{d}S_X }{\mathrm{d}t } + \frac{\mathrm{d}S_P }{\mathrm{d}t } + \frac{\mathrm{d}S_I }{\mathrm{d}t } 
&=-\frac{\pi }{G H} \left\{\frac{2\dot{H} }{H^2 } f_T + 12\dot{H}f_{TT} +\frac{8\pi G }{H^2 }\left(1+\frac{\dot{H} }{H^2 }  \right)\times \left[\rho_{m0}a^{-3} + \frac{1 }{\kappa^2 } \left(4\dot{H}T f_{TT} + 2\dot{H}\left(f_T-1 \right) \right) + \frac{2 B_0^2 }{3a^4 } \left(1-\frac{16\omega_0 B_0^2 }{a^4 }  \right) \right] \right\}.\tag{33}
\end{aligned}
$$

$$
\begin{aligned}
R_E = a\int_0^{\infty} \frac{\mathrm{d}t }{a } ,\quad
\dot{R}_E = H R_E - 1.\tag{34}
\end{aligned}
$$

$$
\begin{aligned}
 \tag{35}
\end{aligned}
$$

## 4

$$
\begin{aligned}
a(t)
=a_0\left(t_s-t \right)^{-h},\quad
h>0,\quad t_s\geqslant t \tag{36}
\end{aligned}
$$

$$
\begin{aligned}
H = \frac{h }{t_s - t } ,\quad
T = -\frac{6h^2 }{\left(t_s-t \right)^2 } ,\quad
\dot{H} = \frac{h }{\left(t_s - t \right)^2 }. \tag{37}
\end{aligned}
$$

$$
\begin{aligned}
f(T)
=c_1\left(-\frac{T }{6h^2 }  \right)^{1/2} + \frac{2\kappa^2 \rho_{m0} }{a_0^3\left(3h+1 \right) } \left(-\frac{6h^2 }{T }  \right)^{3h/2} + \frac{\kappa^2 B_0^2 }{a_0^4\left(4h+1 \right) } \left(-\frac{6h^2 }{T }  \right)^{2h} - \frac{8\kappa^2 B_0^4 \omega_0 }{a_0^8 \left(8h+1 \right) } \left(-\frac{6h^2 }{T }  \right)^{4h},\tag{38}
\end{aligned}
$$

$$
\begin{aligned}
H^2
=\frac{8\pi G }{6 f_T } \left(\rho_t - \frac{f }{16\pi G }  \right).
\end{aligned}
$$

$$
\begin{aligned}
c_1
=12h H_0 \left[\frac{h\kappa^2 \rho_{m0} }{2a_0^3\left(3h+1  \right)H_0^2 } \left(\frac{h }{H_0 }  \right)^{3h} + \frac{h\kappa^2 B_0^2 }{3a_0^4\left(4h+1 \right)H_0^2 } \left(\frac{h }{H_0 }  \right)^{4h} - \frac{16h\kappa^2 B_0^4\omega_0 }{3a_0^8\left(8h+1 \right)H_0^2 } \left(\frac{h }{H_0 }  \right)^{8h} - 1 \right] \tag{39}
\end{aligned}
$$

$$
\begin{aligned}
\omega_t
=\frac{20\kappa^2 B_0^4 \omega_0 }{9h^2a_0^8 } \left(1+z \right)^{(8h+2)/h} - \frac{\kappa^2 B_0^2 }{18h^2 a_0^4 } (1+z)^{(4h+2)/h} - \frac{2(3h+2) }{3h } ,\tag{40}
\end{aligned}
$$

$$
\begin{aligned}
q_t
=\frac{10\kappa^2 B_0^4 \omega_0 }{3h^2 a_0^8 } (1+z)^{(8h+2)/h} - \frac{\kappa^2 B_0^2 }{12 h^2 a_0^4 } (1+z)^{(4h+2)/h} - \frac{5h+4 }{2h } ,\tag{41}
\end{aligned}
$$

$$
\begin{aligned}
f_{TT}
=\frac{(1+z)^{4/h} }{36h^4 } \left[\frac{3h(3h+2)\kappa^2\rho_{m0} }{2a_0^3(3h+1) }(1+z)^3 + \frac{2h(2h+1)\kappa^2 B_0^2 }{a_0^4(4h+1) } (1+z)^4 - \frac{32h(4h+1)\kappa^2 B_0^4 \omega_0 }{a_0^8 (8h+1) } (1+z)^8 - \frac{c_1 }{4(1+z)^{1/h} }   \right].\tag{42}
\end{aligned}
$$

$$
\begin{aligned}
\frac{\mathrm{d}S_H }{\mathrm{d}t } + \frac{\mathrm{d}S_I }{\mathrm{d}t } 
=-\frac{\pi(1+z)^{3/h} }{Gh^3 } \left[\frac{3h(3h+4)\kappa^2\rho_{m0} }{2a_0^3(3h+1) }(1+z)^3 + \frac{4(h+1)\kappa^2 B_0^2 }{3a_0^4(4h+1) } (1+z)^4 - \frac{64h(2h+1)\kappa^2 B_0^4 \omega_0 }{3a_0^8 (8h+1) } (1+z)^8 - \frac{c_1 }{4h(1+z)^{1/h} } \right] + \frac{2\pi }{G h^3 } (1+h)(1+z)^{1/h}.\tag{43}
\end{aligned}
$$

$$
\begin{aligned}
\frac{\mathrm{d}S_E }{\mathrm{d}t } + \frac{\mathrm{d}S_I }{\mathrm{d}t } 
=-\frac{\pi(1+z)^{3/h} }{Gh(1+h)^2 } \left[\frac{(3h+4)\kappa^2\rho_{m0} }{2a_0^3(3h+1) }(1+z)^3 + \frac{4(h+1)\kappa^2 B_0^2 }{3a_0^4(4h+1) } (1+z)^4 - \frac{64(2h+1)\kappa^2 B_0^4 \omega_0 }{3a_0^8 (8h+1) } (1+z)^8 - \frac{c_1 }{4h\kappa^2(1+z)^{1/h} } \right] + \frac{2\pi h }{G (1+h)^3 } (1+z)^{1/h}.\tag{44}
\end{aligned}
$$

$$
\begin{aligned}
f(T)
=c_2\left(-\frac{T }{6h^2 }  \right)^{1/2} + \frac{2\kappa^2\rho_{m0} }{a_0^3(1-3h) } \left(-\frac{T }{6h^2 }  \right)^{3h/2} + \frac{\kappa^2 B_0^2 }{a_0^4(1-4h) } \left(-\frac{T }{6h^2 }  \right)^{2h} - \frac{8\kappa^2 B_0^4 \omega_0 }{a_0^8(1-8h) } \left(-\frac{T }{6h^2 }  \right)^{4h},\tag{45}
\end{aligned}
$$

$$
\begin{aligned}
c_2
=12h H_0\left[-\frac{h\kappa^2 \rho_{m0} }{2a_0^3(1-3h)H_0^2 } \left(\frac{H_0 }{h }  \right)^{3h} - \frac{h\kappa^2 B_0^2 }{3a_0^4(1-4h)H_0^2 } \left(\frac{H_0 }{h }  \right)^{4h} + \frac{16h\kappa^2 B_0^4 \omega_0 }{3a_0 (1-8h)H_0^2 } \left(\frac{H_0 }{h }  \right)^{8h} - 1 \right] \tag{46}
\end{aligned}
$$

