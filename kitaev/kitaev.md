# 1

$$
\Ket{\sigma_1,\cdots,\sigma_N} \mapsto ?
$$

### single spin vs. single two-modes fermion

$$
\begin{align}
\Ket{\sigma_i } \mapsto f^\dag_{\sigma_i} \Ket{0 },\quad \sigma_i = \pm 1/2
\end{align}
$$

单占据子空间投影算符

$$
\begin{equation}
\mathcal{P}_i
\equiv \sum_{\sigma_i} f^\dag_{\sigma_i} \Ket{0 } \Bra{0 } f_{\sigma_i}
\end{equation}
$$

首先想证明

$$
\begin{align}
\forall \sigma_i,\sigma_i',\quad
f^\dag_{\sigma_i} \Ket{0 } \Bra{0 } f_{\sigma_i'}
=\mathcal{P}_i f^\dag_{\sigma_i} f_{\sigma_i'} \mathcal{P}_i
\end{align}
$$

首先恒等算符

$$
\begin{equation}
\begin{split}
\mathcal{P}_i f^\dag_{\sigma_i} f_{\sigma_i'} \mathcal{P}_i
&=\left(\sum_{\sigma_i''} f^\dag_{\sigma_i''} \Ket{0 } \Bra{0 } f_{\sigma_i''} \right) f^\dag_{\sigma_i} f_{\sigma_i'} \left(\sum_{\sigma_i'''} f^\dag_{\sigma_i'''} \Ket{0 } \Bra{0 } f_{\sigma_i'''} \right) \\
&=\sum_{\sigma_i'' \sigma_i'''} f^\dag_{\sigma_i''} \Ket{0 } \Braket{0 | f_{\sigma_i''} f^\dag_{\sigma_i} f_{\sigma_i'} f^\dag_{\sigma_i'''} | 0 } \Bra{0 } f_{\sigma_i'''} \\
&=\sum_{\sigma_i'' \sigma_i'''} f^\dag_{\sigma_i''} \Ket{0 } \Braket{0 | \left(\delta_{\sigma_i,\sigma_i''} - f^\dag_{\sigma_i} f_{\sigma_i''} \right) f_{\sigma_i'} f^\dag_{\sigma_i'''} | 0 } \Bra{0 } f_{\sigma_i'''} \\
&=\sum_{\sigma_i'' \sigma_i'''} \delta_{\sigma_i,\sigma_i''} f^\dag_{\sigma_i''} \Ket{0 } \Braket{0 | f_{\sigma_i'} f^\dag_{\sigma_i'''} | 0 } \Bra{0 } f_{\sigma_i'''} \\
&=\sum_{\sigma_i'' \sigma_i'''} \delta_{\sigma_i,\sigma_i''} f^\dag_{\sigma_i''} \Ket{0 } \delta_{\sigma_i',\sigma_i'''} \Bra{0 } f_{\sigma_i'''} \\
&=f^\dag_{\sigma_i} \Ket{0 } \Bra{0 } f_{\sigma_i'}
\end{split}
\end{equation}
$$

格点 $i $ 上单自旋任意算符

$$
\begin{equation}
\begin{split}
O_i
&=\sum_{\sigma_i\sigma_i'} \Braket{\sigma_i | O_i | \sigma_i' } \Ket{\sigma_i }\Bra{\sigma_i' }
\mapsto \sum_{\sigma_i\sigma_i'} \Braket{\sigma_i | O_i | \sigma_i' } f^\dag_{\sigma_i} \Ket{0 } \Bra{0 } f_{\sigma_i'} \\
&=\sum_{\sigma_i\sigma_i'} \Braket{\sigma_i | O_i | \sigma_i' } \mathcal{P}_i f^\dag_{\sigma_i} f_{\sigma_i'} \mathcal{P}_i \\
\end{split}
\end{equation}
$$

考虑把这样一个映射分为两次映射：

$$
\begin{equation}
\Gamma:\mathcal{H}^{\text{spin}}_i \to \mathcal{H}^{\text{1}}_i
\end{equation}
$$

$$
\begin{equation}
\Gamma_1:\mathcal{H}^{\text{spin}}_i \to \mathcal{H}^{\text{Fock}}_i,\quad
\Gamma_2:\mathcal{H}^{\text{Fock}}_i \to \mathcal{H}^{\text{1}}_i
\end{equation}
$$

$$
\begin{equation}
\Gamma = \Gamma_2 \circ \Gamma_1 
\end{equation}
$$

想证明 算符

$$
\begin{equation}
\Gamma\left(O_1 O_2 \right)
=\Gamma_2 \left(\Gamma_1 \left(O_1 \right) \Gamma_1 \left(O_1 \right) \right)
\end{equation}
$$

## 多自旋与多2模式费米子单占据子空间一一对应

### 态矢的映射

$$
\begin{equation}
\Ket{\sigma_1,\cdots,\sigma_N }
\mapsto f^\dag_{1,\sigma_1} \cdots f^\dag_{N,\sigma_N} \Ket{0 }
\end{equation}
$$

$$
\begin{equation}
\Bra{\sigma_1,\cdots,\sigma_N }
\mapsto \Bra{0 } f_{N,\sigma_N} \cdots f_{1,\sigma_1}
\end{equation}
$$

### 各格点单占据子空间投影算符

$$
\begin{equation}
\mathcal{P}
\equiv \sum_{\sigma_1,\cdots,\sigma_N} f^\dag_{1,\sigma_1} \cdots f^\dag_{N,\sigma_N} \Ket{0 } \Bra{0 } f_{N,\sigma_N} \cdots f_{1,\sigma_1}
\end{equation}
$$

#### 投影算符与任意算符对易

$$
\begin{equation}
\left[\mathcal{P} , \tilde{O} \right] = 0.
\end{equation}
$$

### 算符的映射

$$
\begin{equation}
\begin{split}
O
&=\sum_{\sigma_1,\cdots,\sigma_N} \sum_{\sigma_1',\cdots,\sigma_N'} \Braket{\sigma_1,\cdots,\sigma_N | O | \sigma_1',\cdots,\sigma_N' } \Ket{\sigma_1,\cdots,\sigma_N } \Bra{\sigma_1,\cdots,\sigma_N } \\
&\mapsto \sum_{\sigma_1,\cdots,\sigma_N} \sum_{\sigma_1',\cdots,\sigma_N'} \Braket{\sigma_1,\cdots,\sigma_N | O | \sigma_1',\cdots,\sigma_N' } f^\dag_{1,\sigma_1} \cdots f^\dag_{N,\sigma_N} \Ket{0 } \Bra{0 } f_{N,\sigma_N} \cdots f_{1,\sigma_1} \\
&\mapsto \mathcal{P} \left(\sum_{\sigma_1,\cdots,\sigma_N} \sum_{\sigma_1',\cdots,\sigma_N'} \Braket{\sigma_1,\cdots,\sigma_N | O | \sigma_1',\cdots,\sigma_N' } f^\dag_{1,\sigma_1} \cdots f^\dag_{N,\sigma_N} f_{N,\sigma_N} \cdots f_{1,\sigma_1} \right) \mathcal{P} \\
\end{split}
\end{equation}
$$

也就是说，算符的一一映射等价于先把算符映射到 Fock 空间中的相应算符，再投影到各格点单占据子空间。

### 映射保算符对态矢作用、保算符乘积

### 本征方程对应关系

设 $H $ 是 $N $ 自旋Hilbert空间上的算符，$E $ 和 $\Ket{\psi } $ 是某一组本征解；设 $\tilde{H} $ 是相应 $N $ 两模式费米子Fock空间上的算符；设 $H' $ 是相应 $N $ 两模式费米子各格点单占据子空间上的算符，则

$$
\begin{equation}
H \Ket{\psi } = E \Ket{\psi },
\end{equation}
$$

两边同时做 tilde 映射

$$
\begin{equation}
\tilde{H} \Ket{\tilde{\psi} } = E \Ket{\tilde{\psi} },
\end{equation}
$$

利用投影算符与任意算符对易这一性质，以及 $\mathcal{P}^2=\mathcal{P} $，投影算符作用

$$
\begin{equation}
\mathcal{P} \tilde{H} \Ket{\tilde{\psi} } = E \mathcal{P} \Ket{\tilde{\psi} },
\end{equation}
$$

左边

$$
\begin{equation}
\mathcal{P} \tilde{H} \Ket{\tilde{\psi} }
=\mathcal{P}^2 \tilde{H} \Ket{\tilde{\psi} }
=\mathcal{P} \tilde{H} \mathcal{P} \Ket{\tilde{\psi} }
=\mathcal{P} \tilde{H} \mathcal{P} \mathcal{P} \Ket{\tilde{\psi} }
=H' \Ket{\psi' }
\end{equation}
$$

右边

$$
\begin{equation}
E \mathcal{P} \Ket{\tilde{\psi} }
=E \Ket{\psi' },
\end{equation}
$$

即

$$
\begin{equation}
H' \Ket{\psi' } = E \Ket{\psi' },
\end{equation}
$$

---

设 $\tilde{H} $ 的某一组本征解为 $E,\Ket{\tilde{\psi} } $，下面证明 $E,\Ket{\psi' } $ 也是 $H' $ 的本征解。

$$
\begin{equation}
\tilde{H} \Ket{\tilde{\psi} } = E \Ket{\tilde{\psi} },
\end{equation}
$$

### Kitaev honeycomb 哈密顿量

$$
\begin{equation}
\hat{H}
=-J_x \sum_{\Braket{j,k }_x} \hat{\sigma}_j^x \hat{\sigma}_k^x - J_y \sum_{\Braket{j,k }_y} \hat{\sigma}_j^y \hat{\sigma}_k^y - J_z \sum_{\Braket{j,k }_z} \hat{\sigma}_j^z \hat{\sigma}_k^z
\end{equation}
$$

## 复费米子的Majorana分解

$$
\sigma_x = \Ket{\uarr }\Bra{\darr } + \Ket{\darr }\Bra{\uarr }
\mapsto f^\dag_{\uarr} f_{\darr} + f^\dag_{\darr} f_{\uarr}
$$

$$
\begin{equation}
\tilde{\sigma}_x
=\frac{\mathrm{i} }{2 } \left(c b^z + b^y b^x \right)
\end{equation}
$$

--- 

### Abrikosov Pseudo-Fermion Representation

从自旋-1/2到 2-模式复费米子体系的映射：

$$
\begin{equation}
\Ket{\uparrow } \mapsto f^\dag_{\uparrow} \Ket{0 },\quad
\Ket{\downarrow } \mapsto f^\dag_{\downarrow} \Ket{0 }.
\end{equation}
$$

$$
\begin{equation}
\Gamma : \sigma^\alpha \mapsto \sum_{ab} f^\dag_a \sigma^\alpha_{ab} f_b,
\end{equation}
$$

$$
\begin{equation}
\left\{
\begin{aligned}
&\sigma^x \mapsto f^\dag_\uparrow f_\downarrow + f^\dag_\downarrow f_\uparrow, \\
&\sigma^y \mapsto \mathrm{i}\left(-f^\dag_\uparrow f_\downarrow + f^\dag_\downarrow f_\uparrow \right), \\
&\sigma^z \mapsto f^\dag_\uparrow f_\uparrow - f^\dag_\downarrow f_\downarrow, \\
&f^\dag_\uparrow f_\uparrow + f^\dag_\downarrow f_\downarrow = 1.
\end{aligned}
\right.
\end{equation}
$$

指定第一种复费米子模式为 $f_\uparrow,f^\dag_\uparrow $，第二种复费米子模式为 $f_\downarrow,f^\dag_\downarrow $，则



在单占据子空间

$$
\begin{equation}
\sum_a f^\dag_a f_a = 1
\end{equation}
$$

保持算符乘法和自旋-1/2李代数：

$$
\begin{equation}
\Gamma\left(\sigma^\alpha \sigma^\beta \right)
=\Gamma\left(\sigma^\alpha \right) \Gamma\left(\sigma^\beta \right),
\end{equation}
$$

$$
\begin{equation}
\left[\sigma^\alpha , \sigma^\beta \right] = 2\mathrm{i} \varepsilon^{\alpha\beta\gamma} \sigma^\gamma,\quad
\left[\Gamma\left(\sigma^\alpha \right) , \Gamma\left(\sigma^\beta \right) \right] = 2 \mathrm{i} \varepsilon^{\alpha\beta\gamma} \Gamma\left(\sigma^\gamma \right).
\end{equation}
$$

### Majorana Representation of Complex Fermion

设 $c,c^\dag $ 分别是某种费米子模式的湮灭、产生算符，利用它们可构造出两个 Majorana 算符：

$$
\begin{equation}
\gamma_1 \equiv c + c^\dag,\quad
\gamma_2 \equiv -\mathrm{i}\left(c - c^\dag \right),
\end{equation}
$$

或者说复费米子算符可由 Majorana 算符表示：

$$
\begin{equation}
c = \frac{1 }{2 } \left(\gamma_1 + \mathrm{i} \gamma_2 \right),\quad
c^\dag = \frac{1 }{2 } \left(\gamma_1 - \mathrm{i} \gamma_2 \right).
\end{equation}
$$

利用复费米子反对易关系

$$
\begin{equation}
\left\{c , c^\dag \right\} = 1,\quad
\left\{c , c \right\} = \left\{c^\dag , c^\dag \right\} = 0,
\end{equation}
$$

可以得到 Majorana 算符反对易关系：

$$
\begin{equation}
\left\{\gamma_1 , \gamma_2 \right\} = 0,\quad
\left\{\gamma_1 , \gamma_1 \right\} = 2,\quad
\left\{\gamma_2 , \gamma_2 \right\} = 2,
\end{equation}
$$

或统一写为：

$$
\begin{equation}
\left\{\gamma_i , \gamma_j \right\} = 2\delta_{ij},\quad ij\in \left\{1,2 \right\}.
\end{equation}
$$

$$
\begin{equation}
\gamma_1^2 = \gamma_2^2 = 1,\quad
\gamma_1^\dag = \gamma_1,\quad
\gamma_2^\dag = \gamma_2.
\end{equation}
$$

### 从 spin-1/2 到 2-模式复费米子再到 Majorana 费米子

$$
\begin{equation}
\left\{
\begin{aligned}
&\sigma^x \mapsto f^\dag_\uparrow f_\downarrow + f^\dag_\downarrow f_\uparrow, \\
&\sigma^y \mapsto \mathrm{i}\left(-f^\dag_\uparrow f_\downarrow + f^\dag_\downarrow f_\uparrow \right), \\
&\sigma^z \mapsto f^\dag_\uparrow f_\uparrow - f^\dag_\downarrow f_\downarrow, \\
&f^\dag_\uparrow f_\uparrow + f^\dag_\downarrow f_\downarrow = 1.
\end{aligned}
\right.
\end{equation}
$$

用复费米子算符构造如下的 Majorana 算符：

$$
\begin{equation}
\gamma_{\uparrow,1} = f_{\uparrow} + f^\dag_{\uparrow},\quad
\gamma_{\uparrow,2} = -\mathrm{i}\left(f_{\uparrow} - f^\dag_{\uparrow} \right),
\end{equation}
$$

$$
\begin{equation}
\gamma_{\downarrow,1} = f_{\downarrow} + f^\dag_{\downarrow},\quad
\gamma_{\downarrow,2} = -\mathrm{i}\left(f_{\downarrow} - f^\dag_{\downarrow} \right).
\end{equation}
$$

则

$$
\begin{equation}
\sigma^x
\mapsto f^\dag_\uparrow f_\downarrow + f^\dag_\downarrow f_\uparrow
=\mathrm{i} \gamma_{\uparrow,1} \gamma_{\downarrow,2},
\end{equation}
$$

$$
\begin{equation}
\sigma^y
\mapsto -\mathrm{i}\left(f^\dag_\uparrow f_\downarrow - f^\dag_\downarrow f_\uparrow \right)
=-\mathrm{i} \gamma_{\uparrow,1} \gamma_{\downarrow,1},
\end{equation}
$$

$$
\begin{equation}
\sigma^z
\mapsto f^\dag_\uparrow f_\uparrow - f^\dag_\downarrow f_\downarrow
=\mathrm{i} \gamma_{\uparrow,1} \gamma_{\uparrow,2}.
\end{equation}
$$

单占据条件 $f^\dag_\uparrow f_\uparrow + f^\dag_\downarrow f_\downarrow = 1 $ 化为：

$$
\begin{equation}
\gamma_{\uparrow,1} \gamma_{\uparrow,2} + \gamma_{\downarrow,1} \gamma_{\downarrow,2}
=0
\end{equation}
$$

观察到 $\gamma_{\uparrow,1} $ 比较特殊，若令：

$$
\gamma_{\uparrow,1} = c,\quad
\gamma_{\downarrow,2} = b^x,\quad
\gamma_{\downarrow,1} = -b^y,\quad
\gamma_{\uparrow,2} = b^z,
$$

则有

$$
\begin{equation}
\sigma^x \mapsto \mathrm{i} c b^x
=-\mathrm{i} b^x c,
\end{equation}
$$

$$
\begin{equation}
\sigma^y \mapsto \mathrm{i} c b^y
=-\mathrm{i} b^y c,
\end{equation}
$$

$$
\begin{equation}
\sigma^z \mapsto \mathrm{i} c b^z
=-\mathrm{i} b^z c
\end{equation}
$$

单占据条件化为

$$
\begin{equation}
b^x b^y b^z c = 1.
\end{equation}
$$

### 用 Majorana 算符表达 Kitaev Honeycomb 模型哈密顿量

Kitaev Honeycomb 哈密顿量：

$$
\begin{equation}
H
=K_x \sum_{\Braket{j,k }_x} \sigma_j^x \sigma_k^x + K_y \sum_{\Braket{j,k }_y} \sigma_j^y \sigma_k^y + K_z \sum_{\Braket{j,k }_z} \sigma_j^z \sigma_k^z.
\end{equation}
$$

定义 $\alpha_{jk} $ 为最近邻 $j,k $ 格点的 bond 类型，$\alpha_{ij}\in\left\{x,y,z \right\} $，则

$$
\begin{equation}
H
=\sum_{\Braket{j,k }} K_{\alpha_{jk}} \sigma_j^{\alpha_{jk}} \sigma_k^{\alpha_{jk}}.
\end{equation}
$$

哈密顿量映射为：

$$
\begin{equation}
\begin{split}
H
\mapsto \widetilde{H}
&=\sum_{\Braket{j,k }} K_{\alpha_{jk}} \left(-\mathrm{i} b_j^{\alpha_{jk}} c_j \right) \left(-\mathrm{i} b_k^{\alpha_{jk}} c_k \right) \\
&=-\mathrm{i} \sum_{\Braket{j,k }} K_{\alpha_{jk}} \left(\mathrm{i} b_j^{\alpha_{jk}} b_k^{\alpha_{jk}} \right) c_j c_k.
\end{split}
\end{equation}
$$

为了方便数值计算，定义：

$$
\begin{equation}
\hat{u}_{jk}
\equiv\left\{
\begin{aligned}
&\mathrm{i} b_j^{\alpha_{jk}} b_k^{\alpha_{jk}}&&,j\text{和}k最近邻 \\
&0&&,\text{其他情况}
\end{aligned}
\right.
\end{equation}
$$

则

$$
\begin{equation}
\widetilde{H}
=-\mathrm{i} \sum_{\Braket{j,k }} K_{\alpha_{jk}} \hat{u}_{jk} c_j c_k
\end{equation}
$$

考虑构型 $\left\{u_{jk}=\pm 1,\forall j,k \right\} $，则

$$
\begin{equation}
\widetilde{H}
=-\mathrm{i} \sum_{\Braket{j,k }} K_{\alpha_{jk}} {u}_{jk} c_j c_k,
\end{equation}
$$

其中 $u_{jk} $ 是 $\hat{u}_{jk} $ 的本征值。

### 把每个 unit cell 内两格点的 Majorana-c 算符组合成复费米子

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
=\mathrm{i} \kappa \left[\left(t^{(+)}_{ij} - t^{(+)}_{ji} \right) - \left(t^{(-)}_{ij} - t^{(-)}_{ji} \right) \right]
\end{equation}
$$

$$
\begin{equation}
C'
=-\mathrm{i} \kappa \sum_{i=1}^{N} \left[t^{(+)}_{ii} + t^{(-)}_{ii} \right]
=0
\end{equation}
$$

### 计算基态宇称

已知

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
\end{bmatrix} \\
\end{split}
\end{equation}
$$

其中

$$
\begin{equation}
a_{i}
\equiv \frac{1 }{2 } \left(c_{i,A} + \mathrm{i} c_{i,B} \right),\quad
a^\dag_{i}
\equiv \frac{1 }{2 } \left(c_{i,A} - \mathrm{i} c_{i,B} \right),\quad
\end{equation}
$$

$$
\begin{equation}
c_{i,A}
=a_{i} + a^\dag_{i},\quad
c_{\bm{r},B}
=\frac{1 }{\mathrm{i} } \left(a_{i} - a^\dag_{i} \right),
\end{equation}
$$

设 $\widetilde{H} $ 可以写为

$$
\begin{equation}
\begin{split}
\widetilde{H}
=\frac{\mathrm{i} }{2 } 
\begin{bmatrix}
c_{1,A} &c_{1,B} &\cdots &c_{N,A} &c_{N,B}
\end{bmatrix}
A 
\begin{bmatrix}
c_{1,A} \\
c_{1,B} \\
\vdots \\
c_{N,A} \\
c_{N,B}
\end{bmatrix}
\end{split}
\end{equation}
$$

则反对称的 $A $ 怎么写？

设

$$
\begin{equation}
\begin{split}
\begin{bmatrix}
a_{1} \\
\vdots \\
a_{N} \\
a^\dag_{1} \\
\vdots \\
a^\dag_{N}
\end{bmatrix}
=P
\begin{bmatrix}
a_1 \\
a^\dag_1 \\
\vdots \\
a_N \\
a^\dag_N
\end{bmatrix}
\end{split}
\end{equation}
$$

则上面的矩阵方程可化为

$$
\begin{equation}
\left\{
\begin{aligned}
&a_i = \sum_{j=1}^{N} \left(P_{i,2j-1} a_j + P_{i,2j} a^\dag_j \right) \\
&a^\dag_i = \sum_{j=1}^{N} \left(P_{i+N,2j-1} a_j + P_{i+N,2j} a^\dag_j \right)
\end{aligned}
\right.,i=1,2,\cdots,N
\end{equation}
$$

因此，$P $ 的非零矩阵元为：

$$
\begin{equation}
P_{i,2i-1} = 1,\quad P_{i+N,2i} = 1,\quad
i = 1,2,\cdots,N
\end{equation}
$$

再设

$$
\begin{equation}
\begin{split}
\begin{bmatrix}
a_1 \\
a^\dag_1 \\
\vdots \\
a_N \\
a^\dag_N
\end{bmatrix}
=P'
\begin{bmatrix}
c_{1,A} \\
c_{1,B} \\
\vdots \\
c_{N,A} \\
c_{N,B}
\end{bmatrix}
\end{split}
\end{equation}
$$

注意到

$$
\begin{equation}
\begin{split}
\begin{bmatrix}
a_{i} \\
a^\dag_i
\end{bmatrix}
=\begin{bmatrix}
\frac{1 }{2 } \left(c_{i,A} + \mathrm{i} c_{i,B} \right) \\[1mm]
\frac{1 }{2 } \left(c_{i,A} - \mathrm{i} c_{i,B} \right)
\end{bmatrix}
=\frac{1 }{2 }
\begin{bmatrix}
1 &\mathrm{i} \\
1 &-\mathrm{i}
\end{bmatrix}
\begin{bmatrix}
c_{i,A} \\
c_{i,B}
\end{bmatrix}
\end{split}
\end{equation}
$$

因此

$$
\begin{equation}
P'
=\bigoplus_{i=1}^{N} \frac{1 }{2 }
\begin{bmatrix}
1 &\mathrm{i} \\
1 &-\mathrm{i}
\end{bmatrix}
\end{equation}
$$

总的来说

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
\end{bmatrix} \\
&=\frac{1 }{2 } 
\begin{bmatrix}
c_{1,A} &c_{1,B} &\cdots &c_{N,A} &c_{N,B}
\end{bmatrix}
\left(P P' \right)^\dag h \left(P P' \right)
\begin{bmatrix}
c_{1,A} \\
c_{1,B} \\
\vdots \\
c_{N,A} \\
c_{N,B}
\end{bmatrix} \\
&=\frac{\mathrm{i} }{2 } 
\begin{bmatrix}
c_{1,A} &c_{1,B} &\cdots &c_{N,A} &c_{N,B}
\end{bmatrix}
\left[-\mathrm{i}\left(P P' \right)^\dag h \left(P P' \right) \right]
\begin{bmatrix}
c_{1,A} \\
c_{1,B} \\
\vdots \\
c_{N,A} \\
c_{N,B}
\end{bmatrix}
\end{split}
\end{equation}
$$

令

$$
\begin{equation}
A'
=-\mathrm{i} \left(P P' \right)^\dag h \left(P P' \right),\quad
\end{equation}
$$

其中

$$
\begin{equation}
h
=\begin{bmatrix}
\Xi &\Delta \\
\Delta^\dag &-\Xi^{\mathrm{T}}
\end{bmatrix}
\end{equation}
$$

$$
\begin{equation}
P_{i,2i-1} = 1,\quad P_{i+N,2i} = 1,\quad
i = 1,2,\cdots,N,\quad
P\text{的其余矩阵元为0}
\end{equation}
$$

$$
\begin{equation}
P'
=\bigoplus_{i=1}^{N} \frac{1 }{2 }
\begin{bmatrix}
1 &\mathrm{i} \\
1 &-\mathrm{i}
\end{bmatrix}
=I_{N} \otimes \frac{1 }{2 }
\begin{bmatrix}
1 &\mathrm{i} \\
1 &-\mathrm{i}
\end{bmatrix}
\end{equation}
$$

由 c-Majorana 反对易关系

$$
\begin{equation}
i\ne j,\quad c_i c_j = -c_j c_i
\end{equation}
$$

可知

$$
\begin{equation}
\begin{split}
\widetilde{H}
&=\frac{\mathrm{i} }{2 } \bold{c}^\dag A' \bold{c}
=\frac{\mathrm{i} }{2 } \sum_{i,j,i\ne j} A'_{ij} c_i c_j
=\frac{\mathrm{i} }{2 } \sum_{i,j,i\ne j} -A'_{ij} c_j c_i
=\frac{\mathrm{i} }{2 } \sum_{j,i,j\ne i} -A'_{ji} c_i c_j \\
&=\frac{\mathrm{i} }{2 } \bold{c}^\dag \left(-A'^{\mathrm{T}} \right) \bold{c}
\end{split}
\end{equation}
$$

于是

$$
\begin{equation}
\widetilde{H}
=\frac{\mathrm{i} }{2 } \bold{c}^\dag A' \bold{c}
=\frac{\mathrm{i} }{2 } \bold{c}^\dag \left[\frac{1 }{2 } \left(A'-A'^{\mathrm{T}} \right) \right] \bold{c}
\end{equation}
$$

于是最终有

$$
\begin{equation}
A
=\frac{1 }{2 } \left(A'-A'^{\mathrm{T}} \right)
\end{equation}
$$


---


$$
\begin{equation}
\begin{aligned}
\widetilde{H}
=&\frac{\mathrm{i} }{2 }
\begin{bmatrix}
\cdots &c_{i,A} &c_{i,B} &\cdots
\end{bmatrix}
M
\begin{bmatrix}
\vdots \\
c_{i,A} \\
c_{i,B} \\
\vdots
\end{bmatrix} \\
&=\frac{\mathrm{i} }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} \left(M_{2i-1,2j-1} c_{i,A} c_{j,A} + M_{2i-1,2j} c_{i,A} c_{j,B} + M_{2i,2j-1} c_{i,B} c_{j,A} + M_{2i,2j} c_{i,B} c_{j,B} \right)
\end{aligned}
\end{equation}
$$

对无磁场哈密顿量，

$$
\begin{equation}
\begin{aligned}
\widetilde{H}_0
&=\frac{\mathrm{i} }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} \left(-2 t_{ij} \right) c_{i,A} c_{j,B}
=\frac{\mathrm{i} }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} -\left( t_{ij} - t_{ji} \right) c_{i,A} c_{j,B} \\
&=\frac{\mathrm{i} }{2 } \left[\sum_{i=1}^{N} \sum_{j=1}^{N} \frac{-\left( t_{ij} - t_{ji} \right) }{2 }  c_{i,A} c_{j,B} + \sum_{i=1}^{N} \sum_{j=1}^{N} \frac{\left( t_{ij} - t_{ji} \right) }{2 } c_{j,B} c_{i,A} \right] \\
&=\frac{\mathrm{i} }{2 } \left[\sum_{i=1}^{N} \sum_{j=1}^{N} \frac{-\left( t_{ij} - t_{ji} \right) }{2 }  c_{i,A} c_{j,B} + \sum_{j=1}^{N} \sum_{i=1}^{N} \frac{\left( t_{ji} - t_{ij} \right) }{2 } c_{i,B} c_{j,A} \right] \\
&=\frac{\mathrm{i} }{2 } \left[\sum_{i=1}^{N} \sum_{j=1}^{N} \frac{-\left( t_{ij} - t_{ji} \right) }{2 }  c_{i,A} c_{j,B} + \sum_{j=1}^{N} \sum_{i=1}^{N} \frac{-\left( t_{ij} - t_{ji} \right) }{2 } c_{i,B} c_{j,A} \right] \\
\end{aligned}
\end{equation}
$$

一种取法为

$$
\begin{equation}
\left(M_0 \right)_{2i-1,2j-1} = 0
\end{equation}
$$

$$
\begin{equation}
\left(M_0 \right)_{2i-1,2j} = \frac{-\left( t_{ij} - t_{ji} \right) }{2 }
\end{equation}
$$

$$
\begin{equation}
\left(M_0 \right)_{2i,2j-1} = \frac{-\left( t_{ij} - t_{ji} \right) }{2 }
\end{equation}
$$

$$
\begin{equation}
\left(M_0 \right)_{2i,2j} = 0
\end{equation}
$$

---

对 $\kappa $ 项，

$$
\begin{equation}
\widetilde{H}_\kappa
=\frac{\mathrm{i} }{2 } \sum_{i=1}^{N} \sum_{j=1}^{N} \left[-\kappa \left(t^+_{ij} - t^+_{ji} \right) c_{i,B} c_{j,B} - \kappa\left(t^-_{ij} - t^-_{ji} \right) c_{i,A} c_{j,A} \right]
\end{equation}
$$

${M}_\kappa $ 的一种取法为

$$
\begin{equation}
\left(M_\kappa \right)_{2i-1,2j-1} = -\kappa \left(t^-_{ij} - t^-_{ji} \right)
\end{equation}
$$

$$
\begin{equation}
\left(M_\kappa \right)_{2i-1,2j} = 0
\end{equation}
$$

$$
\begin{equation}
\left(M_\kappa \right)_{2i,2j-1} = 0
\end{equation}
$$

$$
\begin{equation}
\left(M_\kappa \right)_{2i,2j} = -\kappa \left(t^+_{ij} - t^+_{ji} \right)
\end{equation}
$$

---

总哈密顿量为

$$
\begin{equation}
\widetilde{H}
=\widetilde{H}_0 + \widetilde{H}_\kappa
=\frac{\mathrm{i} }{2 }
\begin{bmatrix}
\cdots &c_{i,A} &c_{i,B} &\cdots
\end{bmatrix}
M
\begin{bmatrix}
\vdots \\
c_{i,A} \\
c_{i,B} \\
\vdots
\end{bmatrix} \\ 
\end{equation}
$$

$$
\begin{equation}
M = M_0 + M_\kappa
\end{equation}
$$

