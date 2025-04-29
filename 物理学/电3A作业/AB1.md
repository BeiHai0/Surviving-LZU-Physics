> 证明 AB 效应中的相位差 $\delta $ 是规范不变量。

国际单位制下，

$$
\delta
=-\frac{e }{\hbar} \oint \vec{A}(\vec{r}')\cdot\mathrm{d}\vec{r}'
$$

设：

$$
\vec{A}(\vec{r}')\to\vec{A}'(\vec{r}')=\vec{A}(\vec{r}')+\nabla' \chi(\vec{r}')
$$

则：

$$
\begin{aligned}
\delta'
&=-\frac{e }{\hbar } \oint \vec{A}'(\vec{r}')\cdot\mathrm{d}\vec{r}' \\
&=-\frac{e }{\hbar } \oint\left[\vec{A}(\vec{r}')+\nabla' \chi(\vec{r}') \right]\cdot\mathrm{d}\vec{r}' \\
&=\delta - \frac{e }{\hbar } \oint \nabla'\chi(\vec{r}')\cdot\mathrm{d}\vec{r}' \\
&=\delta - \frac{e }{\hbar } \iint \nabla'\times\left[\nabla'\chi(\vec{r}') \right]\cdot\mathrm{d}\vec{S} \\
&=\delta - \frac{e }{\hbar } \iint \vec{0}\cdot\mathrm{d}\vec{S} \\
&=\delta
\end{aligned}
$$

即 $\delta $ 是规范不变量。