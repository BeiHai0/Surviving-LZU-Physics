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