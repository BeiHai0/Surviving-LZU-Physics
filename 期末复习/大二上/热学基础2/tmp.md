# 热力学部分重点公式

> 这一部分的所有公式可由勒让德变换导出。

## 勒让德变换

理论力学中，我们把拉格朗日量 $L(q,\dot{q},t) $ 关于广义速度 $\dot{q} $ 的勒让德变换定义为哈密顿量 $H(q,p,t) $，也即：

$$
H(q,p,t)
\equiv p \dot{q} - L,\quad
$$

其中，$p\equiv \partial L/\partial \dot{q} $ 称为广义速度的共轭动量，或广义动量。

拉格朗日力学中的运动方程——欧拉-拉格朗日方程

$$
\frac{\partial L }{\partial q } - \frac{\mathrm{d} }{\mathrm{d}t } \frac{\partial L }{\partial \dot{q} } 
=0
$$

等价于哈密顿力学中的哈密顿正则运动方程：

$$
\dot{q}
=\frac{\partial H}{\partial p } ,\quad
\dot{p}
=-\frac{\partial H }{\partial q } 
$$

---

一般地，设量 $O $ 依赖于变量 $x_1,x_2,x_3 $，即

$$
O
=O(x_1,x_2,x_3)
$$

设 $O $ 关于 $x_1,x_2,x_3 $ 的共轭动量分别为 $y_1,y_2,y_3$，即

$$
y_1\equiv \frac{\partial O }{\partial x_1 } ,\quad
y_2\equiv \frac{\partial O }{\partial x_2 } ,\quad
y_3\equiv \frac{\partial O }{\partial x_3 }
$$

则 $O $ 关于变量 $x_1 $ 的勒让德变换 $\tilde{O} $ 定义为：

$$
\tilde{O}(y_1,x_2,x_3)
=y_1 x_1 - O
=\frac{\partial O }{\partial x_1 } x_1 - O
$$

---

热力学中，假设 $O $ 是某个热力学量。

为了方便，$O $ 关于变量 $x_1 $ 的勒让德变换 $\tilde{O} $ 定义多一个负号：

$$
\boxed{
\tilde{O}(y_1,x_2,x_3)
\equiv O - \frac{\partial O }{\partial x_1 } x_1
}
$$

## 内能、自由能、

### 内能

我们知道，内能 $U $ 满足的热力学基本微分方程为：

$$
\boxed{
\mathrm{d}U
=T\mathrm{d}S - p\mathrm{d}V + \mu \mathrm{d}N
}
$$

从上式可见，内能 $U $ 是 $S,V,N $ 的函数

$$
U=U(S,V,N)
$$

偏微分关系为：

$$
\boxed{
\left(\frac{\partial U }{\partial S }  \right)_{V,N}
=T,\quad
\left(\frac{\partial U }{\partial V }  \right)_{S,N}
=-p,\quad
\left(\frac{\partial U }{\partial N }  \right)_{S,V}
=\mu
}
$$

### 焓

把内能 $U(S,V,N) $ 关于 $V $ 的勒让德变换定义为焓 $H(S,p,V) $，即：

$$
H(S,p,N)
\equiv U - \left(\frac{\partial U}{\partial V } \right)_{S,N} V 
=U + pV
$$

焓 $H $ 满足的热力学基本微分方程为：

$$
\mathrm{d}H
=\mathrm{d}U + p\mathrm{d}V + V\mathrm{d}p
=\left(T\mathrm{d}S - p\mathrm{d}V + \mu \mathrm{d}N \right) + p\mathrm{d}V + V\mathrm{d}p
=T\mathrm{d}S + V\mathrm{d}p + \mu\mathrm{d}N
$$

总结一下：

$$
\boxed{
H = H(S,p,N),\quad
H \equiv U + pV,\quad
\mathrm{d}H = T\mathrm{d}S + V\mathrm{d}p + \mu\mathrm{d}N
}
$$

### 亥姆霍兹自由能

把内能 $U(S,V,N) $ 关于 $S $ 的勒让德变换定义为亥姆霍兹自由能 $F(T,V,N) $，即：

$$
F(T,V,N)
\equiv U - \left(\frac{\partial U }{\partial S }  \right)_{V,N} S
=U - TS
$$

亥姆霍兹自由能 $F $ 满足的热力学基本微分方程为：

$$
\mathrm{d}F
=\mathrm{d}U - T\mathrm{d}S - S\mathrm{d}T
=\left(T\mathrm{d}S - p\mathrm{d}V + \mu \mathrm{d}N \right) - T\mathrm{d}S - S\mathrm{d}T
=-S\mathrm{d}T -p\mathrm{d}V + \mu\mathrm{d}N
$$

总结一下：

$$
\boxed{
F = F(T,V,N),\quad
F \equiv U - TS,\quad
\mathrm{d}F = -S\mathrm{d}T -p\mathrm{d}V + \mu\mathrm{d}N
}
$$

### 吉布斯自由能

把内能 $U(S,V,N) $ 关于 $S,V $ 的勒让德变换定义为吉布斯自由能 $G(T,p,N) $，即：

$$
G(T,p,N)
\equiv U - \left(\frac{\partial U }{\partial S }  \right)_{V,N} S - \left(\frac{\partial U}{\partial V } \right)_{S,N} V 
=U - TS + pV
$$

吉布斯自由能 $G $ 满足的热力学基本微分方程为：

$$
\mathrm{d}G
=\mathrm{d}U - T\mathrm{d}S - S\mathrm{d}T + p\mathrm{d}V + V\mathrm{d}p
=\left(T\mathrm{d}S - p\mathrm{d}V + \mu \mathrm{d}N \right) - T\mathrm{d}S - S\mathrm{d}T + p\mathrm{d}V + V\mathrm{d}p
=-S\mathrm{d}T + V\mathrm{d}p + \mu\mathrm{d}N
$$

总结一下：

$$
\boxed{
G = G(T,p,N),\quad
G \equiv U - TS + pV,\quad
\mathrm{d}G = -S\mathrm{d}T + V\mathrm{d}p + \mu\mathrm{d}N
}
$$

### 巨热力学势

把内能 $U(S,V,N) $ 关于 $S,N $ 的勒让德变换定义为巨热力学势 $J(T,V,\mu) $，即：

$$
J(T,V,\mu)
\equiv U - \left(\frac{\partial U }{\partial S }  \right)_{V,N} S - \left(\frac{\partial U }{\partial N }  \right)_{S,V} N
=U - TS - \mu N
$$

巨热力学势 $J $ 满足的热力学基本微分方程为：

$$
\begin{aligned}
\mathrm{d}J
=\mathrm{d}U - T\mathrm{d}S - S\mathrm{d}T - \mu\mathrm{d}N - N\mathrm{d}\mu
=\left(T\mathrm{d}S - p\mathrm{d}V + \mu \mathrm{d}N \right) - T\mathrm{d}S - S\mathrm{d}T - \mu\mathrm{d}N - N\mathrm{d}\mu
=-S\mathrm{d}T - p\mathrm{d}V - N\mathrm{d}\mu
\end{aligned}
$$

总结一下：

$$
\boxed{
J = J(T,V,\mu),\quad
J \equiv -S\mathrm{d}T - p\mathrm{d}V - N\mathrm{d}\mu,\quad
\mathrm{d}J = -S\mathrm{d}T - p\mathrm{d}V - N\mathrm{d}\mu
}
$$