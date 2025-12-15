### Grassmann

#### 费米子相干态

单模相干态：

$$
\begin{equation}
\Ket{z_i }
\equiv \exp\left(-z_i a_i^\dag \right) \Ket{0 }
\end{equation}
$$

$$
\begin{equation}
\Bra{z_i }
\equiv \Bra{0 } \exp\left(-a_i \bar{z}_i \right)
\end{equation}
$$

多模相干态：

$$
\begin{equation}
\Ket{z }
\equiv \exp\left(-\sum_{i} z_i a_i^\dag \right) \Ket{0 }
\end{equation}
$$

$$
\begin{equation}
\Bra{z }
\equiv \Bra{0 } \exp\left(-\sum_{i} a_i \bar{z}_i \right)
\end{equation}
$$

相干态是湮灭算符本征态：

$$
\begin{equation}
a_i \Ket{z } = z_i \Ket{z }
\end{equation}
$$

$$
\begin{equation}
\Bra{z } a_i^\dag = \Bra{z } \bar{z}_i
\end{equation}
$$

相干态与真空态overlap

$$
\begin{equation}
\Braket{0 | z }
=1
\end{equation}
$$

$$
\begin{equation}
\Braket{z | 0 }
=1
\end{equation}
$$

#### 费米子相干态表象完备性关系

$$
\begin{equation}
\int \left(\prod_{i} \mathrm{d}\bar{z}_i \mathrm{d}z_i \right) \exp\left(-\sum_{j} \bar{z}_j z_j \right) \Ket{z }\Bra{z }
=1
\end{equation}
$$

#### Grassmann高斯积分

反对称矩阵 $A_{2N\times 2N},\Theta=\left(\theta_1,\cdots,\theta_{2N} \right)^\top $ 实Grassmann高斯积分：

$$
\begin{equation}
\int \left(\prod_{i=1}^{2N} \mathrm{d} \theta_i \right) \exp\left(-\frac{1 }{2 } \Theta^\top A \Theta \right)
=\mathrm{Pf}(A)
\end{equation}
$$

$$
\begin{equation}
\int \left(\prod_{i=1}^{2N} \mathrm{d} \theta_i \right) \exp\left(\frac{1 }{2 } \Theta^\top A \Theta \right)
=(-1)^N\mathrm{Pf}(A)
\end{equation}
$$

$A_{N\times N},\Theta=\left(\theta_1,\cdots,\theta_{N} \right)^\top, \bar{\Theta}=\left(\bar{\theta}_1,\cdots,\bar{\theta}_{N} \right)^\top $ 复Grassmann高斯积分：

$$
\begin{equation}
\int \left(\prod_i \mathrm{d}\bar{\theta}_i \mathrm{d}\theta_i \right) \exp\left(-\bar{\Theta}^\top A \Theta \right)
=\mathrm{det}(A)
\end{equation}
$$

### 在费米子相干态表象计算overlap

$$
\begin{equation}
\Ket{\tilde{\Omega}_1 }
=\exp\left(\frac{1 }{2 } \sum_{i,j} f^{(1)}_{i,j} a_i^\dag a_j^\dag \right) \Ket{0 },\quad
f^{(1)}_{i,j} = -f^{(1)}_{j,i}
\end{equation}
$$

$$
\begin{equation}
\Ket{\tilde{\Omega}_2 }
=\exp\left(\frac{1 }{2 } \sum_{i,j} f^{(2)}_{i,j} a_i^\dag a_j^\dag \right) \Ket{0 },\quad
f^{(2)}_{i,j} = -f^{(2)}_{j,i}
\end{equation}
$$

$$
\begin{equation}
\begin{split}
\Braket{\widetilde{\Omega}_1 | \widetilde{\Omega}_2 }
&=\int \left(\prod_i \mathrm{d}\bar{z}_i \mathrm{d}z_i \right) \exp\left(-\sum_{j} \bar{z}_j z_j \right) \Braket{\widetilde{\Omega}_1 | z } \Braket{z | \widetilde{\Omega}_2 } \\
&=\int \mathrm{d}\left(\bar{z},z \right) \exp\left(- \bar{z}^\top z \right) \Braket{0 | \exp\left(\frac{1 }{2 } \sum_{i,j} f^{(1)*}_{i,j} a_j a_i | z \right) } \Braket{z | \exp\left(\frac{1 }{2 } \sum_{i,j} f^{(2)}_{i,j} a_i^\dag a_j^\dag \right) | 0 } \\
&=\int \mathrm{d}\left(\bar{z},z \right) \exp\left(- \bar{z}^\top z \right) \exp\left(\frac{1 }{2 } \sum_{i,j} f^{(1)*}_{i,j} z_j z_i \right) \exp\left(\frac{1 }{2 } \sum_{i,j} f^{(2)}_{i,j} \bar{z}_i \bar{z}_j \right) \Braket{0 | z } \Braket{z | 0 } \\
&=\int \mathrm{d}\left(\bar{z},z \right) \exp\left(- \bar{z}^\top z \right) \exp\left(-\frac{1 }{2 } \sum_{i,j} f^{(1)*}_{i,j} z_i z_j \right) \exp\left(\frac{1 }{2 } \sum_{i,j} f^{(2)}_{i,j} \bar{z}_i \bar{z}_j \right) \\
&=\int \mathrm{d}\left(\bar{z},z \right) \exp\left(- \bar{z}^\top z \right) \exp\left(- \frac{1 }{2 }  z^\top f^{(1)*} z \right) \exp\left(\frac{1 }{2 } \bar{z}^\top f^{(2)} \bar{z} \right)
\end{split}
\end{equation}
$$

为了用实Grassmann高斯积分的结果，构造

$$
\begin{equation}
Z
\equiv \left(\bar{z}_1,\cdots,\bar{z}_N,z_1,\cdots,z_N \right)^\top
\end{equation}
$$

从

$$
\begin{equation}
\bar{z}_1,z_1,\bar{z}_2,z_2,\cdots,\bar{z}_N,z_N
\end{equation}
$$

到

$$
\begin{equation}
\bar{z}_1,\cdots,\bar{z}_N,z_1,\cdots,z_N
\end{equation}
$$

共需要多少次最近邻交换？

以

$$
\begin{equation}
\bar{z}_1 \bar{z}_2 \cdots \bar{z}_N z_1 z_2 \cdots z_N
\end{equation}
$$

为正序，则逆序对数量为

$$
\begin{equation}
(N-1) + (N-2) + \cdots + 1
=\frac{N(N-1) }{2 } 
\end{equation}
$$

因此

$$
\begin{equation}
\begin{split}
\mathrm{d}(\bar{z},z)
\equiv \prod_{i} \mathrm{d}\bar{z}_i \mathrm{d} z_i
&=\left(\mathrm{d} \bar{z}_1 \mathrm{d} z_1 \right) \cdots \left(\mathrm{d} \bar{z}_N \mathrm{d} z_N \right) \\
&=\left(-1 \right)^{N(N-1)/2} \mathrm{d} \bar{z}_1 \cdots \mathrm{d} \bar{z}_N \mathrm{d} z_1 \mathrm{d} z_N \\
&=\left(-1 \right)^{N(N-1)/2} \left(\prod_{i} \mathrm{d}\bar{z}_i \right) \left(\prod_j \mathrm{d}z_j \right) \\
&=\left(-1 \right)^{N(N-1)/2} \prod_{i=1}^{2N} \mathrm{d}Z_i
\end{split}
\end{equation}
$$

而

$$
\begin{equation}
\begin{split}
&\exp\left(- \bar{z}^\top z \right) \exp\left(- \frac{1 }{2 }  z^\top f^{(1)*} z \right) \exp\left(\frac{1 }{2 } \bar{z}^\top f^{(2)} \bar{z} \right) \\
=&\exp\left(- \bar{z}^\top z - \frac{1 }{2 }  z^\top f^{(1)*} z + \frac{1 }{2 } \bar{z}^\top f^{(2)} \bar{z} \right) \\
=&\exp\left(- \frac{1 }{2 } \bar{z}^\top z - \frac{1 }{2 } \bar{z}^\top z - \frac{1 }{2 }  z^\top f^{(1)*} z + \frac{1 }{2 } \bar{z}^\top f^{(2)} \bar{z} \right) \\
=&\exp\left(- \frac{1 }{2 } \bar{z}^\top z + \frac{1 }{2 } z^\top \bar{z} - \frac{1 }{2 }  z^\top f^{(1)*} z + \frac{1 }{2 } \bar{z}^\top f^{(2)} \bar{z} \right) \\
\end{split}
\end{equation}
$$

$$
\begin{equation}
\begin{split}
-\frac{1 }{2 } \bar{z}^\top z + \frac{1 }{2 } z^\top \bar{z} -\frac{1 }{2 }  z^\top f^{(1)*} z + \frac{1 }{2 } \bar{z}^\top f^{(2)} \bar{z}
&=\frac{1 }{2 } 
\begin{pmatrix}
\bar{z}^\top & z^\top \\
\end{pmatrix}
\begin{pmatrix}
f^{(2)} &-I \\
I &-f^{(1)*}
\end{pmatrix}
\begin{pmatrix}
\bar{z} \\
z
\end{pmatrix} \\
&=\frac{1 }{2 }  Z^\top M Z
\end{split}
\end{equation}
$$

$$
\begin{equation}
M_{i,j} = -M_{j,i}
\end{equation}
$$

于是

$$
\begin{equation}
\begin{split}
\Braket{\widetilde{\Omega}_1 | \widetilde{\Omega}_2 }
&=\int \mathrm{d}\left(\bar{z},z \right) \exp\left(- \bar{z}^\top z \right) \exp\left(- \frac{1 }{2 }  z^\top f^{(1)*} z \right) \exp\left(\frac{1 }{2 } \bar{z}^\top f^{(2)} \bar{z} \right) \\
&=\left(-1 \right)^{N(N-1)/2} \int \prod_{i=1}^{2N} \mathrm{d}Z_i \exp\left(\frac{1 }{2 }  Z^\top M Z \right) \\
&=\left(-1 \right)^{N(N-1)/2} \int \prod_{i=1}^{2N} \mathrm{d}Z_i \exp\left(-\frac{1 }{2 }  Z^\top \left(-M \right) Z \right) \\
&=\left(-1 \right)^{N(N-1)/2} \mathrm{Pf}(-M) \\
&=\left(-1 \right)^{N(N-1)/2} \cdot (-1)^N \mathrm{Pf}(M) \\
&=\left(-1 \right)^{N(N+1)/2}\mathrm{Pf}(M) \\
\end{split}
\end{equation}
$$