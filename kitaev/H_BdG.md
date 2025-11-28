### 无磁场

$$
\begin{equation}
\widetilde{H}
=-\mathrm{i} \sum_{\Braket{j,k }} K_{\alpha_{jk}} {u}_{jk} c_j c_k,
\end{equation}
$$

其中 $u_{jk} $ 是 $\hat{u}_{jk} $ 的本征值。

首先 $c_j $ 是 $j $ 格点的 Majorana-c 算符。若区分 $A,B $ 子格，用 $c_{\bm{r},\alpha} $ 表示 $\bm{r} $ unit cell 内 $\beta $ 子格格点上的 Majorana-c 算符，则哈密顿量可改写为：

$$
\begin{equation}
\begin{split}
\widetilde{H}
&=-\mathrm{i} \sum_{\Braket{j,k }} K_{\alpha_{jk}} {u}_{jk} c_j c_k \\
&=-\mathrm{i} \sum_{\bm{r}\in \mathrm{UC}} \left(K_x u_{\bm{r},A;\bm{r},B} c_{\bm{r},A} c_{\bm{r},B} + K_y u_{\bm{r},A;\bm{r}+\bm{a}_1,B} c_{\bm{r},A} c_{\bm{r}+\bm{a}_1,B} + K_z u_{\bm{r},A;\bm{r}+\bm{a}_2,B} c_{\bm{r},A} c_{\bm{r}+\bm{a}_2,B} \right) \\
&=-\mathrm{i} \sum_{\bm{r}\in \mathrm{UC}} \sum_{\bm{\delta} \in \left\{\bm{0},\bm{a}_1,\bm{a}_2 \right\}} K_{\bm{\delta}} u_{\bm{r},A;\bm{r}+\bm{\delta},B} c_{\bm{r},A} c_{\bm{r}+\bm{\delta},B}.
\end{split}
\end{equation}
$$

其中

$$
\begin{equation}
\mathrm{UC}
\equiv \left\{\bm{r}_1,\bm{r}_2,\cdots,\bm{r}_N \right\},
\end{equation}
$$

$N=N_1 N_2 $ 为总 unit cell 数，$\bm{r}_i $ 为第 $i $ 个元胞的位置矢量，

$$
\begin{equation}
K_{\bm{\delta}}
\equiv \left\{
\begin{aligned}
&K_x,\quad \bm{\delta} = \bm{0}, \\
&K_y,\quad \bm{\delta} = \bm{a}_1, \\
&K_z,\quad \bm{\delta} = \bm{a}_2.
\end{aligned}
\right.
\end{equation}
$$

把 $\bm{r} $ unit cell 内的两个 Majorana-c 算符组合成复费米子算符：

$$
\begin{equation}
a_{\bm{r}}
\equiv \frac{1 }{2 } \left(c_{\bm{r},A} + \mathrm{i} c_{\bm{r},B} \right),\quad
a^\dag_{\bm{r}}
\equiv \frac{1 }{2 } \left(c_{\bm{r},A} - \mathrm{i} c_{\bm{r},B} \right),\quad
\bm{r} \in \mathrm{UC},
\end{equation}
$$

可以反解出

$$
\begin{equation}
c_{\bm{r},A}
=a_{\bm{r}} + a^\dag_{\bm{r}},\quad
c_{\bm{r},B}
=\frac{1 }{\mathrm{i} } \left(a_{\bm{r}} - a^\dag_{\bm{r}} \right),
\end{equation}
$$

则哈密顿量可表达为

$$
\begin{equation}
\begin{split}
\widetilde{H}
&=-\mathrm{i} \sum_{\bm{r}\in \mathrm{UC}} \sum_{\bm{\delta} \in \left\{\bm{0},\bm{a}_1,\bm{a}_2 \right\}} K_{\bm{\delta}} u_{\bm{r},A;\bm{r}+\bm{\delta},B} c_{\bm{r},A} c_{\bm{r}+\bm{\delta},B} \\
&=-\mathrm{i} \sum_{\bm{r}} \sum_{\bm{\delta} } K_{\bm{\delta}} u_{\bm{r},A;\bm{r}+\bm{\delta},B} \left(a_{\bm{r}} + a^\dag_{\bm{r}} \right) \cdot \frac{1 }{\mathrm{i} } \left(a_{\bm{r+\delta}} - a^\dag_{\bm{r+\delta}} \right) \\
&=\sum_{\bm{r}} \sum_{\bm{\delta} } K_{\bm{\delta}} u_{\bm{r},A;\bm{r}+\bm{\delta},B} \left(a_{\bm{r}} + a^\dag_{\bm{r}} \right)  \left(-a_{\bm{r+\delta}} +  a^\dag_{\bm{r+\delta}} \right) \\
&=\sum_{\bm{\delta}} \sum_{\bm{r}} K_{\bm{\delta}} u_{\bm{r},A;\bm{r}+\bm{\delta},B} \left(a_{\bm{r}} + a^\dag_{\bm{r}} \right)  \left(-a_{\bm{r+\delta}} +  a^\dag_{\bm{r+\delta}} \right) \\
&=\sum_{\bm{\delta}} \sum_{\bm{r}} \sum_{\bm{r}'\in \mathrm{UC}} \sum_{\bm{r}''\in \mathrm{UC}} \delta_{\bm{r}',\bm{r}} \delta_{\bm{r}'',\bm{r}+\bm{\delta}} K_{\bm{\delta}} u_{\bm{r},A;\bm{r}+\bm{\delta},B} \left(a_{\bm{r}'} + a^\dag_{\bm{r}'} \right)  \left(-a_{\bm{r}''} +  a^\dag_{\bm{r}''} \right) \\
&=\sum_{\bm{\delta}} \sum_{\bm{r}'} \sum_{\bm{r}''} \sum_{\bm{r}}\delta_{\bm{r}',\bm{r}} \delta_{\bm{r}'',\bm{r}+\bm{\delta}} K_{\bm{\delta}} u_{\bm{r},A;\bm{r}+\bm{\delta},B} \left(a_{\bm{r}'} + a^\dag_{\bm{r}'} \right)  \left(-a_{\bm{r}''} +  a^\dag_{\bm{r}''} \right) \\
&=\sum_{\bm{\delta}} \sum_{\bm{r}'} \sum_{\bm{r}''} \delta_{\bm{r}',\bm{r}''-\bm{\delta}} K_{\bm{\delta}} u_{\bm{r}',A;\bm{r}'',B} \left(a_{\bm{r}'} + a^\dag_{\bm{r}'} \right)  \left(-a_{\bm{r}''} +  a^\dag_{\bm{r}''} \right) \\
&=\sum_{\bm{r}'} \sum_{\bm{r}''} \left(\sum_{\bm{\delta}} \delta_{\bm{r}',\bm{r}''-\bm{\delta}} K_{\bm{\delta}} u_{\bm{r}',A;\bm{r}'',B} \right) \left(a_{\bm{r}'} + a^\dag_{\bm{r}'} \right)  \left(-a_{\bm{r}''} +  a^\dag_{\bm{r}''} \right) \\
&=\sum_{i=1}^{N} \sum_{j=1}^{N} \left(\sum_{\bm{\delta}} \delta_{\bm{r}_i,\bm{r}_j-\bm{\delta}} K_{\bm{\delta}} u_{\bm{r}_i,A;\bm{r}_j,B} \right) \left(a_i + a^\dag_i \right) \left(-a_j + a^\dag_j \right)
\end{split}
\end{equation}
$$

令

$$
\begin{equation}
t_{ij}
=\sum_{\bm{\delta} \in \left\{\bm{0},\bm{a}_1,\bm{a}_2 \right\}} \delta_{\bm{r}_i,\bm{r}_j-\bm{\delta}} K_{\bm{\delta}} u_{\bm{r}_i,A;\bm{r}_j,B},
\end{equation}
$$

则

$$
\begin{equation}
\begin{split}
\widetilde{H}
&=\sum_{i=1}^{N} \sum_{j=1}^{N} \left(\sum_{\bm{\delta}} \delta_{\bm{r}_i,\bm{r}_j-\bm{\delta}} K_{\bm{\delta}} u_{\bm{r}_i,A;\bm{r}_j,B} \right) \left(a_i + a^\dag_i \right) \left(-a_j + a^\dag_j \right) \\
&=\sum_{i=1}^{N} \sum_{j=1}^{N} t_{ij} \left(a_i + a^\dag_i \right) \left(-a_j + a^\dag_j \right) \\
&=\sum_{i=1}^{N} \sum_{j=1}^{N} \left(-t_{ij} a_i a_j + t_{ij} a^\dag_i a^\dag_j + t_{ij} a_i a^\dag_j - t_{ij} a^\dag_i a_j \right) \\
\end{split}
\end{equation}
$$

$$
\begin{equation}
\begin{split}
\sum_{i=1}^{N} \sum_{j=1}^{N} (-t_{ij}) a_i a_j
&=\frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} (-t_{ij}) a_i a_j + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} (-t_{ij}) a_i a_j \\
&=\frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} t_{ij} a_j a_i + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} (-t_{ij}) a_i a_j \\
&=\frac{1 }{2 } \sum_{j=1}^{N} \sum_{i=1}^{N} t_{ji} a_i a_j + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} (-t_{ij}) a_i a_j \\
&=\frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} \left(t_{ji} - t_{ij} \right) a_i a_j
\end{split}
\end{equation}
$$

$$
\begin{equation}
\begin{split}
\sum_{i=1}^{N} \sum_{j=1}^{N} t_{ij} a^\dag_i a^\dag_j
&=\frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} t_{ij} a^\dag_i a^\dag_j + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} t_{ij} a^\dag_i a^\dag_j \\
&=\frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} -t_{ij} a^\dag_j a^\dag_i + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} t_{ij} a^\dag_i a^\dag_j \\
&=\frac{1 }{2 } \sum_{j=1}^{N} \sum_{i=1}^{N} -t_{ji} a^\dag_i a^\dag_j + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} t_{ij} a^\dag_i a^\dag_j \\
&=\frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} \left(t_{ij} - t_{ji} \right) a^\dag_i a^\dag_j
\end{split}
\end{equation}
$$

$$
\begin{equation}
\begin{split}
\sum_{i=1}^{N} \sum_{j=1}^{N} \left( t_{ij} a_i a^\dag_j - t_{ij} a^\dag_i a_j \right)
&=\sum_{i=1}^{N} \sum_{j=1}^{N} \left[ t_{ij} \left(\delta_{ij} - a^\dag_j a_i \right) - t_{ij} a^\dag_i a_j \right] \\
&=\sum_{i=1}^{N} t_{ii} + \sum_{i=1}^{N} \sum_{j=1}^{N} \left(-t_{ij} \right) a^\dag_j a_i + \sum_{i=1}^{N} \sum_{j=1}^{N} \left(-t_{ij} \right) a^\dag_i a_j \\
&=\sum_{i=1}^{N} t_{ii} + \sum_{j=1}^{N} \sum_{i=1}^{N} \left(-t_{ji} \right) a^\dag_i a_j + \sum_{i=1}^{N} \sum_{j=1}^{N} \left(-t_{ij} \right) a^\dag_i a_j \\
&=\sum_{i=1}^{N} t_{ii} + \sum_{i=1}^{N} \sum_{j=1}^{N} -(t_{ij } + t_{ji}) a^\dag_i a_j
\end{split}
\end{equation}
$$

于是

$$
\begin{equation}
\begin{split}
\widetilde{H}
&=\sum_{i=1}^{N} \sum_{j=1}^{N} \left(-t_{ij} a_i a_j + t_{ij} a^\dag_i a^\dag_j + t_{ij} a_i a^\dag_j - t_{ij} a^\dag_i a_j \right) \\
&=\frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} \left(t_{ji} - t_{ij} \right) a_i a_j + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} \left(t_{ij} - t_{ji} \right) a^\dag_i a^\dag_j + \sum_{i=1}^{N} \sum_{j=1}^{N} -(t_{ij } + t_{ji}) a^\dag_i a_j + \sum_{i=1}^{N} t_{ii}
\end{split}
\end{equation}
$$

设

$$
\begin{equation}
\begin{split}
\widetilde{H}
&=\frac{1 }{2 }
\begin{bmatrix}
a^\dag_{1} &\cdots &a^\dag_{N} &a_{1} &\cdots &a_{N}
\end{bmatrix}
\begin{bmatrix}
\Xi &\Delta \\
\Delta^\dag &-\Xi^{\mathrm{T}}
\end{bmatrix}
\begin{bmatrix}
a_{1} \\
\vdots \\
a_{N} \\
a^\dag_{1} \\
\vdots \\
a^\dag_{N}
\end{bmatrix} + C \\
&=C + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} \Xi_{ij} a^\dag_i a_j + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} \left(-\Xi^{\mathrm{T}} \right)_{ij} a_i a^\dag_j + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} \Delta_{ij} a^\dag_i a^\dag_j + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N}\left(\Delta^\dag \right)_{ij} a_i a_j \\
&=C + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} \Xi_{ij} a^\dag_i a_j + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} \left(-\Xi_{ji} \right) \left(\delta_{ij} - a^\dag_j a_i \right) + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} \Delta_{ij} a^\dag_i a^\dag_j + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N}\left(-\Delta_{ij}^* \right) a_i a_j \\
&=C - \frac{1 }{2 } \sum_{i=1}^{N} \Xi_{ii} + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} \Xi_{ij} a^\dag_i a_j + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} \Xi_{ji} a^\dag_j a_i + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} \Delta_{ij} a^\dag_i a^\dag_j + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N}\left(-\Delta_{ij}^* \right) a_i a_j \\
&=C - \frac{1 }{2 } \sum_{i=1}^{N} \Xi_{ii} + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} \Xi_{ij} a^\dag_i a_j + \frac{1 }{2 } \sum_{j=1}^{N} \sum_{i=1}^{N} \Xi_{ij} a^\dag_i a_j + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} \Delta_{ij} a^\dag_i a^\dag_j + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N}\left(-\Delta_{ij}^* \right) a_i a_j \\
&=C - \frac{1 }{2 } \sum_{i=1}^{N} \Xi_{ii} + \sum_{j=1}^{N} \sum_{i=1}^{N} \Xi_{ij} a^\dag_i a_j + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} \Delta_{ij} a^\dag_i a^\dag_j + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N}\left(-\Delta_{ij}^* \right) a_i a_j \\
\end{split}
\end{equation}
$$

其中

$$
\begin{equation}
\Delta^{\mathrm{T}} =- \Delta,\quad
\Xi^\dag = \Xi.
\end{equation}
$$

对比可得

$$
\begin{equation}
\Xi_{ij} = -\left(t_{ij} + t_{ji} \right),\quad
\Delta_{ij} = t_{ij} - t_{ji},\quad
C = \frac{1 }{2 } \sum_{i=1}^{N} \Xi_{ii} + \sum_{i=1}^{N} t_{ii} = 0.
\end{equation}
$$

### 磁场微扰

如果考虑

$$
\begin{equation}
\begin{split}
H^{(3)}_{\mathrm{eff}} 
=-\kappa \sum_{\Braket{j,k,l }} \sigma_j^x \sigma_k^y \sigma_l^z
=-\kappa \sum_{\bm{r}\in \mathrm{UC}} \left(\mathrm{around}A + \mathrm{around}B \right),
\end{split}
\end{equation}
$$

$$
\begin{equation}
\begin{split}
\mathrm{around}A
&=\sigma^x_{\bm{r},A} \sigma^y_{\bm{r}+\bm{a}_1,B} \sigma^z_{\bm{r}+\bm{a}_2,B} + \sigma^x_{\bm{r},B} \sigma^y_{\bm{r},A} \sigma^z_{\bm{r}+\bm{a}_2,B} + \sigma^x_{\bm{r},B} \sigma^y_{\bm{r}+\bm{a}_1,B} \sigma^z_{\bm{r},A} \\
&=\mathrm{i} u_{\bm{r}+\bm{a}_1,B;\bm{r},A} u_{\bm{r}+\bm{a}_2,B;\bm{r},A} c_{\bm{r}+\bm{a}_1,B} c_{\bm{r}+\bm{a}_2,B} \\
&+\mathrm{i} u_{\bm{r}+\bm{a}_2,B;\bm{r},A} u_{\bm{r},B;\bm{r},A} c_{\bm{r}+\bm{a}_2,B} c_{\bm{r},B} \\
&+\mathrm{i} u_{\bm{r},B;\bm{r},A} u_{\bm{r}+\bm{a}_1,B;\bm{r},A} c_{\bm{r},B} c_{\bm{r}+\bm{a}_1,B} \\
&=\mathrm{i} \sum_{\substack{\left(\bm{\delta}_1,\bm{\delta}_2 \right)\in \\ \left\{\left(\bm{a}_1,\bm{a}_2 \right),\left(\bm{a}_2,\bm{0} \right),\left(\bm{0},\bm{a}_1 \right) \right\}}} u_{\bm{r}+\bm{\delta}_1,B;\bm{r},A} u_{\bm{r}+\bm{\delta}_2,B;\bm{r},A} c_{\bm{r}+\bm{\delta}_1,B} c_{\bm{r}+\bm{\delta}_2,B}
\end{split}
\end{equation}
$$

$$
\begin{equation}
\begin{split}
\mathrm{around}B
&=\sigma^x_{\bm{r},B} \sigma^y_{\bm{r}-\bm{a}_1,A} \sigma^z_{\bm{r}-\bm{a}_2,A} + \sigma^x_{\bm{r},A} \sigma^y_{\bm{r},B} \sigma^z_{\bm{r}-\bm{a}_2,A} + \sigma^x_{\bm{r},A} \sigma^y_{\bm{r}-\bm{a}_1,A} \sigma^z_{\bm{r},B} \\
&=\mathrm{around}A\left(\bm{a}_1 \leftrightarrow -\bm{a}_1, \bm{a}_2 \leftrightarrow -\bm{a}_2,A \leftrightarrow B \right) \\
&=\mathrm{i} \sum_{\substack{\left(\bm{\delta}'_1,\bm{\delta}'_2 \right)\in \\ \left\{\left(-\bm{a}_1,-\bm{a}_2 \right),\left(-\bm{a}_2,\bm{0} \right),\left(\bm{0},-\bm{a}_1 \right) \right\}}} u_{\bm{r}+\bm{\delta}'_1,A;\bm{r},B} u_{\bm{r}+\bm{\delta}'_2,A;\bm{r},B} c_{\bm{r}+\bm{\delta}'_1,A} c_{\bm{r}+\bm{\delta}'_2,A} \\
\end{split}
\end{equation}
$$

$$
\begin{equation}
\begin{split}
-\kappa \sum_{\bm{r}} \mathrm{around}A
&=-\mathrm{i} \kappa \sum_{\bm{r}} \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} u_{\bm{r}+\bm{\delta}_1,B;\bm{r},A} u_{\bm{r}+\bm{\delta}_2,B;\bm{r},A} c_{\bm{r}+\bm{\delta}_1,B} c_{\bm{r}+\bm{\delta}_2,B} \\
&=-\mathrm{i} \kappa \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \sum_{\bm{r}'} \sum_{\bm{r}''} \sum_{\bm{r}} \delta_{\bm{r}',\bm{r}+\bm{\delta}_1} \delta_{\bm{r}'',\bm{r}+\bm{\delta}_2} u_{\bm{r}',B;\bm{r},A} u_{\bm{r}'',B;\bm{r},A} c_{\bm{r}',B} c_{\bm{r}'',B} \\
&=-\mathrm{i} \kappa \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \sum_{\bm{r}'} \sum_{\bm{r}''} \delta_{\bm{r}'-\bm{\delta}_1,\bm{r}''-\bm{\delta}_2} u_{\bm{r}',B;\bm{r}'-\bm{\delta}_1,A} u_{\bm{r}'',B;\bm{r}''-\bm{\delta}_2,A} c_{\bm{r}',B} c_{\bm{r}'',B} \\
&=-\mathrm{i} \kappa \sum_{\bm{r}'} \sum_{\bm{r}''} \left(\sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \delta_{\bm{r}'-\bm{\delta}_1,\bm{r}''-\bm{\delta}_2} u_{\bm{r}',B;\bm{r}'-\bm{\delta}_1,A} u_{\bm{r}'',B;\bm{r}''-\bm{\delta}_2,A} \right) c_{\bm{r}',B} c_{\bm{r}'',B} \\
&=-\mathrm{i} \kappa \sum_{i=1}^{N} \sum_{j=1}^{N} \left(\sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \delta_{\bm{r}_i-\bm{\delta}_1,\bm{r}_j-\bm{\delta}_2} u_{\bm{r}_i,B;\bm{r}_i-\bm{\delta}_1,A} u_{\bm{r}_j,B;\bm{r}_j-\bm{\delta}_2,A} \right) c_{i,B} c_{j,B} \\
\end{split}
\end{equation}
$$

令

$$
\begin{equation}
t^{(+)}_{ij}
=\sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \delta_{\bm{r}_i-\bm{\delta}_1,\bm{r}_j-\bm{\delta}_2} u_{\bm{r}_i,B;\bm{r}_i-\bm{\delta}_1,A} u_{\bm{r}_j,B;\bm{r}_j-\bm{\delta}_2,A}
\end{equation}
$$

$$
\begin{equation}
c_{\bm{r},A}
=a_{\bm{r}} + a^\dag_{\bm{r}},\quad
c_{\bm{r},B}
=\frac{1 }{\mathrm{i} } \left(a_{\bm{r}} - a^\dag_{\bm{r}} \right),
\end{equation}
$$

则

$$
\begin{equation}
\begin{split}
-\kappa \sum_{\bm{r}} \mathrm{around}A
&=-\mathrm{i} \kappa \sum_{i=1}^{N} \sum_{j=1}^{N} \left(\sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \delta_{\bm{r}_i-\bm{\delta}_1,\bm{r}_j-\bm{\delta}_2} u_{\bm{r}_i,B;\bm{r}_i-\bm{\delta}_1,A} u_{\bm{r}_j,B;\bm{r}_j-\bm{\delta}_2,A} \right) c_{i,B} c_{j,B} \\
&=-\mathrm{i} \kappa \sum_{i=1}^{N} \sum_{j=1}^{N} t^{(+)}_{ij} c_{i,B} c_{j,B} \\
&=\mathrm{i} \kappa \sum_{i=1}^{N} \sum_{j=1}^{N} t^{(+)}_{ij} \left(a_i - a^\dag_i \right) \left(a_j - a^\dag_j \right) \\
&=\mathrm{i} \kappa \sum_{i=1}^{N} \sum_{j=1}^{N} t^{(+)}_{ij} \left(a_i a_j + a^\dag_i a^\dag_j - a_i a^\dag_j - a^\dag_i a_j \right) \\
&=\mathrm{i} \kappa \sum_{i=1}^{N} \sum_{j=1}^{N} \frac{\left(t^{(+)}_{ij} - t^{(+)}_{ji} \right) }{2 }  \left(a_i a_j + a^\dag_i a^\dag_j \right) + \mathrm{i} \kappa \sum_{i=1}^{N} \sum_{j=1}^{N} \left(t^{(+)}_{ji} - t^{(+)}_{ij} \right) a^\dag_i a_j - \mathrm{i} \kappa \sum_{i=1}^{N} t^{(+)}_{ii} \\
\end{split}
\end{equation}
$$

令

$$
\begin{equation}
t^{(-)}_{ij}
=\sum_{\left(\bm{\delta}'_1,\bm{\delta}'_2 \right)} \delta_{\bm{r}_i-\bm{\delta}'_1,\bm{r}_j-\bm{\delta}'_2} u_{\bm{r}_i,A;\bm{r}_i-\bm{\delta}'_1,B} u_{\bm{r}_j,A;\bm{r}_j-\bm{\delta}'_2,B}
\end{equation}
$$

则

$$
\begin{equation}
\begin{split}
-\kappa \sum_{\bm{r}} \mathrm{around}B
&=-\mathrm{i} \kappa \sum_{i=1}^{N} \sum_{j=1}^{N} t^{(-)}_{ij} c_{i,A} c_{j,A} \\
&=-\mathrm{i} \kappa \sum_{i=1}^{N} \sum_{j=1}^{N} t^{(-)}_{ij} \left(a_i + a^\dag_i \right) \left(a_j + a^\dag_j \right) \\
&=-\mathrm{i} \kappa \sum_{i=1}^{N} \sum_{j=1}^{N} t^{(-)}_{ij} \left(a_i a_j + a^\dag_i a^\dag_j + a_i a^\dag_j + a^\dag_i a_j \right) \\
&=-\mathrm{i} \kappa \sum_{i=1}^{N} \sum_{j=1}^{N} \frac{\left(t^{(-)}_{ij} - t^{(-)}_{ji} \right) }{2 } \left(a_i a_j + a^\dag_i a^\dag_j \right) + \mathrm{i} \kappa \sum_{i=1}^{N} \sum_{j=1}^{N} \left(t^{(-)}_{ji} - t^{(-)}_{ij} \right) a^\dag_i a_j - \mathrm{i} \kappa \sum_{i=1}^{N} t^{(-)}_{ii} \\
\end{split}
\end{equation}
$$

于是微扰哈密顿量为

$$
\begin{equation}
\begin{split}
\widetilde{H}^{(3)}_{\mathrm{eff}}
&=-\kappa \sum_{\bm{r}\in \mathrm{UC}} \left(\mathrm{around}A + \mathrm{around}B \right) \\
&=\sum_{i=1}^{N} \sum_{j=1}^{N} \frac{\mathrm{i} \kappa }{2 }\left[\left(t^{(+)}_{ij} - t^{(+)}_{ji} \right) - \left(t^{(-)}_{ij} - t^{(-)}_{ji} \right) \right]  \left(a_i a_j + a^\dag_i a^\dag_j \right) + \sum_{i=1}^{N} \sum_{j=1}^{N} \mathrm{i} \kappa \left[\left(t^{(+)}_{ji} - t^{(+)}_{ij} \right) + \left(t^{(-)}_{ji} - t^{(-)}_{ij} \right) \right] a^\dag_i a_j - \mathrm{i} \kappa \sum_{i=1}^{N} \left(t^{(+)}_{ii} + t^{(-)}_{ii} \right) \\
\end{split}
\end{equation}
$$

设 

$$
\begin{equation}
\begin{split}
\widetilde{H}^{(3)}_{\mathrm{eff}}
&=\frac{1 }{2 }
\begin{bmatrix}
a^\dag_{1} &\cdots &a^\dag_{N} &a_{1} &\cdots &a_{N}
\end{bmatrix}
\begin{bmatrix}
\Xi' &\Delta' \\
\Delta'^\dag &-\Xi'^{\mathrm{T}}
\end{bmatrix}
\begin{bmatrix}
a_{1} \\
\vdots \\
a_{N} \\
a^\dag_{1} \\
\vdots \\
a^\dag_{N}
\end{bmatrix} + C' \\
&=C' - \frac{1 }{2 } \sum_{i=1}^{N} \Xi'_{ii} + \sum_{j=1}^{N} \sum_{i=1}^{N} \Xi'_{ij} a^\dag_i a_j + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} \Delta'_{ij} a^\dag_i a^\dag_j + \frac{1 }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N}\left(-(\Delta'_{ij})^* \right) a_i a_j \\
\end{split}
\end{equation}
$$

对比可得

$$
\begin{equation}
\Xi'_{ij}
=\mathrm{i} \kappa \left[\left(t^{(+)}_{ji} - t^{(+)}_{ij} \right) + \left(t^{(-)}_{ji} - t^{(-)}_{ij} \right) \right],\quad
\Delta'_{ij}
=\frac{\mathrm{i} \kappa }{2 }\left[\left(t^{(+)}_{ij} - t^{(+)}_{ji} \right) - \left(t^{(-)}_{ij} - t^{(-)}_{ji} \right) \right]
\end{equation}
$$

$$
\begin{equation}
E_{\mathrm{GS}}
=-614.5997704724723,\quad \mathrm{PBC,PBC}
\end{equation}
$$

$$
\begin{equation}
E_{\mathrm{GS}}
=-614.5997704724723,\quad \mathrm{APBC,PBC}
\end{equation}
$$

-614.5997704724723

-614.5997704724723

-22.30307641362066

-22.30307641362066

-22.30307641362066

-149.9390356885324

-149.9390356885324

-22.30307641362066

-22.30307641362066

---

10 $\times $ 10 unit cell

-157.44132763536777 APBC, PBC

-157.5359866831199 PBC, PBC

-157.44132763536777 PBC, APBC

-157.44132763536777 APBC, APBC

kappa 

-158.12215144545797 APBC, APBC

-158.13066989350511 PBC, APBC

-158.13066989350517 APBC, PBC

-158.002995294399 PBC, PBC