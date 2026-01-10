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

### 度规

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

### 克氏符

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

### Riemann张量

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

$$
\begin{equation}
R^1_{221} = -R^1_{212} = -\sin^2\theta
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

$$
\begin{equation}
R^2_{121} = -R^2_{112} = 1
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

### Ricci张量

$$
\begin{equation}
\begin{split}
R_{\mu\nu}
=R^{\lambda}_{\mu\lambda\nu}
=R^1_{\mu 1 \nu} + R^2_{\mu 2 \nu}
\end{split}
\end{equation}
$$

- $(\mu,\nu)=(1,1) $

$$
\begin{equation}
R_{11} = R^1_{1 1 1} + R^2_{1 2 1} = 1
\end{equation}
$$

- $(\mu,\nu)=(1,2) $

$$
\begin{equation}
R_{12}
=R^1_{1 1 2} + R^2_{1 2 2}
=0
\end{equation}
$$

- $(\mu,\nu)=(2,1) $

$$
\begin{equation}
R_{21}
=R^1_{2 1 1} + R^2_{2 2 1}
=0
\end{equation}
$$

- $(\mu,\nu)=(2,2) $

$$
\begin{equation}
R_{22}
=R^1_{2 1 2} + R^2_{2 2 2}
=\sin^2\theta
\end{equation}
$$

### 曲率标量

$$
\begin{equation}
R
=g^{\mu\nu} R_{\mu\nu}
=g^{11} R_{11} + g^{22} R_{22}
=\frac{2 }{a^2 } 
\end{equation}
$$

### 测地线方程

测地线方程：

$$
\begin{equation}
\ddot{x}^\lambda + \Gamma_{\mu\nu}^\lambda \dot{x}^\mu \dot{x}^\nu
=0
\end{equation}
$$

- $\lambda=1 $

$$
\begin{equation}
\ddot{x}^1 + \Gamma_{22}^1 \dot{x}^2 \dot{x}^2 = 0
\end{equation}
$$

$$
\begin{equation}
\ddot{\theta} -\sin\theta \cos\theta \dot{\phi}^2
=0
\end{equation}
$$

- $\lambda=2 $

$$
\begin{equation}
\ddot{x}^2 + \Gamma_{12}^2 \dot{x}^1 \dot{x}^2 + \Gamma_{21}^2 \dot{x}^2 \dot{x}^1
=0
\end{equation}
$$

$$
\begin{equation}
\ddot{\phi} + 2\cot\theta \dot{\theta} \dot{\phi}
=0
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

$$
\begin{equation}
\mathrm{d}s^2
=g_{\mu\nu}\mathrm{d}x^\mu\mathrm{d}x^\nu
\end{equation}
$$

时轴正交时空，$g_{0i}=0 $，线元可写为

$$
\begin{equation}
\mathrm{d}s^2
=g_{tt} c^2 \mathrm{d}t^2 + g_{ij}\mathrm{d}x^i\mathrm{d}x^j
\end{equation}
$$

考虑光线沿径向传播，则类光线元满足

$$
\begin{equation}
\mathrm{d}s^2
=g_{tt} c^2 \mathrm{d}t^2 + g_{rr}\mathrm{d}r^2
=0
\end{equation}
$$

其中

$$
\begin{equation}
g_{tt} <0,\quad g_{rr}>0
\end{equation}
$$

考虑任意观者 $x^\mu(\tau) $，其四速度 $u^\mu(\tau) $ 满足

$$
\begin{equation}
g_{\mu\nu} u^\mu u^\nu = -c^2
\end{equation}
$$

观者观测的时间间隔为

$$
\begin{equation}
\mathrm{d}t_{\mathrm{obs}}
=-\frac{1 }{c^2 } u_\mu \mathrm{d}x^\mu
=-\frac{1 }{c^2 } \left(u_0\mathrm{d}x^0+u_1\mathrm{d}x^1 \right)
\end{equation}
$$

观者观测的空间距离为

$$
\begin{equation}
\mathrm{d}l_{\mathrm{obs}}
=\sqrt{h_{\mu\nu} \mathrm{d}x^\mu\mathrm{d}x^\nu}
=\sqrt{\left(g_{\mu\nu} + \frac{u_\mu u_\nu }{c^2 }  \right)\mathrm{d}x^\mu\mathrm{d}x^\nu}
\end{equation}
$$

对于类光线元，

$$
\begin{equation}
\mathrm{d}s^2 = g_{\mu\nu}\mathrm{d}x^\mu\mathrm{d}x^\nu
=0
\end{equation}
$$

则

$$
\begin{equation}
\mathrm{d}l_{\mathrm{obs}}
=\sqrt{\frac{1 }{c^2 } \left(u_\mu\mathrm{d}x^\mu \right)^2}
=-\frac{1 }{c } u_\mu\mathrm{d}x^\mu
\end{equation}
$$

测量光速

$$
\begin{equation}
c_{\mathrm{obs}}
=\frac{\mathrm{d}l_{\mathrm{obs}} }{\mathrm{d}t_{\mathrm{obs}} } 
=c
\end{equation}
$$

# 3

## 3.1 

弱引力场近似下，度规表示为

$$
\begin{equation}
g_{\mu\nu}
=\eta_{\mu\nu} + h_{\mu\nu},\quad
\left|h_{\mu\nu} \right| \ll 1
\end{equation}
$$

线性近似理论中只保留 $h_{\mu\nu} $ 中的线性项（一阶小量）。定义

$$
\begin{equation}
\bar{h}_{\mu\nu}
\equiv h_{\mu\nu} - \frac{1 }{2 } \eta_{\mu\nu} h,\quad
h
\equiv \eta^{\mu\nu} h_{\mu\nu},
\end{equation}
$$

试证明，它的逆变换是

$$
\begin{equation}
\bar{\bar{h}}_{\mu\nu}
\equiv \bar{h}_{\mu\nu} - \frac{1 }{2 } \eta_{\mu\nu} \bar{h}
=h_{\mu\nu}
\end{equation}
$$

**证明**：

$$
\begin{equation}
\begin{aligned}
\bar{h}
\equiv \eta^{\mu\nu} \bar{h}_{\mu\nu}
&=\eta^{\mu\nu}\left(h_{\mu\nu} - \frac{1 }{2 } \eta_{\mu\nu} h \right) \\
&=\eta^{\mu\nu} h_{\mu\nu} - \frac{1 }{2 } \eta^{\mu\nu} \eta_{\mu\nu} h \\
&=h - \frac{1 }{2 } \delta^{\mu}_{\mu} h \\
&=-h
\end{aligned}
\end{equation}
$$

于是

$$
\begin{equation}
\begin{aligned}
\bar{\bar{h}}_{\mu\nu}
&\equiv \bar{h}_{\mu\nu} - \frac{1 }{2 } \eta_{\mu\nu} \bar{h} \\
&=\left(h_{\mu\nu} - \frac{1 }{2 } \eta_{\mu\nu} h \right) - \frac{1 }{2 } \eta_{\mu\nu} \left(-h \right) \\
&=h_{\mu\nu}
\end{aligned}
\end{equation}
$$

## 3.2

线性近似理论中，证明克氏符

$$
\begin{equation}
\Gamma^\mu_{\alpha\beta}
=\frac{1 }{2 } \eta^{\mu\nu} \left(\partial_\beta h_{\alpha\nu} + \partial_\alpha h_{\beta\nu} - \partial_\nu h_{\alpha\beta} \right)
=\frac{1 }{2 } \left(h^\mu_{\alpha,\beta} + h^\mu_{\beta,\alpha} - h^{,\mu}_{\alpha\beta} \right)
\end{equation}
$$

线性近似理论中张量指标的升降借助 $\eta_{\mu\nu} $ 和 $\eta^{\mu\nu} $ 进行。并求线性化后的Ricci张量

$$
\begin{equation}
R_{\mu\nu}
=\Gamma^\lambda_{\mu\nu,\lambda} - \Gamma^\lambda_{\mu\lambda,\nu}
=-\frac{1 }{2 } \left(h^{,\alpha}_{\mu\nu,\alpha} + h_{,\mu,\nu} - h^\alpha_{\mu,\nu,\alpha} - h^\alpha_{\nu,\mu,\alpha} \right)
\end{equation}
$$

**证明**：

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

## 3.3

由以上公式，证明线性化Einstein引力场方程

$$
\begin{equation}
\bar{R}_{\mu\nu}
\equiv R_{\mu\nu} - \frac{1 }{2 } \eta_{\mu\nu} R
=8\pi G T_{\mu\nu}
\end{equation}
$$

具体化为

$$
\begin{equation}
\bar{h}^{,\alpha}_{\mu\nu,\alpha} + \eta_{\mu\nu} \bar{h}^{,\alpha,\beta}_{\alpha\beta} - \bar{h}^{,\alpha}_{\mu\alpha,\nu} - \bar{h}^{,\alpha}_{\nu\alpha,\mu}
=-16\pi G T_{\mu\nu}
\end{equation}
$$

**证明**：

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

## 3.4

证明对于静态时空，线性化Ricci

$$
\begin{equation}
R_{\mu\nu}
=\Gamma^\lambda_{\mu\nu,\lambda} - \Gamma^\lambda_{\mu\lambda,\nu}
=-\frac{1 }{2 } \left(h^{,\alpha}_{\mu\nu,\alpha} + h_{,\mu,\nu} - h^\alpha_{\mu,\nu,\alpha} - h^\alpha_{\nu,\mu,\alpha} \right)
\end{equation}
$$

可化为

$$
\begin{equation}
R_{00} = -\frac{1 }{2 } h_{00,i,i},\quad
R_{0i} = \frac{1 }{2 } \left(h_{k0,i,k} - h_{0i,k,k} \right)
\end{equation}
$$

$$
\begin{equation}
R_{ij}
=-\frac{1 }{2 } \left(-h_{00,i,j} + h_{kk,i,j} - h_{ki,j,k} - h_{kj,i,k} + h_{ij,k,k} \right)
\end{equation}
$$

**证明**：

静态时空满足

$$
\begin{equation}
\partial_0 h_{\mu\nu} = 0
\end{equation}
$$

也即

$$
\begin{equation}
h_{\mu\nu,0}
=0
\end{equation}
$$

$$
\begin{equation}
h_{\mu\nu}^{,0}
=\eta^{0\alpha} h_{\mu\nu,\alpha}
=\eta^{00} h_{\mu\nu,0}
=0
\end{equation}
$$

$$
\begin{equation}
h_{,0}
=\eta^{\mu\nu} h_{\mu\nu,0}
=0
\end{equation}
$$

$$
\begin{equation}
h^{,0}
=\eta^{0\alpha} h_{,\alpha}
=\eta^{00} h^{,0}
=0
\end{equation}
$$

$$
\begin{equation}
h^\mu_{\nu,0}
=\eta^{\mu\alpha} h_{\alpha\nu,0}
=0
\end{equation}
$$

于是可计算Ricci张量：

$$
\begin{equation}
\begin{aligned}
R_{00}
&=-\frac{1 }{2 } \left(h^{,\alpha}_{00,\alpha} + h_{,0,0} - h^\alpha_{0,0,\alpha} - h^\alpha_{0,0,\alpha} \right) \\
&=-\frac{1 }{2 } h_{00,\alpha}^{,\alpha} \\
&=-\frac{1 }{2 } h_{00,i}^{,i}
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
R_{0i}
&=-\frac{1 }{2 } \left(h^{,\alpha}_{0i,\alpha} + h_{,0,i} - h^\alpha_{0,i,\alpha} - h^\alpha_{i,0,\alpha} \right) \\
&=\frac{1 }{2 } \left(h^\alpha_{0,i,\alpha} - h^{,\alpha}_{0i,\alpha} \right) \\
&=\frac{1 }{2 } \left(h^k_{0,i,k} - h^{,k}_{0i,k} \right) \\
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
R_{ij}
&=-\frac{1 }{2 } \left(h^{,\alpha}_{ij,\alpha} + h_{,i,j} - h^\alpha_{i,j,\alpha} - h^\alpha_{j,i,\alpha} \right) \\
&=-\frac{1 }{2 } \left(h^{,k}_{ij,k} + h_{,i,j} - h^k_{i,j,k} - h^k_{j,i,k} \right) \\
&=-\frac{1 }{2 } \left(h^{,k}_{ij,k} - h_{00,i,j} + h^k_{k,i,j} - h^k_{i,j,k} - h^k_{j,i,k} \right) \\
\end{aligned}
\end{equation}
$$

由于

$$
\begin{equation}
\eta_{\mu\nu}
=\mathrm{diag}(-1,+1,+1,+1)
\end{equation}
$$

若认为一对重复的上/下指标也代表求和，则：

$$
\begin{equation}
\begin{aligned}
R_{00}
&=-\frac{1 }{2 } h_{00,i}^{,i} \\
&=-\frac{1 }{2 } \eta^{\alpha i} h_{00,i,\alpha} \\
&=-\frac{1 }{2 } h_{00,i,i}
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
R_{0i}
&=\frac{1 }{2 } \left(h^k_{0,i,k} - h^{,k}_{0i,k} \right) \\
&=\frac{1 }{2 } \left(\eta^{k\alpha} h_{\alpha0,i,k} - \eta^{k\alpha} h_{0i,k,\alpha} \right) \\
&=\frac{1 }{2 } \left( h_{k0,i,k} - h_{0i,k,k} \right) \\
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
R_{ij}
&=-\frac{1 }{2 } \left(h^{,k}_{ij,k} - h_{00,i,j} + h^k_{k,i,j} - h^k_{i,j,k} - h^k_{j,i,k} \right) \\
&=-\frac{1 }{2 } \left(\eta^{k\alpha} h_{ij,k,\alpha} - h_{00,i,j} + \eta^{k\alpha} h_{\alpha k,i,j} - \eta^{k\alpha} h_{\alpha i,j,k} - \eta^{k\alpha} h_{kj,i,k} \right) \\
&=-\frac{1 }{2 } \left(-h_{00,i,j} + h_{kk,i,j} - h_{ki,j,k} - h_{kj,i,k} + h_{ij,k,k} \right)
\end{aligned}
\end{equation}
$$

# 4

## 4.1

由 $f(R) $ 引力作用量

$$
\begin{equation}
S
=\frac{1 }{16\pi G } \int \mathrm{d}^4 \sqrt{-g} f(r) + S_m
\end{equation}
$$

变分，推出 $f(R) $ 引力中的引力场方程

$$
\begin{equation}
f'(R) R_{\mu\nu} - \frac{1 }{2 } f(R) g_{\mu\nu} - \left(\nabla_\mu\nabla_\nu - g_{\mu\nu} \nabla^\lambda\nabla_\lambda \right) f'(R)
=8\pi G T_{\mu\nu}
\end{equation}
$$

## 4.2

计算Schwarzchild解的空间部分线元

$$
\begin{equation}
\mathrm{d}s^2
=r^2\left(\mathrm{d}\theta^2 + \sin^2\theta\mathrm{d}\phi^2 \right) + \frac{\mathrm{d}r^2 }{1-2GM/c^2 r } 
\end{equation}
$$

当坐标半径 $r=a $ 时的球面面积；$r=a $ 时的球体体积；从半径为 $r=2GM/c^2 $ 的球面到 $r=3GM/c^2 $ 的球面的径向距离。

## 4.3

计算Schwarzchild度规

$$
\begin{equation}
\mathrm{d}s^2
=-\mathrm{e}^\nu c^2 \mathrm{d}t^2 + r^2\left(\mathrm{d}\theta^2 +\sin^2\theta\mathrm{d}\phi^2 \right) + \mathrm{e}^{-\nu} \mathrm{d}r^2
\end{equation}
$$

$$
\begin{equation}
\mathrm{e}^\nu
=1-\frac{2GM }{c^2 r } 
\end{equation}
$$

情况下所有联络 $\Gamma_{\mu\nu}^\lambda $

## 4.4

据上题结果，由Schwarzchild时空粒子运动方程出发，导出在平面极坐标系下轨道满足的方程（GR中的Binet方程），并讨论水星进动问题。

## 4.5

导出光子在平面极坐标系下轨道所满足的方程，并讨论光线在太阳附近偏折的问题。



