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
&=\mathrm{i} \sum_{\bm{r}\in \mathrm{UC}} \left(K_x u_{\bm{r},A;\bm{r},B} c_{\bm{r},A} c_{\bm{r},B} + K_y u_{\bm{r},A;\bm{\bm{r}+\bm{a}_1},B} c_{\bm{r},A} c_{\bm{r}+\bm{a}_1,B} + K_z u_{\bm{r},A;\bm{\bm{r}+\bm{a}_2},B} c_{\bm{r},A} c_{\bm{r}+\bm{a}_2,B} \right) \\
&=\mathrm{i} \sum_{\bm{r}} \sum_{\bm{\delta}\in\left\{\bm{0},\bm{a}_1,\bm{a}_2 \right\}} K_{\bm{\delta}} u_{\bm{r},A;\bm{r}+\bm{\delta},B} c_{\bm{r},A} c_{\bm{r}+\bm{\delta},B}
\end{aligned}
\end{equation}
$$

#### 引入 $\delta $ 符号

$$
\begin{equation}
\begin{aligned}
H_K^{\mathrm{ext}}[u]
&=\mathrm{i} \sum_{\bm{r}} \sum_{\bm{\delta}} K_{\bm{\delta}} u_{\bm{r},A;\bm{r}+\bm{\delta},B} c_{\bm{r},A} c_{\bm{r}+\bm{\delta},B} \\
&=\mathrm{i} \sum_{\bm{r}} \sum_{\bm{\delta}} \sum_{\bm{r}'} K_{\bm{\delta}} \delta_{\bm{r}+\bm{\delta},\bm{r}'} u_{\bm{r},A;\bm{r}',B} c_{\bm{r},A} c_{\bm{r}',B} \\
&=\mathrm{i} \sum_{\bm{r}} \sum_{\bm{r}'} \sum_{\bm{\delta}} K_{\bm{\delta}} \delta_{\bm{r}+\bm{\delta},\bm{r}'} u_{\bm{r},A;\bm{r}',B} c_{\bm{r},A} c_{\bm{r}',B} \\
\end{aligned}
\end{equation}
$$

实际上我们并没有一般性地定义 $u_{\bm{r},A;\bm{r}',B} $，但由于 $\delta_{\bm{r}+\bm{\delta},\bm{r}'} $ 的存在，那些未定义的对哈密顿量没有贡献。

#### 对元胞编号，把对元胞位矢求和改写成对元胞单指标求和

$$
\begin{equation}
\begin{aligned}
H_K^{\mathrm{ext}}[u]
&=\mathrm{i} \sum_{\bm{r}} \sum_{\bm{r}'} \sum_{\bm{\delta}} K_{\bm{\delta}} \delta_{\bm{r}+\bm{\delta},\bm{r}'} u_{\bm{r},A;\bm{r}',B} c_{\bm{r},A} c_{\bm{r}',B} \\
&=\mathrm{i} \sum_{i=1}^{N} \sum_{j=1}^{N} \sum_{\bm{\delta}} K_{\bm{\delta}} \delta_{\bm{r}_i+\bm{\delta},\bm{r}_j} u_{i,A;j,B} c_{i,A} c_{j,B} \\
&=\mathrm{i} \sum_{i,j} \left(\sum_{\bm{\delta}} K_{\bm{\delta}} \delta_{\bm{r}_i+\bm{\delta},\bm{r}_j} u_{i,A;j,B} \right) c_{i,A} c_{j,B} \\
&\equiv \mathrm{i} \sum_{i,j} \left(M_K \right)_{ij} c_{i,A} c_{j,B} \\
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\left(M_K \right)_{ij}
=\sum_{\bm{\delta}\in \left\{\bm{0},\bm{a}_1,\bm{a}_2 \right\}} K_{\bm{\delta}} \delta_{\bm{r}_i+\bm{\delta},\bm{r}_j} u_{i,A;j,B}
\end{equation}
$$

#### 反对称化后写成 c-Nambu 旋量形式

$$
\begin{equation}
\begin{aligned}
H_K^{\mathrm{ext}}[u]
&=\mathrm{i} \sum_{i,j} \left(M_K \right)_{ij} c_{i,A} c_{j,B} \\
&=\mathrm{i} \bm{c}_A^\dag \bm{M}_K \bm{c}_B \\
&=\mathrm{i} 
\begin{pmatrix}
\bm{c}_A^\dag &\bm{c}_B^\dag
\end{pmatrix}
\begin{pmatrix}
\bm{0} &\bm{M}_K \\
\bm{0} &\bm{0}
\end{pmatrix}
\begin{pmatrix}
\bm{c}_A \\
\bm{c}_B
\end{pmatrix} \\
&=\mathrm{i} 
\bm{\psi}_c^\dag
\begin{pmatrix}
\bm{0} &\bm{M}_K \\
\bm{0} &\bm{0}
\end{pmatrix}
\bm{\psi}_c
\end{aligned}
\end{equation}
$$

利用结论

$$
\begin{equation}
\bm{\psi}_c^\dag \bm{M} \bm{\psi}_c
=\bm{\psi}_c^\dag \left(-\bm{M}^\top \right) \bm{\psi}_c
=\frac{1 }{2 }  \bm{\psi}_c^\dag \left(\bm{M}-\bm{M}^\top  \right) \bm{\psi}_c,\quad \forall \bm{M}
\end{equation}
$$

就得到

$$
\begin{equation}
\begin{aligned}
H_K^{\mathrm{ext}}[u]
&=\mathrm{i} 
\bm{\psi}_c^\dag
\begin{pmatrix}
\bm{0} &\bm{M}_K \\
\bm{0} &\bm{0}
\end{pmatrix}
\bm{\psi}_c \\
&=\frac{\mathrm{i} }{2 } 
\bm{\psi}_c^\dag
\begin{pmatrix}
\bm{0} &\bm{M}_K \\
-\bm{M}_K^\top &\bm{0}
\end{pmatrix}
\bm{\psi}_c \\
&\equiv\frac{\mathrm{i} }{2 } 
\bm{\psi}_c^\dag
\bm{H}_c^K[u]
\bm{\psi}_c
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\bm{H}_c^K[u]
=\begin{pmatrix}
\bm{0} &\bm{M}_K \\
-\bm{M}_K^\top &\bm{0}
\end{pmatrix}
\end{equation}
$$

$$
\begin{equation}
\left(M_K \right)_{ij}
=\sum_{\bm{\delta}\in \left\{\bm{0},\bm{a}_1,\bm{a}_2 \right\}} K_{\bm{\delta}} \delta_{\bm{r}_i+\bm{\delta},\bm{r}_j} u_{i,A;j,B}
\end{equation}
$$

### $H_\kappa $

#### 原始自旋表示

$$
\begin{equation}
\begin{aligned}
H_\kappa
&=-\kappa \sum_{\Braket{j,k,l }} \sigma_j^x \sigma_k^y \sigma_l^z \\
&=-\kappa \sum_{\bm{r}\in \mathrm{UC}} \left(\sigma^x_{\bm{r},A} \sigma^y_{\bm{r}+\bm{a}_1,B} \sigma^z_{\bm{r}+\bm{a}_2,B} + \sigma^x_{\bm{r},B} \sigma^y_{\bm{r},A} \sigma^z_{\bm{r}+\bm{a}_2,B} + \sigma^x_{\bm{r},B} \sigma^y_{\bm{r}+\bm{a}_1,B} \sigma^z_{\bm{r},A} \right) \\
&-\kappa \sum_{\bm{r}\in \mathrm{UC}} \left(\sigma^x_{\bm{r},B} \sigma^y_{\bm{r}-\bm{a}_1,A} \sigma^z_{\bm{r}-\bm{a}_2,A} + \sigma^x_{\bm{r},A} \sigma^y_{\bm{r},B} \sigma^z_{\bm{r}-\bm{a}_2,A} + \sigma^x_{\bm{r},A} \sigma^y_{\bm{r}-\bm{a}_1,A} \sigma^z_{\bm{r},B} \right) \\
&\equiv H_\kappa^A + H_\kappa^B
\end{aligned}
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
H_\kappa \mapsto H_\kappa^{\mathrm{ext}}
=
\end{aligned}
\end{equation}
$$

