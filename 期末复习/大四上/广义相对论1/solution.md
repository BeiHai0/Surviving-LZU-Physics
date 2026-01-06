# 1

计算牛顿近似中的所有非零联络 $\Gamma_{\mu\nu}^\lambda $

# 2

写出逆变、协变与二阶张量的坐标变换式，已知 $A^\mu_\nu=\partial \bar{x}^\mu/\partial x^\nu,\bar{A}^\mu_\nu=\partial x^\mu/\partial\bar{x}^\nu $ 且 $\mathrm{det}\left[A^\mu_\nu \right]\ne 0 $，并写出它们的协变微分表达式。

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

# 5

求弱场线性近似的里奇张量，并导出线性化的场方程。

# 6

推导光线在行星附近的轨道方程，并讨论其偏折，这证明了GR的什么效应？

# 7

推导史瓦西时空与闵可夫斯基时空的类光测地线，简述并画出krusal延拓图与彭罗斯图。