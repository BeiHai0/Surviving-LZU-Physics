标准规范 $\left\{u_{ij}=+1 \right\} $ 下，哈密顿量

$$
\begin{equation}
\begin{aligned}
H(0)
&=\frac{1 }{2 }
\begin{pmatrix}
a^\dag &a^\top
\end{pmatrix}
h(0)
\begin{pmatrix}
a \\
\left(a^\dag \right)^\top
\end{pmatrix} \\
&=\frac{1 }{2 }
\begin{pmatrix}
a^\dag &a^\top
\end{pmatrix}
U(0) D(0) U^\dag(0)
\begin{pmatrix}
a \\
\left(a^\dag \right)^\top
\end{pmatrix} \\
&=\frac{1 }{2 }
\begin{pmatrix}
\alpha^\dag(0) &\alpha^\top(0)
\end{pmatrix}
D(0)
\begin{pmatrix}
\alpha(0) \\
\left(\alpha^\dag(0) \right)^\top
\end{pmatrix}
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
U(0)
=\begin{pmatrix}
W(0) &V^*(0) \\
V(0) &W^*(0)
\end{pmatrix},\quad
D(0)
=\mathrm{diag}(E_1(0),\cdots,E_N(0),-E_1(0),\cdots,-E_N(0))
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
\begin{pmatrix}
\alpha(0) \\
\left(\alpha^\dag(0) \right)^\top
\end{pmatrix}
=U^\dag(0)
\begin{pmatrix}
a \\
\left(a^\dag \right)^\top
\end{pmatrix},\quad
\begin{pmatrix}
\alpha^\dag(0) &\alpha^\top(0)
\end{pmatrix}
=\begin{pmatrix}
a^\dag &a^\top
\end{pmatrix}
U(0)
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{pmatrix}
a \\
\left(a^\dag \right)^\top
\end{pmatrix}
=U(0)
\begin{pmatrix}
\alpha(0) \\
\left(\alpha^\dag(0) \right)^\top
\end{pmatrix},\quad
\begin{pmatrix}
a^\dag &a^\top 
\end{pmatrix}
=\begin{pmatrix}
\alpha^\dag(0) &\alpha^\top(0)
\end{pmatrix}
U^\dag(0)
\end{equation}
$$

则 $H(0) $ 的基态是 $\alpha(0) $ 的真空态 $\Ket{0_{\alpha(0)} } $，可以由 $a $ 的真空 $\Ket{0_a } $ 生成：

$$
\begin{equation}
\Ket{0_{\alpha(0)} }
=\mathcal{N}(0) \exp\left(\frac{1 }{2 } \sum_{i,j} F_{i,j}(0) a_i^\dag a_j^\dag \right) \Ket{0_a }
\end{equation}
$$

$$
\begin{equation}
F(0)
=V(0)^* \left[W^*(0) \right]^{-1}
\end{equation}
$$

$$
\begin{equation}
\mathcal{N}(0)
=\mathrm{det}^{-1/4} \left(I + F^\dag(0) F(0) \right)
\end{equation}
$$

#### 

考虑构型 $\left\{u_{ij} \right\} $ 下，哈密顿量

$$
\begin{equation}
\begin{aligned}
H
&=\frac{1 }{2 }
\begin{pmatrix}
a^\dag &a^\top
\end{pmatrix}
h
\begin{pmatrix}
a \\
\left(a^\dag \right)^\top
\end{pmatrix} \\
&=\frac{1 }{2 }
\begin{pmatrix}
a^\dag &a^\top
\end{pmatrix}
U D U^\dag
\begin{pmatrix}
a \\
\left(a^\dag \right)^\top
\end{pmatrix} \\
&=\frac{1 }{2 }
\begin{pmatrix}
\alpha^\dag(0) &\alpha^\top(0)
\end{pmatrix}
U^\dag(0) U D U^\dag U(0)
\begin{pmatrix}
\alpha(0) \\
\left(\alpha^\dag(0) \right)^\top
\end{pmatrix} \\
&\equiv \frac{1 }{2 }
\begin{pmatrix}
\alpha^\dag(0) &\alpha^\top(0)
\end{pmatrix}
\widetilde{U} D \widetilde{U}^\dag
\begin{pmatrix}
\alpha(0) \\
\left(\alpha^\dag(0) \right)^\top
\end{pmatrix} \\
&\equiv \frac{1 }{2 }
\begin{pmatrix}
\alpha^\dag &\alpha^\top
\end{pmatrix}
D 
\begin{pmatrix}
\alpha \\
\left(\alpha^\dag \right)^\top
\end{pmatrix} \\
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\widetilde{U}
\equiv U^\dag(0) U,\quad
\widetilde{U}^\dag
=U^\dag U(0)
\end{equation}
$$

$$
\begin{equation}
\widetilde{U}
=\begin{pmatrix}
\widetilde{W} &\widetilde{V}^* \\
\widetilde{V} &\widetilde{W}^*
\end{pmatrix},\quad
\widetilde{U}^\dag
=\begin{pmatrix}
\widetilde{W}^\dag &\widetilde{V}^\dag \\
\widetilde{V}^\top &\widetilde{W}^\top 
\end{pmatrix}
\end{equation}
$$

$$
\begin{equation}
\begin{pmatrix}
\alpha^\dag &\alpha^\top
\end{pmatrix}
=\begin{pmatrix}
\alpha^\dag(0) &\alpha^\top(0)
\end{pmatrix}
\widetilde{U}
=\begin{pmatrix}
\alpha^\dag(0) &\alpha^\top(0)
\end{pmatrix}
\begin{pmatrix}
\widetilde{W} &\widetilde{V}^* \\
\widetilde{V} &\widetilde{W}^*
\end{pmatrix},\quad
\end{equation}
$$

$$
\begin{equation}
\begin{pmatrix}
\alpha \\
\left(\alpha^\dag \right)^\top
\end{pmatrix}
=\widetilde{U}^\dag 
\begin{pmatrix}
\alpha(0) \\
\left(\alpha^\dag(0) \right)^\top
\end{pmatrix}
=\begin{pmatrix}
\widetilde{W}^\dag &\widetilde{V}^\dag \\
\widetilde{V}^\top &\widetilde{W}^\top 
\end{pmatrix}
\begin{pmatrix}
\alpha(0) \\
\left(\alpha^\dag(0) \right)^\top
\end{pmatrix}
\end{equation}
$$

$H $ 的基态是 $\alpha $ 的真空态 $\Ket{0_\alpha } $，可以由 $\alpha(0) $ 的真空态 $\Ket{0_{\alpha(0)} } $ 生成：

$$
\begin{equation}
\Ket{0_\alpha }
=\widetilde{\mathcal{N}} \exp\left(\frac{1 }{2 } \sum_{i,j} \widetilde{F}_{i,j} \alpha_i^\dag(0) \alpha_j^\dag(0) \right) \Ket{0_{\alpha(0)} }
\end{equation}
$$

$$
\begin{equation}
\widetilde{F}
=\widetilde{V}^* \left(\widetilde{W}^* \right)^{-1}
\end{equation}
$$

$$
\begin{equation}
\widetilde{\mathcal{N}}
=\mathrm{det}^{-1/4}\left(I + \widetilde{F}^\dag \widetilde{F} \right)
\end{equation}
$$

实际上 $\widetilde{\mathcal{N}} $ 可以化简。

$$
\begin{equation}
\widetilde{N}
=\left|\mathrm{det}\left(\widetilde{W} \right) \right|^{1/2}
\end{equation}
$$

#### c-Majorana如何换成 $\alpha(0) $

$$
\begin{equation}
c_{i,A}
=a_{i} + a^\dag_{i},\quad
c_{i,B}
=\frac{1 }{\mathrm{i} } \left(a_{i} - a^\dag_{i} \right),
\end{equation}
$$

$$
\begin{equation}
\begin{pmatrix}
a \\
\left(a^\dag \right)^\top
\end{pmatrix}
=U(0)
\begin{pmatrix}
\alpha(0) \\
\left(\alpha^\dag(0) \right)^\top
\end{pmatrix}
\end{equation}
$$

$$
\begin{equation}
U(0)
=\begin{pmatrix}
\bold{W}(0) &\bold{V}^*(0) \\
\bold{V}(0) &\bold{W}^*(0)
\end{pmatrix}
\end{equation}
$$

$$
\begin{equation}
a_i = \frac{1 }{2 } \left(c_{i,A} + \mathrm{i}c_{i,B} \right),\quad
a_i^\dag = \frac{1 }{2 } \left(c_{i,A} - \mathrm{i}c_{i,B} \right)
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
a
\equiv \begin{pmatrix}
a_1 \\
\vdots \\
a_N
\end{pmatrix}
=\frac{1 }{2 } c_A + \frac{\mathrm{i} }{2 } c_B
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\left(a^\dag \right)^\top
=\frac{1 }{2 } c_A - \frac{\mathrm{i} }{2 } c_B
\end{equation}
$$

一方面

$$
\begin{equation}
\begin{aligned}
\begin{pmatrix}
a \\
\left(a^\dag \right)^\top
\end{pmatrix}
=\begin{pmatrix}
\frac{1 }{2 } I &\frac{\mathrm{i} }{2 } I \\[1mm]
\frac{1 }{2 } I &-\frac{\mathrm{i} }{2 } I
\end{pmatrix}
\begin{pmatrix}
c_A \\
c_B
\end{pmatrix}
\end{aligned}
\end{equation}
$$

另一方面

$$
\begin{equation}
\begin{pmatrix}
a \\
\left(a^\dag \right)^\top
\end{pmatrix}
=U(0)
\begin{pmatrix}
\alpha(0) \\
\left(\alpha^\dag(0) \right)^\top
\end{pmatrix}
\end{equation}
$$

$$
\begin{equation}
U(0)
=\begin{pmatrix}
\bold{W}(0) &\bold{V}^*(0) \\
\bold{V}(0) &\bold{W}^*(0)
\end{pmatrix}
\end{equation}
$$

于是

$$
\begin{equation}
\begin{aligned}
\begin{pmatrix}
c_A \\
c_B
\end{pmatrix}
&=\begin{pmatrix}
\frac{1 }{2 } I &\frac{\mathrm{i} }{2 } I \\[1mm]
\frac{1 }{2 } I &-\frac{\mathrm{i} }{2 } I
\end{pmatrix}^{-1}
\begin{pmatrix}
\bold{W}(0) &\bold{V}^*(0) \\
\bold{V}(0) &\bold{W}^*(0)
\end{pmatrix}
\begin{pmatrix}
\alpha(0) \\
\left(\alpha^\dag(0) \right)^\top
\end{pmatrix}
=\begin{pmatrix}
I &I \\[1mm]
-\mathrm{i} I &\mathrm{i} I
\end{pmatrix}
\begin{pmatrix}
\bold{W}(0) &\bold{V}^*(0) \\
\bold{V}(0) &\bold{W}^*(0)
\end{pmatrix}
\begin{pmatrix}
\alpha(0) \\
\left(\alpha^\dag(0) \right)^\top
\end{pmatrix} \\
&\equiv U'(0)
\begin{pmatrix}
\alpha(0) \\
\left(\alpha^\dag(0) \right)^\top
\end{pmatrix}
=\begin{pmatrix}
W(0) + V(0) &V^*(0) + W^*(0) \\
\mathrm{i}\left(-W(0) + V(0) \right) &\mathrm{i}\left(-V^*(0) + W^*(0) \right)
\end{pmatrix}
\begin{pmatrix}
\alpha(0) \\
\left(\alpha^\dag(0) \right)^\top
\end{pmatrix} \\
&\equiv \begin{pmatrix}
\bold{U}_{11}'(0) &\bold{U}_{12}'(0) \\
\bold{U}_{21}'(0) &\bold{U}_{22}'(0)
\end{pmatrix}
\begin{pmatrix}
\alpha(0) \\
\left(\alpha^\dag(0) \right)^\top
\end{pmatrix}
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\boxed{
c_{i,A}
=U'_{i,}(0)
\begin{pmatrix}
\alpha(0) \\
\left(\alpha^\dag(0) \right)^\top
\end{pmatrix}
=\bold{U}_{11}'(0)_{i,} \alpha(0) + \bold{U}_{12}'(0)_{i,} \left(\alpha^\dag(0) \right)^\top
}
\end{equation}
$$

$$
\begin{equation}
\boxed{
c_{i,A}=c_{i,A}^\dag
=\alpha^\dag(0) \left[\bold{U}_{11}'(0)_{i,} \right]^\dag + \alpha^\top(0) \left[\bold{U}_{12}'(0)_{i,} \right]^\dag
}
\end{equation}
$$

$$
\begin{equation}
\boxed{
c_{j,B}
=U'_{j+N,}(0)
\begin{pmatrix}
\alpha(0) \\
\left(\alpha^\dag(0) \right)^\top
\end{pmatrix}
=\bold{U}_{21}'(0)_{j,} \alpha(0) + \bold{U}_{22}'(0)_{j,} \left(\alpha^\dag(0) \right)^\top
}
\end{equation}
$$

$$
\begin{equation}
\boxed{
c_{j,B}
=c_{j,B}^\dag
=\alpha^\dag(0) \left[\bold{U}_{21}'(0)_{j,} \right]^\dag + \alpha^\top(0) \left[\bold{U}_{22}'(0)_{j,} \right]^\dag
}
\end{equation}
$$

#### 跃迁振幅

$$
\begin{equation}
\begin{aligned}
&\Braket{0_\chi , 0_{\alpha(1)} | d_{\bm{r},x}(1) H_h d^\dag_{\bm{r},y}(2) | 0_\chi , 0_{\alpha(2)} } \\
=&\Braket{\chi(\bm{r},x) , 0_{\alpha(1)} | \alpha(1) \left[-h_z \left(\sigma_{\bm{r}}^z + \sigma_{\bm{r}+\bm{\delta}_z}^z \right) \right] \alpha^\dag(2) | \chi(\bm{r},y) , 0_{\alpha(2)} } \\
=&-h_z\Braket{\chi(\bm{r},x) , 0_{\alpha(1)} | \alpha(1) \left(\sigma_{\bm{r}}^z + \sigma_{\bm{r}+\bm{\delta}_z}^z \right)  \alpha^\dag(2) | \chi(\bm{r},y) , 0_{\alpha(2)} } \\
=&-h_z\Braket{\chi , 0_{\alpha(1)} | \alpha(1) \left[-\mathrm{i}\left(1 + \mathrm{i} c_{i,A} c_{j,B} \right) \right] \alpha^\dag(2) | \chi , 0_{\alpha(2)} } \\
=&\mathrm{i} h_z\Braket{\chi , 0_{\alpha(1)} | \alpha(1) \left(1 + \mathrm{i} c_{i,A} c_{j,B} \right) \alpha^\dag(2) | \chi , 0_{\alpha(2)} } \\
=&\mathrm{i} h_z \widetilde{\mathcal{N}}(1) \widetilde{\mathcal{N}}(2) \Braket{\chi , 0_{\alpha(0)} | \exp\left(\frac{1 }{2 } F_{i,j}^*(1) \alpha_i(0) \alpha_j(0) \right) \alpha(1) \left(1 + \mathrm{i} c_{i,A} c_{j,B} \right) \alpha^\dag(2) \exp\left(\frac{1 }{2 } \sum_{i,j} F_{i,j}(2) \alpha_i^\dag(0) \alpha_j^\dag(0) \right) | \chi , 0_{\alpha(0)}} \\
\equiv&\mathrm{i} h_z\Braket{\Psi(1) | \alpha(1) \left(1 + \mathrm{i} c_{i,A} c_{j,B} \right) \alpha^\dag(2) |\Psi(2) } \\
=&\mathrm{i} h_z \Braket{\Psi(1) | \Psi(2) } \langle \alpha(1) \left(1 + \mathrm{i} c_{i,A} c_{j,B} \right) \alpha^\dag(2) \rangle \\
=&h_z \langle \Psi(1) | \Psi(2) \rangle \left[\mathrm{i} \langle \alpha(1) \alpha^\dag(2) \rangle - \langle \alpha(1) c_{i,A} c_{j,B} \alpha^\dag(2) \rangle \right]
\end{aligned}
\end{equation}
$$

- $\Braket{\Psi(1) | \Psi(2) } $

$$
\begin{equation}
\begin{aligned}
\Braket{\Psi(1) | \Psi(2) }
=\widetilde{N}(1) \widetilde{N}(2) \left(-1 \right)^{N(N+1)/2} \mathrm{Pf}(M)
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
M
\equiv \begin{pmatrix}
\widetilde{F}(2) &-I \\
I &-\widetilde{F}^*(1)
\end{pmatrix}
\end{equation}
$$

$$
\begin{equation}
\widetilde{N}
=\left|\mathrm{det}\left(\widetilde{W} \right) \right|^{1/2}
\end{equation}
$$

$$
\begin{equation}
\widetilde{F}
=\widetilde{V}^* \left(\widetilde{W}^* \right)^{-1}
\end{equation}
$$

$$
\begin{equation}
\widetilde{U}
\equiv U^\dag(0) U,\quad
\widetilde{U}^\dag
=U^\dag U(0)
\end{equation}
$$

$$
\begin{equation}
\widetilde{U}
=\begin{pmatrix}
\widetilde{W} &\widetilde{V}^* \\
\widetilde{V} &\widetilde{W}^*
\end{pmatrix},\quad
\widetilde{U}^\dag
=\begin{pmatrix}
\widetilde{W}^\dag &\widetilde{V}^\dag \\
\widetilde{V}^\top &\widetilde{W}^\top 
\end{pmatrix}
\end{equation}
$$

- $\langle \alpha(1) \alpha^\dag(2) \rangle $

$$
\begin{equation}
\begin{pmatrix}
\alpha(1) \\
\left(\alpha^\dag(1) \right)^\top
\end{pmatrix}
=\widetilde{U}^\dag(1)
\begin{pmatrix}
\alpha(0) \\
\left(\alpha^\dag(0) \right)^\top
\end{pmatrix}
=\begin{pmatrix}
\widetilde{W}^\dag(1) &\widetilde{V}^\dag(1) \\
\widetilde{V}^\top(1) &\widetilde{W}^\top(1)
\end{pmatrix}
\begin{pmatrix}
\alpha(0) \\
\left(\alpha^\dag(0) \right)^\top
\end{pmatrix}
\end{equation}
$$

$$
\begin{equation}
\boxed{
\alpha(1)
=\widetilde{W}^\dag(1) \alpha(0) + \widetilde{V}^\dag(1) \left(\alpha^\dag(0) \right)^\top
}
\end{equation}
$$

$$
\begin{equation}
\begin{pmatrix}
\alpha^\dag(2) &\alpha^\top(2)
\end{pmatrix}
=\begin{pmatrix}
\alpha^\dag(0) &\alpha^\top(0)
\end{pmatrix}
\widetilde{U}(2)
=\begin{pmatrix}
\alpha^\dag(0) &\alpha^\top(0)
\end{pmatrix}
\begin{pmatrix}
\widetilde{W}(2) &\widetilde{V}^*(2) \\
\widetilde{V}(2) &\widetilde{W}^*(2)
\end{pmatrix},\quad
\end{equation}
$$

$$
\begin{equation}
\boxed{
\alpha^\dag(2)
=\alpha^\dag(0) \widetilde{W}(2) + \alpha^\top(0) \widetilde{V}(2)
}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
&\Braket{\alpha(1) \alpha^\dag(2) } \\
=&\Braket{\left[\widetilde{W}^\dag(1) \alpha(0) + \widetilde{V}^\dag(1) \left(\alpha^\dag(0) \right)^\top \right] \left[\alpha^\dag(0) \widetilde{W}(2) + \alpha^\top(0) \widetilde{V}(2) \right] } \\
=&\Braket{
    \begin{pmatrix}
    \widetilde{V}^\dag(1) &\widetilde{W}^\dag(1)
    \end{pmatrix}
    \begin{pmatrix}
    \left(\alpha^\dag(0) \right)^\top \\
    \alpha(0)
    \end{pmatrix}
    \begin{pmatrix}
    \alpha^\dag(0) &\alpha^\top(0)
    \end{pmatrix}
    \begin{pmatrix}
    \widetilde{W}(2) \\
    \widetilde{V}(2)
    \end{pmatrix}
 } \\
=&\begin{pmatrix}
\widetilde{V}^\dag(1) &\widetilde{W}^\dag(1)
\end{pmatrix}
\Braket{
    \begin{pmatrix}
    \left(\alpha^\dag(0) \right)^\top \alpha^\dag(0) &\left(\alpha^\dag(0) \right)^\top \alpha^\top(0) \\
    \alpha(0) \alpha^\dag(0) &\alpha(0) \alpha^\top(0)
    \end{pmatrix}
 }
\begin{pmatrix}
\widetilde{W}(2) \\
\widetilde{V}(2)
\end{pmatrix} \\
=&\begin{pmatrix}
\widetilde{V}^\dag(1) &\widetilde{W}^\dag(1)
\end{pmatrix}
\left(-M^{-1} +
\begin{pmatrix}
0 &I \\
0 &0
\end{pmatrix} \right)
\begin{pmatrix}
\widetilde{W}(2) \\
\widetilde{V}(2)
\end{pmatrix}
\end{aligned}
\end{equation}
$$

- $\langle \alpha(1) c_{i,A} c_{j,B} \alpha^\dag(2) \rangle $

Wick定理给出

$$
\begin{equation}
\begin{aligned}
&\Braket{\alpha(1) c_{i,A} c_{j,B} \alpha^\dag(2) } \\
=&\Braket{\alpha(1) c_{i,A} }\Braket{c_{j,B} \alpha^\dag(2) } - \Braket{\alpha(1) c_{j,B} }\Braket{c_{i,A} \alpha^\dag(2) } + \Braket{\alpha(1) \alpha^\dag(2) }\Braket{c_{i,A} c_{j,B} }
\end{aligned}
\end{equation}
$$

- - $\Braket{\alpha(1) c_{i,A} } $

$$
\begin{equation}
\boxed{
\alpha(1)
=\widetilde{W}^\dag(1) \alpha(0) + \widetilde{V}^\dag(1) \left(\alpha^\dag(0) \right)^\top
}
\end{equation}
$$

$$
\begin{equation}
\boxed{
c_{i,A}=c_{i,A}^\dag
=\alpha^\dag(0) \left[\bold{U}_{11}'(0)_{i,} \right]^\dag + \alpha^\top(0) \left[\bold{U}_{12}'(0)_{i,} \right]^\dag
}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
&\Braket{\alpha(1) c_{i,A} } \\
=&\Braket{\left\{\widetilde{W}^\dag(1) \alpha(0) + \widetilde{V}^\dag(1) \left(\alpha^\dag(0) \right)^\top \right\} \left\{\alpha^\dag(0) \left[\bold{U}_{11}'(0)_{i,} \right]^\dag + \alpha(0)^\top\left[\bold{U}_{12}'(0)_{i,} \right]^\dag \right\} } \\
=&\begin{pmatrix}
\widetilde{V}^\dag(1) &\widetilde{W}^\dag(1)
\end{pmatrix}
\Braket{
    \begin{pmatrix}
    \left(\alpha^\dag(0) \right)^\top \\
    \alpha(0)
    \end{pmatrix}
    \begin{pmatrix}
    \alpha^\dag(0) &\alpha^\top(0)
    \end{pmatrix}
 }
\begin{pmatrix}
\left[\bold{U}_{11}'(0)_{i,} \right]^\dag \\
\left[\bold{U}_{12}'(0)_{i,} \right]^\dag
\end{pmatrix} \\
=&\begin{pmatrix}
\widetilde{V}^\dag(1) &\widetilde{W}^\dag(1)
\end{pmatrix}
\left(-M^{-1} + 
\begin{pmatrix}
0 &I \\
0 &0
\end{pmatrix} \right)
\begin{pmatrix}
\left[\bold{U}_{11}'(0)_{i,} \right]^\dag \\
\left[\bold{U}_{12}'(0)_{i,} \right]^\dag
\end{pmatrix} \\
\end{aligned}
\end{equation}
$$

- - $\Braket{\alpha(1) c_{j,B} } $

$$
\begin{equation}
\boxed{
\alpha(1)
=\widetilde{W}^\dag(1) \alpha(0) + \widetilde{V}^\dag(1) \left(\alpha^\dag(0) \right)^\top
}
\end{equation}
$$

$$
\begin{equation}
\boxed{
c_{j,B}
=c_{j,B}^\dag
=\alpha^\dag(0) \left[\bold{U}_{21}'(0)_{j,} \right]^\dag + \alpha^\top(0) \left[\bold{U}_{22}'(0)_{j,} \right]^\dag
}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
&\Braket{\alpha(1) c_{j,B} } \\
=&\Braket{\left\{\widetilde{W}^\dag(1) \alpha(0) + \widetilde{V}^\dag(1) \left(\alpha^\dag(0) \right)^\top \right\} \left\{\alpha^\dag(0) \left[\bold{U}_{21}'(0)_{j,} \right]^\dag + \alpha^\top(0) \left[\bold{U}_{22}'(0)_{j,} \right]^\dag \right\} } \\
=&\begin{pmatrix}
\widetilde{V}^\dag(1) &\widetilde{W}^\dag(1)
\end{pmatrix}
\Braket{
    \begin{pmatrix}
    \left(\alpha^\dag(0) \right)^\top \\
    \alpha(0)
    \end{pmatrix}
    \begin{pmatrix}
    \alpha^\dag(0) &\alpha^\top(0)
    \end{pmatrix}
 }
\begin{pmatrix}
\left[\bold{U}_{21}'(0)_{j,} \right]^\dag \\
\left[\bold{U}_{22}'(0)_{j,} \right]^\dag
\end{pmatrix} \\
=&\begin{pmatrix}
\widetilde{V}^\dag(1) &\widetilde{W}^\dag(1)
\end{pmatrix}
\left(-M^{-1} + 
\begin{pmatrix}
0 &I \\
0 &0
\end{pmatrix} \right)
\begin{pmatrix}
\left[\bold{U}_{21}'(0)_{j,} \right]^\dag \\
\left[\bold{U}_{22}'(0)_{j,} \right]^\dag
\end{pmatrix} \\
\end{aligned}
\end{equation}
$$

- - $\Braket{c_{i,A} \alpha^\dag(2) } $

$$
\begin{equation}
\boxed{
\alpha^\dag(2)
=\alpha^\dag(0) \widetilde{W}(2) + \alpha^\top(0) \widetilde{V}(2)
}
\end{equation}
$$

$$
\begin{equation}
\boxed{
c_{i,A}
=U'_{i,}(0)
\begin{pmatrix}
\alpha(0) \\
\left(\alpha^\dag(0) \right)^\top
\end{pmatrix}
=\bold{U}_{11}'(0)_{i,} \alpha(0) + \bold{U}_{12}'(0)_{i,} \left(\alpha^\dag(0) \right)^\top
}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
&\Braket{c_{i,A} \alpha^\dag(2) } \\
=&\Braket{\left\{\bold{U}_{11}'(0)_{i,} \alpha(0) + \bold{U}'_{12}(0)_{i,} \left(\alpha^\dag(0) \right)^\top \right\} \left\{\alpha^\dag(0) \widetilde{W}(2) + \alpha^\top(0) \widetilde{V}(2) \right\} } \\
=&\begin{pmatrix}
\bold{U}'_{12}(0)_{i,} &\bold{U}'_{11}(0)_{i,}
\end{pmatrix}
\Braket{
    \begin{pmatrix}
    \left(\alpha^\dag(0) \right)^\top \\
    \alpha(0)
    \end{pmatrix}
    \begin{pmatrix}
    \alpha^\dag(0) &\alpha^\top(0)
    \end{pmatrix}
}
\begin{pmatrix}
\widetilde{W}(2) \\
\widetilde{V}(2)
\end{pmatrix} \\
=&\begin{pmatrix}
\bold{U}'_{12}(0)_{i,} &\bold{U}'_{11}(0)_{i,}
\end{pmatrix}
\left(-M^{-1} + 
\begin{pmatrix}
0 &I \\
0 &0
\end{pmatrix} \right)
\begin{pmatrix}
\widetilde{W}(2) \\
\widetilde{V}(2)
\end{pmatrix}
\end{aligned}
\end{equation}
$$

- - $\Braket{c_{j,B} \alpha^\dag(2) } $

$$
\begin{equation}
\boxed{
\alpha^\dag(2)
=\alpha^\dag(0) \widetilde{W}(2) + \alpha^\top(0) \widetilde{V}(2)
}
\end{equation}
$$

$$
\begin{equation}
\boxed{
c_{j,B}
=U'_{j+N,}(0)
\begin{pmatrix}
\alpha(0) \\
\left(\alpha^\dag(0) \right)^\top
\end{pmatrix}
=\bold{U}_{21}'(0)_{j,} \alpha(0) + \bold{U}_{22}'(0)_{j,} \left(\alpha^\dag(0) \right)^\top
}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
&\Braket{c_{j,B} \alpha^\dag(2) } \\
=&\Braket{\left\{\bold{U}_{21}'(0)_{j,} \alpha(0) + \bold{U}_{22}'(0)_{j,} \left(\alpha^\dag(0) \right)^\top \right\} \left\{\alpha^\dag(0) \widetilde{W}(2) + \alpha^\top(0) \widetilde{V}(2) \right\} } \\
=&\begin{pmatrix}
\bold{U}'_{22}(0)_{j,} &\bold{U}'_{21}(0)_{j,}
\end{pmatrix}
\Braket{
    \begin{pmatrix}
    \left(\alpha^\dag(0) \right)^\top \\
    \alpha(0)
    \end{pmatrix}
    \begin{pmatrix}
    \alpha^\dag(0) &\alpha^\top(0)
    \end{pmatrix}
}
\begin{pmatrix}
\widetilde{W}(2) \\
\widetilde{V}(2)
\end{pmatrix} \\
=&\begin{pmatrix}
\bold{U}'_{22}(0)_{j,} &\bold{U}'_{21}(0)_{j,}
\end{pmatrix}
\left(-M^{-1} + 
\begin{pmatrix}
0 &I \\
0 &0
\end{pmatrix} \right)
\begin{pmatrix}
\widetilde{W}(2) \\
\widetilde{V}(2)
\end{pmatrix}
\end{aligned}
\end{equation}
$$

- - $\Braket{c_{i,A} c_{j,B} } $

$$
\begin{equation}
\boxed{
c_{i,A}
=U'_{i,}(0)
\begin{pmatrix}
\alpha(0) \\
\left(\alpha^\dag(0) \right)^\top
\end{pmatrix}
=\bold{U}_{11}'(0)_{i,} \alpha(0) + \bold{U}_{12}'(0)_{i,} \left(\alpha^\dag(0) \right)^\top
}
\end{equation}
$$

$$
\begin{equation}
\boxed{
c_{j,B}
=c_{j,B}^\dag
=\alpha^\dag(0) \left[\bold{U}_{21}'(0)_{j,} \right]^\dag + \alpha^\top(0) \left[\bold{U}_{22}'(0)_{j,} \right]^\dag
}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
&\Braket{c_{i,A} c_{j,B} } \\
=&\Braket{\left\{\bold{U}_{11}'(0)_{i,} \alpha(0) + \bold{U}_{12}'(0)_{i,} \left(\alpha^\dag(0) \right)^\top \right\} \left\{\alpha^\dag(0) \left[\bold{U}_{21}'(0)_{j,} \right]^\dag + \alpha^\top(0) \left[\bold{U}_{22}'(0)_{j,} \right]^\dag \right\} } \\
=&\begin{pmatrix}
\bold{U}'_{12}(0)_{i,} &\bold{U}'_{11}(0)_{i,}
\end{pmatrix}
\Braket{
    \begin{pmatrix}
    \left(\alpha^\dag(0) \right)^\top \alpha^\dag(0) &\left(\alpha^\dag(0) \right)^\top \alpha^\top(0) \\
    \alpha(0) \alpha^\dag(0) &\alpha(0) \alpha^\top(0)
    \end{pmatrix}
 }
\begin{pmatrix}
\left[\bold{U}'_{21}(0)_{j,} \right]^\dag \\
\left[\bold{U}'_{22}(0)_{j,} \right]^\dag \\
\end{pmatrix} \\
=&\begin{pmatrix}
\bold{U}'_{12}(0)_{i,} &\bold{U}'_{11}(0)_{i,}
\end{pmatrix}
\left(-M^{-1} +
\begin{pmatrix}
0 &I \\
0 &0
\end{pmatrix} \right)
\begin{pmatrix}
\left[\bold{U}'_{21}(0)_{j,} \right]^\dag \\
\left[\bold{U}'_{22}(0)_{j,} \right]^\dag \\
\end{pmatrix}
\end{aligned}
\end{equation}
$$

### 以B子格为中心

要算

$$
\begin{equation}
\begin{aligned}
&\Braket{0_\chi,0_{\alpha(1)} | \chi_{\bm{r}+\bm{a}_2,x} \alpha(1) H_h \alpha^\dag(2) \chi^\dag_{\bm{r}-\bm{a}_1+\bm{a}_2,y} | 0_\chi,0_{\alpha(2)} } \\
=&\Braket{0_\chi,0_{\alpha(1)} | \chi_{\bm{r}+\bm{a}_2,x} \alpha(1) \left[-h_z \left(\sigma_{\bm{r}} + \sigma_{\bm{r}+\bm{\delta}_z} \right) \right] \alpha^\dag(2) \chi^\dag_{\bm{r}-\bm{a}_1+\bm{a}_2,y} | 0_\chi,0_{\alpha(2)} } \\
\end{aligned}
\end{equation}
$$

注意到

$$
\begin{equation}
\chi_{\bm{r},\alpha}
\equiv \frac{1 }{2 } \left(b_{\bm{r}}^\alpha + \mathrm{i}b_{\bm{r}+\bm{\delta}_\alpha}^\alpha \right),\quad
\chi_{\bm{r},\alpha}^\dag
\equiv \frac{1 }{2 } \left(b_{\bm{r}}^\alpha - \mathrm{i}b_{\bm{r}+\bm{\delta}_\alpha}^\alpha \right),\quad
\bm{r}\in A
\end{equation}
$$

$$
\begin{equation}
b_{\bm{r}}^\alpha
=\chi_{\bm{r},\alpha} + \chi^\dag_{\bm{r},\alpha},\quad
b_{\bm{r}+\bm{\delta}_\alpha}^\alpha
=\frac{1 }{\mathrm{i} } \left(\chi_{\bm{r},\alpha} - \chi^\dag_{\bm{r},\alpha} \right)
\end{equation}
$$

于是

$$
\begin{equation}
\begin{aligned}
\sigma_{\bm{r}+\bm{\delta}_z}^z
&=\mathrm{i} b_{\bm{r}+\bm{\delta}_z}^z c_{\bm{r}+\bm{\delta}_z}
=-\mathrm{i} b_{\bm{r}+\bm{\delta}_z}^x b_{\bm{r}+\bm{\delta}_z}^y \\
&=-\mathrm{i} b_{\bm{r+a_2+\delta_x}}^x b_{\bm{r-a_1+a_2+\delta_y}}^y \\
&=-\mathrm{i} \cdot \frac{1 }{\mathrm{i} } \left(\chi_{\bm{r+a_2},x} - \chi_{\bm{r+a_2},x}^\dag \right) \cdot \frac{1 }{\mathrm{i} } \left(\chi_{\bm{r-a_1+a_2},y} - \chi_{\bm{r-a_1+a_2},y}^\dag \right) \\
&=\mathrm{i} \left(\chi_{\bm{r+a_2},x} - \chi_{\bm{r+a_2},x}^\dag \right) \left(\chi_{\bm{r-a_1+a_2},y} - \chi_{\bm{r-a_1+a_2},y}^\dag \right)
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
\sigma_{\bm{r+\delta_z}} \chi^\dag_{\bm{r}-\bm{a}_1+\bm{a}_2,y} 
&=\mathrm{i} \left(\chi_{\bm{r+a_2},x} - \chi_{\bm{r+a_2},x}^\dag \right) \left(\chi_{\bm{r-a_1+a_2},y} - \chi_{\bm{r-a_1+a_2},y}^\dag \right) \cdot \chi^\dag_{\bm{r}-\bm{a}_1+\bm{a}_2,y} \\
&=\mathrm{i} \left(\chi_{\bm{r+a_2},x} - \chi_{\bm{r+a_2},x}^\dag \right) \\
\text{在braket中}&=-\mathrm{i} \chi_{\bm{r+a_2},x}^\dag
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
\sigma_{\bm{r}}^z
&=\mathrm{i}b_{\bm{r}}^z c_{\bm{r}}
=b^x_{\bm{r+\delta_z}} b^y_{\bm{r+\delta_z}} b^z_{\bm{r+\delta_z}} c_{\bm{r+\delta_z}} \left(\mathrm{i}b_{\bm{r}}^z c_{\bm{r}} \right) \\
&=\left(-\mathrm{i} b_{\bm{r}+\bm{\delta}_z}^x b_{\bm{r}+\bm{\delta}_z}^y \right) \left(\mathrm{i} c_{\bm{r}} c_{\bm{r+\delta_z}} \right) \left(-\mathrm{i} b_{\bm{r}}^z b_{\bm{r+\delta_z}}^z \right) \\
&=\left(-\mathrm{i} b_{\bm{r}+\bm{\delta}_z}^x b_{\bm{r}+\bm{\delta}_z}^y \right) \left(\mathrm{i} c_{\bm{r}} c_{\bm{r+\delta_z}} \right) \cdot 1 \\
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
\sigma_{\bm{r}}^z \chi^\dag_{\bm{r}-\bm{a}_1+\bm{a}_2,y} 
&=\left(-\mathrm{i} b_{\bm{r}+\bm{\delta}_z}^x b_{\bm{r}+\bm{\delta}_z}^y \right) \left(\mathrm{i} c_{\bm{r}} c_{\bm{r+\delta_z}} \right) \chi^\dag_{\bm{r}-\bm{a}_1+\bm{a}_2,y} \\
&=\left(\mathrm{i} c_{\bm{r}} c_{\bm{r+\delta_z}} \right) \left(-\mathrm{i} b_{\bm{r}+\bm{\delta}_z}^x b_{\bm{r}+\bm{\delta}_z}^y \right) \chi^\dag_{\bm{r}-\bm{a}_1+\bm{a}_2,y} \\
&=\left(\mathrm{i} c_{\bm{r}} c_{\bm{r+\delta_z}} \right) \left[\mathrm{i} \left(\chi_{\bm{r+a_2},x} - \chi_{\bm{r+a_2},x}^\dag \right) \right] \\
&=-c_{\bm{r}} c_{\bm{r+\delta_z}} \left(\chi_{\bm{r+a_2},x} - \chi_{\bm{r+a_2},x}^\dag \right) \\
\text{在braket中}&=c_{\bm{r}} c_{\bm{r+\delta_z}} \chi_{\bm{r+a_2},x}^\dag
\end{aligned}
\end{equation}
$$

因此

$$
\begin{equation}
\begin{aligned}
&\Braket{0_\chi,0_{\alpha(1)} | \chi_{\bm{r}+\bm{a}_2,x} \alpha(1) H_h \alpha^\dag(2) \chi^\dag_{\bm{r}-\bm{a}_1+\bm{a}_2,y} | 0_\chi,0_{\alpha(2)} } \\
=&\Braket{0_\chi,0_{\alpha(1)} | \chi_{\bm{r}+\bm{a}_2,x} \alpha(1) \left[-h_z \left(\sigma_{\bm{r}} + \sigma_{\bm{r}+\bm{\delta}_z} \right) \right] \alpha^\dag(2) \chi^\dag_{\bm{r}-\bm{a}_1+\bm{a}_2,y} | 0_\chi,0_{\alpha(2)} } \\
=&-h_z \Braket{0_\chi,0_{\alpha(1)} | \chi_{\bm{r}+\bm{a}_2,x} \alpha(1) \left[\left(c_{\bm{r}} c_{\bm{r+\delta_z}} -\mathrm{i} \right) \right] \alpha^\dag(2) \chi_{\bm{r}+\bm{a}_2,x}^\dag | 0_\chi,0_{\alpha(2)} } \\
=&\mathrm{i} h_z \Braket{0_\chi,0_{\alpha(1)} | \chi_{\bm{r}+\bm{a}_2,x} \alpha(1) \left(1 + \mathrm{i} c_{\bm{r}} c_{\bm{r+\delta_z}} \right) \alpha^\dag(2) \chi_{\bm{r}+\bm{a}_2,x}^\dag | 0_\chi,0_{\alpha(2)} } \\
=&\mathrm{i} h_z \Braket{0_\chi,0_{\alpha(1)} | \alpha(1) \left(1 + \mathrm{i} c_{\bm{r}} c_{\bm{r+\delta_z}} \right) \alpha^\dag(2) | 0_\chi,0_{\alpha(2)} } \\
=&\mathrm{i} h_z \Braket{0_\chi,0_{\alpha(1)} | \alpha(1) \left(1 + \mathrm{i} c_{i,A} c_{j,B} \right) \alpha^\dag(2) | 0_\chi,0_{\alpha(2)} }
\end{aligned}
\end{equation}
$$

#### $T(\bm{a}_1) $ 的作用

$$
\begin{equation}
\begin{aligned}
&T(\bm{a}_1) 
\begin{pmatrix}
a_1 &a_2 &\cdots &a_{N_1} &a_{N_1+1} &a_{N_1+2} &\cdots &a_{2N_1} &\cdots &\cdots
\end{pmatrix}
T^{-1}(\bm{a}_1) \\
=&\begin{pmatrix}
a_2 &a_3 &\cdots &-a_{1} &a_{N_1+2} &a_{N_1+3} &\cdots &-a_{N_1} &\cdots &\cdots
\end{pmatrix} \\
=&\begin{pmatrix}
a_1 &a_2 &\cdots &a_{N_1} &a_{N_1+1} &a_{N_1+2} &\cdots &a_{2N_1} &\cdots &\cdots
\end{pmatrix}
\bigoplus_{i=1}^{N_2} 
\begin{pmatrix}
0 &0 &0 &0 &\cdots &-1 \\
1 &0 &0 &0 &\cdots &0 \\
0 &1 &0 &0 &\cdots &0 \\
0 &0 &1 &0 &\cdots &0 \\
\vdots &\vdots &\vdots &\ddots &\vdots &\vdots \\
0 &0 &0 &\cdots &1 &0
\end{pmatrix} \\
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
T_1
\equiv \bigoplus_{i=1}^{N_2} 
\begin{pmatrix}
0 &0 &0 &0 &\cdots &-1 \\
1 &0 &0 &0 &\cdots &0 \\
0 &1 &0 &0 &\cdots &0 \\
0 &0 &1 &0 &\cdots &0 \\
\vdots &\vdots &\vdots &\ddots &\vdots &\vdots \\
0 &0 &0 &\cdots &1 &0
\end{pmatrix}
\end{equation}
$$

$$
\begin{equation}
T(\bm{a}_1)
\begin{pmatrix}
a^\dag &a^\top \\
\end{pmatrix}
T^{-1}(\bm{a}_1)
=\begin{pmatrix}
a^\dag &a^\top \\
\end{pmatrix}
\begin{pmatrix}
T_1 &0 \\
0 &T_1
\end{pmatrix}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
T(\bm{a}_1)
\begin{pmatrix}
a \\
\left(a^\dag \right)^\top
\end{pmatrix}
T^{-1}(\bm{a}_1)
&=\begin{pmatrix}
T_1^\dag &0 \\
0 &T_1^\dag
\end{pmatrix}
\begin{pmatrix}
a \\
\left(a^\dag \right)^\top
\end{pmatrix} \\
&=\begin{pmatrix}
T_1^\top &0 \\
0 &T_1^\top
\end{pmatrix}
\begin{pmatrix}
a \\
\left(a^\dag \right)^\top
\end{pmatrix} \\
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
\begin{pmatrix}
a^\dag &a^\top \\
\end{pmatrix}
&=T(\bm{a}_1)
\begin{pmatrix}
a^\dag &a^\top \\
\end{pmatrix}
T^{-1}(\bm{a}_1)
\begin{pmatrix}
T_1 &0 \\
0 &T_1
\end{pmatrix}^{-1} \\
&=T(\bm{a}_1)
\begin{pmatrix}
a^\dag &a^\top \\
\end{pmatrix}
T^{-1}(\bm{a}_1)
\begin{pmatrix}
T_1 &0 \\
0 &T_1
\end{pmatrix}^{\dag} \\
&=T(\bm{a}_1)
\begin{pmatrix}
a^\dag &a^\top \\
\end{pmatrix}
T^{-1}(\bm{a}_1)
\begin{pmatrix}
T_1^\top &0 \\
0 &T_1^\top
\end{pmatrix} \\
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\boxed{
\begin{aligned}
T(-\bm{a}_1)
\begin{pmatrix}
a^\dag &a^\top \\
\end{pmatrix}
T^{-1}(-\bm{a}_1)
&=T^{-1}(\bm{a}_1)
\begin{pmatrix}
a^\dag &a^\top \\
\end{pmatrix} 
T(\bm{a}_1) \\
&=\begin{pmatrix}
a^\dag &a^\top \\
\end{pmatrix}
\begin{pmatrix}
T_1^\top &0 \\
0 &T_1^\top
\end{pmatrix}
\end{aligned}
}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
T(-\bm{a}_1)
\begin{pmatrix}
a^\top \\
\left(a^\dag \right)^\top
\end{pmatrix}
T^{-1}(-\bm{a}_1)
=\begin{pmatrix}
T_1 &0 \\
0 &T_1
\end{pmatrix}
\begin{pmatrix}
a \\
\left(a^\dag \right)^\top
\end{pmatrix}
\end{aligned}
\end{equation}
$$

#### $T(\bm{a}_2) $ 的作用

$$
\begin{equation}
\begin{aligned}
&T(\bm{a}_2) 
\begin{pmatrix}
a_1 &a_2 &\cdots &a_{N_1} &a_{N_1+1} &a_{N_1+2} &\cdots &a_{2N_1} &\cdots &\cdots
\end{pmatrix}
T^{-1}(\bm{a}_2) \\
=&T(\bm{a}_1) 
\begin{pmatrix}
a_{N_1+1} &a_{N_1+2} &\cdots &a_{2N_1} &a_{2N_1+1} &a_{2N_1+2} &\cdots &a_{3N_1} &\cdots &-a_{1} &-a_{2} &\cdots &-a_{N_1}
\end{pmatrix}
T^{-1}(\bm{a}_1) \\
=&\begin{pmatrix}
a_1 &a_2 &\cdots &a_{N_1} &a_{N_1+1} &a_{N_1+2} &\cdots &a_{2N_1} &\cdots &\cdots
\end{pmatrix}
\begin{pmatrix}
0 &0 &0 &0 &\cdots &-I_{N_1} \\
I_{N_1} &0 &0 &0 &\cdots &0 \\
0 &I_{N_1} &0 &0 &\cdots &0 \\
0 &0 &\ddots &\cdots &\cdots &0 \\
\vdots &\vdots &\vdots &\ddots &\cdots &0 \\
0 &0 &0 &\cdots &I_{N_1} &0
\end{pmatrix}
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
T_2
\equiv \begin{pmatrix}
0 &0 &0 &0 &\cdots &-I_{N_1} \\
I_{N_1} &0 &0 &0 &\cdots &0 \\
0 &I_{N_1} &0 &0 &\cdots &0 \\
0 &0 &\ddots &\cdots &\cdots &0 \\
\vdots &\vdots &\vdots &\ddots &\cdots &0 \\
0 &0 &0 &\cdots &I_{N_1} &0
\end{pmatrix}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
T(\bm{a}_2)
\begin{pmatrix}
a^\dag &a^\top
\end{pmatrix}
T^{-1}(\bm{a}_2)
=\begin{pmatrix}
a^\dag &a^\top
\end{pmatrix}
\begin{pmatrix}
T_2 &0 \\
0 &T_2
\end{pmatrix}
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
T(\bm{a}_2)
\begin{pmatrix}
a \\
\left(a^\dag \right)^\top
\end{pmatrix}
T^{-1}(\bm{a}_2)
&=\begin{pmatrix}
T_2^\dag &0 \\
0 &T_2^\dag
\end{pmatrix}
\begin{pmatrix}
a \\
\left(a^\dag \right)^\top
\end{pmatrix} \\
&=\begin{pmatrix}
T_2^\top &0 \\
0 &T_2^\top
\end{pmatrix}
\begin{pmatrix}
a \\
\left(a^\dag \right)^\top
\end{pmatrix} \\
\end{aligned}
\end{equation}
$$

#### 哈密顿量的关系

已知 $H(\bm{r},x/y/z) $，要求 $H(\bm{r}+\bm{a}_2,x) $ 和 $H(\bm{r}-\bm{a}_1+\bm{a}_2,y) $

$$
\begin{equation}
\begin{aligned}
H(\bm{r}+\bm{a}_2,x)
&=T(\bm{a}_2) H(\bm{r},x) T^{-1}(\bm{a}_2) \\
&=\frac{1 }{2 }
T(\bm{a}_2)
\begin{pmatrix}
a^\dag &a^\top 
\end{pmatrix}
T^{-1}(\bm{a}_2)
h(\bm{r},x)
T(\bm{a}_2)
\begin{pmatrix}
a \\
\left(a^\dag \right)^\top 
\end{pmatrix}
T^{-1}(\bm{a}_2) \\
&=\frac{1 }{2 } 
\begin{pmatrix}
a^\dag &a^\top 
\end{pmatrix}
\begin{pmatrix}
T_2 &0 \\
0 &T_2
\end{pmatrix}
h(\bm{r},x)
\begin{pmatrix}
T_2^\top &0 \\
0 &T_2^\top
\end{pmatrix}
\begin{pmatrix}
a \\
\left(a^\dag \right)^\top 
\end{pmatrix}
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\boxed{
h(\bm{r}+\bm{a}_2)
=\begin{pmatrix}
T_2 &0 \\
0 &T_2
\end{pmatrix}
h(\bm{r},x)
\begin{pmatrix}
T_2^\top &0 \\
0 &T_2^\top
\end{pmatrix}
}
\end{equation}
$$

$$
\begin{equation}
h(\bm{r},x) U = U D
\Longrightarrow
h(\bm{r}+\bm{a}_2) \left(\bold{T}_2 U \right) = \left(\bold{T}_2 U \right) D
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
H(\bm{r}-\bm{a}_1+\bm{a}_2,y)
&=T(-\bm{a}_1) T(\bm{a}_2) H(\bm{r},y) T^{-1}(\bm{a}_2) T^{-1}(-\bm{a}_1) \\
&=\frac{1 }{2 }
T(-\bm{a_1}) T(\bm{a}_2)
\begin{pmatrix}
a^\dag &a^\top 
\end{pmatrix}
T^{-1}(\bm{a}_2) T^{-1}(-\bm{a}_1)
h(\bm{r},y)
T(-\bm{a}_1)T(\bm{a}_2)
\begin{pmatrix}
a \\
\left(a^\dag \right)^\top 
\end{pmatrix}
T^{-1}(\bm{a}_2) T^{-1}(-\bm{a}_1) \\
&=\frac{1 }{2 } 
\begin{pmatrix}
a^\dag &a^\top 
\end{pmatrix}
\begin{pmatrix}
T_2 &0 \\
0 &T_2
\end{pmatrix}
\begin{pmatrix}
T_1^\top &0 \\
0 &T_1^\top
\end{pmatrix}
h(\bm{r},y)
\begin{pmatrix}
T_1 &0 \\
0 &T_1
\end{pmatrix}
\begin{pmatrix}
T_2^\top &0 \\
0 &T_2^\top
\end{pmatrix}
\begin{pmatrix}
a \\
\left(a^\dag \right)^\top 
\end{pmatrix}
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\boxed{
h(\bm{r}-\bm{a}_1+\bm{a}_2,y)
=\begin{pmatrix}
T_2 &0 \\
0 &T_2
\end{pmatrix}
\begin{pmatrix}
T_1^\top &0 \\
0 &T_1^\top
\end{pmatrix}
h(\bm{r},y)
\begin{pmatrix}
T_1 &0 \\
0 &T_1
\end{pmatrix}
\begin{pmatrix}
T_2^\top &0 \\
0 &T_2^\top
\end{pmatrix}
}
\end{equation}
$$

$$
\begin{equation}
h(\bm{r},y) U = U D
\Longrightarrow
h(\bm{r}-\bm{a}_1+\bm{a}_2) \left(\bold{T}_2 \bold{T}_1^\top U \right) = \left(\bold{T}_2 \bold{T}_1^\top U \right) D
\end{equation}
$$

