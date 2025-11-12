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




