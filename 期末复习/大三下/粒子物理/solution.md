> 真不会写啊！老学长们太不容易了。现在的期末题应该没这么难吧。。。

# 一、简答题

## 1

> 请叙述⾃然界中的四种基本相互作⽤，并⽐较各种相互作⽤的强弱。

PPT 167

||强相互作用|电磁相互作用|弱相互作用|引力相互作用|
|:---:|:---:|:---:|:---:|:---:|
|力程|$\sim 10^{-15}~\mathrm{m} $|$\infty $|$\sim 10^{-18}~\mathrm{m} $|$\infty $|
|作用强度|$0.15 $|$0.0073 $|$6.34\times 10^{-10} $|$5.90\times 10^{-30} $|
|媒介粒子|介子、胶子|光子|$W^+,W^-,Z^0 $|引力子|

## 2

> 请在⾃然单位制中将室温⽤ $\mathrm{GeV,s(秒),fm(费米)} $ 表示。

PPT 104；另外，PPT 上 $\mathrm{1~eV=(\cdots)^{-1}~K} $ 写错了。

室温 $T\approx 300~\mathrm{K} .$

根据自然单位制温度和能量换算关系

$$
\mathrm{1~K \approx 8.62\times 10^{-5} ~eV}
$$

$$
\mathrm{
T
\approx 300~K
=300\times 8.62\times 10^{-5} ~eV
\approx 2.59\times 10^{-2}~eV
=2.59\times 10^{-11}~GeV
}
$$

根据自然单位制时间和能量换算关系

$$
\mathrm{1~\left(MeV  \right)^{-1} \approx 6.58\times 10^{-22}~s  }  
$$

$$
\mathrm{
T
\approx 2.59\times 10^{-11}~GeV
=2.59\times 10^{-8}~MeV
=2.59\times 10^{-8}\cdot \frac{1 }{6.58\times 10^{-22} }~s^{-1}
\approx 3.94\times 10^{13}~s^{-1}
}
$$

根据自然单位制时间和长度换算关系

$$
\mathrm{1~s = 3\times 10^{8}~m}
$$

$$
\mathrm{
T
\approx 3.94\times 10^{13}~s^{-1}
=\frac{3.94\times 10^{13} }{3\times 10^8 }~m^{-1}
\approx 1.31\times 10^{5}~m^{-1}
=1.31\times 10^5 \left(10^{15}~fm \right)^{-1}
=1.31\times 10^{-10}~\mathrm{fm}^{-1}
}
$$

## 3

> 在美国费⽶实验室的 Tevatron 对撞机上 $p \bar{p} \to W^+ $ 的散射截面是 $\sigma = 10~\mathrm{nb} $，并且实验亮度为 $\mathcal{L}=10^{31}~\mathrm{cm^{-2}s^{-1}} $，请问，⼀年内 $(\sim 10^7~\mathrm{s}) $ 可以产⽣多少个 $W^+ $ 玻色子？

$$
N
=\sigma \mathcal{L} t
$$

其中 $N $ 是某过程产生的事件数；$\sigma $ 是散射截面；$\mathcal{L} $ 是亮度；$t $ 是持续时间。

$$
\mathrm{1~b = 10^{-24}~cm^2},\quad
\mathrm{1~nb = 10^{-9}~b = 10^{-33}~cm^2}
$$

$$
\begin{aligned}
N
=\sigma \mathcal{L} t
=\mathrm{\left(10 \times 10^{-33}~cm^2 \right) \times \left(10^{31}~cm^{-2}s^{-1} \right) \times \left(10^7~s \right) }
=10^6
\end{aligned}
$$

## 4

> 请说明光子质量项 $m_\gamma^2 A_\mu A^\mu $ 破坏 $\mathrm{U(1)} $ 规范对称性。

规范变换：

$$
A_\mu\to A_\mu - \partial_\mu \alpha
$$

光子质量项的变换：

$$
\begin{aligned}
m_\gamma^2 A_\mu A^\mu
\to m_\gamma^2 \left(A_\mu - \partial_\mu \alpha \right) \left(A^\mu - \partial^\mu \alpha \right)
\ne m_\gamma^2 A_\mu A^\mu
\end{aligned}
$$

## 5

> 请说明深度非弹散射过程 $e^- p \to e^- X $ 中观测到的 Bjorken 标度不变性，并阐述如何使⽤费曼部分子模型解释此标度不变性。

> GPT 生成

**1. 深度非弹散射过程概述**

深度非弹散射 (Deep Inelastic Scattering, DIS) 是指高能电子与质子碰撞过程：

$$
e^- (k) + p (P) \to e^- (k') + X,
$$

其中 \(X\) 是质子碎裂后产生的多粒子末态，动量转移为

$$
q = k - k', \quad Q^2 \equiv -q^2,
$$

满足 \(Q^2 \gg m_p^2\)，体现了高能深度探测。

**2. Bjorken 标度变量定义**

定义无量纲变量

$$
x \equiv \frac{Q^2}{2 P \cdot q},
$$

称为 Bjorken 变量，物理上对应质子内部分子的动量分数。

**3. Bjorken 标度不变性**

实验观测到，在高 \(Q^2\) 和大能量传递极限下，结构函数（描述质子内部结构的函数）

$$
F_1(x, Q^2), \quad F_2(x, Q^2)
$$

表现出对 \(Q^2\) 的依赖非常弱，即近似只依赖于 Bjorken \(x\)：

$$
F_i(x, Q^2) \approx F_i(x),
$$

这称为 **Bjorken 标度不变性（Scaling）**。

**4. 费曼部分子模型的解释**

费曼部分子模型将质子视为由近自由的点状部分子（quarks）组成：

- 质子在高能散射过程中表现为一束携带动量分数 \(x\) 的部分子。
- 高能电子与这些部分子弹性散射。
- 由于部分子近自由，散射过程瞬时，电子“看到”的是一个带有固定动量分数的自由粒子。
- 结构函数由部分子动量分布函数 \(f_i(x)\) 给出：

$$
F_2(x) = \sum_i e_i^2 x f_i(x),
$$

其中 \(e_i\) 是第 \(i\) 种部分子的电荷。

**5. 标度不变性的物理含义**

- 部分子模型中，结构函数仅由部分子分布决定，与 \(Q^2\) 无关（忽略 QCD 进化效应）。
- 因此，在大能量极限，结构函数显示标度不变，即不随探测能量尺度改变。
- 这反映了部分子是点状且近自由的属性。

**总结**

DIS 中的 Bjorken 标度不变性说明质子内部结构在高能下表现为独立的点状部分子。费曼部分子模型通过将质子视为含有不同动量分数的自由部分子，成功解释了结构函数对 \(Q^2\) 的弱依赖性，从而解释了标度不变性。

## 6

> 考虑正负电子对撞机上 $e^+ e^- \to \mu^+ \mu^- $ 对产生过程，请在同⼀图形中画出 $N_\nu=3 $ 和 $N_\nu=4 $ 两种情况下的 $\mu^+ \mu^- $ 的不变质量，其中 $N_\nu $ 是无质量中微子的种类数目。

> Gemini生成

在正负电子对撞机上 $e^+ e^- \to \mu^+ \mu^-$ 对产生过程主要通过两种机制发生：

1.  **电磁相互作用：** 通过一个虚光子 ($\gamma^*$) 交换。
2.  **弱相互作用：** 通过一个虚 $Z^0$ 玻色子交换。

$\mu^+ \mu^-$ 的**不变质量** $M_{\mu\mu}$ 就是对撞的质心系能量 $\sqrt{s}$。在 $e^+ e^-$ 对撞机上，这个能量是可调的。

$N_\nu$ 的影响:

无质量中微子的种类数目 ($N_\nu$) 会影响 $Z^0$ 玻色子的**总宽度 (total decay width) $\Gamma_Z$**。$Z^0$ 玻色子可以通过多种途径衰变，包括衰变为中微子-反中微子对 ($Z^0 \to \nu\bar{\nu}$)。

$Z^0$ 玻色子的总宽度可以表示为：
$$\Gamma_Z = \Gamma_{\text{hadronic}} + \Gamma_{\text{leptonic}} + N_\nu \Gamma_{\nu\bar{\nu}}$$
其中：
* $\Gamma_{\text{hadronic}}$ 是 $Z^0$ 衰变为强子的宽度。
* $\Gamma_{\text{leptonic}}$ 是 $Z^0$ 衰变为带电轻子对（如 $e^+e^-$, $\mu^+\mu^-$, $\tau^+\tau^-$）的宽度。
* $\Gamma_{\nu\bar{\nu}}$ 是 $Z^0$ 衰变为单一中微子-反中微子对的宽度。

$Z^0$ 玻色子的总宽度 $\Gamma_Z$ 越小，它在共振峰处的寿命就越长，峰值就越高。反之，宽度越大，峰值就越低，共振曲线越宽。

理论预测：$\mu^+ \mu^-$ 产生截面与 $N_\nu$:

$e^+ e^- \to \mu^+ \mu^-$ 过程的总截面 $\sigma(e^+ e^- \to \mu^+ \mu^-)$，作为 $\sqrt{s}$（即 $\mu^+ \mu^-$ 不变质量）的函数，在 $Z^0$ 玻色子的质量附近会有一个显著的共振峰。这个共振峰的高度和形状与 $Z^0$ 玻色子的参数密切相关。

当 $N_\nu$ 增加时，$\Gamma_Z$ 会增加，这将导致 $Z^0$ 共振峰的**峰值降低**，而**峰宽变宽**。

$$\sigma(e^+ e^- \to \mu^+ \mu^-) \propto \frac{s}{(s - M_Z^2)^2 + s^2 (\Gamma_Z/M_Z)^2}$$
其中，$M_Z$ 是 $Z^0$ 玻色子的质量。当 $s = M_Z^2$ 时，截面达到峰值，峰值与 $1/\Gamma_Z^2$ 成正比。

图形绘制:

要在同一图中画出 $N_\nu=3$ 和 $N_\nu=4$ 两种情况下的 $\mu^+ \mu^-$ 不变质量分布（即截面作为 $\sqrt{s}$ 的函数），我们可以预期：

1.  **共振峰位置：** 两种情况下的共振峰都将出现在相同的能量位置，即 $M_Z \approx 91.1876 \text{ GeV}$。
2.  **峰值高度：** $N_\nu=4$ 时的峰值将**低于** $N_\nu=3$ 时的峰值，因为 $N_\nu=4$ 意味着更大的 $\Gamma_Z$。
3.  **峰宽：** $N_\nu=4$ 时的峰将略微**更宽**，因为更大的 $\Gamma_Z$ 会导致更宽的共振。

## 7

> 请说明为什么 $\tau^- $ 轻子衰变道 $\tau^- \to \nu_\tau e^- \bar{\nu}_e $ 的分支比是 $20\%. $（提示：画出费曼图分析）

> GPT 生成

**1. 衰变过程及费曼图**

主导过程为弱相互作用，费曼图如下：

$$
\tau^- \to \nu_\tau + W^{-*} \to \nu_\tau + \left( e^- \bar{\nu}_e \right),
$$

即 \(\tau^-\) 先发射虚拟的 \(W^-\) 玻色子，\(W^-\) 再衰变成 \(e^- \bar{\nu}_e\)。

**2. 理论分析**

- \(\tau^-\) 衰变主要通过弱电流相互作用，过程类似于 \(\mu^-\) 衰变，但质量更大，允许更多衰变通道。
- \(W^-\) 虚粒子的衰变模式有三类：

  1. **电子通道**：$$W^- \to e^- \bar{\nu}_e$$
  
  2. **μ子通道**：$$W^- \to \mu^- \bar{\nu}_\mu$$
  
  3. **强子通道**：$$W^- \to \text{各种强子通道（主要是轻夸克对）}$$

**3. 分支比估算**

- 由于弱电流对三代轻子耦合相同，电子和μ子衰变通道分支比近似相等，各占约 \(10\%\)。
- 剩余约 \(70\%\) 衰变到强子通道（夸克颜色自由度为3），导致强子衰变概率较大。

总结：

$$
\mathrm{Br}(\tau^- \to \nu_\tau e^- \bar{\nu}_e) \approx \frac{1}{3} \times (1 - \text{强子衰变比}) \approx 20\%.
$$

**4. 具体数值匹配**

- 实验测得电子通道衰变分支比约 \(17.8\%\)。
- 结合 μ子通道和强子通道分布，符合上述理论估计。

**结论**

由于虚拟 \(W^-\) 衰变到电子、μ子、夸克三种主要通道，颜色自由度和相同电弱耦合导致电子通道衰变分支约为 \(20\%\)，这与实验结果一致。

## 8

> 请说明实验上如何发现下列粒子（任选5个）：（1）电子；（2）$\mu $ 轻子；（3）$\tau $ 轻子；（4）$\pi $ 介子；（5）粲夸克；（6）底夸克；（7）顶夸克；（8）中微子；（9）$W $ 玻色子；（10）$Z $ 玻色子；（11）希格斯粒子；（12）胶子。

（1）电子：Ch0P9 真空管阴极射线实验中，根据带电粒子在电磁场中偏转的原理，调整电磁场，可测定粒子的速度和质量。1897 年汤姆逊发现电子。

（2）$\mu $ 轻子 Ch0P21：1936年，安德森在宇宙线中发现 $\mu $ 轻子。

（3）$\tau $ 轻子 Ch0P40：1975年，正负电子对撞机上发现 $\tau $ 子。

（4）$\pi $ 介子：Ch0P21 拍摄大量宇宙射线在不同高度穿过乳胶的底片，并对底片中粒子留下的轨迹进行分析。1947 年鲍威尔发现汤川预言的介子，这个介子命名为 $\pi $ 介子。

（5）粲夸克 Ch0P32, Ch3P74：丁肇中等人用质子轰击铍靶的实验中发现一个长寿命的粒子，命名为 $J $ 粒子；Burton Richter 等人在正负电子对撞实验中也发现一个长寿命的粒子，命名为 $\psi $ 粒子。两组人发现的是同一个粒子，现在称为 $J/\psi $ 粒子。

（6）底夸克 Ch0P33：1977年，莱昂·莱德曼等人400 GeV 的质子束撞击固定靶（铜或铂）发现新粒子 $\Upsilon $，这是由底夸克构成的束缚态。

（7）顶夸克 Ch0P34：质子-反质子对撞机上发现一个最重的夸克，称为顶夸克。

（8）中微子 Ch0P38：1956年，莱因斯和考恩用核反应堆发出的反中微子和质子碰撞，第一次直接证实了中微子的存在。

（9）$W $ 玻色子 Ch0P50：1983年，欧洲核子中心的质子-反质子对撞机上发现 $W^\pm $ 粒子。

（10）$Z $ 玻色子 Ch0P50：质子-反质子对撞机，把加速器束流亮度提高10倍后找到 $Z^0 .$

（11）希格斯粒子 Ch0P61：欧洲核子中心 CMS 组合 ATLAS 组发现希格斯粒子。

（12）胶子：

# 二

> 请说明下面哪些过程是可以发生并通过何种相互作用发生。如果某过程被禁戒，请说明原因。

$$
e^+ \mu^- \to e^- \mu^+,\quad \mu^+ \to e^+ \nu_e \bar{\nu}_\mu
$$

$$
p \to n e^+ \nu_e,\quad \Lambda \to p \pi^-
$$

$$
\pi^+ n \to \Lambda K^+,\quad p p \to p p \bar{p} \bar{p}
$$

$$
e^- e^+ \to \mu^- \mu^+,\quad p \to e^+ \gamma
$$

$$
\pi^- \to \mu^- \nu_\mu,\quad K^+ \to \pi^+ \gamma
$$

$e^+ \mu^- \to e^- \mu^+ $：可通过电磁相互作用发生；

$\mu^+ \to e^+ \nu_e \bar{\nu}_\mu $：可通过弱相互作用发生；

$p \to n e^+ \nu_e $：可通过弱相互作用发生；

$\Lambda \to p \pi^- $：可通过弱相互作用发生；

$\pi^+ n \to \Lambda K^+ $：可通过强相互作用发生；

$p p \to p p \bar{p} \bar{p} $：禁戒，违反电荷守恒和重子数守恒；

$e^- e^+ \to \mu^- \mu^+ $：可通过电磁相互作用发生；

$p \to e^+ \gamma $：禁戒，违反重子数守恒；

$\pi^- \to \mu^- \nu_\mu $：可通过弱相互作用发生；

$K^+ \to \pi^+ \gamma $：基本不发生。

# 三

> 实验上观测到强衰变过程 $\rho^0 \to \pi^+ \pi^- $，但没有观测到 $\rho^0 \to \pi^0 \pi^0 $ 衰变。请据此推导出 $\rho $ 的量子数：（1）$G $ 宇称；（2）自旋；（3）内禀宇称，并提供**禁戒** $\rho^0 \to \pi^0 \pi^0 $ 衰变过程的三种不同原因。

（1）强相互作用过程中 G 宇称守恒，G 宇称是相乘性守恒量，$\pi $ 介子 G 宇称为 $-1 $，则 $\rho^0 $ 的 G 宇称为：$G'\left(\rho^0 \right)=G'\left(\pi^+ \right) G'\left(\pi^- \right)=(-1)(-1)=+1 $

（2）$\rho $ 有 $\rho^+,\rho^0,\rho^- $ 三种不同电荷态，因此同位旋为 $I\left(\rho^{\pm,0} \right)=1 $；$\rho^0 $ 介子是纯中性粒子，具有 C 宇称，满足 $G'\left(\rho^0 \right)=(-1)^{I\left(\rho^0 \right)} C'\left(\rho^0 \right) $，因此 $C'\left(\rho^0 \right)=-1 $；$\pi^+ \pi^- $ 是纯中性系统，具有 C 宇称。根据强相互作用 C 宇称守恒，$C'\left(\pi^+ \pi^- \right)=C'\left(\rho^0 \right)=-1 $；$\pi $ 介子自旋为零，因此 $\pi^+ \pi^- $ 系统总自旋为 $S\left(\pi^+ \pi^- \right)=0 $；根据一对正反粒子组成系统满足 $C'=(-1)^{L+S} $ 可知 $\pi^+ \pi^- $ 相对轨道角动量 $L\left(\pi^+ \pi^- \right)=奇数 $；根据反应前后总角动量守恒，反应前只有 $\rho^0 $，不存在轨道角动量，只有自旋对总角动量有贡献。反应后总角动量为 $J\left(\pi^+ \pi^- \right)=L\left(\pi^+ \pi^- \right) + S\left(\pi^+ \pi^- \right)=L\left(\pi^+ \pi^- \right)=奇数 $，因此 $\rho $ 自旋满足：$S\left(\rho^{\pm,0} \right)=奇数 $

（3）一对正反玻色子对组成系统的内禀宇称为 $P'_{内禀}\left(\pi^+\pi^- \right)=+1 $；由于 $L\left(\pi^+\pi^- \right)=奇数$，轨道宇称为 $P'_{轨道}\left(\pi^+ \pi^- \right)=(-1)^{L\left(\pi^+\pi^- \right)}=-1 $，末态总宇称为 $P'_{总}\left(\pi^+\pi^- \right)=P'_{内禀}\left(\pi^+\pi^- \right)P'_{轨道}\left(\pi^+ \pi^- \right)=-1 $；初态单个 $\rho^0 $ 没有轨道宇称，则根据强相互作用宇称守恒，有 $P'_{内禀}\left(\rho^0 \right)=P'_{总}\left(\pi^+\pi^- \right)=-1 .$

三种禁戒的原因：C 宇称不守恒、总角动量不守恒、同位旋对称性限制。

C 宇称不守恒：$\rho^0$ 是C-odd（$C=-1$）的矢量介子，而 $\pi^0$ 是C-even（$C=+1$）的赝标量介子。末态 $\pi^0 \pi^0$ 的总C宇称为 $(+1)^2 = +1$，与初态 $\rho^0$ 的 $C=-1$ 矛盾。

总角动量不守恒：$\rho^0$ 是自旋为 $1$ 的矢量介子，而 $\pi^0$ 是自旋为 $0$ 的赝标量介子。末态 $\pi^0 \pi^0$ 的总角动量只能为 $0$（$L=0$ 的S波态），无法与初态 $\rho^0$ 的自旋 $1$ 匹配。

同位旋对称性限制：$\rho^0$ 属于同位旋三重态（$I=1, I_3=0$），而 $\pi^0$ 的同位旋与 $\rho^0$ 相同。末态 $\pi^0 \pi^0$ 必须满足对称波函数（玻色统计），但 $I=1$ 的两粒子系统无法构成 $I_3=0$ 的对称态（仅 $I=0$ 或 $2$ 允许）。补充：$\rho^0 \to \pi^+ \pi^-$ 允许，因其末态可通过 $I=1$ 的反对称组合实现。

# 四

> 分别列出 $\pi^+ \pi^- \pi^0 $ 和 $\pi^0 \pi^0 \pi^0 $ 的各种同位旋态。

> Gemini 生成

在分析之前，我们需要明确几个核心概念：
1.  **π 介子**: $\pi^+, \pi^0, \pi^-$ 构成一个同位旋三重态，总同位旋量子数 $I=1$。
2.  **同位旋第三分量 ($I_3$)**: 三个电荷态对应不同的同位旋第三分量：
    * $\pi^+: I_3 = +1$
    * $\pi^0: I_3 = 0$
    * $\pi^-: I_3 = -1$
3.  **同位旋耦合**: 多个粒子的总同位旋态由单个粒子的同位旋矢量相加得到，其规则与角动量耦合相同。例如，两个同位旋为 $I_a$ 和 $I_b$ 的粒子，其总同位旋 $I_{total}$ 的可能取值为：
    $$
    I_{total} = |I_a - I_b|, |I_a - I_b| + 1, \dots, I_a + I_b
    $$
4.  **$I_3$ 的可加性**: 系统的总同位旋第三分量是各组分 $I_3$ 的代数和。
    $$
    I_{3, \text{total}} = \sum_i I_{3,i}
    $$
5.  **玻色-爱因斯坦统计**: π 介子是玻色子。对于由**全同粒子**组成的系统（如 $\pi^0 \pi^0 \pi^0$），其总波函数在交换任意两个粒子时必须是对称的。这对可能的量子态构成了强烈的限制。

1 $\pi^+ \pi^- \pi^0$ 系统的同位旋态：

这是一个由三个可区分粒子（电荷不同）组成的系统，因此我们不需要考虑交换对称性的限制，只需进行标准的同位旋耦合计算。

**第一步：计算系统的总 $I_3$**

$$I_{3, \text{total}} = I_3(\pi^+) + I_3(\pi^-) + I_3(\pi^0) = (+1) + (-1) + (0) = 0$$
这意味着最终的总同位旋态 $|I, I_3\rangle$ 必须是 $|I, 0\rangle$ 的形式。

**第二步：耦合三个 $I=1$ 的同位旋**

我们分步进行耦合，记为 $1 \otimes 1 \otimes 1$：
1.  首先耦合 $\pi^+$ 和 $\pi^-$（两个 $I=1$ 的粒子）：
    $$
    I_{12} = |1 - 1|, \dots, 1 + 1 \implies I_{12} = 0, 1, 2
    $$
2.  然后将上述结果与第三个粒子 $\pi^0$（$I=1$）进行耦合：
    * 若 $I_{12}=0$，与 $I=1$ 耦合得到总同位旋 $I_{total} = 1$。
    * 若 $I_{12}=1$，与 $I=1$ 耦合得到总同位旋 $I_{total} = |1-1|, \dots, 1+1 \implies I_{total} = 0, 1, 2$。
    * 若 $I_{12}=2$，与 $I=1$ 耦合得到总同位旋 $I_{total} = |2-1|, \dots, 2+1 \implies I_{total} = 1, 2, 3$。

**第三步：整合所有可能的结果**

将所有可能的值集合起来，我们得到 $\pi^+ \pi^- \pi^0$ 系统可能的总同位旋 $I$ 为：
$$I = 0, 1, 2, 3$$

由于系统的总 $I_3=0$，而以上四个同位旋多重态（$I=0, 1, 2, 3$）都包含 $I_3=0$ 的成员，所以这些态都是允许的。

**结论**:
$\pi^+ \pi^- \pi^0$ 系统可以处于以下总同位旋态：
* $I = 0$
* $I = 1$
* $I = 2$
* $I = 3$

2 $\pi^0 \pi^0 \pi^0$ 系统的同位旋态：

这是一个由三个**全同玻色子**组成的系统。除了同位旋耦合规则外，我们还必须满足玻色-爱因斯坦统计的要求。

**第一步：计算系统的总 $I_3$**

$$I_{3, \text{total}} = I_3(\pi^0) + I_3(\pi^0) + I_3(\pi^0) = 0 + 0 + 0 = 0$$

**第二步：应用玻色-爱因斯坦统计**

系统的总波函数 $\Psi_{\text{total}}$ 必须在交换任意两个 $\pi^0$ 介子时是对称的。总波函数可以分解为空间部分和同位旋部分的乘积：
$$\Psi_{\text{total}} = \Psi_{\text{spatial}} \times \Psi_{\text{isospin}}$$

对于 $\pi^0 \pi^0 \pi^0$ 系统，三个粒子在同位旋空间是完全一样的（都是 $|I=1, I_3=0\rangle$）。因此，其同位旋波函数 $\Psi_{\text{isospin}}$ **天然就是对称的**。

为了使总波函数 $\Psi_{\text{total}}$ 保持对称，空间波函数 $\Psi_{\text{spatial}}$ 也必须是完全对称的。

根据量子力学中角动量耦合的对称性规则，当耦合三个相同的同位旋 $I=1$ 时，得到的总同位旋态具有特定的交换对称性：
* $I=3$ 态：完全对称
* $I=2$ 态：混合对称
* $I=1$ 态：可以构造出完全对称和混合对称的态
* $I=0$ 态：完全反对称

由于 $3\pi^0$ 的同位旋波函数必须是完全对称的，我们只能选择那些可以构成完全对称组合的总同位旋 $I$。对于三个 $I=1$ 的耦合，这些态是：
$$I = 1, 3$$
总同位旋为 $I=0$ 和 $I=2$ 的态无法构成一个对三个全同 $\pi^0$ 全对称的同位旋波函数，因此是被禁止的。

**一个更严格的论证（基于C宇称）**：
一个 $n$ 个 $\pi^0$ 组成的系统，其电荷共轭宇称（C-parity）为 $C = (+1)^n$。对于 $3\pi^0$ 系统，$C=+1$。同时，对于一个中性、非奇异的玻色子系统，C宇称和总角动量 $L$、总同位旋 $I$ 之间有关系 $C = (-1)^{L+I}$。
因此，对于 $3\pi^0$ 系统，必须满足：
$$(-1)^{L+I} = +1 \implies L+I = \text{偶数}$$
此外，由于三个全同玻色子的空间波函数对称性限制，对于 $L=0$（S波）态，系统是不存在的。最低的轨道角动量态要求 $L+I$ 为奇数（这是一个更深入的对称性分析结果）。综合这两个限制，最终得到**总同位旋 $I$ 必须是奇数**。

**结论**:
在 $I=0, 1, 2, 3$ 的可能性中，只有奇数值是允许的。因此，$\pi^0 \pi^0 \pi^0$ 系统可以处于以下总同位旋态：
* $I = 1$
* $I = 3$

总结：

| 系统 | 总 $I_3$ | 关键限制 | 可能的总同位旋 $I$ |
| :--- | :---: | :--- | :--- |
| $\pi^+ \pi^- \pi^0$ | 0 | 无（粒子可区分） | 0, 1, 2, 3 |
| $\pi^0 \pi^0 \pi^0$ | 0 | 玻色-爱因斯坦统计（全同粒子） | 1, 3 |

# 五

> 找出如下总散射截面之间的关系（设同位旋振幅 $A_0,A_1 $ 和 $A_3 $）

(1) $K^- + p \to \pi^+ + \Sigma^- $

(2) $K^- + p \to \pi^0 + \Sigma^0 $

(3) $K^- + p \to \pi^- + \Sigma^+ $

其中，$K^-(I=1/2,I_z=-1/2) $ 和 $\Sigma^{\pm,0}(I=1,I_z=\pm 1,0) $

> GPT 生成

反应过程同位旋分析

考虑以下三个强相互作用过程：

1. $K^- + p \to \pi^+ + \Sigma^-$  
2. $K^- + p \to \pi^0 + \Sigma^0$  
3. $K^- + p \to \pi^- + \Sigma^+$

设总同位旋振幅为 $A_I$，其中 $I=0,1$，我们将使用同位旋叠加和 Clebsch-Gordan 系数来表示各通道的振幅。

初态同位旋

- $K^-$: $I=1/2$, $I_z = -1/2$
- $p$: $I=1/2$, $I_z = +1/2$
- $\Rightarrow$ 总初态：$I=0$ 或 $I=1$

末态同位旋

- $\pi$: $I=1$
- $\Sigma$: $I=1$
- $\Rightarrow$ 总末态：$I=0$, $1$, $2$

但因强相互作用守恒，同位旋在总过程保持守恒，因此只考虑与初态匹配的 $I=0$ 和 $I=1$。

写出每个过程的振幅（用 Clebsch-Gordan 系数）

记总振幅为 $\mathcal{M} = \sum_I A_I \cdot C_I$，其中 $C_I$ 是 Clebsch-Gordan 系数。

过程(1)：$K^- + p \to \pi^+ + \Sigma^-$

- 初态 $I=0,1$，$I_z=0$
- 末态 $\pi^+(I_z=+1)$, $\Sigma^-(I_z=-1)$ ⇒ $I_z=0$
- 振幅为：

$$
\mathcal{M}_1 = A_0 \cdot \braket{1,1;1,-1|0,0} + A_1 \cdot \braket{1,1;1,-1|1,0}
= A_0 \cdot \frac{1}{\sqrt{3}} + A_1 \cdot \frac{1}{\sqrt{2}}
$$

过程(2)：$K^- + p \to \pi^0 + \Sigma^0$

- $\pi^0(I_z=0)$, $\Sigma^0(I_z=0)$ ⇒ $I_z=0$
- 振幅为：

$$
\mathcal{M}_2 = A_0 \cdot \braket{1,0;1,0|0,0} + A_1 \cdot \braket{1,0;1,0|1,0}
= A_0 \cdot \left(-\frac{1}{\sqrt{3}}\right) + A_1 \cdot 0
= -\frac{1}{\sqrt{3}} A_0
$$

过程(3)：$K^- + p \to \pi^- + \Sigma^+$

- $\pi^- (I_z=-1)$, $\Sigma^+(I_z=+1)$ ⇒ $I_z=0$
- 振幅为：

$$
\mathcal{M}_3 = A_0 \cdot \braket{1,-1;1,+1|0,0} + A_1 \cdot \braket{1,-1;1,+1|1,0}
= A_0 \cdot \frac{1}{\sqrt{3}} - A_1 \cdot \frac{1}{\sqrt{2}}
$$

总结三条通道振幅

$$
\begin{aligned}
\mathcal{M}_1 &= \frac{1}{\sqrt{3}} A_0 + \frac{1}{\sqrt{2}} A_1 \\
\mathcal{M}_2 &= -\frac{1}{\sqrt{3}} A_0 \\
\mathcal{M}_3 &= \frac{1}{\sqrt{3}} A_0 - \frac{1}{\sqrt{2}} A_1 \\
\end{aligned}
$$

散射截面关系

设 $\sigma_i \propto |\mathcal{M}_i|^2$，可以写为：

$$
\begin{aligned}
\sigma_1 &\propto \left| \frac{1}{\sqrt{3}} A_0 + \frac{1}{\sqrt{2}} A_1 \right|^2 \\
\sigma_2 &\propto \left| -\frac{1}{\sqrt{3}} A_0 \right|^2 = \frac{1}{3} |A_0|^2 \\
\sigma_3 &\propto \left| \frac{1}{\sqrt{3}} A_0 - \frac{1}{\sqrt{2}} A_1 \right|^2 \\
\end{aligned}
$$

可构造一个组合验证：

$$
\sigma_1 + \sigma_3 = \frac{2}{3}|A_0|^2 + |A_1|^2 \propto 2\sigma_2 + |A_1|^2
$$

这表明测量这些过程可以反推出 $A_1$ 成分的存在。

# 六

> 在未来质心系能量为 $1000~\mathrm{GeV} $ 的正负电⼦直线加速器上，我们期望可观测到⼀对正反顶夸克事例

$$
e^+ e^- \to t \bar{t},\quad
t \to W^+ b,\quad
\bar{t} \to W^- \bar{b}
$$

(1) 请画出顶夸克对产⽣过程的费曼图。

(2) 请说明顶夸克对事例的衰变末态中可以存在2个，4个或6个夸克，并给出每种情况出现的几率。

(3) 考虑如下两种末态：1. 四个夸克、$\mu^+ $；2. 两个夸克、$e^-,\mu^+ $；请画图说明如何在探测器上观测这两种末态。

> GPT 生成

在强子对撞机（如 LHC）中，顶夸克对主要通过以下两种机制产生：

1. **胶子-胶子融合**（占主导）：

$$
g + g \to t + \bar{t}
$$

对应的费曼图包括：

- \(s\)-道图：两胶子融合成一个中间态虚拟胶子，再产生 \(t\bar{t}\) 对；
- \(t\)-道与 \(u\)-道图：一个胶子与另一个胶子的夸克线交换。

2. **夸克-反夸克湮灭**（在质子-反质子对撞中显著）：

$$
q + \bar{q} \to t + \bar{t}
$$

费曼图：

- 单一 \(s\)-道图：通过一个中间态虚拟胶子产生 \(t\bar{t}\) 对。

$$
\text{(2) 顶夸克对衰变末态中可能存在的夸克数与几率}
$$

每个顶夸克几乎总是衰变为一个底夸克和一个 \(W\) 玻色子：

$$
t \to b + W^+, \quad \bar{t} \to \bar{b} + W^-
$$

两个 \(W\) 玻色子可以衰变为：

- **轻子 + 轻子中微子**（轻子衰变）：每个 \(W\) 有 \(e\nu_e, \mu\nu_\mu, \tau\nu_\tau\) 三种轻子衰变方式；
- **夸克 + 反夸克对**（强子衰变）：如 \(u\bar{d}, c\bar{s}\) 等。

考虑两种 \(W\) 的组合：

- **双轻子态**：两个 \(W\) 都轻子衰变，末态中有两个轻子 + 两个底夸克 → **2 个夸克**  
  概率为：

  $$
  \left( \frac{1}{3} \right)^2 = \frac{1}{9}
  $$

- **半轻子态**：一个 \(W\) 轻子衰变，一个 \(W\) 强子衰变，末态有两个轻子 + 两个轻夸克 + 两个底夸克 → **4 个夸克**  
  概率为：

  $$
  2 \times \left( \frac{1}{3} \right) \left( \frac{2}{3} \right) = \frac{4}{9}
  $$

- **全强子态**：两个 \(W\) 都强子衰变，末态有两个底夸克 + 四个轻夸克 → **6 个夸克**  
  概率为：

  $$
  \left( \frac{2}{3} \right)^2 = \frac{4}{9}
  $$

**末态 1：四个夸克 + \mu^+**

对应情形：

- \(t \to b + W^+ \to b + u\bar{d} \)
- \(\bar{t} \to \bar{b} + W^- \to \bar{b} + \mu^- \bar{\nu}_\mu \)

最终状态为：

- 两个底夸克 \(b, \bar{b}\)：在探测器中形成两个 **b-喷注 (b-jets)**；
- 两个轻夸克 \(u, \bar{d}\)：形成两个 **轻喷注 (jets)**；
- 一个高能带电轻子 \(\mu^+\)：在 **μ 子探测器** 中形成明确轨迹；
- 一个中微子 \(\nu_\mu\)：导致 **缺失能量**（missing transverse energy, MET）。

**探测器签名**：

- 4 jets，其中两个可识别为 b-jets；
- 一条 \(\mu^+\) 轨迹；
- 明显 MET。

**末态 2：两个夸克 + \(e^-, \mu^+\)**

对应情形：

- \(t \to b + W^+ \to b + e^+ \nu_e \)
- \(\bar{t} \to \bar{b} + W^- \to \bar{b} + \mu^- \bar{\nu}_\mu \)

最终状态为：

- 两个 b-喷注；
- 一个 \(e^-\)、一个 \(\mu^+\)：分别在 **电磁簇射器** 和 **μ 子探测器** 中留下轨迹；
- 两个中微子：产生较大的 **MET**。

**探测器签名**：

- 2 b-jets；
- 一条 \(e^-\) 轨迹 + 一条 \(\mu^+\) 轨迹；
- 强烈 MET（比半轻子通道更明显）。

# 七

$R_X $ 定义如下：

$$
R_X
\equiv \frac{\sigma\left(e^+ e^- \to X \right) }{\sigma\left(e^+ e^- \to \mu^+ \mu^- \right) } 
$$

考虑下列各种新物理奇异粒子，假设这些奇异粒⼦仅参与QED相互作用。当正负电⼦对撞机具有足够高的能量可以产生⼀对新物理粒子时，请计算相应的 $R $ 值：

(1) $R_L $：$\mathrm{SU}(2) $ 弱同位旋二重态的新轻子 $L $，设其超荷为 $Y=+3 $

$$
L
=\begin{bmatrix}
L_1 \\
L_2
\end{bmatrix}
$$

(2) $R_{Q'} $：$\mathrm{SU}(2) $ 弱同位旋三重态的新夸克 $Q' $，设其超荷为 $Y=+4/3 $

$$
Q'
=\begin{bmatrix}
Q_1' \\
Q_2' \\
Q_3'
\end{bmatrix}
$$

> GPT 生成

设新粒子仅通过 QED 与光子相互作用，我们可以利用 QED 中的对易产生截面公式：

$$
\sigma(e^+e^- \to f\bar{f}) \propto Q_f^2 N_c
$$

其中：
- $Q_f$ 是粒子的电荷，
- $N_c$ 是颜色因子（对于轻子 $=1$，夸克 $=3$）。

归一化对 $\mu^+\mu^-$ 截面得到：

$$
R_X = \sum_i N_c Q_i^2
$$

---

**(1) $R_L$：$\mathrm{SU}(2)$ 弱二重态新轻子，$Y = +3$**

弱双重态的两个分量的电荷由公式

$$
Q = T_3 + \frac{Y}{2}
$$

可得：

- $L_1$: $T_3 = +\frac{1}{2} \Rightarrow Q = \frac{1}{2} + \frac{3}{2} = +2$
- $L_2$: $T_3 = -\frac{1}{2} \Rightarrow Q = -\frac{1}{2} + \frac{3}{2} = +1$

由于是轻子，$N_c = 1$，故：

$$
R_L = 1 \cdot (2)^2 + 1 \cdot (1)^2 = 4 + 1 = 5
$$

---

**(2) $R_{Q'}$：$\mathrm{SU}(2)$ 弱三重态新夸克，$Y = +\frac{4}{3}$**

弱三重态的分量 $T_3 = +1, 0, -1$，电荷为：

- $Q_1'$: $T_3 = +1 \Rightarrow Q = 1 + \frac{2}{3} = \frac{5}{3}$
- $Q_2'$: $T_3 = 0 \Rightarrow Q = 0 + \frac{2}{3} = \frac{2}{3}$
- $Q_3'$: $T_3 = -1 \Rightarrow Q = -1 + \frac{2}{3} = -\frac{1}{3}$

（注：$\frac{Y}{2} = \frac{4}{6} = \frac{2}{3}$）

每个为夸克，$N_c = 3$，故：

$$
R_{Q'} = 3 \left[ \left( \frac{5}{3} \right)^2 + \left( \frac{2}{3} \right)^2 + \left( \frac{1}{3} \right)^2 \right]
= 3 \left[ \frac{25}{9} + \frac{4}{9} + \frac{1}{9} \right]
= 3 \cdot \frac{30}{9}
= 10
$$


# 八

仅考虑QED理论。在非极化的正负电子对撞机上，忽略电子质量时，$e^+ e^- \to \tau^+ \tau^- $ 的散射振幅模方为：

$$
\overline{\left|\mathcal{M} \right|^2}
=\frac{2 e^4 Q_\tau^2 }{\left(p_1 \cdot p_2 \right)^2 } \left[\left(p_1\cdot p_4 \right)\left(p_2\cdot p_3 \right) + \left(p_1\cdot p_3 \right)\left(p_2\cdot p_4 \right) + m_\tau^2\left(p_1\cdot p_2 \right) \right]
$$

其中，$p_{1,2,3,4} $ 分别是 $e^-,e^+,\tau^-,\tau^+ $ 的动量，$Q_\tau $ 是 $\tau $ 轻子电荷。

(1) 令质心系能量为 $\sqrt{s} $，设 $e^- $ 和 $e^+ $ 分别沿 $+\hat{z} $ 和 $-\hat{z} $ 方向入射。请推导 $e^+ e^- $ 质心系中末态 $\tau^- $ 的空间极化角 $\theta $ 的微分散射截面，并计算总散射截面。

(2) 计算前后不对称性

$$
A_{FB}
\equiv \frac{\sigma\left(\cos\theta>0 \right) - \sigma\left(\cos\theta<0 \right) }{\sigma\left(\cos\theta>0 \right) + \sigma\left(\cos\theta<0 \right) } 
$$

并解释物理原因。

(3) 如果光子仅仅和左手手征性的带电轻子相互作用，在忽略电子和 $\tau $ 轻子质量的情况下，请通过螺旋度振幅分析给出散射振幅模方。

(4) 接上问，请写出末态 $\tau^- $ 的空间极化角的微分散射截面，并计算 $A_{FB} .$

(5) 如果 $\tau^\pm  $ 自旋为零，请说明 $\tau^- $ 极化角微分散射截⾯在前后方向处为零。

(6) 如果光子自旋为0，请给出末态 $\tau^- $ 的空间极化角微分分布。

(7) 请写出强子对撞机上 $\tau^+ \tau^- $ 产⽣过程的散射截面。

(8) 考虑 $\tau $ 质量不可忽略的情况。当 $m_\tau=500~\mathrm{GeV} $，请分析在 $\sqrt{s}=2000~\mathrm{GeV} $ 的质子-反质子强子对撞机上价夸克和海夸克的贡献大小；当 $m_\tau=1~\mathrm{GeV} $ 时重复上面分析。

> GPT 生成

$$
\text{(1) 质心系微分截面与总截面推导}
$$

设质心系能量为 \(\sqrt{s}\)，入射电子与正电子动量分别为

$$
p_1 = (E, 0, 0, +E), \quad p_2 = (E, 0, 0, -E), \quad E = \frac{\sqrt{s}}{2}.
$$

末态 \(\tau^-\) 的动量大小为

$$
k = \frac{\sqrt{s}}{2} \beta, \quad \beta = \sqrt{1 - \frac{4 m_\tau^2}{s}}.
$$

利用能量动量守恒，末态粒子能量为

$$
E_3 = E_4 = \frac{\sqrt{s}}{2}.
$$

计算动量点积：

$$
p_1 \cdot p_2 = 2 E^2 = \frac{s}{2}.
$$

末态四动量方向定义 \(\tau^-\) 空间极化角为 \(\theta\)，则

$$
p_1 \cdot p_3 = E E_3 - |\vec{p}_1||\vec{p}_3| \cos \theta = \frac{s}{4} (1 - \beta \cos \theta),
$$

$$
p_1 \cdot p_4 = \frac{s}{4} (1 + \beta \cos \theta),
$$

$$
p_2 \cdot p_3 = \frac{s}{4} (1 + \beta \cos \theta), \quad p_2 \cdot p_4 = \frac{s}{4} (1 - \beta \cos \theta).
$$

将以上代入振幅模方表达式：

$$
\overline{|\mathcal{M}|^2} = \frac{2 e^4 Q_\tau^2}{(p_1 \cdot p_2)^2} \left[ (p_1 \cdot p_4)(p_2 \cdot p_3) + (p_1 \cdot p_3)(p_2 \cdot p_4) + m_\tau^2 (p_1 \cdot p_2) \right].
$$

代入点积结果：

\[
\begin{aligned}
& (p_1 \cdot p_4)(p_2 \cdot p_3) + (p_1 \cdot p_3)(p_2 \cdot p_4) \\
= & \left(\frac{s}{4} (1 + \beta \cos \theta)\right)\left(\frac{s}{4} (1 + \beta \cos \theta)\right) + \left(\frac{s}{4} (1 - \beta \cos \theta)\right)\left(\frac{s}{4} (1 - \beta \cos \theta)\right) \\
= & \frac{s^2}{16} \left[ (1 + \beta \cos \theta)^2 + (1 - \beta \cos \theta)^2 \right] \\
= & \frac{s^2}{16} \left[ 2 + 2 \beta^2 \cos^2 \theta \right] = \frac{s^2}{8} \left(1 + \beta^2 \cos^2 \theta \right).
\end{aligned}
\]

带入质量项：

$$
m_\tau^2 (p_1 \cdot p_2) = m_\tau^2 \cdot \frac{s}{2}.
$$

故振幅模方为

$$
\overline{|\mathcal{M}|^2} = \frac{2 e^4 Q_\tau^2}{(s/2)^2} \left[ \frac{s^2}{8} (1 + \beta^2 \cos^2 \theta) + \frac{m_\tau^2 s}{2} \right] = \frac{8 e^4 Q_\tau^2}{s^2} \left[ \frac{s^2}{8} (1 + \beta^2 \cos^2 \theta) + \frac{m_\tau^2 s}{2} \right].
$$

简化得

$$
\overline{|\mathcal{M}|^2} = e^4 Q_\tau^2 \left[1 + \beta^2 \cos^2 \theta + \frac{4 m_\tau^2}{s} \right].
$$

---

微分截面公式为（无极化，电子近似无质量）

$$
\frac{d\sigma}{d\Omega} = \frac{1}{64 \pi^2 s} \frac{|\vec{p}_3|}{|\vec{p}_1|} \overline{|\mathcal{M}|^2}.
$$

代入

$$
|\vec{p}_3| = \frac{\sqrt{s}}{2} \beta, \quad |\vec{p}_1| = \frac{\sqrt{s}}{2},
$$

得

$$
\frac{d\sigma}{d\Omega} = \frac{1}{64 \pi^2 s} \beta \cdot e^4 Q_\tau^2 \left[1 + \beta^2 \cos^2 \theta + \frac{4 m_\tau^2}{s} \right].
$$

用 \(\alpha = \frac{e^2}{4 \pi}\) 表示精细结构常数

$$
\Rightarrow \frac{d\sigma}{d\Omega} = \frac{\alpha^2 Q_\tau^2 \beta}{4 s} \left[1 + \beta^2 \cos^2 \theta + \frac{4 m_\tau^2}{s} \right].
$$

---

总截面为

$$
\sigma = \int d\Omega \frac{d\sigma}{d\Omega} = 2\pi \int_0^\pi d\theta \sin\theta \frac{d\sigma}{d\Omega}.
$$

积分角度部分：

$$
I = \int_0^\pi \sin \theta \left(1 + \beta^2 \cos^2 \theta\right) d\theta = 2 \left(1 + \frac{\beta^2}{3}\right).
$$

所以总截面

$$
\sigma = \frac{\alpha^2 Q_\tau^2 \beta}{4 s} \cdot 2 \pi \cdot 2 \left(1 + \frac{\beta^2}{3}\right) + \frac{4 m_\tau^2}{s} \times 4 \pi \frac{\alpha^2 Q_\tau^2 \beta}{4 s},
$$

化简为

$$
\sigma = \frac{4 \pi \alpha^2 Q_\tau^2}{3 s} \beta \left(1 - \frac{\beta^2}{3} + \frac{6 m_\tau^2}{s}\right).
$$

---

$$
\text{(2) 前后不对称性 } A_{FB}
$$

定义

$$
A_{FB} = \frac{\sigma(\cos\theta > 0) - \sigma(\cos\theta < 0)}{\sigma(\cos\theta > 0) + \sigma(\cos\theta < 0)}.
$$

纯 QED 过程由光子交换支配，散射振幅关于 \(\cos \theta\) 对称，故

$$
A_{FB} = 0.
$$

物理解释：光子是矢量玻色子，不含手征耦合，正负方向对称。

---

$$
\text{(3) 光子仅与左手带电轻子相互作用的振幅模方}
$$

忽略质量，仅左手手征性参与耦合，采用螺旋度投影算符 \(\frac{1 - \gamma_5}{2}\)。

螺旋度选择规则使散射振幅中只有特定螺旋态非零，计算得到

$$
\frac{d\sigma}{d\Omega} \propto (1 + \cos \theta)^2,
$$

显著偏向前向散射。

---

$$
\text{(4) 只左手相互作用时的前后不对称性}
$$

计算积分

$$
\sigma(\cos\theta > 0) \propto \int_0^1 (1 + x)^2 dx = \frac{7}{3}, \quad \sigma(\cos\theta < 0) \propto \int_{-1}^0 (1 + x)^2 dx = \frac{1}{3}.
$$

故

$$
A_{FB} = \frac{7/3 - 1/3}{7/3 + 1/3} = \frac{6/3}{8/3} = \frac{3}{4}.
$$

---

$$
\text{(5) \(\tau^\pm\) 自旋为零时}
$$

零自旋粒子无内禀方向性，角分布均匀且对称，前后方向微分截面趋近于零。

---

$$
\text{(6) 光子自旋为零时}
$$

若光子自旋为标量，自旋传递被抑制，角分布均匀：

$$
\frac{d\sigma}{d\Omega} = \text{常数}.
$$

---

$$
\text{(7) 强子对撞机上 \(\tau^+ \tau^-\) 产生截面}
$$

强子对撞机中，主要过程为夸克反夸克对产生：

$$
q \bar{q} \to \gamma^*/Z \to \tau^+ \tau^-.
$$

总截面通过PDF加权计算：

$$
\sigma_{pp} = \sum_q \int dx_1 dx_2 \, f_q(x_1, Q^2) f_{\bar{q}}(x_2, Q^2) \hat{\sigma}(q \bar{q} \to \tau^+ \tau^-; \hat{s} = x_1 x_2 s).
$$

---

$$
\text{(8) \(\tau\) 质量效应与价夸克、海夸克贡献分析}
$$

- 当 \(m_\tau = 500~\mathrm{GeV}\), \(\sqrt{s} = 2000~\mathrm{GeV}\)，阈值高，价夸克PDF较大，贡献主导。
- 当 \(m_\tau = 1~\mathrm{GeV}\)，阈值低，低 \(x\) 区域海夸克贡献显著。

质量越大，生产越依赖大 \(x\) 区域的价夸克；质量较小时，海夸克贡献不可忽视。

---
