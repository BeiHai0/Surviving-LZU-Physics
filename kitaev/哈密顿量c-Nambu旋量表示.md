给定一个哈密顿量 $H $，如何将其表达为

$$
\begin{equation}
H
=\frac{\mathrm{i} }{2 } \bm{\psi}_c^\dag \bm{H}_c \bm{\psi}_c
\end{equation}
$$

### $H_K $

#### 原始自旋表示

$$
\begin{equation}
H_K
=\sum_{\Braket{j,k }_\mu} \sum_{\mu\in \left\{x,y,z \right\}} K_\mu \sigma_j^\mu \sigma_k^\mu
\end{equation}
$$

#### Majorana 表示

$$
\begin{equation}
\sigma_j^\mu \mapsto \mathrm{i} b_j^\mu c_j
\end{equation}
$$

$$
\begin{equation}
\hat{u}_{jk} = -\mathrm{i} b_j^\mu b_k^\mu
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
H_K \mapsto H_K^{\mathrm{ext}}
&=\sum_{\Braket{j,k }_\mu} \sum_{\mu} K_\mu \left(\mathrm{i} b_j^\mu c_j \right) \left(\mathrm{i} b_k^\mu c_k \right)
=\mathrm{i} \sum_{\Braket{j,k }_\mu} \sum_{\mu} K_\mu \left(-\mathrm{i} b_j^\mu b_k^\mu \right) c_j c_k
=\mathrm{i} \sum_{\Braket{j,k }_\mu} \sum_{\mu} \\
&=\mathrm{i} \sum_{\Braket{j,k }_\mu} \sum_{\mu} K_\mu \hat{u}_{jk} c_j c_k
\end{aligned}
\end{equation}
$$

#### 考虑 $\hat{u}_{jk} $ 本征值为 $u_{jk} $ 的本征子空间

$$
\begin{equation}
\begin{aligned}
H_K^{\mathrm{ext}}
\mapsto H_K^{\mathrm{ext}}[u]
=\mathrm{i} \sum_{\Braket{j,k }_\mu} \sum_{\mu} K_\mu u_{jk} c_j c_k
\end{aligned}
\end{equation}
$$

#### 把对 bond 求和改写成对元胞位矢求和

$$
\begin{equation}
\begin{aligned}
H_K^{\mathrm{ext}}[u]
&=\mathrm{i} \sum_{\Braket{j,k }_\mu} \sum_{\mu} K_\mu u_{jk} c_j c_k \\
&=\mathrm{i} \sum_{\bm{r}\in \mathrm{UC}} \left(K_x u_{\bm{r},A;\bm{r},B} c_{\bm{r},A} c_{\bm{r},B} + K_y u_{\bm{r},A;\bm{\bm{r}+\bm{a}_1},B} c_{\bm{r},A} c_{\bm{r}+\bm{a}_1,B} + K_z u_{\bm{r},A;\bm{\bm{r}+\bm{a}_2},B} c_{\bm{r},A} c_{\bm{r}+\bm{a}_2,B} \right)
\end{aligned}
\end{equation}
$$

#### 对元胞编号，把对元胞位矢求和改写成对元胞单指标求和

$$
\begin{equation}
\begin{aligned}
H_K^{\mathrm{ext}}[u]
&=\mathrm{i} \sum_{\bm{r}\in \mathrm{UC}} \left(K_x u_{\bm{r},A;\bm{r},B} c_{\bm{r},A} c_{\bm{r},B} + K_y u_{\bm{r},A;\bm{r}+\bm{a}_1,B} c_{\bm{r},A} c_{\bm{r}+\bm{a}_1,B} + K_z u_{\bm{r},A;\bm{\bm{r}+\bm{a}_2},B} c_{\bm{r},A} c_{\bm{r}+\bm{a}_2,B} \right) \\
&=\mathrm{i} \sum_{i=1}^{N} \left(K_x u_{\bm{r}_i,A;\bm{r}_i,B} c_{\bm{r}_i,A} c_{\bm{r}_i,B} + K_y u_{\bm{r}_i,A;\bm{r}_i+\bm{a}_1,B} c_{\bm{r}_i,A} c_{\bm{r}_i+\bm{a}_1,B} + K_z u_{\bm{r}_i,A;\bm{\bm{r}_i+\bm{a}_2},B} c_{\bm{r}_i,A} c_{\bm{r}_i+\bm{a}_2,B} \right) \\
\end{aligned}
\end{equation}
$$



### $H_\kappa $