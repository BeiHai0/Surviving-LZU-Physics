# 1

## 1.1

> 证明弧元 $\mathrm{d}s^2\equiv eg_{\mu\nu}\mathrm{d}x^\mu\mathrm{d}x^\nu $ 是坐标变换下的不变量。

$$
\begin{align}
\mathrm{d}x'^\mu
=\frac{\partial x'^\mu }{\partial x^\nu } \mathrm{d}x^\nu
=A^\mu_\nu \mathrm{d}x^\nu
\end{align}
$$

$$
\begin{equation}
\begin{split}
\mathrm{d}s'^2
&\equiv e g'_{\mu\nu} \mathrm{d}x'^\mu \mathrm{d}x'^\nu \\
&=e \bar{A}_\mu^\alpha \bar{A}_\nu^\beta g_{\alpha\beta} \left(A^\mu_\lambda \mathrm{d}x^\lambda \right) \left(A^\nu_\rho \mathrm{d}x^\rho \right) \\
&=e g_{\alpha\beta} \left(\bar{A}_\mu^\alpha A^\mu_\lambda \right) \left(\bar{A}_\nu^\beta A^\nu_\rho \right) \mathrm{d}x^\lambda \mathrm{d}x^\rho \\
&=e g_{\alpha\beta} \delta^\alpha_\lambda \delta^\beta_\rho \mathrm{d}x^\lambda \mathrm{d}x^\rho \\
&=e g_{\alpha\beta} \mathrm{d}x^\alpha \mathrm{d}x^\beta
\end{split}
\end{equation}
$$

## 1.2

> 由协变微商的协变性推导联络在坐标变换下的变换式。

由定义

$$
\begin{align}
\nabla_\mu \phi^\nu(x)
\equiv \partial_\mu \phi^\nu(x) + \Gamma^\nu_{\mu \lambda} \phi^\lambda(x)
\end{align}
$$

$$
\begin{align}
\nabla'_\mu \phi'^\nu(x')
\equiv \partial'_\mu \phi'^\nu(x) + \Gamma'^\nu_{\mu \lambda} \phi'^\lambda(x')
\end{align}
$$

我们知道 $\partial_\mu $ 是协变矢量，$\phi^\nu(x) $ 是逆变矢量，利用它们的变换规律

$$
\begin{align}
\partial'_\mu
=\bar{A}_\mu^\alpha \partial_\alpha,\quad
\phi'^\nu(x')
=A^\nu_\beta \phi^\beta(x)
\end{align}
$$

有

$$
\begin{equation}
\begin{split}
\nabla'_\mu \phi'^\nu(x')
&\equiv \partial'_\mu \phi'^\nu(x) + \Gamma'^\nu_{\mu \lambda} \phi'^\lambda(x') \\
&=\bar{A}_\mu^\alpha \partial_\alpha \left[A^\nu_\beta \phi^\beta(x) \right] + \Gamma'^\nu_{\mu \lambda} A^\lambda_\gamma \phi^\gamma(x) \\
&=\bar{A}_\mu^\alpha \left(\partial_\alpha A^\nu_\beta \right) \phi^\beta(x) + \bar{A}_\mu^\alpha A^\nu_\beta \partial_\alpha \phi^\beta(x) + \Gamma'^\nu_{\mu \lambda} A^\lambda_\gamma \phi^\gamma(x) \\
\end{split}
\end{equation}
$$

而我们希望逆变矢量的协变微商是一个张量，其满足张量的变换规律

$$
\begin{equation}
\begin{split}
\nabla'_\mu \phi'^\nu(x')
&=\bar{A}_\mu^{\alpha} A^\nu_{\beta} \nabla_\alpha \phi^\beta(x) \\
&=\bar{A}_\mu^{\alpha} A^\nu_{\beta} \left[\partial_\alpha \phi^\beta(x) + \Gamma^\beta_{\alpha \gamma} \phi^\gamma(x) \right] \\
&=\bar{A}_\mu^{\alpha} A^\nu_{\beta} \partial_\alpha \phi^\beta(x) + \bar{A}_\mu^{\alpha} A^\nu_{\beta} \Gamma^\beta_{\alpha \gamma} \phi^\gamma(x)
\end{split}
\end{equation}
$$

有

$$
\begin{align}
\bar{A}_\mu^\alpha \left(\partial_\alpha A^\nu_\beta \right) \phi^\beta(x) + \red{\bar{A}_\mu^\alpha A^\nu_\beta \partial_\alpha \phi^\beta(x)} + \Gamma'^\nu_{\mu \lambda} A^\lambda_\gamma \phi^\gamma(x)
=\red{\bar{A}_\mu^{\alpha} A^\nu_{\beta} \partial_\alpha \phi^\beta(x)} + \bar{A}_\mu^{\alpha} A^\nu_{\beta} \Gamma^\beta_{\alpha \gamma} \phi^\gamma(x)
\end{align}
$$

化简为

$$
\begin{align}
\Gamma'^\nu_{\mu \lambda} A^\lambda_\gamma \phi^\gamma(x)
=\bar{A}_\mu^{\alpha} A^\nu_{\beta} \Gamma^\beta_{\alpha \gamma} \phi^\gamma(x) - \bar{A}_\mu^\alpha \left(\partial_\alpha A^\nu_{\red{\beta}} \right) \phi^{\red{\beta}}(x)
\end{align}
$$

替换哑标得

$$
\begin{align}
\Gamma'^\nu_{\mu \lambda} A^\lambda_\gamma \phi^\gamma(x)
=\bar{A}_\mu^{\alpha} A^\nu_{\beta} \Gamma^\beta_{\alpha \gamma} \phi^\gamma(x) - \bar{A}_\mu^\alpha \left(\partial_\alpha A^\nu_{\red{\gamma}} \right) \phi^{\red{\gamma}}(x)
\end{align}
$$

因此有

$$
\begin{align}
\Gamma'^\nu_{\mu \lambda} A^\lambda_\gamma
=\bar{A}_\mu^{\alpha} A^\nu_{\beta} \Gamma^\beta_{\alpha \gamma} - \bar{A}_\mu^\alpha \left(\partial_\alpha A^\nu_{\gamma} \right) 
\end{align}
$$

两边同乘 $\bar{A}^\gamma_\rho $，并对 $\gamma $ 求和，$\left(11 \right) $ 式左边

$$
\begin{equation}
\begin{split}
\Gamma'^\nu_{\mu \lambda} A^\lambda_\gamma \bar{A}^\gamma_\rho
&=\Gamma'^\nu_{\mu \lambda} \delta^\lambda_\rho \\
&=\Gamma'^\nu_{\mu \rho}
\end{split}
\end{equation}
$$

$\left(11 \right) $ 式右边

$$
\begin{equation}
\begin{split}
\bar{A}^\gamma_\rho \left[\bar{A}_\mu^{\alpha} A^\nu_{\beta} \Gamma^\beta_{\alpha \gamma} - \bar{A}_\mu^\alpha \left(\partial_\alpha A^\nu_{\gamma} \right) \right]
&=\bar{A}^\gamma_\rho \bar{A}_\mu^{\alpha} A^\nu_{\beta} \Gamma^\beta_{\alpha \gamma} - \bar{A}_\mu^\alpha \red{\bar{A}^\gamma_\rho \partial_\alpha A^\nu_{\gamma}} \\
&=\bar{A}^\gamma_\rho \bar{A}_\mu^{\alpha} A^\nu_{\beta} \Gamma^\beta_{\alpha \gamma} - \bar{A}_\mu^\alpha \red{\left[\partial_\alpha\left(\bar{A}^\gamma_\rho A^\nu_\gamma \right) - A^\nu_\gamma \partial_\alpha \bar{A}^\gamma_\rho \right]} \\
&=\bar{A}^\gamma_\rho \bar{A}_\mu^{\alpha} A^\nu_{\beta} \Gamma^\beta_{\alpha \gamma} - \bar{A}_\mu^\alpha \red{\left[\partial_\alpha \delta^\nu_\rho - A^\nu_\gamma \partial_\alpha \bar{A}^\gamma_\rho \right]} \\
&=\bar{A}^\gamma_\rho \bar{A}_\mu^{\alpha} A^\nu_{\beta} \Gamma^\beta_{\alpha \gamma} + \bar{A}_\mu^\alpha A^\nu_\gamma \partial_\alpha \bar{A}^\gamma_\rho \\
&=A^\nu_{\beta} \bar{A}_\mu^{\alpha} \bar{A}^\gamma_\rho \Gamma^\beta_{\alpha \gamma} + A^\nu_\gamma \bar{A}_\mu^\alpha \partial_\alpha \bar{A}^\gamma_\rho \\
\end{split}
\end{equation}
$$

于是得到联络的变换规律

$$
\begin{align}
\Gamma'^\nu_{\mu \rho}
=A^\nu_{\beta} \bar{A}_\mu^{\alpha} \bar{A}^\gamma_\rho \Gamma^\beta_{\alpha \gamma} + A^\nu_\gamma \bar{A}_\mu^\alpha \partial_\alpha \bar{A}^\gamma_\rho
\end{align}
$$

替换指标就得到

$$
\begin{align}
\Gamma'^\mu_{\nu\lambda}
=A^\mu_{\alpha} \bar{A}_\nu^{\beta} \bar{A}_\lambda^\gamma \Gamma^\alpha_{\beta\gamma} + A^\mu_\alpha \bar{A}_\nu^\beta \partial_\beta \bar{A}^\alpha_\lambda
\end{align}
$$

## 1.3

> 证明挠率 $\Gamma_{[\mu,\nu]}^\lambda $ 是一个张量。

$$
\begin{align}
\Gamma'^\lambda_{\mu\nu}
=A^\lambda_\alpha \bar{A}_\mu^\beta \bar{A}_\nu^\gamma \Gamma^\alpha_{\beta\gamma} + A^\lambda_\alpha \bar{A}_\mu^\beta \partial_\beta \bar{A}^\alpha_\nu
\end{align}
$$

$$
\begin{align}
\Gamma'^\lambda_{\nu\mu}
=A^\lambda_\alpha \bar{A}_\nu^\beta \bar{A}_\mu^\gamma \Gamma^\alpha_{\beta\gamma}  + A^\lambda_\alpha \bar{A}_\nu^\beta \partial_\beta \bar{A}^\alpha_\mu
\end{align}
$$

注意到

$$
\begin{equation}
\begin{split}
\bar{A}_\mu^\beta \partial_\beta \bar{A}^\alpha_\nu - \bar{A}_\nu^\beta \partial_\beta \bar{A}^\alpha_\mu
&\equiv \frac{\partial x^\beta }{\partial x'^\mu } \frac{\partial }{\partial x^\beta } \frac{\partial x^\alpha }{\partial x'^\nu } - \frac{\partial x^\beta }{\partial x'^\nu } \frac{\partial }{\partial x^\beta } \frac{\partial x^\alpha }{\partial x'^\mu } \\
&=\frac{\partial }{\partial x'^\mu } \frac{\partial x^\alpha }{\partial x'^\nu } - \frac{\partial }{\partial x'^\nu } \frac{\partial x^\alpha }{\partial x'^\mu } \\
&=0
\end{split}
\end{equation}
$$

因此

$$
\begin{equation}
\begin{split}
\Gamma'^\lambda_{[\mu,\nu]}
&\equiv \Gamma'^\lambda_{\mu\nu} - \Gamma'^\lambda_{\nu\mu} \\
&=\left(A^\lambda_\alpha \bar{A}_\mu^\beta \bar{A}_\nu^\gamma \Gamma^\alpha_{\beta\gamma} + A^\lambda_\alpha \bar{A}_\mu^\beta \partial_\beta \bar{A}^\alpha_\nu \right) - \left(A^\lambda_\alpha \bar{A}_\nu^\beta \bar{A}_\mu^\gamma \Gamma^\alpha_{\beta\gamma}  + A^\lambda_\alpha \bar{A}_\nu^\beta \partial_\beta \bar{A}^\alpha_\mu \right) \\
&=\left(A^\lambda_\alpha \bar{A}_\mu^\beta \bar{A}_\nu^\gamma \Gamma^\alpha_{\beta\gamma} - A^\lambda_\alpha \bar{A}_\nu^\beta \bar{A}_\mu^\gamma \Gamma^\alpha_{\beta\gamma} \right) + A^\lambda_\alpha\left(\bar{A}_\mu^\beta \partial_\beta \bar{A}^\alpha_\nu - \bar{A}_\nu^\beta \partial_\beta \bar{A}^\alpha_\mu \right) \\
&=A^\lambda_\alpha \bar{A}_\mu^\beta \bar{A}_\nu^\gamma \Gamma^\alpha_{\beta\gamma} - A^\lambda_\alpha \bar{A}_\nu^{\red{\beta}} \bar{A}_\mu^{\green{\gamma}} \Gamma^\alpha_{\red{\beta}\green{\gamma}} \\
&=A^\lambda_\alpha \bar{A}_\mu^\beta \bar{A}_\nu^\gamma \Gamma^\alpha_{\beta\gamma} - A^\lambda_\alpha \bar{A}_\nu^{\red{\gamma}} \bar{A}_\mu^{\green{\beta}} \Gamma^\alpha_{\red{\gamma}\green{\beta}} \\
&=A^\lambda_\alpha \bar{A}_\mu^\beta \bar{A}_\nu^\gamma \left(\Gamma^\alpha_{\beta\gamma} - \Gamma^\alpha_{\gamma\beta} \right) \\
&=A^\lambda_\alpha \bar{A}_\mu^\beta \bar{A}_\nu^\gamma \Gamma^\alpha_{\left[\beta,\gamma \right]}
\end{split}
\end{equation}
$$

## 1.4

> 由 $\nabla_\lambda g_{\mu\nu}=0 $ 证明 $\nabla_\lambda g^{\mu\nu}=0 .$

$$
\begin{align}
g^{\mu\alpha} g_{\alpha\nu}
=\delta^\mu_\nu
\end{align}
$$

两边用协变微商作用

$$
\begin{align}
\nabla_\lambda \left(g^{\mu\alpha} g_{\alpha\nu} \right)
=0
\end{align}
$$

利用协变微商的莱布尼兹律

$$
\begin{equation}
\begin{split}
\nabla_\lambda \left(g^{\mu\alpha} g_{\alpha\nu} \right)
&=\left(\nabla_\lambda g^{\mu\alpha} \right) g_{\alpha\nu} + g^{\mu\alpha}\left(\nabla_\lambda g_{\alpha\nu} \right) \\
&=\left(\nabla_\lambda g^{\mu\alpha} \right) g_{\alpha\nu}
\end{split}
\end{equation}
$$

得到

$$
\begin{equation}
\begin{split}
\left(\nabla_\lambda g^{\mu\alpha} \right) g_{\alpha\nu} = 0
\end{split}
\end{equation}
$$

上式两边乘 $g^{\nu\beta} $ 并对 $\nu $ 求和

$$
\begin{equation}
\begin{split}
0
&=\left(\nabla_\lambda g^{\mu\alpha} \right) g_{\alpha\nu} g^{\nu\beta} \\
&=\left(\nabla_\lambda g^{\mu\alpha} \right) \delta^\beta_\alpha \\
&=\nabla_\lambda g^{\mu\beta}
\end{split}
\end{equation}
$$

## 1.5

> 假设有一对称张量 $f_{\mu\nu} $ 及其逆 $f^{\mu\nu} $ 可对张量指标进行升降
> 
> $$
> \begin{align}
> f_{\mu\nu} \phi^\nu
> =\phi_\mu,\quad
> f^{\mu\nu} \phi_\nu
> =\phi^\mu
> \end{align}
> $$
> 
> 由协变微商定义及其性质，证明此张量的协变微商为零，即
> 
> $$
> \begin{align}
> \nabla_\lambda f_{\mu\nu} = 0
> \end{align}
> $$

$$
\begin{align}
\phi_\mu = f_{\mu\nu} \phi^\nu
\end{align}
$$

$$
\begin{equation}
\begin{split}
\nabla_\lambda \phi_\mu
&=\nabla_\lambda\left(f_{\mu\nu} \phi^\nu \right) \\
&=\left(\nabla_\lambda f_{\mu\nu} \right) \phi^\nu + f_{\mu\nu} \left(\nabla_\lambda \phi^\nu \right) \\
&=\left(\nabla_\lambda f_{\mu\nu} \right) \phi^\nu + \nabla_\lambda \phi_\mu \\
\end{split}
\end{equation}
$$

前后对比得

$$
\begin{align}
\left(\nabla_\lambda f_{\mu\nu} \right) \phi^\nu = 0
\end{align}
$$

由 $\phi^\nu $ 的任意性有

$$
\begin{align}
\nabla_\lambda f_{\mu\nu} = 0
\end{align}
$$

# 2

## 2.1

> 已知 $\mathrm{d}s^2=g_{\mu\nu} \mathrm{d}x^\mu \mathrm{d}x^\nu=-\mathrm{d}\tau^2 $，从变分原理 $\displaystyle{\delta \int_A^B \mathrm{d}s=0 }$ 或 $\displaystyle{\delta\int_A^B \left(\mathrm{d}\tau/\mathrm{d}\lambda \right)^2 \mathrm{d}\lambda=0 }$ 求出“短”程线方程。

段先生书上已经有对线长变分求短程线的过程，也就是从

$$
\begin{equation}
\delta \int_{\lambda_1}^{\lambda_2} \sqrt{-g_{\mu\nu} \dot{x}^\mu \dot{x}^{\nu}} \mathrm{d}\lambda
=0
\end{equation}
$$

出发找到 $x^\mu(\lambda) $ 要满足的方程。

这里

$$
\begin{equation}
\mathrm{d}\tau
=\sqrt{-g_{\mu\nu}\mathrm{d}x^\mu\mathrm{d}x^\nu}
=\sqrt{-g_{\mu\nu} \dot{x}^\mu \dot{x}^{\nu}}\mathrm{d}\lambda,
\end{equation}
$$

也就是从

$$
\begin{equation}
\delta \int_{\lambda_1}^{\lambda_2} -g_{\mu\nu} \dot{x}^\mu \dot{x}^{\nu} \mathrm{d}\lambda
=0
\end{equation}
$$

出发推导短程线方程。也即

$$
\begin{equation}
\int_{\lambda_1}^{\lambda_2} \delta(-g_{\mu\nu} \dot{x}^\mu \dot{x}^{\nu}) \mathrm{d}\lambda
=0
\end{equation}
$$

令：

$$
\begin{equation}
F(x,\dot{x}) 
=-g_{\mu\nu} \dot{x}^\mu \dot{x}^\nu,
\end{equation}
$$

$$
\begin{equation}
\begin{split}
\delta F
&=-\delta\left(g_{\mu\nu} \dot{x}^\mu \dot{x}^\nu \right) \\
&=-\left[\dot{x}^\mu \dot{x}^\nu \delta g_{\mu\nu} + g_{\mu\nu} \dot{x}^\nu \delta\dot{x}^\mu + g_{\mu\nu} \dot{x}^\mu \delta \dot{x}^\nu \right] \\
&=-\left[\dot{x}^\mu \dot{x}^\nu \partial_\alpha g_{\mu\nu} \delta x^\alpha + g_{\mu\nu} \dot{x}^\nu \frac{\mathrm{d} }{\mathrm{d}\lambda } \delta x^\mu + g_{\mu\nu} \dot{x}^\mu \frac{\mathrm{d} }{\mathrm{d}\lambda } \delta x^\nu \right] \\
&=-\left[\dot{x}^\mu \dot{x}^\nu \partial_\alpha g_{\mu\nu} \delta x^\alpha + g_{\alpha\nu} \dot{x}^\nu \frac{\mathrm{d} }{\mathrm{d}\lambda } \delta x^\alpha + g_{\mu\alpha} \dot{x}^\mu \frac{\mathrm{d} }{\mathrm{d}\lambda } \delta x^\alpha \right] \\
&=-\left\{\dot{x}^\mu \dot{x}^\nu \partial_\alpha g_{\mu\nu} \delta x^\alpha + \frac{\mathrm{d} }{\mathrm{d}\lambda } \left[\left(g_{\alpha\nu} \dot{x}^\nu + g_{\mu\alpha} \dot{x}^\mu \right) \delta x^\alpha \right] - \delta x^\alpha \frac{\mathrm{d} }{\mathrm{d}\lambda } \left(g_{\alpha\nu} \dot{x}^\nu + g_{\mu\alpha} \dot{x}^\mu \right) \right\} \\
&=-\frac{\mathrm{d} }{\mathrm{d}\lambda } \left[\left(g_{\alpha\nu} \dot{x}^\nu + g_{\mu\alpha} \dot{x}^\mu \right) \delta x^\alpha \right] + \delta x^\alpha \left[\left(\dot{x}^\nu \partial_\beta g_{\alpha\nu} \dot{x}^\beta + g_{\alpha\nu} \ddot{x}^\nu + \dot{x}^\mu \partial_\beta g_{\mu\alpha} \dot{x}^\beta + g_{\mu\alpha} \ddot{x}^\mu \right) - \dot{x}^\mu \dot{x}^\nu \partial_\alpha g_{\mu\nu} \right] \\
&=-\frac{\mathrm{d} }{\mathrm{d}\lambda } \left[\left(g_{\alpha\nu} \dot{x}^\nu + g_{\mu\alpha} \dot{x}^\mu \right) \delta x^\alpha \right] + \delta x^\alpha \left[\left(\dot{x}^\nu \partial_\mu g_{\alpha\nu} \dot{x}^\mu + g_{\alpha\mu} \ddot{x}^\mu + \dot{x}^\mu \partial_\nu g_{\mu\alpha} \dot{x}^\nu + g_{\alpha\mu} \ddot{x}^\mu \right) - \dot{x}^\mu \dot{x}^\nu \partial_\alpha g_{\mu\nu} \right] \\
&=-\frac{\mathrm{d} }{\mathrm{d}\lambda } \left[\left(g_{\alpha\nu} \dot{x}^\nu + g_{\mu\alpha} \dot{x}^\mu \right) \delta x^\alpha \right] + \delta x^\alpha \left[\dot{x}^\mu \dot{x}^\nu\left(\partial_\mu g_{\alpha\nu} + \partial_\nu g_{\alpha\mu} - \partial_\alpha g_{\mu\nu} \right) + 2g_{\alpha\mu} \ddot{x}^\mu \right] \\
\end{split}
\end{equation}
$$

由 $\displaystyle{\int_{\lambda_1}^{\lambda} \delta F \mathrm{d}\lambda }$ 可得

$$
\begin{equation}
\dot{x}^\mu \dot{x}^\nu\left(\partial_\mu g_{\alpha\nu} + \partial_\nu g_{\alpha\mu} - \partial_\alpha g_{\mu\nu} \right) + 2g_{\alpha\mu} \ddot{x}^\mu
=0
\end{equation}
$$

上式两边同乘 $g_{\lambda \alpha} $ 可得

$$
\begin{equation}
\Gamma^\lambda_{\mu\nu} \dot{x}^\mu \dot{x}^\nu + \ddot{x}^\lambda
=0
\end{equation}
$$

也即短程线方程：

$$
\begin{equation}
\frac{\mathrm{d}^2 x^\lambda }{\mathrm{d}\lambda^2 } + \Gamma^\lambda_{\mu\nu} \frac{\mathrm{d}x^\mu }{\mathrm{d}\lambda } \frac{\mathrm{d}x^\nu }{\mathrm{d}\lambda } 
=0.
\end{equation}
$$




## 2.2

> 已知 $\nabla_\nu A_\mu = \partial_\nu A_\mu - \Gamma^\lambda_{\nu \mu} A_\lambda $，利用标量微分关系 $\nabla_\nu U=\partial_\nu U $ 以及莱布尼茨法则证明 $\nabla_\nu B^\mu = \partial_\nu B^\mu + \Gamma^\mu_{\nu \lambda} B^\lambda .$

一方面，协变微商满足莱布尼兹法则：

$$
\begin{equation}
\begin{split}
\nabla_\nu\left(A_\mu B^\mu \right)
&=B^\mu \nabla_\nu A_\mu + A_\mu \nabla_\nu B^\mu \\
&=B^\mu\left(\partial_\nu A_\mu - \Gamma_{\nu\mu}^\lambda A_\lambda \right) + A_\mu \nabla_\nu B^\mu \\
&=B^\mu \partial_\nu A_\mu - B^\mu \Gamma_{\nu\mu}^\lambda A_\lambda + A_\mu \nabla_\nu B^\mu \\
\end{split}
\end{equation}
$$

另一方面，$A_\mu B^\mu $ 是标量，其协变微商等于普通偏微分：

$$
\begin{equation}
\begin{split}
\nabla_\nu\left(A_\mu B^\mu \right)
&=\partial_\nu \left( A_\mu B^\mu\right) \\
&=B^\mu \partial_\nu A_\mu + A_\mu \partial_\nu B^\mu \\
\end{split}
\end{equation}
$$

对比可得：

$$
\begin{equation}
\begin{split}
A_\mu \nabla_\nu B^\mu
&=A_\mu \partial_\nu B^\mu + B^\mu \Gamma_{\nu\mu}^\lambda A_\lambda \\
&=A_\mu \partial_\nu B^\mu + A_\lambda \Gamma_{\nu\mu}^\lambda B^\mu \\
&=A_\mu \partial_\nu B^\mu + A_\mu \Gamma_{\nu\lambda}^\mu B^\lambda \\
\end{split}
\end{equation}
$$

从而得到：

$$
\begin{equation}
\nabla_\nu B^\mu
=\partial_\nu B^\mu + \Gamma^\mu_{\nu\lambda} B^\lambda
\end{equation}
$$

## 2.3

> 一个嵌入三维欧氏空间的普通球面，选用球极坐标，其线元为 $\mathrm{d}s^2 = a^2 \mathrm{d}\theta^2 + a^2 \sin^2\theta \mathrm{d}\phi^2 $，求：(1) $g^{\nu\mu} $；(2) 全部非零克氏符 $\Gamma^\lambda_{\mu\nu} $；(3) 全部非零 $R^\nu_{\mu\sigma\lambda},R_{\mu\nu},R $；(4) 写出该度规表示的球面空间的测地线方程。

取 $\left(x^1, x^2 \right) = \left(\theta, \phi \right) $，根据线元

$$
\begin{equation}
\mathrm{d}s^2
=g_{\mu\nu}\mathrm{d}x^\mu\mathrm{d}x^\nu
=a^2 \mathrm{d}\theta^2 + a^2 \sin^2\theta \mathrm{d}\phi^2
\end{equation}
$$

可得度规

$$
\begin{equation}
g_{11}=a^2,\quad
g_{12}=g_{21}=0,\quad
g_{22}=a^2\sin^2\theta,
\end{equation}
$$

$$
\begin{equation}
\left[g_{\mu\nu} \right]
=\begin{bmatrix}
a^2 &0 \\
0 &a^2\sin^2\theta
\end{bmatrix}
\end{equation}
$$

以及逆度规

$$
\begin{equation}
\left[g^{\mu\nu} \right]
=\begin{bmatrix}
\frac{1 }{a^2 } &0 \\
0 &\frac{1 }{a^2\sin^2\theta } 
\end{bmatrix}
\end{equation}
$$

$$
\begin{equation}
g^{11}=\frac{1 }{a^2 } ,\quad
g^{12}=g^{21}=0,\quad
g^{22}=\frac{1 }{a^2\sin^2\theta } ,
\end{equation}
$$

由度规 $g_{\mu\nu} $ 以及逆度规 $g^{\mu\nu} $ 可得克氏符：

$$
\begin{equation}
\Gamma_{\mu\nu}^\lambda
=\frac{1 }{2 } g^{\lambda\sigma}\left(\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma \mu} - \partial_\sigma g_{\mu\nu} \right),
\end{equation}
$$

$$
\begin{equation}
\begin{split}
\Gamma_{\mu\nu}^1
&=\frac{1 }{2 } g^{1\sigma}\left(\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma \mu} - \partial_\sigma g_{\mu\nu} \right) \\
&=\frac{1 }{2 } g^{11}\left(\partial_\mu g_{1\nu} + \partial_\nu g_{1 \mu} - \partial_1 g_{\mu\nu} \right) \\
&=\frac{1 }{2a^2 } \left(-\partial_1 g_{\mu\nu} \right) \\
&=-\frac{1 }{2a^2 } \partial_1 g_{\mu\nu}
\end{split}
\end{equation}
$$

$$
\begin{equation}
\Gamma^1_{11} = \Gamma^1_{12} = \Gamma^1_{21} = 0,
\end{equation}
$$

$$
\begin{equation}
\Gamma^1_{22}
=-\frac{1 }{2a^2 } \partial_1 g_{22}
=-\frac{1 }{2a^2 } \partial_\theta \left(a^2\sin^2\theta \right)
=-\sin\theta\cos\theta,
\end{equation}
$$

$$
\begin{equation}
\begin{split}
\Gamma^2_{\mu\nu}
&=\frac{1 }{2 } g^{2\sigma}\left(\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma \mu} - \partial_\sigma g_{\mu\nu} \right) \\
&=\frac{1 }{2 } g^{22}\left(\partial_\mu g_{2\nu} + \partial_\nu g_{2 \mu} - \partial_2 g_{\mu\nu} \right) \\
&=\frac{1 }{2 } g^{22}\left(\partial_\mu g_{2\nu} + \partial_\nu g_{2 \mu} \right) \\
&=\frac{1 }{2a^2\sin^2\theta } \left(\partial_\mu g_{2\nu} + \partial_\nu g_{2 \mu} \right) \\
\end{split}
\end{equation}
$$

$$
\begin{equation}
\Gamma^2_{11} = \Gamma^2_{22} = 0,
\end{equation}
$$

$$
\begin{equation}
\begin{split}
\Gamma^2_{12}
=\Gamma^2_{21}
=\frac{1 }{2a^2\sin^2\theta } \left(\partial_1 g_{22} + \partial_2 g_{2 1} \right) 
=\frac{1 }{2a^2\sin^2\theta } \partial_\theta \left(a^2 \sin^2\theta \right)
=\frac{\cos\theta }{\sin\theta } 
=\cot\theta
\end{split}
\end{equation}
$$

$$
\begin{equation}
R_{\sigma\mu\nu}^\lambda
=\partial_\mu \Gamma_{\nu\sigma}^\lambda - \partial_\nu \Gamma_{\mu\sigma}^\lambda + \Gamma_{\mu\alpha}^\lambda \Gamma_{\nu\sigma}^\alpha - \Gamma_{\nu\alpha}^\lambda \Gamma_{\mu\sigma}^\alpha
\end{equation}
$$

$$
\begin{equation}
\begin{split}
R^1_{212}
=\partial_1 \Gamma_{22}^1 - \partial_2 \Gamma_{12}^1 + \Gamma_{1\alpha}^1 \Gamma_{22}^\alpha - \Gamma_{2\alpha}^1 \Gamma_{12}^\alpha
=\sin^2\theta
\end{split}
\end{equation}
$$

- $\lambda=1 $

- - $(\mu,\nu)=(1,2) $

$$
\begin{equation}
\begin{aligned}
R^1_{\sigma 1 2}
&=\partial_1 \Gamma_{2\sigma}^1 - \partial_2 \Gamma_{1\sigma}^1 + \Gamma_{1\alpha}^1 \Gamma_{2\sigma}^\alpha - \Gamma_{2\alpha}^1 \Gamma_{1\sigma}^\alpha \\
&=\partial_1 \Gamma_{2\sigma}^1 - \Gamma_{22}^1 \Gamma_{1\sigma}^2 \\
\end{aligned}
\end{equation}
$$

- - - $\sigma=1 $

$$
\begin{equation}
\begin{aligned}
R^1_{1 1 2}
&=\partial_1 \Gamma_{2 1}^1 - \Gamma_{22}^1 \Gamma_{1 1}^2 \\
&=- \Gamma_{22}^1 \Gamma_{1 1}^2 \\
&=0
\end{aligned}
\end{equation}
$$

- - - $\sigma=2 $

$$
\begin{equation}
\begin{aligned}
R^1_{2 1 2}
&=\partial_1 \Gamma_{22}^1 - \Gamma_{22}^1 \Gamma_{12}^2 \\
&=\sin^2\theta
\end{aligned}
\end{equation}
$$

- $\lambda=2 $

- - $\left(\mu,\nu \right)=(1,2) $

$$
\begin{equation}
\begin{aligned}
R_{\sigma1 2}^2
&=\partial_1 \Gamma_{ 2\sigma}^2 - \partial_ 2 \Gamma_{1\sigma}^2 + \Gamma_{1\alpha}^2 \Gamma_{ 2\sigma}^\alpha - \Gamma_{ 2\alpha}^2 \Gamma_{1\sigma}^\alpha \\
&=\partial_1 \Gamma_{ 2\sigma}^2 + \Gamma_{12}^2 \Gamma_{ 2\sigma}^2 - \Gamma_{ 21}^2 \Gamma_{1\sigma}^1 \\
&=\partial_1 \Gamma_{ 2\sigma}^2 + \cot\theta \Gamma_{ 2\sigma}^2 - \cot\theta \Gamma_{1\sigma}^1 \\
\end{aligned}
\end{equation}
$$

- - - $\sigma=1 $

$$
\begin{equation}
\begin{aligned}
R_{1 1 2}^2
&=\partial_1 \Gamma_{ 2 1 }^2 + \cot\theta \Gamma_{ 2 1 }^2 - \cot\theta \Gamma_{1 1 }^1 \\
&=\partial_\theta \cot\theta + \cot\theta \cdot \cot\theta \\
&=-1
\end{aligned}
\end{equation}
$$

- - - $\sigma=2 $

$$
\begin{equation}
\begin{aligned}
R_{2 1 2}^2
&=\partial_1 \Gamma_{ 2 2 }^2 + \cot\theta \Gamma_{ 2 2 }^2 - \cot\theta \Gamma_{1 2 }^1 \\
&=0
\end{aligned}
\end{equation}
$$

----

$$
\begin{equation}
\begin{split}
R_{\mu\nu}
=R^{\lambda}_{\mu\lambda\nu}
=R^1_{\mu 1 \nu} + R^2_{\mu 2 \nu}
=R^1_{\mu 1 \nu}
\end{split}
\end{equation}
$$

## 2.4

> 由协变矢量双重协变微商非对称部分 $\phi_{\lambda;[\mu;\nu]} $ 推导曲率张量与挠率张量 $\nabla_\mu \nabla_\nu \phi_\lambda - \nabla_\nu \nabla_\mu \phi_\lambda = -R^\sigma_{\lambda\mu\nu} \phi_\sigma - T^\alpha_{\mu\nu} \nabla_\alpha \phi_\lambda .$

$$
\begin{equation}
\begin{split}
\nabla_\mu \nabla_\nu \phi_\lambda - \mu \leftrightarrow \nu
&=\nabla_\mu \left(\nabla_\nu \phi_\lambda \right) - \mu \leftrightarrow \nu \\
&=\partial_\mu \left(\nabla_\nu \phi_\lambda \right) - \Gamma_{\mu\nu}^\alpha \nabla_\alpha \phi_\lambda - \Gamma_{\mu\lambda}^\alpha \nabla_\nu \phi_\alpha - \mu \leftrightarrow \nu \\
&=\partial_\mu \left(\partial_\nu \phi_\lambda - \Gamma_{\nu\lambda}^\alpha \phi_\alpha \right) - \Gamma_{\mu\nu}^\alpha \nabla_\alpha \phi_\lambda - \Gamma_{\mu\lambda}^\alpha \left(\partial_\nu \phi_\alpha - \Gamma_{\nu\alpha}^\beta \phi_\beta \right) - \mu \leftrightarrow \nu \\
&=\partial_\mu \partial_\nu \phi_\lambda - \left(\partial_\mu \Gamma_{\nu\lambda}^\alpha \right) \phi_\alpha - \Gamma_{\nu\lambda}^\alpha \partial_\mu \phi_\alpha - \Gamma_{\mu\lambda}^\alpha \partial_\nu \phi_\alpha + \Gamma_{\mu\lambda}^\alpha \Gamma_{\nu\alpha}^\beta \phi_\beta - \Gamma_{\mu\nu}^\alpha \nabla_\alpha \phi_\lambda - \mu \leftrightarrow \nu  \\
&=-\left(\partial_\mu \Gamma_{\nu\lambda}^\alpha - \partial_\nu \Gamma_{\mu\lambda}^\alpha\right)\phi_\alpha + \Gamma_{\mu\lambda}^\alpha \Gamma_{\nu\alpha}^\beta \phi_\beta - \Gamma_{\nu\lambda}^\alpha \Gamma_{\mu\alpha}^\beta \phi_\beta - \left(\Gamma_{\mu\nu}^\alpha - \Gamma_{\nu\mu}^\alpha \right)\nabla_\alpha \phi_\lambda \\
&=-\left(\partial_\mu \Gamma_{\nu\lambda}^\beta - \partial_\nu \Gamma_{\mu\lambda}^\beta\right)\phi_\beta + \Gamma_{\mu\lambda}^\alpha \Gamma_{\nu\alpha}^\beta \phi_\beta - \Gamma_{\nu\lambda}^\alpha \Gamma_{\mu\alpha}^\beta \phi_\beta - \left(\Gamma_{\mu\nu}^\alpha - \Gamma_{\nu\mu}^\alpha \right)\nabla_\alpha \phi_\lambda \\
&=-\left(\partial_\mu \Gamma_{\nu\lambda}^\beta - \partial_\nu \Gamma_{\mu\lambda}^\beta + \Gamma_{\nu\lambda}^\alpha \Gamma_{\mu\alpha}^\beta - \Gamma_{\mu\lambda}^\alpha \Gamma_{\nu\alpha}^\beta \right)\phi_\beta - \left(\Gamma_{\mu\nu}^\alpha - \Gamma_{\nu\mu}^\alpha \right)\nabla_\alpha \phi_\lambda \\
&=-R_{\lambda\mu\nu}^\beta \phi_\beta - T_{\mu\nu}^\alpha \nabla_\alpha \phi_\lambda
\end{split}
\end{equation}
$$

## 2.5

> 试求出适用任意时轴正交时空、任意观者的光速表达式，并由此验证广义相对论中的光速不变原理。提示：利用类光线元，并只考虑光线沿径向传播的简单情形。






