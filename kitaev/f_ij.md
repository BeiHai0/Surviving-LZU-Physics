### 基态波函数

基态 $\Ket{\Omega } $ 是 $\alpha $ 准粒子的真空态，满足：

$$
\begin{equation}
\alpha_i \Ket{\Omega }
=0
\end{equation}
$$

也即

$$
\begin{equation}
\sum_{j=1}^{N} \left(w_{ji}^* a_j + v_{ji}^* a^\dag_j \right) \Ket{\Omega }
=0
\end{equation}
$$

#### 基态形式

$$
\begin{equation}
\Ket{\Omega }
=\mathcal{N} \exp\left(\frac{1 }{2 } \sum_{i,j} f_{i,j} a_i^\dag a_j^\dag \right) \Ket{0_a }
\end{equation}
$$

其中 $\Ket{0_a } $ 是 $a $ 费米子真空态，$f_{i,j}=-f_{j,i} $

由于

$$
\begin{equation}
\begin{split}
\left[a_i^\dag a_j^\dag , a_k^\dag a_l^\dag \right]
=0
\end{split}
\end{equation}
$$

而

$$
\begin{equation}
[A , B] = 0
\Longrightarrow \exp(A+B) = \exp(A) \exp(B)
\end{equation}
$$

于是

$$
\begin{equation}
\begin{split}
\Ket{\Omega }
&=\mathcal{N} \exp\left(\frac{1 }{2 } \sum_{i,j} f_{i,j} a_i^\dag a_j^\dag \right) \Ket{0_a } \\
&=\mathcal{N} \prod_{i,j} \exp\left(\frac{1 }{2 } f_{i,j} a_i^\dag a_j^\dag \right) \Ket{0_a }
\end{split}
\end{equation}
$$

注意到

$$
\begin{equation}
\begin{split}
\exp\left(\frac{1 }{2 } f_{i,j} a_i^\dag a_j^\dag \right) \Ket{0_a }
&=\sum_{k=0}^{\infty} \frac{1 }{k! } \left(\frac{1 }{2 } f_{i,j} a_i^\dag a_j^\dag \right)^k \Ket{0_a } \\
&=\left(1 + \frac{1 }{1! } \cdot \frac{1 }{2^1 } f_{i,j} a_i^\dag a_j^\dag + \frac{1 }{2! } \cdot \frac{1 }{2^2 } a_i^\dag a_j^\dag a_i^\dag a_j^\dag + \cdots \right) \Ket{0_a } \\
&=\left(1 + \frac{1 }{2 } f_{i,j} a_i^\dag a_j^\dag \right) \Ket{0_a }
\end{split}
\end{equation}
$$

于是

$$
\begin{equation}
\begin{split}
\Ket{\Omega }
&=\mathcal{N} \prod_{i,j} \exp\left(\frac{1 }{2 } f_{i,j} a_i^\dag a_j^\dag \right) \Ket{0_a } \\
&=\mathcal{N} \prod_{i,j} \left(1 + \frac{1 }{2 } f_{i,j} a_i^\dag a_j^\dag \right) \Ket{0_a }
\end{split}
\end{equation}
$$

#### 求基态波函数 $f_{i,j} $

$$
\alpha_i 
=\sum_{j=1}^{N} \left(w_{ji}^* a_j + v_{ji}^* a^\dag_j \right)
$$

$$
\begin{equation}
\Ket{\Omega }
=\mathcal{N} \prod_{l,m} \left(1 + \frac{1 }{2 } f_{l,m} a_l^\dag a_m^\dag \right) \Ket{0_a }
\end{equation}
$$

基态由

$$
\begin{equation}
\alpha_i \Ket{\Omega }
=0
\end{equation}
$$

确定。

利用

$$
\begin{equation}
AB = \left[A , B \right] + BA
\end{equation}
$$

$$
\begin{equation}
\left[A , \prod_i B_i \right]
=\sum_{k} \left(\prod_{j<k} B_j \right) \left[A , B_k \right] \left(\prod_{j>k} B_j \right)
\end{equation}
$$

$$
\begin{equation}
\left[1 + \frac{1 }{2 } f_{i,j} a_i^\dag a_j^\dag , 1 + \frac{1 }{2 } f_{l,m} a_l^\dag a_m^\dag \right]
=0
\end{equation}
$$

$$
\begin{equation}
\begin{split}
\left[a_j , 1+\frac{1 }{2 } f_{l',m'} a_{l'}^\dag a_{m'}^\dag \right]
&=\frac{1 }{2 } f_{l',m'} \left[a_j , a_{l'}^\dag a_{m'}^\dag \right] \\
&=\frac{1 }{2 } f_{l',m'} \left(\left[a_j , a_{l'}^\dag \right]a_{m'}^\dag + a_{l'}^\dag\left[a_j , a_{m'}^\dag \right] \right) \\
&=\frac{1 }{2 } f_{l',m'} \left[ \left(\left\{a_j , a_{l'}^\dag \right\} - 2 a_{l'}^\dag a_j \right) a_{m'}^\dag + a_{l'}^\dag\left(\left\{a_j , a_{m'}^\dag \right\} - 2 a_{m'}^\dag a_j \right) \right] \\
&=\frac{1 }{2 } f_{l',m'} \left[ \left(\delta_{j,l'} - 2 a_{l'}^\dag a_j \right) a_{m'}^\dag + a_{l'}^\dag\left(\delta_{j,m'} - 2 a_{m'}^\dag a_j \right) \right] \\
&=\frac{1 }{2 } f_{l',m'} \left(\delta_{j,l'} a_{m'}^\dag + \delta_{j,m'} a_{l'}^\dag - 2a_{l'}^\dag a_j a_{m'}^\dag - 2a_{l'}^\dag a_{m'}^\dag a_j \right) \\
&=\frac{1 }{2 } f_{l',m'} \left[\delta_{j,l'} a_{m'}^\dag + \delta_{j,m'} a_{l'}^\dag - 2a_{l'}^\dag \left(\delta_{j,m'} - a_{m'}^\dag a_j \right) - 2a_{l'}^\dag a_{m'}^\dag a_j \right] \\
&=\frac{1 }{2 } f_{l',m'} \left(\delta_{j,l'} a_{m'}^\dag - \delta_{j,m'} a_{l'}^\dag \right) \\
\end{split}
\end{equation}
$$

$$
\begin{equation}
\left[a_{m'}^\dag , 1 + \frac{1 }{2 } f_{l,m} a_l^\dag a_m^\dag \right]
=0
\end{equation}
$$

$$
\begin{equation}
\begin{split}
&\frac{1 }{2 } f_{l',m'} \left(\delta_{j,l'} a_{m'}^\dag - \delta_{j,m'} a_{l'}^\dag \right) \cdot \left(1 + \frac{1 }{2 } f_{l',m'} a_{l'}^\dag a_{m'}^\dag \right) \\
=&\frac{1 }{2 } f_{l',m'} \left(\delta_{j,l'} a_{m'}^\dag - \delta_{j,m'} a_{l'}^\dag \right) + \frac{1 }{4 } f_{l',m'}^2 \left(\delta_{j,l'} a_{m'}^\dag - \delta_{j,m'} a_{l'}^\dag \right) a_{l'}^\dag a_{m'}^\dag \\
=&\frac{1 }{2 } f_{l',m'} \left(\delta_{j,l'} a_{m'}^\dag - \delta_{j,m'} a_{l'}^\dag \right)
\end{split}
\end{equation}
$$

有

$$
\begin{equation}
\begin{split}
a_j \prod_{l,m} \left(1 + \frac{1 }{2 } f_{l,m} a_l^\dag a_m^\dag \right) \Ket{0_a }
&=\left[a_j , \prod_{l,m} \left(1 + \frac{1 }{2 } f_{l,m} a_l^\dag a_m^\dag \right) \right] \Ket{0_a } + \prod_{l,m} \left(1 + \frac{1 }{2 } f_{l,m} a_l^\dag a_m^\dag \right) a_j \Ket{0_a } \\
&=\left[a_j , \prod_{l,m} \left(1 + \frac{1 }{2 } f_{l,m} a_l^\dag a_m^\dag \right) \right] \Ket{0_a } \\
&=\sum_{l',m'} \left[a_j , 1 + \frac{1 }{2 } f_{l',m'} a_{l'}^\dag a_{m'}^\dag \right] \prod_{(l,m)\setminus (l',m')} \left(1 + \frac{1 }{2 } f_{l,m} a_l^\dag a_m^\dag \right) a_j \Ket{0_a } \\
&=\sum_{l',m'} \frac{1 }{2 } f_{l',m'} \left(\delta_{j,l'} a_{m'}^\dag - \delta_{j,m'} a_{l'}^\dag \right) \prod_{(l,m)\setminus (l',m')} \left(1 + \frac{1 }{2 } f_{l,m} a_l^\dag a_m^\dag \right) a_j \Ket{0_a } \\
&=\sum_{l',m'} \frac{1 }{2 } f_{l',m'} \left(\delta_{j,l'} a_{m'}^\dag - \delta_{j,m'} a_{l'}^\dag \right) \cdot \left(1 + \frac{1 }{2 } f_{l',m'} a_{l'}^\dag a_{m'}^\dag \right) \prod_{(l,m)\setminus (l',m')} \left(1 + \frac{1 }{2 } f_{l,m} a_l^\dag a_m^\dag \right) a_j \Ket{0_a } \\
&=\sum_{l',m'} \frac{1 }{2 } f_{l',m'} \left(\delta_{j,l'} a_{m'}^\dag - \delta_{j,m'} a_{l'}^\dag \right) \prod_{l,m} \left(1 + \frac{1 }{2 } f_{l,m} a_l^\dag a_m^\dag \right) a_j \Ket{0_a } \\
&=\left[\sum_{m'} \frac{1 }{2 } f_{j,m'} a_{m'}^\dag - \sum_{l'} \frac{1 }{2 } f_{l',j} a_{l'}^\dag \right] \prod_{l,m} \left(1 + \frac{1 }{2 } f_{l,m} a_l^\dag a_m^\dag \right) a_j \Ket{0_a } \\
&=\left[\sum_{m'} \frac{1 }{2 } f_{j,m'} a_{m'}^\dag + \sum_{l'} \frac{1 }{2 } f_{j,l'} a_{l'}^\dag \right] \prod_{l,m} \left(1 + \frac{1 }{2 } f_{l,m} a_l^\dag a_m^\dag \right) a_j \Ket{0_a } \\
&=\sum_{k} f_{j,k} a_{k}^\dag \prod_{l,m} \left(1 + \frac{1 }{2 } f_{l,m} a_l^\dag a_m^\dag \right) a_j \Ket{0_a } \\
\end{split}
\end{equation}
$$

于是 $a_j $ 对 $\Ket{\Omega } $ 的作用为

$$
\begin{equation}
\begin{split}
a_j \Ket{\Omega }
&=\mathcal{N} a_j \prod_{l,m} \left(1 + \frac{1 }{2 } f_{l,m} a_l^\dag a_m^\dag \right) \Ket{0_a } \\
&=\mathcal{N} \sum_{k} f_{j,k} a_{k}^\dag \prod_{l,m} \left(1 + \frac{1 }{2 } f_{l,m} a_l^\dag a_m^\dag \right) a_j \Ket{0_a } \\
&=\sum_{k} f_{j,k} a_k^\dag \Ket{\Omega }
\end{split}
\end{equation}
$$

基态由

$$
\begin{equation}
\alpha_i \Ket{\Omega }
=0
\end{equation}
$$

确定，也即

$$
\begin{equation}
\sum_{j=1}^{N} \left(w_{ji}^* a_j + v_{ji}^* a^\dag_j \right) \Ket{\Omega }
=0
\end{equation}
$$

把 $a_j \Ket{\Omega } $ 代入：

$$
\begin{equation}
\begin{split}
0
&=\sum_{j=1}^{N} \left(w_{ji}^* a_j + v_{ji}^* a^\dag_j \right) \Ket{\Omega } \\
&=\sum_{j=1}^{N} \left(w_{ji}^* \sum_{k} f_{j,k} a_k^\dag + v_{ji}^* a^\dag_j \right) \Ket{\Omega } \\
&=\sum_{j=1}^{N} \left(w_{ji}^* \sum_{k} f_{j,k} a_k^\dag + v_{ji}^* \sum_{k} \delta_{j,k} a^\dag_k \right) \Ket{\Omega } \\
&=\sum_{j=1}^{N} \left(\sum_{k} w_{ji}^* f_{j,k} a_k^\dag + \sum_{k} v_{ji}^* \delta_{j,k} a^\dag_k \right) \Ket{\Omega } \\
&=\sum_{j=1}^{N} \sum_{k} \left(w_{ji}^* f_{j,k} a_k^\dag + v_{ji}^* \delta_{j,k} a^\dag_k \right) \Ket{\Omega } \\
&=\sum_{k} \sum_{j=1}^{N} \left(w_{ji}^* f_{j,k} a_k^\dag + v_{ji}^* \delta_{j,k} a^\dag_k \right) \Ket{\Omega } \\
&=\sum_{k} \left[ \sum_{j=1}^{N} \left(w_{ji}^* f_{j,k} + v_{ji}^* \delta_{j,k} \right) \right] a^\dag_k \Ket{\Omega } \\
\end{split}
\end{equation}
$$

因此有

$$
\begin{equation}
\sum_{j=1}^{N} \left(w_{ji}^* f_{j,k} + v_{ji}^* \delta_{j,k} \right)
=0,\quad \forall i,k
\end{equation}
$$

利用 $f_{j,k} $ 的反对称性有

$$
\begin{equation}
\sum_{j=1}^{N} \left(-f_{k,j} w_{ji}^* + \delta_{k,j} v_{ji}^* \right)
=0,\quad \forall i,k
\end{equation}
$$

构造 $\bold{f} $ 矩阵：

$$
\begin{equation}
\bold{f}
=\begin{pmatrix}
f_{1,1} &f_{1,2} &\cdots \\
f_{2,1} &\ddots &\vdots \\
\vdots &\cdots &\ddots
\end{pmatrix}
\end{equation}
$$

则化为

$$
\begin{equation}
-\left(\bold{f} \bold{w}^* \right)_{k,i} + \left(\bold{I} \bold{v}^* \right)_{k,i}
=0,\quad \forall i,k
\end{equation}
$$

也即矩阵方程

$$
\begin{equation}
\bold{f} \bold{w}^* = \bold{v}^*
\end{equation}
$$

于是

$$
\begin{equation}
\bold{f}
=\bold{v}^*\left(\bold{w}^* \right)^{-1}
\end{equation}
$$