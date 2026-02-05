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

$$
\begin{equation}
K_{\bm{0}} = K_x,\quad
K_{\bm{a}_1} = K_y,\quad
K_{\bm{a}_2} = K_z
\end{equation}
$$

#### 引入 $\delta $ 符号

$$
\begin{equation}
\begin{aligned}
H_K^{\mathrm{ext}}[u]
&=\mathrm{i} \sum_{\bm{r}} \sum_{\bm{\delta}} K_{\bm{\delta}} u_{\bm{r},A;\bm{r}+\bm{\delta},B} c_{\bm{r},A} c_{\bm{r}+\bm{\delta},B} \\
&=\mathrm{i} \sum_{\bm{r}} \sum_{\bm{\delta}} \sum_{\bm{r}'} K_{\bm{\delta}} \delta_{\bm{r}+\bm{\delta},\bm{r}'} u_{\bm{r},A;\bm{r}+\bm{\delta},B} c_{\bm{r},A} c_{\bm{r}',B} \\
&=\mathrm{i} \sum_{\bm{r}} \sum_{\bm{r}'} \sum_{\bm{\delta}} K_{\bm{\delta}} \delta_{\bm{r}+\bm{\delta},\bm{r}'} u_{\bm{r},A;\bm{r}+\bm{\delta},B} c_{\bm{r},A} c_{\bm{r}',B} \\
\end{aligned}
\end{equation}
$$

#### 对元胞编号，把对元胞位矢求和改写成对元胞单指标求和

$$
\begin{equation}
\begin{aligned}
H_K^{\mathrm{ext}}[u]
&=\mathrm{i} \sum_{\bm{r}} \sum_{\bm{r}'} \sum_{\bm{\delta}} K_{\bm{\delta}} \delta_{\bm{r}+\bm{\delta},\bm{r}'} u_{\bm{r},A;\bm{r}+\bm{\delta},B} c_{\bm{r},A} c_{\bm{r}',B} \\
&=\mathrm{i} \sum_{i=1}^{N} \sum_{j=1}^{N} \sum_{\bm{\delta}} K_{\bm{\delta}} \delta_{\bm{r}_i+\bm{\delta},\bm{r}_j} u_{\bm{r}_i,A;\bm{r}_i+\bm{\delta},B} c_{i,A} c_{j,B} \\
&=\mathrm{i} \sum_{i,j} \left(\sum_{\bm{\delta}} K_{\bm{\delta}} \delta_{\bm{r}_i+\bm{\delta},\bm{r}_j} u_{\bm{r}_i,A;\bm{r}_i+\bm{\delta},B} \right) c_{i,A} c_{j,B} \\
&\equiv \mathrm{i} \sum_{i,j} \left(M_K \right)_{ij} c_{i,A} c_{j,B} \\
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\left(M_K \right)_{ij}
=\sum_{\bm{\delta}\in \left\{\bm{0},\bm{a}_1,\bm{a}_2 \right\}} K_{\bm{\delta}} \delta_{\bm{r}_i+\bm{\delta},\bm{r}_j} u_{\bm{r}_i,A;\bm{r}_i+\bm{\delta},B}
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
&\equiv\frac{\mathrm{i} }{2 } \bm{\psi}_c^\dag \bm{H}_c^K[u] \bm{\psi}_c
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
=\sum_{\bm{\delta}\in \left\{\bm{0},\bm{a}_1,\bm{a}_2 \right\}} K_{\bm{\delta}} \delta_{\bm{r}_i+\bm{\delta},\bm{r}_j} u_{\bm{r}_i,A;\bm{r}_i+\bm{\delta},B}
\end{equation}
$$

若定义

$$
\begin{equation}
\left(M_K^x \right)_{ij}
=\delta_{\bm{r}_i,\bm{r}_j} u_{\bm{r}_i,A;\bm{r}_i,B}
\end{equation}
$$

$$
\begin{equation}
\left(M_K^y \right)_{ij}
=\delta_{\bm{r}_i+\bm{a}_1,\bm{r}_j} u_{\bm{r}_i,A;\bm{r}_i+\bm{a}_1,B}
\end{equation}
$$

$$
\begin{equation}
\left(M_K^z \right)_{ij}
=\delta_{\bm{r}_i+\bm{a}_2,\bm{r}_j} u_{\bm{r}_i,A;\bm{r}_i+\bm{a}_2,B}
\end{equation}
$$

则

$$
\begin{equation}
\bm{M}_K
=K_x \bm{M}_K^x + K_y \bm{M}_K^y + K_z \bm{M}_K^z
=\sum_{\mu} K_\mu \bm{M}_K^\mu
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
\sigma_j^x \mapsto \mathrm{i} b_j^x c_j = D_j \left(-\mathrm{i} b_j^y b_j^z \right)
\end{equation}
$$

$$
\begin{equation}
\sigma_j^y \mapsto \mathrm{i} b_j^y c_j = D_j \left(-\mathrm{i} b_j^z b_j^x \right)
\end{equation}
$$

$$
\begin{equation}
\sigma_j^z \mapsto \mathrm{i} b_j^z c_j = D_j\left(-\mathrm{i} b_j^x b_j^y \right)
\end{equation}
$$

$$
\begin{equation}
\hat{u}_{jk} = -\mathrm{i} b_j^\mu b_k^\mu
\end{equation}
$$

最后的计算都要回到物理子空间，因此 $D_j $ 可替换成 $+1 $.

$$
\begin{equation}
\begin{aligned}
\sigma^x_{\bm{r},A} \sigma^y_{\bm{r}+\bm{a}_1,B} \sigma^z_{\bm{r}+\bm{a}_2,B}
&\mapsto \left(-\mathrm{i} b_{\bm{r},A}^y b_{\bm{r},A}^z \right) \left(\mathrm{i} b_{\bm{r}+\bm{a}_1,B}^y c_{\bm{r}+\bm{a}_1,B} \right) \left(\mathrm{i} b_{\bm{r}+\bm{a}_2,B}^z c_{\bm{r}+\bm{a}_2,B} \right) \\
&=-\mathrm{i} \left(-\mathrm{i} b_{\bm{r},A}^y b_{\bm{r}+\bm{a}_1,B}^y \right) \left(-\mathrm{i} b_{\bm{r},A}^z b_{\bm{r}+\bm{a}_2,B}^z \right) c_{\bm{r}+\bm{a}_1,B} c_{\bm{r}+\bm{a}_2,B} \\
&=-\mathrm{i} u_{\bm{r},A;\bm{r}+\bm{a}_1,B} u_{\bm{r},A;\bm{r}+\bm{a}_2,B} c_{\bm{r}+\bm{a}_1,B} c_{\bm{r}+\bm{a}_2,B} \\
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
\sigma^x_{\bm{r},B} \sigma^y_{\bm{r},A} \sigma^z_{\bm{r}+\bm{a}_2,B}
&\mapsto \left(\mathrm{i} b_{\bm{r},B}^x c_{\bm{r},B} \right) \left(-\mathrm{i} b_{\bm{r},A}^z b_{\bm{r},A}^x \right) \left(\mathrm{i} b_{\bm{r}+\bm{a}_2,B}^z c_{\bm{r}+\bm{a}_2,B} \right) \\
&=-\mathrm{i} \left(-\mathrm{i} b_{\bm{r},A}^z b_{\bm{r}+\bm{a}_2,B}^z \right) \left(-\mathrm{i} b_{\bm{r},A}^x b_{\bm{r},B}^x \right) c_{\bm{r}+\bm{a}_2,B} c_{\bm{r},B} \\
&=-\mathrm{i} u_{\bm{r},A;\bm{r}+\bm{a}_2,B} u_{\bm{r},A;\bm{r},B} c_{\bm{r}+\bm{a}_2,B} c_{\bm{r},B}
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
\sigma^x_{\bm{r},B} \sigma^y_{\bm{r}+\bm{a}_1,B} \sigma^z_{\bm{r},A}
&\mapsto \left(\mathrm{i} b_{\bm{r},B}^x c_{\bm{r},B} \right) \left(\mathrm{i} b_{\bm{r}+\bm{a}_1,B}^y c_{\bm{r}+\bm{a}_1,B} \right) \left(-\mathrm{i} b_{\bm{r},A}^x b_{\bm{r},A}^y \right) \\
&=-\mathrm{i} \left(-\mathrm{i} b_{\bm{r},A}^x b_{\bm{r},B}^x \right) \left(-\mathrm{i} b_{\bm{r},A}^y b_{\bm{r}+\bm{a}_1,B}^y \right) c_{\bm{r},B} c_{\bm{r}+\bm{a}_1,B} \\
&=-\mathrm{i} u_{\bm{r},A;\bm{r},B} u_{\bm{r},A;\bm{r}+\bm{a}_1,B} c_{\bm{r},B} c_{\bm{r}+\bm{a}_1,B}
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
H_\kappa^A[u]
&=\mathrm{i} \kappa \sum_{\bm{r}} \big(u_{\bm{r},A;\bm{r}+\bm{a}_1,B} u_{\bm{r},A;\bm{r}+\bm{a}_2,B} c_{\bm{r}+\bm{a}_1,B} c_{\bm{r}+\bm{a}_2,B} \\
&+u_{\bm{r},A;\bm{r}+\bm{a}_2,B} u_{\bm{r},A;\bm{r},B} c_{\bm{r}+\bm{a}_2,B} c_{\bm{r},B} \\
&+u_{\bm{r},A;\bm{r},B} u_{\bm{r},A;\bm{r}+\bm{a}_1,B} c_{\bm{r},B} c_{\bm{r}+\bm{a}_1,B} \big) \\
&=\mathrm{i} \kappa \sum_{\bm{r}} \sum_{\substack{\left(\bm{\delta}_1,\bm{\delta}_2 \right)\in \\ \left\{\left(\bm{a}_1,\bm{a}_2 \right),\left(\bm{a}_2,\bm{0} \right),\left(\bm{0},\bm{a}_1 \right) \right\}}} u_{\bm{r},A;\bm{r}+\bm{\delta}_1,B} u_{\bm{r},A;\bm{r}+\bm{\delta}_2,B} c_{\bm{r}+\bm{\delta}_1,B} c_{\bm{r}+\bm{\delta}_2,B} \\
&=\mathrm{i} \kappa \sum_{\bm{r}} \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \sum_{\bm{r}',\bm{r}''} \delta_{\bm{r}',\bm{r}+\bm{\delta}_1} \delta_{\bm{r}'',\bm{r}+\bm{\delta}_2} u_{\bm{r},A;\bm{r}',B} u_{\bm{r},A;\bm{r}'',B} c_{\bm{r}',B} c_{\bm{r}'',B} \\
&=\mathrm{i} \kappa \sum_{\bm{r}',\bm{r}''} \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \sum_{\bm{r}} \delta_{\bm{r}'-\bm{\delta}_1,\bm{r}} \delta_{\bm{r}''-\bm{\delta}_2,\bm{r}} u_{\bm{r}'-\bm{\delta}_1,A;\bm{r}',B} u_{\bm{r}''-\bm{\delta}_2,A;\bm{r}'',B} c_{\bm{r}',B} c_{\bm{r}'',B} \\
&=\mathrm{i} \kappa \sum_{\bm{r}',\bm{r}''} \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \delta_{\bm{r}'-\bm{\delta}_1,\bm{r}''-\bm{\delta}_2}  u_{\bm{r}'-\bm{\delta}_1,A;\bm{r}',B} u_{\bm{r}''-\bm{\delta}_2,A;\bm{r}'',B} c_{\bm{r}',B} c_{\bm{r}'',B} \\
&=\mathrm{i} \kappa \sum_{i=1}^{N} \sum_{j=1}^{N} \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \delta_{\bm{r}_i-\bm{\delta}_1,\bm{r}_j-\bm{\delta}_2} u_{\bm{r}_i-\bm{\delta}_1,A;\bm{r}_i,B} u_{\bm{r}_j-\bm{\delta}_2,A;\bm{r}_j,B} c_{i,B} c_{j,B} \\
&\equiv \mathrm{i} \kappa \sum_{i,j} \left(M_\kappa^A \right)_{ij} c_{i,B} c_{j,B} \\
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
\left(M_\kappa^A \right)_{ij}
&=\sum_{\substack{\left(\bm{\delta}_1,\bm{\delta}_2 \right)\in \\ \left\{\left(\bm{a}_1,\bm{a}_2 \right),\left(\bm{a}_2,\bm{0} \right),\left(\bm{0},\bm{a}_1 \right) \right\}}} \delta_{\bm{r}_i-\bm{\delta}_1,\bm{r}_j-\bm{\delta}_2} u_{\bm{r}_i-\bm{\delta}_1,A;\bm{r}_i,B} u_{\bm{r}_j-\bm{\delta}_2,A;\bm{r}_j,B} \\
&=\delta_{\bm{r}_i-\bm{a}_1,\bm{r}_j-\bm{a}_2} u_{\bm{r}_i-\bm{a}_1,A;\bm{r}_i,B} u_{\bm{r}_j-\bm{a}_2,A;\bm{r}_j,B} \\
&+ \delta_{\bm{r}_i-\bm{a}_2,\bm{r}_j} u_{\bm{r}_i-\bm{a}_2,A;\bm{r}_i,B} u_{\bm{r}_j,A;\bm{r}_j,B} \\
&+ \delta_{\bm{r}_i,\bm{r}_j-\bm{a}_1} u_{\bm{r}_i,A;\bm{r}_i,B} u_{\bm{r}_j-\bm{a}_1,A;\bm{r}_j,B}
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
H_\kappa^A[u]
&=\mathrm{i} \kappa \sum_{i,j} \left(M_\kappa^A \right)_{ij} c_{i,B} c_{j,B} \\
&=\mathrm{i} \kappa \bm{c}_B^\dag \bm{M}_\kappa^A \bm{c}_B \\
&=\mathrm{i} \kappa
\begin{pmatrix}
\bm{c}_A^\dag &\bm{c}_B^\dag
\end{pmatrix}
\begin{pmatrix}
\bm{0} &\bm{0} \\
\bm{0} &\bm{M}_\kappa^A
\end{pmatrix}
\begin{pmatrix}
\bm{c}_A \\
\bm{c}_B
\end{pmatrix} \\
&=\mathrm{i} \kappa \bm{\psi}_c^\dag
\begin{pmatrix}
\bm{0} &\bm{0} \\
\bm{0} &\bm{M}_\kappa^A
\end{pmatrix}
\bm{\psi}_c \\
&=\frac{\mathrm{i} }{2 } \bm{\psi}_c^\dag \kappa 
\begin{pmatrix}
\bm{0} &\bm{0} \\
\bm{0} &\bm{M}_\kappa^A - \left(\bm{M}_\kappa^A \right)^\top
\end{pmatrix}
\bm{\psi}_c \\
&\equiv \frac{\mathrm{i} }{2 } \bm{\psi}_c^\dag \bm{H}_{\kappa,c}^A[u] \bm{\psi}_c
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\bm{H}_{\kappa,c}^A[u]
=\kappa \cdot 
\begin{pmatrix}
\bm{0} &\bm{0} \\
\bm{0} &\bm{M}_\kappa^A - \left(\bm{M}_\kappa^A \right)^\top
\end{pmatrix}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
\sigma^x_{\bm{r},B} \sigma^y_{\bm{r}-\bm{a}_1,A} \sigma^z_{\bm{r}-\bm{a}_2,A}
&\mapsto \left(-\mathrm{i} b_{\bm{r},B}^y b_{\bm{r},B}^z \right) \left(\mathrm{i} b_{\bm{r}-\bm{a}_1,A}^y c_{\bm{r}-\bm{a}_1,A} \right) \left(\mathrm{i} b_{\bm{r}-\bm{a}_2,A}^z c_{\bm{r}-\bm{a}_2,A} \right) \\
&=-\mathrm{i} \left(-\mathrm{i} b_{\bm{r}-\bm{a}_1,A}^y b_{\bm{r},B}^y \right) \left(-\mathrm{i} b_{\bm{r}-\bm{a}_2,A}^z b_{\bm{r},B}^z \right) c_{\bm{r}-\bm{a}_1,A} c_{\bm{r}-\bm{a}_2,A} \\
&=-\mathrm{i} u_{\bm{r}-\bm{a}_1,A;\bm{r},B} u_{\bm{r}-\bm{a}_2,A;\bm{r},B} c_{\bm{r}-\bm{a}_1,A} c_{\bm{r}-\bm{a}_2,A} \\
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
\sigma^x_{\bm{r},A} \sigma^y_{\bm{r},B} \sigma^z_{\bm{r}-\bm{a}_2,A}
&\mapsto \left(\mathrm{i} b_{\bm{r},A}^x c_{\bm{r},A} \right) \left(-\mathrm{i} b_{\bm{r},B}^z b_{\bm{r},B}^x  \right) \left(\mathrm{i} b_{\bm{r}-\bm{a}_2,A}^z c_{\bm{r}-\bm{a}_2,A} \right) \\
&=-\mathrm{i} \left(-\mathrm{i} b_{\bm{r}-\bm{a}_2,A}^z b_{\bm{r},B}^z \right) \left(-\mathrm{i} b_{\bm{r},A}^x b_{\bm{r},B}^x \right) c_{\bm{r}-\bm{a}_2,A} c_{\bm{r},A} \\
&=-\mathrm{i} u_{\bm{r}-\bm{a}_2,A;\bm{r},B} u_{\bm{r},A;\bm{r},B} c_{\bm{r}-\bm{a}_2,A} c_{\bm{r},A}
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
\sigma^x_{\bm{r},A} \sigma^y_{\bm{r}-\bm{a}_1,A} \sigma^z_{\bm{r},B}
&\mapsto \left(\mathrm{i} b_{\bm{r},A}^x c_{\bm{r},A} \right) \left(\mathrm{i} b_{\bm{r}-\bm{a}_1,A}^y c_{\bm{r}-\bm{a}_1,A} \right) \left(-\mathrm{i} b_{\bm{r},B}^x b_{\bm{r},B}^y \right) \\
&=-\mathrm{i} \left(-\mathrm{i} b_{\bm{r},A}^x b_{\bm{r},B}^x \right) \left(-\mathrm{i} b_{\bm{r}-\bm{a}_1,A}^y b_{\bm{r},B}^y \right) c_{\bm{r},A} c_{\bm{r}-\bm{a}_1} \\
&=-\mathrm{i} u_{\bm{r},A;\bm{r},B} u_{\bm{r}-\bm{a}_1,A;\bm{r},B} c_{\bm{r},A} c_{\bm{r}-\bm{a}_1}
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
H_\kappa^B[u]
&=\mathrm{i} \kappa \sum_{\bm{r}\in \mathrm{UC}} \big(u_{\bm{r}-\bm{a}_1,A;\bm{r},B} u_{\bm{r}-\bm{a}_2,A;\bm{r},B} c_{\bm{r}-\bm{a}_1,A} c_{\bm{r}-\bm{a}_2,A} \\
&+ u_{\bm{r}-\bm{a}_2,A;\bm{r},B} u_{\bm{r},A;\bm{r},B} c_{\bm{r}-\bm{a}_2,A} c_{\bm{r},A} \\
&+ u_{\bm{r},A;\bm{r},B} u_{\bm{r}-\bm{a}_1,A;\bm{r},B} c_{\bm{r},A} c_{\bm{r}-\bm{a}_1} \big) \\
&=\mathrm{i} \kappa \sum_{\bm{r}} \sum_{\substack{\left(\bm{\delta}_1,\bm{\delta}_2 \right)\in \\ \left\{\left(\bm{a}_1,\bm{a}_2 \right),\left(\bm{a}_2,\bm{0} \right),\left(\bm{0},\bm{a}_1 \right) \right\}}} u_{\bm{r}-\bm{\delta}_1,A;\bm{r},B} u_{\bm{r}-\bm{\delta}_2,A;\bm{r},B} c_{\bm{r}-\bm{\delta}_1,A} c_{\bm{r}-\bm{\delta}_2,A} \\
&=\mathrm{i} \kappa \sum_{\bm{r}} \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \sum_{\bm{r}',\bm{r}''} \delta_{\bm{r}-\bm{\delta}_1,\bm{r}'} \delta_{\bm{r}-\bm{\delta}_2,\bm{r}''} u_{\bm{r}',A;\bm{r},B} u_{\bm{r}'',A;\bm{r},B} c_{\bm{r}',A} c_{\bm{r}'',A} \\
&=\mathrm{i} \kappa \sum_{\bm{r}',\bm{r}''} \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \sum_{\bm{r}} \delta_{\bm{r},\bm{r}'+\bm{\delta}_1} \delta_{\bm{r},\bm{r}''+\bm{\delta}_2} u_{\bm{r}',A;\bm{r}'+\bm{\delta}_1,B} u_{\bm{r}'',A;\bm{r}''+\bm{\delta}_2,B} c_{\bm{r}',A} c_{\bm{r}'',A} \\
&=\mathrm{i} \kappa \sum_{\bm{r}',\bm{r}''} \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \delta_{\bm{r}'+\bm{\delta}_1,\bm{r}''+\bm{\delta}_2} u_{\bm{r}',A;\bm{r}'+\bm{\delta}_1,B} u_{\bm{r}'',A;\bm{r}''+\bm{\delta}_2,B} c_{\bm{r}',A} c_{\bm{r}'',A} \\
&=\mathrm{i} \kappa \sum_{i=1}^{N} \sum_{j=1}^{N} \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \delta_{\bm{r}_i+\bm{\delta}_1,\bm{r}_j+\bm{\delta}_2} u_{\bm{r}_i,A;\bm{r}_i+\bm{\delta}_1,B} u_{\bm{r}_j,A;\bm{r}_j+\bm{\delta}_2} c_{i,A} c_{j,A} \\
&\equiv \mathrm{i} \kappa \sum_{i,j} \left(M_\kappa^B \right)_{ij} c_{i,A} c_{j,A}
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\left(M_\kappa^B \right)_{ij}
=\sum_{\substack{\left(\bm{\delta}_1,\bm{\delta}_2 \right)\in \\ \left\{\left(\bm{a}_1,\bm{a}_2 \right),\left(\bm{a}_2,\bm{0} \right),\left(\bm{0},\bm{a}_1 \right) \right\}}} \delta_{\bm{r}_i+\bm{\delta}_1,\bm{r}_j+\bm{\delta}_2} u_{\bm{r}_i,A;\bm{r}_i+\bm{\delta}_1,B} u_{\bm{r}_j,A;\bm{r}_j+\bm{\delta}_2}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
H_\kappa^B[u]
&=\mathrm{i} \kappa \sum_{i,j} \left(M_\kappa^B \right)_{ij} c_{i,A} c_{j,A} \\
&=\mathrm{i} \kappa \bm{c}_A^\dag \bm{M}_\kappa^B \bm{c}_A \\
&=\mathrm{i} \kappa 
\begin{pmatrix}
\bm{c}_A^\dag &\bm{c}_B^\dag
\end{pmatrix}
\begin{pmatrix}
\bm{M}_\kappa^B &\bm{0} \\
\bm{0} &\bm{0}
\end{pmatrix}
\begin{pmatrix}
\bm{c}_A &\bm{c}_B \\
\end{pmatrix} \\
&=\mathrm{i} \kappa \bm{\psi}_c^\dag
\begin{pmatrix}
\bm{M}_\kappa^B &\bm{0} \\
\bm{0} &\bm{0}
\end{pmatrix} \bm{\psi}_c \\
&=\frac{\mathrm{i} }{2 } \bm{\psi}_c^\dag \kappa
\begin{pmatrix}
\bm{M}_\kappa^B - \left(\bm{M}_\kappa^B \right)^\top &\bm{0} \\
\bm{0} &\bm{0}
\end{pmatrix} \bm{\psi}_c \\
&\equiv \frac{\mathrm{i} }{2 } \bm{\psi}_c^\dag \bm{H}_{\kappa,c}^B[u] \bm{\psi}_c
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\bm{H}_{\kappa,c}^B[u]
=\kappa \cdot 
\begin{pmatrix}
\bm{M}_\kappa^B - \left(\bm{M}_\kappa^B \right)^\top &\bm{0} \\
\bm{0} &\bm{0}
\end{pmatrix}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
H_\kappa[u]
&=H_\kappa^A[u] + H_\kappa^B[u] \\
&=\frac{\mathrm{i} }{2 } \bm{\psi}_c^\dag \left(\bm{H}_{\kappa,c}^A[u] + \bm{H}_{\kappa,c}^B[u] \right) \bm{\psi}_c \\
&\equiv \frac{\mathrm{i} }{2 } \bm{\psi}_c^\dag \bm{H}_{\kappa,c}[u] \bm{\psi}_c \\
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\bm{H}_{\kappa,c}[u]
=\bm{H}_{\kappa,c}^A[u] + \bm{H}_{\kappa,c}^B[u]
=\kappa \bm{M}_\kappa^{AB}
\end{equation}
$$

$$
\begin{equation}
\bm{M}_\kappa^{AB}
=\begin{pmatrix}
\bm{M}_\kappa^B - \left(\bm{M}_\kappa^B \right)^\top &\bm{0} \\
\bm{0} &\bm{M}_\kappa^A - \left(\bm{M}_\kappa^A \right)^\top
\end{pmatrix}
\end{equation}
$$

#### 总哈密顿量

$$
\begin{equation}
H_K[u]
=\frac{\mathrm{i} }{2 } \bm{\psi}_c^\dag \bm{H}_c^K[u] \bm{\psi}_c
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
\bm{M}_K
=K_x \bm{M}_K^x + K_y \bm{M}_K^y + K_z \bm{M}_K^z
=\sum_{\mu} K_\mu \bm{M}_K^\mu
\end{equation}
$$

$$
\begin{equation}
H_\kappa[u]
=\frac{\mathrm{i} }{2 } \bm{\psi}_c^\dag \bm{H}_{\kappa,c}[u] \bm{\psi}_c
\end{equation}
$$

$$
\begin{equation}
\bm{H}_{\kappa,c}[u]
=\bm{H}_{\kappa,c}^A[u] + \bm{H}_{\kappa,c}^B[u]
=\kappa \bm{M}_\kappa^{AB}
\end{equation}
$$

$$
\begin{equation}
\bm{M}_\kappa^{AB}
=\begin{pmatrix}
\bm{M}_\kappa^B - \left(\bm{M}_\kappa^B \right)^\top &\bm{0} \\
\bm{0} &\bm{M}_\kappa^A - \left(\bm{M}_\kappa^A \right)^\top
\end{pmatrix}
\end{equation}
$$