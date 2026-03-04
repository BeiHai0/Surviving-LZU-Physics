$$
\begin{equation}
H_0
=H_K+H_\kappa
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
H_K
&=\sum_{\bm{r}} \left(K_x \sigma_{\bm{r},A}^x \sigma_{\bm{r},B}^x + K_y \sigma_{\bm{r},A}^y \sigma_{\bm{r}+\bm{a}_1,B}^y + K_z \sigma_{\bm{r},A}^z \sigma_{\bm{r}+\bm{a}_2,B}^z \right) \\
&=\sum_{\bm{r}} \sum_{\mu} K_\mu \sigma_{\bm{r},A}^\mu \sigma_{\bm{r}+\bm{\delta}_\mu,B}^\mu
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\bm{\delta}_x = \bm{0},\quad
\bm{\delta}_y = \bm{a}_1,\quad
\bm{\delta}_z = \bm{a}_2
\end{equation}
$$

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

$$
\begin{equation}
H_{\mathrm{TB}}
=H_{\mathrm{hop}} + H_{\mathrm{on-site}}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
H_{\mathrm{hop}}
&=\sum_{\bm{r},\mu} \sum_{\bm{r}',\nu} d^\dag_{\bm{r},\mu} \Braket{0_\chi,0_{\alpha(\bm{r},\mu)} | d_{\bm{r},\mu} H_h d^\dag_{\bm{r}',\nu} | 0_\chi,0_{\alpha(\bm{r}',\nu)} } d_{\bm{r}',\nu} \\
(\text{最近邻})&=\sum_{\bm{r}} \bigg[ d^\dag_{\bm{r},x} \Braket{0_\chi,0_{\alpha(\bm{r},x)} | d_{\bm{r},x} H_h d^\dag_{\bm{r},y} | 0_\chi,0_{\alpha(\bm{r},y)} } d_{\bm{r},y} \\
&+d^\dag_{\bm{r},z} \Braket{0_\chi,0_{\alpha(\bm{r},z)} | d_{\bm{r},z} H_h d^\dag_{\bm{r},x} | 0_\chi,0_{\alpha(\bm{r},x)} } d_{\bm{r},x} \\
&+d^\dag_{\bm{r},y} \Braket{0_\chi,0_{\alpha(\bm{r},y)} | d_{\bm{r},y} H_h d^\dag_{\bm{r},z} | 0_\chi,0_{\alpha(\bm{r},z)} } d_{\bm{r},z} \\
&+d^\dag_{\bm{r+a_2},x} \Braket{0_\chi,0_{\alpha(\bm{r+a_2},x)} | d_{\bm{r+a_2},x} H_h d^\dag_{\bm{r-a_1+a_2},y} | 0_\chi,0_{\alpha(\bm{r-a_1+a_2},y)} } d_{\bm{r-a_1+a_2},y} \\
&+d^\dag_{\bm{r},z} \Braket{0_\chi,0_{\alpha(\bm{r},z)} | d_{\bm{r},z} H_h d^\dag_{\bm{r+a_2},x} | 0_\chi,0_{\alpha(\bm{r+a_2},x)} } d_{\bm{r+a_2},x} \\
&+d^\dag_{\bm{r-a_1+a_2},y} \Braket{0_\chi,0_{\alpha(\bm{r-a_1+a_2},y)} | d_{\bm{r-a_1+a_2},y} H_h d^\dag_{\bm{r},z} | 0_\chi,0_{\alpha(\bm{r},z)} } d_{\bm{r},z} \bigg] \\
&+\mathrm{H.c.} \\
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
H_{\mathrm{hop}}
&=\sum_{\bm{r}} \bigg[ h_z d^\dag_{\bm{r},x} T^A_{xy} d_{\bm{r},y} + h_x d^\dag_{\bm{r},y} T^A_{yz} d_{\bm{r},z} + h_y d^\dag_{\bm{r},z} T^A_{zx} d_{\bm{r},x} \\
&+ h_z d^\dag_{\bm{r+a_2},x} T^B_{xy} d_{\bm{r-a_1+a_2},y} + h_x d^\dag_{\bm{r-a_1+a_2},y} T^B_{yz} d_{\bm{r},z} + h_y d^\dag_{\bm{r},z} T^B_{zx} d_{\bm{r+a_2},x} \bigg] \\
&+\mathrm{H.c.} \\
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
H_{\mathrm{hop}}
&=\sum_{\bm{k}} \bigg(h_z d^\dag_{\bm{k},x} T^A_{xy} d_{\bm{k},y}  + h_x d^\dag_{\bm{k},y} T^A_{yz} d_{\bm{k},z} + h_y d^\dag_{\bm{k},z} T^A_{zx} d_{\bm{k},x}  \\
&+ h_z \mathrm{e}^{-\mathrm{i} \bm{k}\cdot\bm{a}_1 } d^\dag_{\bm{k},x} T^B_{xy} d_{\bm{k},y} + h_x \mathrm{e}^{\mathrm{i}\bm{k}\cdot\left(\bm{a}_1 - \bm{a}_2 \right)} d^\dag_{\bm{k},y} T^B_{yz} d_{\bm{k},z} + h_y \mathrm{e}^{\mathrm{i}\bm{k}\cdot\bm{a}_2} d^\dag_{\bm{k},z} T^B_{zx} d_{\bm{k},x} \bigg) + \mathrm{H.c.} \\
&=\sum_{\bm{k}} \left[ h_z d^\dag_{\bm{k},x} \left(T^A_{xy} + \mathrm{e}^{-\mathrm{i}\bm{k}\cdot\bm{a}_1} T^B_{xy} \right) d_{\bm{k},y} + h_x d^\dag_{\bm{k},y} \left(T^A_{yz} + \mathrm{e}^{\mathrm{i}\bm{k}\cdot\left(\bm{a}_1-\bm{a}_2 \right) } T^B_{yz} \right) d_{\bm{k},z} + h_y d^\dag_{\bm{k},z} \left(T^A_{zx} + \mathrm{e}^{\mathrm{i}\bm{k}\cdot\bm{a}_2} T^B_{zx} \right) d_{\bm{k},x} \right] + \mathrm{H.c.} \\
&=\sum_{\bm{k}}
\begin{pmatrix}
d^\dag_{\bm{k},x} &d^\dag_{\bm{k},y} &d^\dag_{\bm{k},z}
\end{pmatrix}
\begin{pmatrix}
0 &h_z \left(T^A_{xy} + \mathrm{e}^{-\mathrm{i}\bm{k}\cdot\bm{a}_1} T^B_{xy} \right) &h_y \left(T^A_{zx} + \mathrm{e}^{\mathrm{i}\bm{k}\cdot\bm{a}_2} T^B_{zx} \right)^\dag \\
h_z \left(T^A_{xy} + \mathrm{e}^{-\mathrm{i}\bm{k}\cdot\bm{a}_1} T^B_{xy} \right)^\dag &0 &h_x \left(T^A_{yz} + \mathrm{e}^{\mathrm{i}\bm{k}\cdot\left(\bm{a}_1-\bm{a}_2 \right) } T^B_{yz} \right) \\
h_y \left(T^A_{zx} + \mathrm{e}^{\mathrm{i}\bm{k}\cdot\bm{a}_2} T^B_{zx} \right) &h_x \left(T^A_{yz} + \mathrm{e}^{\mathrm{i}\bm{k}\cdot\left(\bm{a}_1-\bm{a}_2 \right) } T^B_{yz} \right)^\dag &0
\end{pmatrix}
\begin{pmatrix}
d_{\bm{k},x} \\
d_{\bm{k},y} \\
d_{\bm{k},z}
\end{pmatrix}
\end{aligned}
\end{equation}
$$



