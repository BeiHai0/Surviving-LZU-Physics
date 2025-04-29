
库仑定律:

$$
\vec{F}_{12}
=\frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r_{12}^2}\vec{e}_{12}
$$

电场定义：

$$
\vec{E}
=\frac{\vec{F}}{q_0}
=\frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}\vec{e}_r
$$

电偶极矩：

$$
\vec{p}
=q\vec{l}
$$

电场强度通量：

$$
\varPhi_E
=\iint\limits_{S} \vec{E}\cdot\mathrm{d}\vec{S}
$$

静电场的环路定理：

$$
\oint\limits_L \vec{E}\cdot\mathrm{d}\vec{l}
=0
$$

高斯定理：

$$
\oiint\limits_{S}\vec{E}\cdot\mathrm{d}\vec{S}
=\frac{1}{\varepsilon_0}\sum_{(S内)}q
$$

电势能改变量(从1到2)：

$$
\Delta E_p
\equiv E_{p_2}-E_{p_1}
=-A_{12}
=-\int_1^2\vec{F}\cdot\mathrm{d}\vec{l}
=-\int_1^2q_0\vec{E}\cdot\mathrm{d}\vec{l}
=-q_0\int_1^2\vec{E}\cdot\mathrm{d}\vec{l}
$$

电势差(场点1相对于场点2的电势差;1,2只是场点的编号)：

$$
U_{12}
=\frac{-\Delta E_p}{q_0}
=\frac{-(E_{p_2}-E_{p_1})}{q_0}
=\frac{A_{12}}{q_0}
=\int_1^2\vec{E}\cdot\mathrm{d}\vec{l}
$$

电势:相对于电势零点的电势差(1,0只是场点的编号)

$$
\varphi_P
\equiv U_{P0}
=\int_1^0\vec{E}\cdot\mathrm{d}\vec{l}
$$

设无穷远处为电势零点，离点电荷 $Q$ 距离为 $r$ 处场点 $P$ 电势：

$$
\varphi_P
=\frac{1}{4\pi\varepsilon_0}\frac{Q}{r}
$$

电场和电势的关系(电场等于电势的负梯度)：

$$
\vec{E}
=-\nabla U
$$

带电体系静电能：

多个点电荷的情形：

$$

\begin{cases}

E_{p1}=0 \\
E_{p2}=q_2U_{12} \\
E_{p3}=q_3(U_{13}+U_{23}) \\
\vdots \\
E_{pn}=q_n(U_{1n}+U_{2n}+\cdots+U_{n-1,n})

\end{cases}

$$

用求和符号表达：

$$
E_{pi}=q_i\sum_{j=1}^{i-1}U_{ji} ,~~~~~~~~(i=1,2,\cdots,n)
$$

总电势能：

$$
E_p
=\sum_{i=1}^n E_{pi}
=\sum_{i=1}^n q_i\sum_{j=1}^{i-1}U_{ji}
=\sum_{i=1}^n\sum_{j=1}^{i-1}q_i U_{ji}
=\frac{1}{4\pi\varepsilon_0}\sum_{i=1}^n\sum_{j=1}^{i-1}\frac{q_iq_j}{r_{ij}}
$$

$$
E_p
=\frac{1}{4\pi\varepsilon_0}\sum_{i=1}^n\sum_{j=1}^{i-1}\frac{q_iq_j}{r_{ij}}
=\frac{1}{2}\frac{1}{4\pi\varepsilon_0}\underset{(j\ne i)}{\sum_{i=1}^n\sum_{j=1}^n}\frac{q_iq_j}{r_{ij}}
=\frac{1}{8\pi\varepsilon_0}\underset{(j\ne i)}{\sum_{i=1}^n\sum_{j=1}^n}\frac{q_iq_j}{r_{ij}}
$$

记$U_i$为除$q_i$外其余电荷在$q_i$位置$P_i$上产生的电势，则电势能又可以写成：

$$
E_p
=\frac{1}{2}\sum_{i=1}^n q_iU_i
$$

综上，共有三种方法计算$W_互$

电荷连续分布情形的静电能：

体电荷分布：

$$
W_e
=\frac{1}{2}\iiint\limits_{V}\rho_eU\mathrm{d}V
$$

面电荷分布：

$$
W_e
=\frac{1}{2}\iint\limits_{S}\sigma_e U \mathrm{d}S
$$

线电荷分布：

$$
W_e
=\frac{1}{2}\int\limits_{l} \eta_e U \mathrm{d}l
$$

可定义电势能：

$$
E_p=q_0U
$$

导体表面之外附近空间的场强$\vec{E} $与该处导体表面的电荷面密度$\sigma_e $的关系：

电容：

孤立导体的电容 $C$ 与导体的尺寸和形状有关，与 $q,U$ 无关

$$
C=\frac{q}{U}
$$

电容器的串联：

$$
\frac{1}{C}=\frac{1}{C_1}+\frac{1}{C_2}+\cdots+\frac{1}{C_n}
$$

推导：

$$
C=\frac{q}{U}
=\frac{q}{U_1+U_2+\cdots+U_n}
=\frac{q}{\frac{q}{C_1}+\frac{q}{C_2}+\cdots+\frac{q}{C_n}}
=\frac{1}{\frac{1}{C_1}+\frac{1}{C_2}+\cdots+\frac{1}{C_n}}
$$

电容器的并联：

$$
C=C_1+C_2+\cdots+C_n
$$

电极化强度(度量电介质极化状态)：

$$
\vec{P}=\frac{\sum\vec{p}_{分子}}{\Delta V}
$$

电极化强度与极化电荷分布的关系：

$$
\oiint\limits_{S} \vec{P}\cdot d\vec{S}=-\sum_{(S内)}q'
$$

其中，$\vec{P}$ 是电极化强度，$q'$ 是极化电荷

极化电荷面密度：

$$
\sigma'=\frac{dq'}{dS}=P\cos\theta=\vec{P}\cdot\vec{e}_n=P_n
$$

比例常量 $\chi_e$ 叫作极化率. 极化率与电介质的种类有关，是介质材料的属性. 真空中$\chi_e=0$

电位移矢量：
$$
\vec{D}=\varepsilon_0\vec{E}+\vec{P}
$$

相对介电常量：

$$
\vec{D}=(1+\chi_e)\varepsilon_0\vec{E}=\varepsilon\varepsilon_0\vec{E}
$$

$$
\varepsilon=1+\chi_e
$$

$\varepsilon $ 称为电介质的相对介电常量.真空中 $\varepsilon=1$

有介质时的高斯定理(注意，等式右边没有$\frac{1}{\varepsilon_0}$)：

$$
\oiint_S\vec{D}\cdot \mathrm{d}\vec{S}=\sum_{(S内)}q_0
$$
其中,$q_0$ 是 $S$ 内的自由电荷.


电介质解题几板斧：

$$
\sigma_e'=\vec{P}\cdot\vec{e}_n=P_n \\
\vec{P}=\chi_e\varepsilon_0\vec{E} \\
\varepsilon=1+\chi_e \\
\vec{D}=\varepsilon_0\vec{E}+\vec{P}=\varepsilon\varepsilon_0\vec{E} \\ 
\oiint_S\vec{D}\cdot d\vec{S}=\sum_{S内}q_0 \\

$$







