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
\left[A \right]_{2N \times 2N}
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

考虑构型 $\left\{u_{jk}=1\right\} $，其中 $j $ 属于 $A $ 子格，$k $ 属于 $B $ 子格，那么 $\left[A \right]_{2N \times 2N} $ 的具体形式为？

---

考虑加磁场后

$$
\begin{aligned}
H^{(3)}_{\mathrm{eff}}
=-\kappa \sum_{jkl} \sigma_j^x \sigma_k^y \sigma_l^z
=\frac{\mathrm{i} }{4 }
\begin{bmatrix}
c_{1,A} &\cdots &c_{N,A} &c_{1,B} &\cdots c_{N,B}
\end{bmatrix}
\left[A^{(3)} \right]_{2N \times 2N}
\begin{bmatrix}
c_{1,A} \\
\cdots \\
c_{N,A} \\
c_{1,B} \\
\cdots \\
c_{N,B}
\end{bmatrix}
\end{aligned}
$$

考虑构型 $\left\{u_{jk}=1\right\} $，其中 $j $ 属于 $A $ 子格，$k $ 属于 $B $ 子格，那么 $\left[A^{(3)} \right]_{2N \times 2N} $ 的具体形式为？

```
import numpy as np

def build_A3(Lx, Ly, bc_x='PBC', bc_y='PBC', kappa=0.1):
    """
    构造与kappa相关的A^(3)矩阵
    """
    N = Lx * Ly  # 每个子格点数量
    A3 = np.zeros((2*N, 2*N))
    
    def idx(x, y, sub):
        # sub=0 -> A, sub=1 -> B
        return x + y*Lx + sub*N

    for x in range(Lx):
        for y in range(Ly):
            j = idx(x, y, 0)  # A子格
            
            # k：右边B子格
            kx, ky = x+1, y
            if kx >= Lx:
                if bc_x=='PBC':
                    kx = 0
                else:  # APBC
                    kx = 0
                    sign_x = -1
            else:
                sign_x = 1
            k = idx(kx, ky, 1)
            
            # l：上方B子格
            lx, ly = x, y+1
            if ly >= Ly:
                if bc_y=='PBC':
                    ly = 0
                else:
                    ly = 0
                    sign_y = -1
            else:
                sign_y = 1
            l = idx(lx, ly, 1)
            
            # 总边界符号
            sign = 1
            if 'sign_x' in locals():
                sign *= sign_x
            if 'sign_y' in locals():
                sign *= sign_y
            # 清理locals避免影响下一轮
            if 'sign_x' in locals(): del sign_x
            if 'sign_y' in locals(): del sign_y
            
            # j->k->l 顺序，反对称
            A3[j,k] +=  kappa * sign
            A3[k,l] +=  kappa * sign
            A3[l,j] +=  kappa * sign
            A3[k,j] -=  kappa * sign
            A3[l,k] -=  kappa * sign
            A3[j,l] -=  kappa * sign
    
    return A3

# 示例
Lx, Ly = 4, 4
A_pp = build_A3(Lx, Ly, bc_x='PBC', bc_y='PBC')
A_ap = build_A3(Lx, Ly, bc_x='APBC', bc_y='PBC')
A_pa = build_A3(Lx, Ly, bc_x='PBC', bc_y='APBC')
A_aa = build_A3(Lx, Ly, bc_x='APBC', bc_y='APBC')

print("A_pp shape:", A_pp.shape)

```