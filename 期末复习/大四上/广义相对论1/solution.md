# 1

计算牛顿近似中的所有非零联络 $\Gamma_{\mu\nu}^\lambda .$

# 2

写出逆变、协变与二阶张量的坐标变换式，已知 $A^\mu_\nu=\partial \bar{x}^\mu/\partial x^\nu,\bar{A}^\mu_\nu=\partial x^\mu/\partial\bar{x}^\nu $ 且 $\mathrm{det}\left[A^\mu_\nu \right]\ne 0 $ 

$$
\begin{equation}
\phi'^\mu(x')
=A^\mu_\alpha \phi^\alpha(x)
\end{equation}
$$

$$
\begin{equation}
\phi'_\mu(x')
=\bar{A}_\mu^\alpha \phi_\alpha(x)
\end{equation}
$$

$$
\begin{equation}
\phi'^{\mu\nu}(x')
=A^\mu_\alpha A^\nu_\beta \phi^{\alpha\beta}(x)
\end{equation}
$$

$$
\begin{equation}
\phi'^\mu_\nu(x')
=A^\mu_\alpha \bar{A}_\nu^\beta \phi^\alpha_\beta(x)
\end{equation}
$$

$$
\begin{equation}
\phi'_{\mu\nu}(x')
=\bar{A}_\mu^\alpha \bar{A}_\nu^\beta \phi_{\alpha\beta}(x)
\end{equation}
$$

$$
\begin{equation}
\nabla_\mu \phi^\nu
=\partial_\mu \phi^\nu + \Gamma_{\mu\lambda}^\nu \phi^\lambda
\end{equation}
$$

$$
\begin{equation}
\nabla_\mu \phi_\nu
=\partial_\mu \phi_\nu - \Gamma_{\mu\nu}^\lambda \phi_\lambda
\end{equation}
$$

$$
\begin{equation}
\nabla_\mu \phi^{\nu\lambda}
=\partial_\mu \phi^{\nu\lambda} + \Gamma_{\mu\rho}^\nu \phi^{\rho\lambda} + \Gamma_{\mu\rho}^\lambda \phi^{\nu\rho}
\end{equation}
$$

$$
\begin{equation}
\nabla_\mu \phi^\nu_\lambda
=\partial_\mu \phi^\nu_\lambda + \Gamma_{\mu\rho}^\nu \phi^\rho_\lambda - \Gamma_{\mu\lambda}^\rho \phi^\nu_\rho
\end{equation}
$$

$$
\begin{equation}
\nabla_\mu \phi_{\nu\lambda}
=\partial_\mu \phi_{\nu\lambda} - \Gamma_{\mu\nu}^\rho \phi_{\rho\lambda} - \Gamma_{\mu\lambda}^\rho \phi_{\nu\rho}
\end{equation}
$$

# 3

由比安基恒等式证明 $\left(R^{\mu\nu} - \frac{1 }{2 } g^{\mu\nu} R \right)_{;\nu}=0 $

比安基恒等式：

$$
\begin{equation}
\nabla_\lambda R^\rho{}_{\sigma\mu\nu} + \nabla_\mu R^\rho{}_{\sigma\nu\lambda} + \nabla_\nu R^\rho{}_{\sigma\lambda\mu}
=0
\end{equation}
$$

令 $\rho=\mu $ 得到

$$
\begin{equation}
\begin{aligned}
\nabla_\lambda R^\mu{}_{\sigma\mu\nu} + \nabla_\mu R^\mu{}_{\sigma\nu\lambda} + \nabla_\nu R^\mu{}_{\sigma\lambda\mu}
=0
\end{aligned}
\end{equation}
$$

由 $R_{\mu\nu}\equiv R^\lambda{}_{\mu\lambda\nu} $ 可知第一项化为

$$
\begin{equation}
\nabla_\lambda R^\mu{}_{\sigma\mu\nu} = \nabla_\lambda R_{\sigma\nu}
\end{equation}
$$

由 $R^{\rho}{}_{\sigma\mu\nu} = -R^\rho{}_{\sigma\nu\mu} $ 知第三项化为

$$
\begin{equation}
\nabla_\nu R^\mu{}_{\sigma\lambda\mu}
=-\nabla_\nu R^\mu{}_{\sigma\mu\lambda}
=-\nabla_\nu R_{\sigma\lambda}
\end{equation}
$$

于是有

$$
\begin{equation}
\nabla_\nu R_{\sigma\lambda}
=\nabla_\lambda R_{\sigma\nu} + \nabla_\mu R^\mu{}_{\sigma\nu\lambda}
\end{equation}
$$

两边同乘 $g^{\sigma\lambda} $，利用 $\nabla_\nu g^{\sigma\lambda}=0 $ 、协变微分的莱布尼兹律以及 $R\equiv g^{\mu\nu} R_{\mu\nu},R^\mu{}_{\nu}\equiv g^{\mu\rho} R_{\rho\nu} $ 有

$$
\begin{equation}
\begin{aligned}
\nabla_\nu R
=\nabla_\lambda R^\lambda{}_{\nu} + \nabla_\mu\left(g^{\sigma\lambda} R^{\mu}{}_{\sigma\nu\lambda} \right)
\end{aligned}
\end{equation}
$$

上式右边第二项，利用 $R_{\mu\nu\lambda\rho}=-R_{\nu\mu\lambda\rho},R^\lambda{}_{\sigma\mu\nu} = -R^\lambda{}_{\sigma\nu\mu} $ 有

$$
\begin{equation}
\begin{aligned}
g^{\sigma\lambda} R^{\mu}{}_{\sigma\nu\lambda}
&=g^{\mu\rho}g^{\sigma\lambda} R_{\rho\sigma\nu\lambda}
=g^{\mu\rho} g^{\sigma\lambda} R_{\nu\lambda\rho\sigma} \\
&=-g^{\mu\rho} g^{\sigma\lambda} R_{\lambda\nu\rho\sigma}
=-g^{\mu\rho} R^\sigma{}_{\nu\rho\sigma}
=g^{\mu\rho} R^\sigma{}_{\nu\sigma\rho} \\
&=g^{\mu\rho} R_{\nu\rho}
=R^\mu{}_{\nu}
\end{aligned}
\end{equation}
$$

于是得到

$$
\begin{equation}
\nabla_\nu R = \nabla_\lambda R^\lambda{}_{\nu} + \nabla_\mu R^\mu{}_{\nu}
\end{equation}
$$

也即

$$
\begin{equation}
\nabla_\nu R
=2 \nabla_\mu R^\mu{}_{\nu},\quad
\nabla_\mu R^\mu{}_{\nu}
=\frac{1 }{2 } \nabla_\nu R
=\frac{1 }{2 } \delta^\mu{}_{\nu} \nabla_\mu R
\end{equation}
$$

即

$$
\begin{equation}
\nabla_\mu\left(R^\mu{}_\nu - \frac{1 }{2 } \delta^\mu{}_{\nu} R \right)
=0
\end{equation}
$$

两边同乘 $g^{\rho\nu} $ 得

$$
\begin{equation}
\nabla_\mu\left(R^{\mu\rho} - \frac{1 }{2 } g^{\rho\mu} R \right)
=0
\end{equation}
$$

又 $R^{\mu\nu} = R^{\nu\mu} $ 于是

$$
\begin{equation}
\nabla_\mu\left(R^{\rho\mu} - \frac{1 }{2 } g^{\rho\mu} R \right)
=0
\end{equation}
$$

等价于

$$
\begin{equation}
\left(R^{\mu\nu} - \frac{1 }{2 } g^{\mu\nu} R \right)_{;\nu}=0
\end{equation}
$$

# 4

写出爱因斯坦作用量，并变分得到场方程。已知Palatini公式

$$
\begin{equation}
\sqrt{-g} g^{\mu\nu} \delta R_{\mu\nu} 
=\partial_\mu\left(\sqrt{-g} \phi^\mu \right)
\end{equation}
$$

且

$$
\begin{equation}
\delta g
=g g^{\mu\nu} \delta g_{\mu\nu}
=-g g_{\mu\nu} \delta g^{\mu\nu}
\end{equation}
$$

总作用量

$$
\begin{equation}
I = I_g + I_m
\end{equation}
$$

其中 $I_g $ 是引力场作用量，$I_m $ 是引力源物质作用量。

$$
\begin{equation}
I_g
=\int\limits_M L_g \sqrt{-g} \mathrm{d}^4x
=\frac{c^3 }{16\pi G } \int\limits_M R \sqrt{-g} \mathrm{d}^4 x,\quad L_g = \frac{c^3 }{16\pi G } R
\end{equation}
$$

想算 $I_g $ 对度规的变分，要先算 $R\sqrt{-g} $ 对度规的变分。

$$
\begin{equation}
\begin{aligned}
\delta(R \sqrt{-g})
&=\delta\left(g^{\mu\nu} R_{\mu\nu} \sqrt{-g} \right) \\
&=\left(\delta g^{\mu\nu} \right) R_{\mu\nu} \sqrt{-g} + g^{\mu\nu} \left(\delta R_{\mu\nu} \right) \sqrt{-g} + g^{\mu\nu} R_{\mu\nu} \delta\left(\sqrt{-g} \right)
\end{aligned}
\end{equation}
$$

利用Palatini.II公式

$$
\begin{equation}
\sqrt{-g} g^{\mu\nu} \delta R_{\mu\nu}
=\partial_\mu\left(\sqrt{-g}\phi^\mu \right),\quad
\phi^\mu
\equiv g^{\lambda\nu} \delta \Gamma_{\lambda\nu}^\mu - g^{\mu\nu} \delta \Gamma_{\lambda\nu}^\lambda
\end{equation}
$$

以及

$$
\begin{equation}
\delta g 
=g g^{\mu\nu} \delta g_{\mu\nu}
=-g g_{\mu\nu} \delta g^{\mu\nu}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
\delta\left(\sqrt{-g} \right)
=-\frac{1 }{2 } \frac{\delta g }{\sqrt{-g} } 
=-\frac{1 }{2 } \frac{-g g_{\mu\nu} \delta g^{\mu\nu} }{\sqrt{-g} } 
=-\frac{1 }{2 } \sqrt{-g} g_{\mu\nu} \delta g^{\mu\nu}
\end{aligned}
\end{equation}
$$

于是有

$$
\begin{equation}
\begin{aligned}
\delta(R \sqrt{-g})
&=\left(\delta g^{\mu\nu} \right) R_{\mu\nu} \sqrt{-g} + g^{\mu\nu} \left(\delta R_{\mu\nu} \right) \sqrt{-g} + g^{\mu\nu} R_{\mu\nu} \delta\left(\sqrt{-g} \right) \\
&=R_{\mu\nu} \sqrt{-g} \delta g^{\mu\nu} + \partial_\mu \left(\sqrt{-g} \phi^\mu \right) - \frac{1 }{2 } \sqrt{-g} R g_{\mu\nu} \delta g^{\mu\nu}
\end{aligned}
\end{equation}
$$

因此引力场作用量对度规的变分为

$$
\begin{equation}
\begin{aligned}
\delta I_g
&=\frac{c^3 }{16\pi G } \int\limits_M \delta\left(R \sqrt{-g} \right) \mathrm{d}^4 x \\
&=\frac{c^3 }{16\pi G } \int\limits_M \left(R_{\mu\nu} \sqrt{-g} \delta g^{\mu\nu} + \partial_\mu \left(\sqrt{-g} \phi^\mu \right) - \frac{1 }{2 } \sqrt{-g} R g_{\mu\nu} \delta g^{\mu\nu} \right) \mathrm{d}^4 x \\
&=\frac{c^3 }{16\pi G } \int\limits_M \left(R_{\mu\nu} - \frac{1 }{2 } g_{\mu\nu} R \right) \left(\delta g^{\mu\nu} \right) \sqrt{-g} \mathrm{d}^4 x \\
\end{aligned}
\end{equation}
$$

接下来还需要引力源物质作用量对度规的变分。

$$
\begin{equation}
\begin{aligned}
I_m
=\frac{1 }{c } \int\limits_M L_m \sqrt{-g} \mathrm{d}^4 x
\end{aligned}
\end{equation}
$$

假定拉式密度 $L_m $ 只含 $g^{\mu\nu} $，而不含 $\partial_\lambda g^{\mu\nu} $，则

$$
\begin{equation}
\begin{aligned}
\delta I_m
&=\frac{1 }{c } \int\limits_M \delta \left(L_m \sqrt{-g} \right) \mathrm{d}^4 x \\
&=\frac{1 }{c } \int\limits_M \frac{\partial \left(L_m \sqrt{-g} \right) }{\partial g^{\mu\nu} } \delta g^{\mu\nu} \mathrm{d}^4 x \\
\end{aligned}
\end{equation}
$$

定义

$$
\begin{equation}
T_{\mu\nu}
\equiv -\frac{2 }{\sqrt{-g} } \frac{\partial \left(L_m \sqrt{-g} \right) }{\partial g^{\mu\nu} },\quad
\frac{\partial \left(L_m \sqrt{-g} \right) }{\partial g^{\mu\nu} }
=-\frac{1 }{2 } \sqrt{-g} T_{\mu\nu}
\end{equation}
$$

则

$$
\begin{equation}
\begin{aligned}
\delta I_m
&=\frac{1 }{c } \int\limits_M \frac{\partial \left(L_m \sqrt{-g} \right) }{\partial g^{\mu\nu} } \delta g^{\mu\nu} \mathrm{d}^4 x \\
&=-\frac{1 }{2c } \int\limits_M T_{\mu\nu} \left(\delta g^{\mu\nu} \right) \sqrt{-g} \mathrm{d}^4 x
\end{aligned}
\end{equation}
$$

最小作用量原理说，$\delta I=0 $ 给出体系的运动方程，也即

$$
\begin{equation}
\begin{aligned}
0
&=\delta I
=\delta I_g + \delta I_m
=\frac{c^3 }{16\pi G } \int\limits_M \left(R_{\mu\nu} - \frac{1 }{2 } g_{\mu\nu} R \right) \left(\delta g^{\mu\nu} \right) \sqrt{-g} \mathrm{d}^4 x -\frac{1 }{2c } \int\limits_M T_{\mu\nu} \left(\delta g^{\mu\nu} \right) \sqrt{-g} \mathrm{d}^4 x \\
&=\frac{c^3 }{16\pi G } \int\limits_M \left(R_{\mu\nu} - \frac{1 }{2 } g_{\mu\nu} R - \frac{8\pi G }{c^4 } T_{\mu\nu} \right) \left(\delta g^{\mu\nu} \right) \sqrt{-g} \mathrm{d}^4 x
\end{aligned}
\end{equation}
$$

最终得到爱因斯坦引力场方程：

$$
\begin{equation}
R_{\mu\nu} - \frac{1 }{2 } g_{\mu\nu} R = \frac{8\pi G }{c^4 } T_{\mu\nu}
\end{equation}
$$

# 5

求弱场线性近似的里奇张量，并导出线性化的场方程。

# 6

推导光线在行星附近的轨道方程，并讨论其偏折，这证明了GR的什么效应？

# 7

推导史瓦西时空与闵可夫斯基时空的类光测地线，简述并画出Kruskal延拓图与彭罗斯图。

闵氏时空线元

$$
\begin{equation}
\mathrm{d}s^2
=-c^2\mathrm{d}t^2 + \mathrm{d}r^2 + r^2\left(\mathrm{d}\theta^2 + \sin^2\theta\mathrm{d}\phi^2 \right)
\end{equation}
$$

类光测地线满足

$$
\begin{equation}
\mathrm{d}s^2 = 0
\end{equation}
$$

如果只考虑径向，则

$$
\begin{equation}
-c^2 \mathrm{d}t^2 + \mathrm{d}r^2 = 0
\end{equation}
$$

取 $c=1 $，则

$$
\begin{equation}
\left(\frac{\mathrm{d}t }{\mathrm{d}r }  \right)^2
=1,\quad
\frac{\mathrm{d}t }{\mathrm{d}r } = \pm 1,
\end{equation}
$$

径向类光测地线为

$$
\begin{equation}
t = \pm r + \mathrm{const}
\end{equation}
$$

史瓦西时空线元

$$
\begin{equation}
\mathrm{d}s^2
=-c^2 \left(1-\frac{2GM }{c^2 r }  \right)\mathrm{d}t^2 + \left(1-\frac{2GM }{c^2 r}  \right)^{-1} \mathrm{d}r^2 + r^2\left(\mathrm{d}\theta^2 + \sin^2\theta\mathrm{d}\phi^2 \right)
\end{equation}
$$

如果只考虑径向，并取 $c=G=1 $，则

$$
\begin{equation}
\mathrm{d}s^2
=-\left(1-\frac{2M }{r }  \right)\mathrm{d}t^2 + \left(1-\frac{2M }{r }  \right)^{-1} \mathrm{d}r^2
\end{equation}
$$

类光测地线满足

$$
\begin{equation}
\mathrm{d}s^2 = 0
\end{equation}
$$

即

$$
\begin{equation}
\left(\frac{\mathrm{d}t }{\mathrm{d}r }  \right)^2
=\left(1-\frac{2M }{r }  \right)^{-2},\quad
\frac{\mathrm{d}t }{\mathrm{d}r }
=\pm \left(1-\frac{2M }{r }  \right)^{-1}
\end{equation}
$$

$$
\begin{equation}
\mathrm{d}t
=\pm \frac{1 }{1-2M/r } \mathrm{d}r
=\pm \frac{r }{r-2M } \mathrm{d}r
=\pm \frac{r-2M + 2M }{r-2M } \mathrm{d}r
=\pm\left(1 + \frac{2M }{r-2M }  \right)\mathrm{d}(r-2M)
\end{equation}
$$

两边积分得

$$
\begin{equation}
t = \pm \left(r + 2M\ln\left|r-2M \right| \right) + \mathrm{const}
\end{equation}
$$

史瓦西时空径向线元：

$$
\begin{equation}
\mathrm{d}s^2
=-\left(1-2M/r \right) \mathrm{d}t^2 + \left(1-2M/r \right)^{-1} \mathrm{d}r^2
\end{equation}
$$

考虑坐标变换

$$
\left\{
\begin{aligned}
&T = 4M\left(\frac{r }{2M } -1 \right)^{1/2} \mathrm{e}^{\frac{r }{4M } } \sinh\left(\frac{t }{4M }  \right) \\
&R = 4M\left(\frac{r }{2M } -1 \right)^{1/2} \mathrm{e}^{\frac{r }{4M } } \cosh\left(\frac{t }{4M }  \right)
\end{aligned}
\right.,r>2M,\mathrm{I}
$$

$$
\left\{
\begin{aligned}
&T = -4M\left(\frac{r }{2M } -1 \right)^{1/2} \mathrm{e}^{\frac{r }{4M } } \sinh\left(\frac{t }{4M }  \right) \\
&R = -4M\left(\frac{r }{2M } -1 \right)^{1/2} \mathrm{e}^{\frac{r }{4M } } \cosh\left(\frac{t }{4M }  \right)
\end{aligned}
\right.,r>2M,\mathrm{II}
$$

$$
\left\{
\begin{aligned}
&T = 4M\left(1 - \frac{r }{2M } \right)^{1/2} \mathrm{e}^{\frac{r }{4M } } \cosh\left(\frac{t }{4M }  \right) \\
&R = 4M\left(1 - \frac{r }{2M } \right)^{1/2} \mathrm{e}^{\frac{r }{4M } } \sinh\left(\frac{t }{4M }  \right)
\end{aligned}
\right.,r<2M,F
$$

$$
\left\{
\begin{aligned}
&T = -4M\left(1 - \frac{r }{2M } \right)^{1/2} \mathrm{e}^{\frac{r }{4M } } \cosh\left(\frac{t }{4M }  \right) \\
&R = -4M\left(1 - \frac{r }{2M } \right)^{1/2} \mathrm{e}^{\frac{r }{4M } } \sinh\left(\frac{t }{4M }  \right)
\end{aligned}
\right.,r<2M,P
$$

Kruskal坐标下的线元：

$$
\begin{equation}
\mathrm{d}s^2
=\frac{2M }{r } \mathrm{e}^{-r/2M} \left(-\mathrm{d}T^2 + \mathrm{d}R^2 \right) + r^2\left(\mathrm{d}\theta^2 + \sin^2\theta\mathrm{d}\phi^2 \right)
\end{equation}
$$

$r $ 与 $R,T $ 的关系：

$$
\begin{equation}
R^2 - T^2 = 16 M^2 \left(\frac{r }{2M } -1 \right) \mathrm{e}^{r/2M}
\end{equation}
$$

> 上式对四个区域都成立。

Kruskal坐标消除了度规分量在引力半径处的奇异性，但无法消除 $r=0 $ 的奇点。

Kruskal度规具有最大解析区和最高完备性。

- 类时未来无穷远 $I^+: $ $r $ 有限，$t\to +\infty $

- 类时过去无穷远 $I^-: $ $r $ 有限，$t\to -\infty $

- 类空无穷远 $I^0: $ $t $ 有限，$r\to +\infty $

- 类光未来无穷远 $J^+: $ $(t-r) $ 有限，$(t+r)\to +\infty $

- 类光过去无穷远 $J^-: $ $(t+r) $ 有限，$(t-r)\to +\infty $ 

<div align="center">
  <img src="fig/fig1.png" width="30%" title="图片描述">
</div>

<div align="center">
  <img src="fig/fig2.png" width="30%" title="图片描述">
</div>

<div align="center">
  <img src="fig/fig3.png" width="70%" title="图片描述">
</div>

<div align="center">
  <img src="fig/fig4.png" width="30%" title="图片描述">
</div>