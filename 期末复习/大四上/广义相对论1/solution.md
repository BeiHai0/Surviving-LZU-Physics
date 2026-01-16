# 1

计算牛顿近似中的所有非零联络 $\Gamma_{\mu\nu}^\lambda .$

牛顿近似线元：

$$
\begin{equation}
\mathrm{d}s^2
=-c^2\mathrm{d}t^2\left(1-h_{00} \right) + \left(\mathrm{d}x^1 \right)^2 + \left(\mathrm{d}x^2 \right)^2 + \left(\mathrm{d}x^3 \right)^2
\end{equation}
$$

度规：

$$
\begin{equation}
g_{00} = -\left(1-h_{00} \right),\quad
g_{0i} = g^{0i} = 0,\quad
g_{ij} = \delta_{ij}
\end{equation}
$$

利用小量近似 $1/(1-x) \approx 1 + x,\left|x \right|\ll 1 $ 有逆度规：

$$
\begin{equation}
g^{00} = -(1+h_{00}),\quad
g^{0i} = g^{i0} = 0,\quad
g^{ij} = \delta^{ij}
\end{equation}
$$

知道了度规和逆度规，就可以计算黎曼联络：

$$
\begin{equation}
\Gamma^\lambda_{\mu\nu}
=\frac{1 }{2 } g^{\lambda\sigma} \left(\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma\mu} - \partial_\sigma g_{\mu\nu} \right)
\end{equation}
$$

- $\lambda=i $

$$
\begin{equation}
\begin{aligned}
\Gamma^i_{\mu\nu}
&=\frac{1 }{2 } g^{i\sigma} \left(\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma\mu} - \partial_\sigma g_{\mu\nu} \right) \\
&=\frac{1 }{2 } g^{ij} \left(\partial_\mu g_{j\nu} + \partial_\nu g_{j\mu} - \partial_j g_{\mu\nu} \right) \\
&=\frac{1 }{2 } \delta^{ij} \left(\partial_\mu g_{j\nu} + \partial_\nu g_{j\mu} - \partial_j g_{\mu\nu} \right) \\
\end{aligned}
\end{equation}
$$

- - $(\mu,\nu)=(l,m) $

$$
\begin{equation}
\begin{aligned}
\Gamma^i_{lm}
&=\frac{1 }{2 } \delta^{ij} \left(\partial_l g_{jm} + \partial_m g_{jl} - \partial_j g_{lm} \right) \\
&=0
\end{aligned}
\end{equation}
$$

- - $(\mu,\nu)=(0,m) $

$$
\begin{equation}
\begin{aligned}
\Gamma^i_{0m}
&=\frac{1 }{2 } \delta^{ij} \left(\partial_0 g_{jm} + \partial_m g_{j0} - \partial_j g_{0m} \right) \\
&=0
\end{aligned}
\end{equation}
$$

- - $(\mu,\nu)=(l,0) $

$$
\begin{equation}
\begin{aligned}
\Gamma^i_{l0}
&=0
\end{aligned}
\end{equation}
$$

- - $(\mu,\nu)=(0,0) $

$$
\begin{equation}
\begin{aligned}
\Gamma^i_{00}
&=\frac{1 }{2 } \delta^{ij} \left(\partial_0 g_{j0} + \partial_0 g_{j0} - \partial_j g_{00} \right) \\
&=-\frac{1 }{2 } \delta^{ij} \partial_j \left[-(1-h_{00}) \right] \\
&=-\frac{1 }{2 } \delta^{ij} \partial_j h_{00} \\
&=-\frac{1 }{2 } \partial_i h_{00}
\end{aligned}
\end{equation}
$$

- $\lambda=0 $

$$
\begin{equation}
\begin{aligned}
\Gamma^0_{\mu\nu}
&=\frac{1 }{2 } g^{0\sigma} \left(\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma\mu} - \partial_\sigma g_{\mu\nu} \right) \\
&=\frac{1 }{2 } g^{00} \left(\partial_\mu g_{0\nu} + \partial_\nu g_{0\mu} - \partial_0 g_{\mu\nu} \right) \\
\end{aligned}
\end{equation}
$$

- - $(\mu,\nu)=(l,m) $

$$
\begin{equation}
\begin{aligned}
\Gamma^0_{lm}
&=\frac{1 }{2 } g^{00} \left(\partial_l g_{0m} + \partial_m g_{0l} - \partial_0 g_{lm} \right) \\
&=0
\end{aligned}
\end{equation}
$$

- - $(\mu,\nu)=(0,m) $

$$
\begin{equation}
\begin{aligned}
\Gamma^0_{0m}
&=\frac{1 }{2 } g^{00} \left(\partial_0 g_{0m} + \partial_m g_{00} - \partial_0 g_{0m} \right) \\
&=\frac{1 }{2 } g^{00} \partial_m g_{00} \\
&=\frac{1 }{2 } \left[-(1+h_{00}) \right] \partial_m \left[-(1-h_{00}) \right] \\
&\approx -\frac{1 }{2 } \partial_m h_{00}
\end{aligned}
\end{equation}
$$

> 舍去二阶小量

- - $(\mu,\nu)=(l,0) $

$$
\begin{equation}
\begin{aligned}
\Gamma^0_{l0}
=-\frac{1 }{2 } \partial_l h_{00}
\end{aligned}
\end{equation}
$$

- - $(\mu,\nu)=(0,0) $

$$
\begin{equation}
\begin{aligned}
\Gamma^0_{00}
&=\frac{1 }{2 } g^{00} \left(\partial_0 g_{00} + \partial_0 g_{00} - \partial_0 g_{00} \right) \\
&=0
\end{aligned}
\end{equation}
$$

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

由于

$$
\begin{equation}
g_{\mu\nu}
=\eta_{\mu\nu} + h_{\mu\nu},\quad
\left|h_{\mu\nu} \right|\ll 1,
\end{equation}
$$

线性近似理论只保留小量 $h_{\mu\nu} $ 的一阶项，于是

$$
\begin{equation}
\begin{aligned}
\Gamma^\mu_{\alpha\beta}
&\equiv \frac{1 }{2 } g^{\mu\nu}\left(\partial_\alpha g_{\beta \nu} + \partial_\beta g_{\alpha\nu} - \partial_\nu g_{\alpha\beta} \right) \\
&\equiv \frac{1 }{2 } \left(\eta^{\mu\nu} + h^{\mu\nu} \right) \left[\partial_\alpha \left(\eta_{\beta \nu} + h_{\beta \nu} \right) + \partial_\beta \left(\eta_{\alpha\nu + h_{\alpha\nu}} \right) - \partial_\nu \left(\eta_{\alpha\beta} + h_{\alpha\beta} \right) \right] \\
&=\frac{1 }{2 } \eta^{\mu\nu} \left(\partial_\beta h_{\alpha\nu} + \partial_\alpha h_{\beta\nu} - \partial_\nu h_{\alpha\beta} \right) \\
&=\frac{1 }{2 } \left[\partial_\beta \left(\eta^{\mu\nu} h_{\alpha\nu} \right) + \partial_\alpha \left(\eta^{\mu\nu} h_{\beta\nu} \right) - \eta^{\mu\nu} \partial_\nu \left( h_{\alpha\beta} \right) \right] \\
&=\frac{1 }{2 } \left(\partial_\beta h^\mu_\alpha + \partial_\alpha h^\mu_\beta - \partial^\mu h_{\alpha\beta} \right) \\
&=\frac{1 }{2 } \left(h^\mu_{\alpha,\beta} + h^\mu_{\beta,\alpha} - h^{,\mu}_{\alpha\beta} \right)
\end{aligned}
\end{equation}
$$

克氏符 $\Gamma $ 是 $h_{\mu\nu} $ 一阶小量的叠加，因此 Riemann 曲率张量中的 $\Gamma \Gamma $ 项可以舍去，此时 Riemann 曲率张量为：

$$
\begin{equation}
\begin{aligned}
R^\lambda_{\mu\alpha\nu}
&\equiv \partial_\alpha \Gamma^\lambda_{\nu\mu} - \partial_\nu \Gamma^\lambda_{\alpha\mu} + \Gamma^\lambda_{\alpha\beta} \Gamma^\beta_{\nu\mu} - \Gamma^\lambda_{\nu\beta} \Gamma^\beta_{\alpha\mu} \\
&=\partial_\alpha \Gamma^\lambda_{\nu\mu} - \partial_\nu \Gamma^\lambda_{\alpha\mu} \\
&=\frac{1 }{2 } \left[\partial_\alpha \left(h^\lambda_{\nu,\mu} + h^\lambda_{\mu,\nu} - h^{,\lambda}_{\nu\mu} \right) - \partial_\nu \left(h^\lambda_{\alpha,\mu} + h^\lambda_{\mu,\alpha} - h^{,\lambda}_{\alpha\mu} \right) \right]
\end{aligned}
\end{equation}
$$

Ricci张量为

$$
\begin{equation}
\begin{aligned}
R_{\mu\nu}
&=R^\alpha_{\mu\alpha\nu} \\
&=\frac{1 }{2 } \left[\partial_\alpha \left(h^\alpha_{\nu,\mu} + h^\alpha_{\mu,\nu} - h^{,\alpha}_{\nu\mu} \right) - \partial_\nu \left(h^\alpha_{\alpha,\mu} + h^\alpha_{\mu,\alpha} - h^{,\alpha}_{\alpha\mu} \right) \right] \\
&=\frac{1 }{2 } \left(\partial_\alpha h^\alpha_{\nu,\mu} + \partial_\nu h^{,\alpha}_{\alpha\mu} - \partial_\alpha h^{,\alpha}_{\nu\mu} - \partial_\nu h^\alpha_{\alpha,\mu} \right) \\
&=-\frac{1 }{2 } \left(h^{,\alpha}_{\nu\mu,\alpha} + h^\alpha_{\alpha,\mu,\nu} - h^\alpha_{\nu,\mu,\alpha} - h^{,\alpha}_{\alpha\mu,\nu} \right) \\
&=-\frac{1 }{2 } \left(h^{,\alpha}_{\mu\nu,\alpha} + h^\alpha_{\alpha,\mu,\nu} - h^\alpha_{\nu,\mu,\alpha} - h^{,\alpha}_{\alpha\mu,\nu} \right) \\
\end{aligned}
\end{equation}
$$

注意到

$$
\begin{equation}
h^\alpha_{\alpha,\mu,\nu}
=\eta^{\lambda\alpha}h_{\lambda\alpha,\mu,\nu}
=\left(\eta^{\lambda\alpha} h_{\lambda\alpha} \right)_{,\mu,\nu}
=h_{,\mu,\nu}
\end{equation}
$$

$$
\begin{equation}
h^{,\alpha}_{\alpha\mu,\nu}
=\eta^{\alpha\beta}h_{\alpha\mu,\nu,\beta}
=h^\beta_{\mu,\nu,\beta}
=h^\alpha_{\mu,\nu,\alpha}
\end{equation}
$$

因此Ricci张量可化为

$$
\begin{equation}
\begin{aligned}
R_{\mu\nu}
=-\frac{1 }{2 } \left(h^{,\alpha}_{\mu\nu,\alpha} + h^\alpha_{\alpha,\mu,\nu} - h^\alpha_{\nu,\mu,\alpha} - h^{,\alpha}_{\alpha\mu,\nu} \right) \\
=-\frac{1 }{2 } \left(h^{,\alpha}_{\mu\nu,\alpha} + h_{,\mu,\nu} - h^\alpha_{\nu,\mu,\alpha} - h^\alpha_{\mu,\nu,\alpha} \right) \\
\end{aligned}
\end{equation}
$$

先算Ricci标量：

$$
\begin{equation}
\begin{aligned}
R
&=\eta^{\mu\nu} R_{\mu\nu} \\
&=-\frac{1 }{2 } \eta^{\mu\nu} \left(h^{,\alpha}_{\mu\nu,\alpha} + h_{,\mu,\nu} - h^\alpha_{\nu,\mu,\alpha} - h^\alpha_{\mu,\nu,\alpha} \right) \\
&=-\frac{1 }{2 } \left(h^{,\alpha}_{,\alpha} + h^{,\nu}_{,\nu} - h^{\alpha,\nu}_{\nu,\alpha} - h^{\alpha,\mu}_{\mu,\alpha} \right) \\
&=-\frac{1 }{2 } \left(2 h^{,\alpha}_{,\alpha} - 2 h^{\alpha,\beta}_{\beta,\alpha} \right) \\
&=- h^{,\alpha}_{,\alpha} + h^{\alpha,\beta}_{\beta,\alpha} \\
\end{aligned}
\end{equation}
$$

利用

$$
\begin{equation}
\bar{h} = -h,\quad 
\bar{h}_{\mu\nu}
\equiv h_{\mu\nu} - \frac{1 }{2 } \eta_{\mu\nu} h
=h_{\mu\nu} + \frac{1 }{2 } \eta_{\mu\nu} \bar{h}
\Longrightarrow h_{\mu\nu} = \bar{h}_{\mu\nu} - \frac{1 }{2 }  \eta_{\mu\nu} \bar{h}
\end{equation}
$$

$$
\begin{equation}
h^\alpha_\nu
=\bar{h}^\alpha_\nu - \frac{1 }{2 } \delta^\alpha_\nu \bar{h}
\end{equation}
$$

有

$$
\begin{equation}
\begin{aligned}
\bar{R}_{\mu\nu}
&\equiv R_{\mu\nu} - \frac{1 }{2 } \eta_{\mu\nu} R \\
&=-\frac{1 }{2 } \left(h^{,\alpha}_{\mu\nu,\alpha} + h_{,\mu,\nu} - h^\alpha_{\nu,\mu,\alpha} - h^\alpha_{\mu,\nu,\alpha} \right) - \frac{1 }{2 } \eta_{\mu\nu} \left(- h^{,\alpha}_{,\alpha} + h^{\alpha,\beta}_{\beta,\alpha}  \right) \\
&=-\frac{1 }{2 } \left[h^{,\alpha}_{\mu\nu,\alpha} + h_{,\mu,\nu} - h^\alpha_{\nu,\mu,\alpha} - h^\alpha_{\mu,\nu,\alpha} -\eta_{\mu\nu} h^{,\alpha}_{,\alpha} + \eta_{\mu\nu} h^{\alpha,\beta}_{\beta,\alpha} \right] \\
&=-\frac{1 }{2 } \left[\left(\bar{h}_{\mu\nu,\alpha}^{,\alpha} - \frac{1 }{2 } \eta_{\mu\nu} \bar{h}^{,\alpha}_{,\alpha} \right) + \left(-\bar{h}_{,\mu,\nu} \right) - \left(\bar{h}^\alpha_{\nu,\mu,\alpha} - \frac{1 }{2 } \delta^\alpha_\nu \bar{h}_{,\mu,\alpha} \right) - \left(\bar{h}^\alpha_{\mu,\nu,\alpha} - \frac{1 }{2 } \delta^\alpha_\mu \bar{h}_{,\nu,\alpha} \right) - \left(-\eta_{\mu\nu} \bar{h}^{,\alpha}_{,\alpha} \right) + \left(\eta_{\mu\nu} \left(\bar{h}^{\alpha,\beta}_{\beta,\alpha} - \frac{1 }{2 } \delta^\alpha_\beta \bar{h}^{,\beta}_{,\alpha} \right) \right) \right] \\
&=-\frac{1 }{2 } \left[\bar{h}^{,\alpha}_{\mu\nu,\alpha} - \bar{h}^\alpha_{\nu,\mu,\alpha} - \bar{h}^\alpha_{\mu,\nu,\alpha} + \eta_{\mu\nu} \bar{h}^{\alpha,\beta}_{\beta,\alpha} \right] \\
&=-\frac{1 }{2 } \left[\bar{h}^{,\alpha}_{\mu\nu,\alpha} - \bar{h}^\alpha_{\nu,\mu,\alpha} - \bar{h}^\alpha_{\mu,\nu,\alpha} + \eta_{\mu\nu} \eta^{\alpha\rho} \bar{h}_{\rho\beta,\alpha}^{,\beta} \right] \\
&=-\frac{1 }{2 } \left[\bar{h}^{,\alpha}_{\mu\nu,\alpha} - \bar{h}^\alpha_{\nu,\mu,\alpha} - \bar{h}^\alpha_{\mu,\nu,\alpha} + \eta_{\mu\nu} \bar{h}_{\rho\beta}^{,\rho,\beta} \right] \\
&=-\frac{1 }{2 } \left[\bar{h}^{,\alpha}_{\mu\nu,\alpha} + \eta_{\mu\nu} \bar{h}_{\alpha\beta}^{,\alpha,\beta} - \bar{h}^\alpha_{\nu,\mu,\alpha} - \bar{h}^\alpha_{\mu,\nu,\alpha} \right] \\
\end{aligned}
\end{equation}
$$

最后，Einstein引力场方程

$$
\begin{equation}
\bar{R}_{\mu\nu}
\equiv R_{\mu\nu} - \frac{1 }{2 } \eta_{\mu\nu} R
=8\pi G T_{\mu\nu}
\end{equation}
$$

就化为：

$$
\begin{equation}
-\frac{1 }{2 } \left[\bar{h}^{,\alpha}_{\mu\nu,\alpha} + \eta_{\mu\nu} \bar{h}_{\alpha\beta}^{,\alpha,\beta} - \bar{h}^\alpha_{\nu,\mu,\alpha} - \bar{h}^\alpha_{\mu,\nu,\alpha} \right] \\
=8\pi G T_{\mu\nu}
\end{equation}
$$

也即：

$$
\begin{equation}
\bar{h}^{,\alpha}_{\mu\nu,\alpha} + \eta_{\mu\nu} \bar{h}_{\alpha\beta}^{,\alpha,\beta} - \bar{h}^\alpha_{\nu,\mu,\alpha} - \bar{h}^\alpha_{\mu,\nu,\alpha}
=-16\pi G T_{\mu\nu}
\end{equation}
$$

# 6

推导光线在行星附近的轨道方程，并讨论其偏折，这证明了GR的什么效应？

考虑史瓦西时空，以线长 $s $ 为参数，在 $\theta=\pi/2 $ 平面内

$$
\begin{equation}
\frac{\mathrm{d}^2 t }{\mathrm{d}s^2 } + \nu' \frac{\mathrm{d}t }{\mathrm{d}s } \frac{\mathrm{d}r }{\mathrm{d}s } 
=0,\quad \mathrm{or} \quad 
\mathrm{d}s^2 = -c^2\mathrm{e}^\nu \mathrm{d}t^2 + \mathrm{e}^{-\nu}\mathrm{d}r^2 + r^2\mathrm{d}\phi^2
\end{equation}
$$

$$
\begin{equation}
\frac{\mathrm{d}^2 r }{\mathrm{d}s^2 } + \frac{c^2 \nu'}{2 } \mathrm{e}^{2\nu} \left(\frac{\mathrm{d}t }{\mathrm{d}s } \right)^2 - \frac{\nu' }{2 } \left(\frac{\mathrm{d}r }{\mathrm{d}s }  \right)^2 - r\mathrm{e}^\nu \left(\frac{\mathrm{d}\phi }{\mathrm{d}s }  \right)^2
=0
\end{equation}
$$

$$
\begin{equation}
\frac{\mathrm{d}^2 \phi }{\mathrm{d}s^2 } + \frac{2 }{r } \frac{\mathrm{d}r }{\mathrm{d}s } \frac{\mathrm{d}\phi }{\mathrm{d}s } 
=0
\end{equation}
$$

注意到上面第三条方程

$$
\begin{equation}
\frac{\mathrm{d}^2 \phi }{\mathrm{d}s^2 } + \frac{2 }{r } \frac{\mathrm{d}r }{\mathrm{d}s } \frac{\mathrm{d}\phi }{\mathrm{d}s } 
=0,\quad
r^2\frac{\mathrm{d}^2 \phi }{\mathrm{d}s^2 } + 2r \frac{\mathrm{d}r }{\mathrm{d}s } \frac{\mathrm{d}\phi }{\mathrm{d}s } 
=0,\quad
r^2 \frac{\mathrm{d} }{\mathrm{d}s }  \frac{\mathrm{d} \phi }{\mathrm{d}s } + \frac{\mathrm{d}\left(r^2 \right) }{\mathrm{d}s } \frac{\mathrm{d}\phi }{\mathrm{d}s } 
=0
\end{equation}
$$

也即

$$
\begin{equation}
\frac{\mathrm{d} }{\mathrm{d}s } \left(r^2 \frac{\mathrm{d}\phi }{\mathrm{d}s }  \right)
=0
\end{equation}
$$

因此

$$
\begin{equation}
r^2 \frac{\mathrm{d}\phi }{\mathrm{d}s } = \mathrm{const} \equiv \frac{h }{c } 
\end{equation}
$$

这是 GR 中的角动量守恒。

我们要找轨道方程，因此需要找到 $r,\phi $ 的微分方程。

由于 $\theta=\pi/2 $，则线元

$$
\begin{equation}
\mathrm{d}s^2
=-c^2 \mathrm{e}^\nu \mathrm{d}t^2 + \mathrm{e}^{-\nu}\mathrm{d}r^2 + r^2\left(\mathrm{d}\theta^2 +\sin^2\theta\mathrm{d}\phi^2 \right),\quad
\mathrm{e}^\nu
=1-\frac{2GM }{c^2 r } 
\end{equation}
$$

可化简为

$$
\begin{equation}
\mathrm{d}s^2
=-c^2 \mathrm{e}^\nu \mathrm{d}t^2 + \mathrm{e}^{-\nu}\mathrm{d}r^2 + r^2\mathrm{d}\phi^2
\end{equation}
$$

利用线元 $\mathrm{d}s^2 $ 与线长 $\mathrm{d}s $ 的关系

$$
\begin{equation}
\mathrm{d}s
=\sqrt{-\mathrm{d}s^2},\quad
\left(\mathrm{d}s \right)^2
=-\mathrm{d}s^2
=c^2 \mathrm{e}^\nu \mathrm{d}t^2 - \mathrm{e}^{-\nu}\mathrm{d}r^2 - r^2\mathrm{d}\phi^2
\end{equation}
$$

两边同除 $\left(\mathrm{d}s \right)^2 $，再同乘 $\mathrm{e}^\nu $，得到

$$
\begin{equation}
\left(\frac{\mathrm{d}r }{\mathrm{d}s }  \right)^2
=c^2 \mathrm{e}^{2\nu} \left(\frac{\mathrm{d}t }{\mathrm{d}s }  \right)^2 - r^2 \mathrm{e}^\nu \left(\frac{\mathrm{d}\phi }{\mathrm{d}s }  \right)^2 - \mathrm{e}^\nu
\end{equation}
$$

上式代入 $r $ 关于 $s $ 的二阶偏微分方程，就消去 $t $：

$$
\begin{equation}
\frac{\mathrm{d}^2 r }{\mathrm{d}s^2 } + \frac{\nu' }{2 } \mathrm{e}^\nu r^2 \left(\frac{\mathrm{d} \phi}{\mathrm{d}s }  \right)^2 - r\mathrm{e}^\nu \left(\frac{\mathrm{d}\phi }{\mathrm{d}s }  \right)^2 + \frac{1 }{2 } \nu' \mathrm{e}^\nu
=0
\end{equation}
$$

$$
\begin{equation}
\frac{\mathrm{d}^2 r }{\mathrm{d}s^2 } + \left(\frac{1 }{2 } r^2 \nu' \mathrm{e}^\nu - r \mathrm{e}^\nu  \right) \left(\frac{\mathrm{d} \phi}{\mathrm{d}s }  \right)^2 + \frac{1 }{2 } \nu' \mathrm{e}^\nu
=0
\end{equation}
$$

这就是GR中参数形式的行星轨道方程。

利用 GR 中的角动量守恒

$$
\begin{equation}
r^2 \frac{\mathrm{d}\phi }{\mathrm{d}s } 
=\frac{h }{c } ,\quad
\frac{\mathrm{d}\phi }{\mathrm{d}s } = \frac{h }{cr^2 } 
\end{equation}
$$

进一步化简为

$$
\begin{equation}
\frac{\mathrm{d}^2 r }{\mathrm{d}s^2 } + \left(\frac{\nu' }{2 } r^2 - r \right)\mathrm{e}^\nu \left(\frac{h }{c r^2 }  \right)^2 + \frac{1 }{2 } \nu' \mathrm{e}^\nu
=0
\end{equation}
$$

$$
\begin{equation}
\frac{\mathrm{d}^2 r }{\mathrm{d}s^2 } + \frac{1 }{2 } \nu' \mathrm{e}^\nu \left(\frac{h^2 }{c^2 r^2}  + 1 \right) - r\mathrm{e}^\nu \left(\frac{h }{c r^2 } \right)^2
=0
\end{equation}
$$

令 $u=\frac{1 }{r }  $，注意到

$$
\begin{equation}
\mathrm{e}^\nu = 1 - \frac{2GM }{c^2 r } = 1 - \frac{2GM }{c^2 } u
\end{equation}
$$

$$
\begin{equation}
\nu' \mathrm{e}^\nu = \left(\mathrm{e}^\nu \right)'
=\frac{2GM }{c^2 r^2}
=\frac{2GM }{c^2 } u^2 
\end{equation}
$$

$$
\begin{equation}
\frac{\mathrm{d}\phi }{\mathrm{d}s } 
=\frac{h }{cr^2 }
=\frac{h }{c } u^2
\end{equation}
$$

$$
\begin{equation}
\frac{\mathrm{d} }{\mathrm{d}s } 
=\frac{\mathrm{d}\phi }{\mathrm{d}s } \frac{\mathrm{d} }{\mathrm{d}\phi } 
=\frac{h }{c } u^2 \frac{\mathrm{d} }{\mathrm{d}\phi } 
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
\frac{\mathrm{d}^2 r }{\mathrm{d}s } 
&=\frac{\mathrm{d} }{\mathrm{d}s } \left(\frac{\mathrm{d}(1/u) }{\mathrm{d}s }  \right)
=\frac{\mathrm{d} }{\mathrm{d}s } \left(-\frac{1 }{u^2 } \frac{\mathrm{d}u }{\mathrm{d}s }  \right)
=\frac{\mathrm{d} }{\mathrm{d}s } \left[-\frac{1 }{u^2 } \cdot \left(\frac{h }{c } u^2 \frac{\mathrm{d} u}{\mathrm{d}\phi }  \right) \right] \\
&=-\frac{h }{c } \frac{\mathrm{d} }{\mathrm{d}s } \left(\frac{\mathrm{d}u }{\mathrm{d}\phi }  \right) 
=-\frac{h }{c } \cdot \frac{h }{c } u^2 \frac{\mathrm{d} }{\mathrm{d}\phi } \left(\frac{\mathrm{d}u }{\mathrm{d}\phi }  \right) \\
&=-\frac{h^2 }{c^2 } u^2 \frac{\mathrm{d}^2 u }{\mathrm{d}\phi^2 } 
\end{aligned}
\end{equation}
$$

于是轨道的参数方程就化为如下的轨道方程：

$$
\begin{equation}
\frac{\mathrm{d}^2 u }{\mathrm{d}\phi^2 } + u
=\frac{3GM }{c^2 } u^2 + \frac{GM }{h^2 } 
\end{equation}
$$

上式就是GR中的Binet方程。

设 $u_0 $ 满足牛顿力学中的Binet方程

$$
\begin{equation}
\frac{\mathrm{d}^2 u_0 }{\mathrm{d}\phi^2 } +u_0
=\frac{GM }{h^2 } 
\end{equation}
$$

其解为

$$
\begin{equation}
u_0
=\frac{1 }{p } \left(1+e\cos\phi \right),\quad
p
=\frac{h^2 }{GM }
\end{equation}
$$

令 $\alpha=3GM/c^2 $，则

$$
\begin{equation}
\frac{\mathrm{d}^2 u }{\mathrm{d}\phi^2 } + u
=\alpha u^2 + \frac{GM }{h^2 } 
\end{equation}
$$

设 $u=u_0+\alpha u_1 $，则

$$
\begin{equation}
\frac{\mathrm{d}^2u_0 }{\mathrm{d}\phi^2 } +u_0 + \alpha \frac{\mathrm{d}^2u_1 }{\mathrm{d}\phi^2 } +\alpha u_1
=\alpha\left(u_0+\alpha u_1 \right)^2 + \frac{GM }{h^2 } 
\end{equation}
$$

利用 $u_0 $ 满足的方程就得到

$$
\begin{equation}
\alpha \frac{\mathrm{d}^2u_1 }{\mathrm{d}\phi^2 } +\alpha u_1
=\alpha\left(u_0+\alpha u_1 \right)^2
\end{equation}
$$

由于 $\alpha $ 是个小量，约去右边括号内的高阶小量，再利用 $u_0 $ 的表达式，就得到

$$
\begin{equation}
\frac{\mathrm{d}^2u_1 }{\mathrm{d}\phi^2 } + u_1
=u_0^2
=\frac{\left(1+e\cos\phi \right)^2 }{p^2 } 
=\frac{1 }{p^2 } \left[\left(1+\frac{e^2 }{2 }  \right) + 2e\cos\phi + \frac{e^2 }{2 } \cos 2\phi \right]
\end{equation}
$$

设 $u_1 $ 的形式解为

$$
\begin{equation}
u_1 = A + B \phi\sin\phi + C \cos 2\phi
\end{equation}
$$

$$
\begin{equation}
\frac{\mathrm{d}u_1 }{\mathrm{d}\phi } 
=B\left(\sin\phi + \phi\cos\phi \right) - 2C\sin2\phi
\end{equation}
$$

$$
\begin{equation}
\frac{\mathrm{d}^2u_1 }{\mathrm{d}\phi^2 } 
=B\left(2\cos\phi - \phi\sin\phi \right) - 4C\cos2\phi
\end{equation}
$$

代回方程得到

$$
\begin{equation}
B\left(2\cos\phi - \phi\sin\phi \right) -4C\cos2\phi + A + B\phi\sin\phi + C\cos2\phi
=\frac{1 }{p^2 } \left[\left(1+\frac{e^2 }{2 }  \right) + 2e\cos\phi + \frac{e^2 }{2 } \cos 2\phi \right]
\end{equation}
$$

对比各项前的系数就得到

$$
\begin{equation}
A = \frac{1 }{p^2 } \left(1+\frac{e^2 }{2 }  \right),\quad
B = \frac{e }{p^2 } ,\quad
C = -\frac{e^2 }{6p^2 } 
\end{equation}
$$

因此

$$
\begin{equation}
u_1
=\frac{1 }{p^2 } \left(1+\frac{e^2 }{2 }  \right) + \frac{e }{p^2 } \phi\sin\phi - \frac{e^2 }{6p^2 } \cos2\phi
\end{equation}
$$

$$
\begin{equation}
u
=u_0 + \alpha u_1
=\frac{1 }{p } \left[\left(1+e\cos\phi \right) + \frac{\alpha }{p } \left(1+\frac{e^2 }{2 }  \right) + \frac{\alpha e }{p } \phi\sin\phi - \frac{1 }{6 } \frac{\alpha e^2 }{p^2 } \cos2\phi \right]
\end{equation}
$$

上面只有 $\phi\sin\phi $ 项是累加的，只保留对轨道有长期影响的项：

$$
\begin{equation}
u
=\frac{1 }{p } \left[\left(1+e\cos\phi \right) + \frac{\alpha e }{p } \phi\sin\phi \right]
\end{equation}
$$

由于 $\alpha $ 是小量，则

$$
\begin{equation}
1 \approx \cos\left(\frac{\alpha }{p } \phi \right),\quad
\frac{\alpha }{p } \phi \approx \sin \left(\frac{\alpha }{p } \phi \right)
\end{equation}
$$

于是

$$
\begin{equation}
\begin{aligned}
u
&=\frac{1 }{p } \left[\left(1+e\cos\phi \right) + \frac{\alpha e }{p } \phi\sin\phi \right] \\
&=\frac{1 }{p } \left[1 + e\left(1\cdot \cos \phi + \frac{\alpha }{p } \phi \sin\phi \right) \right] \\
&\approx \frac{1 }{p } \left[1 + e\left(\cos\left(\frac{\alpha }{p } \phi \right) \cos \phi + \sin\left(\frac{\alpha }{p } \phi \right) \sin\phi \right) \right] \\
&=\frac{1 }{p } \left[1 + \cos\left(\left(1-\frac{\alpha }{p } \right)\phi \right) \right] \\
&\equiv \frac{1 }{p } \left(1 + e\cos \Phi \right)
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\Phi
\equiv \left(1-\frac{\alpha }{p }  \right) \phi
\end{equation}
$$

当 $\Phi=\Phi_n=(2n+1)\pi $ 时，$\cos\Phi=-1 $，此时 $u $ 最小，$r $ 最大，相应 $\phi_n $ 为

$$
\begin{equation}
\phi_n
=\frac{\Phi_n }{1-\alpha/p } 
\approx \Phi_n \left(1 + \frac{\alpha }{p }  \right)
\end{equation}
$$

$$
\begin{equation}
\phi_{n+1} 
\approx \Phi_{n+1}\left(1+\frac{\alpha }{p }  \right)
\end{equation}
$$

于是

$$
\begin{equation}
\phi_{n+1} - \phi_n
=2\pi \left(1+\frac{\alpha }{p }  \right)
\end{equation}
$$

一周期进动角为

$$
\begin{equation}
\Delta
=\phi_{n+1} - \phi_n - 2\pi
=2\pi \frac{\alpha }{p } 
=\frac{6\pi GM }{c^2 p } 
\end{equation}
$$

由

$$
\begin{equation}
T^2
=\frac{4\pi^2 }{GM } a^3,\quad
GM
=4\pi^2 \frac{a^3 }{T^2 } ,\quad
p
=a\left(1-e^2 \right)
\end{equation}
$$

可得

$$
\begin{equation}
\Delta
=\frac{24\pi^3 a^2}{c^2 T^2\left(1-e^2 \right) } 
\end{equation}
$$

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

史瓦西时空线元：

$$
\begin{equation}
\mathrm{d}s^2
=-\left(1-2M/r \right) \mathrm{d}t^2 + \left(1-2M/r \right)^{-1} \mathrm{d}r^2 + r^2\left(\mathrm{d}\theta^2 + \sin^2\theta\mathrm{d}\phi^2 \right)
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