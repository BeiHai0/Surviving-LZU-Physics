$$
\begin{equation}
\left(M_K^{\bm{\delta}} \right)_{ij}
=\delta_{\bm{r}_i-\bm{\delta},\bm{r}_j} u_{\bm{r}_i-\bm{\delta},A;\bm{r}_i,B},\quad
\bm{\delta} \in \left\{\bm{0},\bm{a}_1,\bm{a}_2 \right\}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
H_\kappa^A[u]
&=\mathrm{i} \kappa \sum_{\bm{r}} \sum_{\substack{\left(\bm{\delta}_1,\bm{\delta}_2 \right)\in \\ \left\{\left(\bm{a}_1,\bm{a}_2 \right),\left(\bm{a}_2,\bm{0} \right),\left(\bm{0},\bm{a}_1 \right) \right\}}} u_{\bm{r}-\bm{\delta}_1,A;\bm{r},B} u_{\bm{r}-\bm{\delta}_2,A;\bm{r},B} c_{\bm{r}-\bm{\delta}_1,A} c_{\bm{r}-\bm{\delta}_2,A} \\
&=\mathrm{i} \kappa \sum_{\bm{r}',\bm{r}''} \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \sum_{\bm{r}} \delta_{\bm{r}-\bm{\delta}_1,\bm{r}'} \delta_{\bm{r}-\bm{\delta}_2,\bm{r}''} u_{\bm{r}-\bm{\delta}_1,A;\bm{r},B} u_{\bm{r}-\bm{\delta}_2,A;\bm{r},B} c_{\bm{r}',A} c_{\bm{r}'',A} \\
&=\mathrm{i} \kappa \sum_{\bm{r}',\bm{r}''} \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \sum_{\bm{r}} \left(\delta_{\bm{r}-\bm{\delta}_1,\bm{r}'} u_{\bm{r}-\bm{\delta}_1,A;\bm{r},B} \right) \left(\delta_{\bm{r}-\bm{\delta}_2,\bm{r}''} u_{\bm{r}-\bm{\delta}_2,A;\bm{r},B} \right) c_{\bm{r}',A} c_{\bm{r}'',A} \\
&=\mathrm{i} \kappa \sum_{i,j} \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \sum_{k} \left(\delta_{\bm{r}_k-\bm{\delta}_1,\bm{r}_i} u_{\bm{r}_k-\bm{\delta}_1,A;\bm{r}_k,B} \right) \left(\delta_{\bm{r}_k-\bm{\delta}_2,\bm{r}_j} u_{\bm{r}_k-\bm{\delta}_2,A;\bm{r}_k,B} \right) c_{i,A} c_{j,A} \\
&=\mathrm{i} \kappa \sum_{i,j} \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \sum_{k} \left(M_K^{\bm{\delta}_1} \right)_{ki} \left(M_K^{\bm{\delta}_2} \right)_{kj} c_{i,A} c_{j,A} \\
&=\mathrm{i} \kappa \sum_{i,j} \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \sum_{k} \left(M_K^{\bm{\delta}_1} \right)^\top_{ik} \left(M_K^{\bm{\delta}_2} \right)_{kj} c_{i,A} c_{j,A} \\
&=\mathrm{i} \kappa \sum_{i,j} \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \left[\left(M_K^{\bm{\delta}_1} \right)^\top \left(M_K^{\bm{\delta}_2} \right) \right]_{ij} c_{i,A} c_{j,A} \\
&\equiv \mathrm{i} \kappa \sum_{i,j} \left(M_\kappa^A \right)_{ij} c_{i,A} c_{j,A}
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\left(M_\kappa^A \right)_{ij}
=\sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \left[\left(M_K^{\bm{\delta}_1} \right)^\top \left(M_K^{\bm{\delta}_2} \right) \right]_{ij}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
H_\kappa^A[u]
&=\mathrm{i} \kappa \sum_{i,j} \left(M_\kappa^A \right)_{ij} c_{i,A} c_{j,A} \\
&=\mathrm{i} \kappa \bm{c}_A^\dag \bm{M}_\kappa^A \bm{c}_A \\
&=\mathrm{i} \kappa 
\begin{pmatrix}
\bm{c}_A^\dag &\bm{c}_B^\dag
\end{pmatrix}
\begin{pmatrix}
\bm{M}_\kappa^A &\bm{0} \\
\bm{0} &\bm{0}
\end{pmatrix}
\begin{pmatrix}
\bm{c}_A &\bm{c}_B \\
\end{pmatrix} \\
&=\mathrm{i} \kappa \bm{\psi}_c^\dag
\begin{pmatrix}
\bm{M}_\kappa^A &\bm{0} \\
\bm{0} &\bm{0}
\end{pmatrix} \bm{\psi}_c \\
&=\frac{\mathrm{i} }{2 } \bm{\psi}_c^\dag \kappa
\begin{pmatrix}
\bm{M}_\kappa^A - \left(\bm{M}_\kappa^A \right)^\top &\bm{0} \\
\bm{0} &\bm{0}
\end{pmatrix} \bm{\psi}_c \\
&\equiv \frac{\mathrm{i} }{2 } \bm{\psi}_c^\dag \left(\kappa \bm{H}_{c}^A[u] \right) \bm{\psi}_c \\
&\equiv \frac{\mathrm{i} }{2 } \bm{\psi}_c^\dag \bm{H}_{\kappa,c}^A[u] \bm{\psi}_c
\end{aligned}
\end{equation}
$$

---

$$
\begin{equation}
\begin{aligned}
H_\kappa^B[u]
&=\mathrm{i} \kappa \sum_{\bm{r}} \sum_{\substack{\left(\bm{\delta}_1,\bm{\delta}_2 \right)\in \\ \left\{\left(\bm{a}_1,\bm{a}_2 \right),\left(\bm{a}_2,\bm{0} \right),\left(\bm{0},\bm{a}_1 \right) \right\}}} u_{\bm{r},A;\bm{r}+\bm{\delta}_1,B} u_{\bm{r},A;\bm{r}+\bm{\delta}_2,B} c_{\bm{r}+\bm{\delta}_1,B} c_{\bm{r}+\bm{\delta}_2,B} \\
&=\mathrm{i} \kappa \sum_{\bm{r}} \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \sum_{\bm{r}',\bm{r}''} \delta_{\bm{r}',\bm{r}+\bm{\delta}_1} \delta_{\bm{r}'',\bm{r}+\bm{\delta}_2} u_{\bm{r},A;\bm{r}+\bm{\delta}_1,B} u_{\bm{r},A;\bm{r}+\bm{\delta}_2,B} c_{\bm{r}',B} c_{\bm{r}'',B} \\
&=\mathrm{i} \kappa \sum_{\bm{r}',\bm{r}''} \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \sum_{\bm{r}} \left(\delta_{\bm{r}',\bm{r}+\bm{\delta}_1} u_{\bm{r},A;\bm{r}+\bm{\delta}_1,B} \right) \left(\delta_{\bm{r}'',\bm{r}+\bm{\delta}_2} u_{\bm{r},A;\bm{r}+\bm{\delta}_2,B} \right) c_{\bm{r}',B} c_{\bm{r}'',B} \\
&=\mathrm{i} \kappa \sum_{\bm{r}',\bm{r}''} \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \sum_{\bm{r}} \left(\delta_{\bm{r}'-\bm{\delta}_1,\bm{r}} u_{\bm{r}'-\bm{\delta}_1,A;\bm{r}',B} \right) \left(\delta_{\bm{r}''-\bm{\delta}_2,\bm{r}} u_{\bm{r}''-\bm{\delta}_2,A;\bm{r}'',B} \right) c_{\bm{r}',B} c_{\bm{r}'',B} \\
&=\mathrm{i} \kappa \sum_{i,j} \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \sum_{k} \left(\delta_{\bm{r}_i-\bm{\delta}_1,\bm{r}_k} u_{\bm{r}_i-\bm{\delta}_1,A;\bm{r}_i,B} \right) \left(\delta_{\bm{r}_j-\bm{\delta}_2,\bm{r}_k} u_{\bm{r}_j-\bm{\delta}_2,A;\bm{r}_j,B} \right) c_{i,B} c_{j,B} \\
&=\mathrm{i} \kappa \sum_{i,j} \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \sum_{k} \left(M_K^{\bm{\delta}_1} \right)_{ik} \left(M_K^{\bm{\delta}_2} \right)_{jk} c_{i,B} c_{j,B} \\
&=\mathrm{i} \kappa \sum_{i,j} \sum_{\left(\bm{\delta}_1,\bm{\delta}_2 \right)} \left[\left(M_K^{\bm{\delta}_1} \right)\left(M_K^{\bm{\delta}_2} \right)^\top \right]_{ij} c_{i,B} c_{j,B} \\
&\equiv \mathrm{i} \kappa \sum_{i,j} \left(M_\kappa^B \right)_{ij} c_{i,B} c_{j,B}
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\left(M_\kappa^B \right)_{ij}
=\left[\left(M_K^{\bm{\delta}_1} \right)\left(M_K^{\bm{\delta}_2} \right)^\top \right]_{ij}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
H_\kappa^B[u]
&=\mathrm{i} \kappa \sum_{i,j} \left(M_\kappa^B \right)_{ij} c_{i,B} c_{j,B} \\
&=\mathrm{i} \kappa \bm{c}_B^\dag \bm{M}_\kappa^B \bm{c}_B \\
&=\mathrm{i} \kappa
\begin{pmatrix}
\bm{c}_A^\dag &\bm{c}_B^\dag
\end{pmatrix}
\begin{pmatrix}
\bm{0} &\bm{0} \\
\bm{0} &\bm{M}_\kappa^B
\end{pmatrix}
\begin{pmatrix}
\bm{c}_A \\
\bm{c}_B
\end{pmatrix} \\
&=\mathrm{i} \kappa \bm{\psi}_c^\dag
\begin{pmatrix}
\bm{0} &\bm{0} \\
\bm{0} &\bm{M}_\kappa^B
\end{pmatrix}
\bm{\psi}_c \\
&=\frac{\mathrm{i} }{2 } \bm{\psi}_c^\dag \kappa 
\begin{pmatrix}
\bm{0} &\bm{0} \\
\bm{0} &\bm{M}_\kappa^B - \left(\bm{M}_\kappa^B \right)^\top
\end{pmatrix}
\bm{\psi}_c \\
&\equiv \frac{\mathrm{i} }{2 } \bm{\psi}_c^\dag \left(\kappa \bm{H}_{c}^B[u] \right) \bm{\psi}_c \\
&\equiv \frac{\mathrm{i} }{2 } \bm{\psi}_c^\dag \bm{H}_{\kappa,c}^B[u] \bm{\psi}_c
\end{aligned}
\end{equation}
$$
