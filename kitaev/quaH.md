Kitaev 蜂窝模型中，对于一个确定的构型 $\left\{u_{jk} \right\} $ 来说，哈密顿量为

$$
\begin{align}
H
=\frac{\mathrm{i} }{4 } \sum_{j,k} A_{jk} c_j c_k,
\end{align}
$$

两个初基平移矢量分别记为 $\vec{a}_1,\vec{a}_2 $，设沿 $\vec{a}_1 $ 方向有 $N_1 $ 个unit cell，沿 $\vec{a}_2 $ 方向有 $N_2 $ 个 unit cell，则共有 $N=N_1 N_2 $ 个 unit cell，共有 $2N $ 个格点。

所有格点可分为 $A,B $ 子格。$B $ 子格的三条 bond 构成一个 "Y"，则形式上哈密顿量可写成

$$
\begin{align}
H
=\frac{\mathrm{i} }{4 }
\begin{bmatrix}
c_{1,A} &\cdots &c_{N,A} &c_{1,B} &\cdots c_{N,B}
\end{bmatrix}
\left[H \right]_{2N \times 2N}
\begin{bmatrix}
c_{1,A} \\
\cdots \\
c_{N,A} \\
c_{1,B} \\
\cdots \\
c_{N,B}
\end{bmatrix}
\end{align}
$$

考虑构型 $\left\{u_{jk}=1\right\} $，其中 $j $ 属于 $A $ 子格，$k $ 属于 $B $ 子格，那么 $\left[H \right]_{2N \times 2N} $ 的具体形式为？