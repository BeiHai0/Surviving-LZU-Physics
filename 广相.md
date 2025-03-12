# 第1章 拓扑空间简介

#### 映射

设 $X,Y $ 为非空集合。一个从 $X $ 到 $Y $ 的映射（记作 $f:X\to Y $）是一个法则，它给 $X $ 的**每一**元素指定 $Y $ 的唯一的对应元素。若 $y\in Y $ 是 $x\in X $ 的对应元素，就写为 $y=f(x) $，并称 $y $ 为 $x $ 在映射 $f $ 下的像，称 $x $ 为 $y $ 的原像（或逆像）。$X $ 称为映射 $f $ 的定义域，$X $ 的全体元素在映射 $f $ 下的像的集合（记作 $f[X] $）称为映射 $f:X\to Y $ 的值域。

#### 一一映射

映射 $f:X\to Y $ 叫一一的（one-to-one），若任一 $y\in Y $ 有不多于一个逆像。

若 $f $ 为一一映射，则存在逆映射 $f^{-1}:f[X]\to X $

不论 $f:X\to Y $ 是否有逆，都可定义任一子集 $B\sub Y $ 在 $f $ 下的“逆像”（这里带引号的“逆像”是一个集合）$f^{-1}[B] $ 为：

$$
f^{-1}[B]:=
\{x\in X|f(x)\in B \}\sub X
$$

#### 到上映射

映射 $f:X\to Y $ 叫到上的（onto），若任一 $y\in Y $ 都有逆像（可多于一个）。

#### 拓扑

非空集合 $X $ 的一个拓扑（topology）$\mathscr{T} $ 是 $X $ 的若干子集的集合，满足：

（1）$X,\varnothing\in \mathscr{T} $

（2）若 $O_i\in \mathscr{T},i=1,2,\cdots,n $，则 $\displaystyle{\bigcap\limits_{i=1}^{n} O_i\in \mathscr{T} }$ 

（3）若 $O_\alpha\in \mathscr{T}\forall \alpha $，则 $\displaystyle{\bigcup\limits_{\alpha} O_\alpha \in \mathscr{T} }$ 

指定了拓扑 $\mathscr{T} $ 的集合 $X $ 称为拓扑空间。

拓扑空间 $X $ 的子集 $O $ 称为开子集，若 $O\in \mathscr{T} $ 。

#### 离散拓扑

设 $X $ 为任意非空集合，令 $\mathscr{T} $ 为集合 $X $ 的全部子集的集合，则 $\mathscr{T} $ 称为离散拓扑。

#### 凝聚拓扑

$\mathscr{T}=\{X,\varnothing \} $

#### 通常拓扑

设 $X=\R^n $，则 $\mathscr{T}_{\mathrm{u}}:=\{空集或 \R^n 中能表示为开球之并的子集 \} $ 称为 $\R^n $ 的通常拓扑（usual topology）。

开球（open ball）定义为 $B(x_0,r):=\{x\in \R^n|~|x-x_0|<r \} $，$x_0 $ 称为球心，$r>0 $ 称为半径。

在把 $\R^n $ 看作拓扑空间时，若无声明就是指 $(\R^n,\mathscr{T}) $

#### 乘积拓扑（product topology）

设 $(X_1,\mathscr{T}_1),(X_2,\mathscr{T}_2) $ 为拓扑空间，$X=X_1\times X_2 $，定义 $X $ 的拓扑为：

$$
\mathscr{T}
:=\{O\subset|O 可表示为 O_1\times O_2 的子集之并,O_1\in \mathscr{T}_1,O_2\in \mathscr{T}_2  \}
$$

#### 诱导拓扑和拓扑子空间

设 $(X,\mathscr{T}) $ 是拓扑空间，$A $ 为 $X $ 的任一非空子集。$A $ 的、由 $\mathscr{T} $ 导出的诱导拓扑，记为 $\mathscr{S} $，定义为：

$$
\mathscr{S}
:=\{V\sub A|\exist O\in \mathscr{T}~使~V=A\bigcap O  \}
$$

可以证明，这样定义的诱导拓扑 $\mathscr{S} $ 满足拓扑的定义。

$(A,\mathscr{S}) $ 称为 $(X,\mathscr{T}) $ 的拓扑子空间。

#### 映射的连续性

设 $(X,\mathscr{T}) $ 和 $(Y,\mathscr{S}) $ 为拓扑空间。映射 $f:X\to Y $ 称为连续的，若 $f^{-1}[O]\in\mathscr{T}~~\forall O\in \mathscr{S} $

#### 映射的连续性另一种说法



#### 互相同胚

拓扑空间 $(X,\mathscr{T}) $ 和 $(Y,\mathscr{S}) $ 称为互相同胚，若 $\exist $ 映射 $f:X\to Y $，满足：

(a) $f $是一一到上的；

(b) $f $ 及 $f^{-1} $ 都连续。

这样的 $f $ 称为从 $(X,\mathscr{T}) $ 到 $(Y,\mathscr{S}) $ 的同胚映射，简称同胚。

#### 开覆盖

$X $ 的开子集的集合 $\{O_\alpha \} $ 叫 $A\sub X $ 的一个开覆盖，若 $A\sub \bigcup\limits_{\alpha} O_\alpha $，也可说 $\{O_\alpha \} $ 覆盖 $A $



# 第2章 流形和向量场

## 微分流形

### $n $ 维微分流形

拓扑空间 $(M,\mathscr{T}) $ 称为 $n $ 维微分流形，简称 $n $ 维流形，若 $M $ 有开覆盖 $\{O_\alpha \} $，即 $M=\bigcup\limits_{\alpha} O_\alpha $ 满足：

(a) 对每一 $O_\alpha $ $\exist $ 同胚 $\psi_\alpha:O_\alpha\to V_\alpha $（$V_\alpha $ 是 $\R^n $ 用通常拓扑衡量的开子集）；

(b) 若 $O_\alpha\bigcap O_{\beta}\ne \varnothing $，则复合映射 $\psi_\beta \circ\psi_\alpha^{-1} $ 是 $\mathrm{C}^{\infty} $ 光滑的。

- $\psi_\beta \circ\psi_\alpha^{-1} $ 是从 $\psi_\alpha[O_\alpha\bigcap O_\beta] \sub \R^n $ 到 $\psi_\beta[O_\alpha\bigcap O_\beta] \sub \R^n  $ 的映射。

- 设 $p\in O_\alpha $，则 $\psi_\alpha(p)\in \R^n $，故 $\psi_\alpha(p) $ 点有 $n $ 个自然坐标。把这 $n $ 个数称为 $p $ 点在映射 $\psi_\alpha $ 下获得的坐标。

- 若 $O_\alpha\bigcap O_\beta\ne \varnothing $，则 $O_\alpha\bigcap O_\beta $ 内的点既可通过 $\psi_\alpha $ 又可通过 $\psi_\beta $ 获得坐标，这两组坐标一般不同。$(O_\alpha,\psi_\alpha) $ 构成一个（局域）坐标系，其坐标域为 $O_\alpha $；$(O_\beta,\psi_\beta) $ 构成另一坐标系，其坐标域为 $O_\beta $。$O_\alpha\bigcap O_\beta $ 内的点至少有两组坐标，分别记作 $\{x^\mu \} $ 和 $x'^{\nu}(\mu,\nu=1,2,\cdots,n) $

由映射 $\psi_\beta\circ\psi_\alpha^{-1} $ 提供的、体现两组坐标之间关系的 $n $ 个 $n $ 元函数

$$
x'^{1}=x'^{1}(x^1,\cdots,x^n),\cdots,x'^{n}=x'^{n}(x^1,\cdots,x^n)
$$

就称为一个坐标变换。

坐标系 $(O_\alpha,\psi_\alpha) $ 在数学上又称为图。满足 $n $ 维微分流形定义条件 (a)(b) 的全体图的集合 $\{(O_\alpha,\psi_\alpha) \} $ 称为图册。条件 (b) 又叫相容性条件。图册中任意两个图都是相容的。

$f:M\to M' $ 称为 $\mathbb{C}^r $ 类映射，若 $\forall p\in M $，映射 $\psi'_\beta\circ f\circ \psi_\alpha^{-1} $ 对应的 n' 个 $n $ 元函数是 $\mathbb{C}^r $  类的。




