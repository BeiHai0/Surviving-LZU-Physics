# -*- coding: utf-8 -*-

from kitaev_data_manager import KitaevDataManager
import numpy as np
from pfapack import pfaffian
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# ==============================
# 工具函数
# ==============================

def build_U0_prime_matrix(U0, N):
    I_N = np.eye(N, dtype=complex)
    U0_prime = np.block([
        [I_N, I_N],
        [-1j*I_N, 1j*I_N]
    ]) @ U0

    return (U0_prime[:N, :N], U0_prime[:N, N:],
            U0_prime[N:, :N], U0_prime[N:, N:])


def build_T_1_matrix(N1, N2):
    single_block = np.eye(N1, k=-1)
    single_block[0, N1-1] = -1
    return np.kron(np.eye(N2), single_block)


def build_T_2_matrix(N1, N2):
    single_block = np.eye(N2, k=-1)
    single_block[0, N2-1] = -1
    return np.kron(single_block, np.eye(N1))


# ==============================
# 初始化
# ==============================

manager = KitaevDataManager()

N1, N2 = 20, 20
bc1, bc2 = -1, -1
N = N1 * N2

n1, n2 = N1//2, N2//2

# ===== 晶格 =====
a1 = np.array([1.0, 0.0])
a2 = np.array([0.5, np.sqrt(3)/2])

delta_x = np.array([-0.5, -0.5/np.sqrt(3)])
delta_y = np.array([0.5, -0.5/np.sqrt(3)])
delta_z = np.array([0, 1/np.sqrt(3)])
delta_list = [None, delta_x, delta_y, delta_z]

# ===== 动量 =====
Gamma = np.array([0.0, 0.0])
K = np.array([4*np.pi/3, 0.0])

# ===== 平移矩阵 =====
T_1 = build_T_1_matrix(N1, N2)
T_2 = build_T_2_matrix(N1, N2)


# ==============================
# 主计算
# ==============================

for Kx, Ky, Kz in [(1,1,1), (-1,-1,-1)]:
    for kappa in [0.04]:

        sigma_A_list = []
        sigma_B_list = []

        params = {'Kx':Kx, 'Ky':Ky, 'Kz':Kz, 'kappa':kappa}

        # ===== 读数据 =====
        phi = manager.load_data('gap_closing_vec', N1, N2, bc1, bc2, **params)
        phi_list = [None, phi[:N], phi[N:2*N], phi[2*N:3*N]]

        W_u_0 = manager.load_data('W_u_0', N1, N2, bc1, bc2, **params)
        V_u_0 = manager.load_data('V_u_0', N1, N2, bc1, bc2, **params)

        U0 = np.block([[W_u_0, V_u_0.conj()],
                       [V_u_0, W_u_0.conj()]])
        U0_dagger = U0.T.conj()

        U0_p11, U0_p12, U0_p21, U0_p22 = build_U0_prime_matrix(U0, N)

        # ===== 选 k 点 =====
        k = Gamma if Kx == 1 else K

        i = n1 + N1 * n2
        r_i = n1 * a1 + n2 * a2

        for l in [1,2,3]:

            # ======================
            # A 子格
            # ======================
            phase_A = np.exp(1j * np.dot(k, r_i))

            W_A = manager.load_data(f'W_u_{l}', N1, N2, bc1, bc2, **params)
            V_A = manager.load_data(f'V_u_{l}', N1, N2, bc1, bc2, **params)

            U_A = np.block([[W_A, V_A.conj()],
                            [V_A, W_A.conj()]])
            U_A_tilde = U0_dagger @ U_A

            W = U_A_tilde[:N, :N]
            V = U_A_tilde[N:, :N]

            F = V.conj() @ np.linalg.inv(W.conj())

            M = np.block([[F, -np.eye(N)],
                          [np.eye(N), np.zeros((N,N))]])

            M_inv = np.block([[np.zeros((N,N)), np.eye(N)],
                              [-np.eye(N), F]])

            overlap = (1/np.sqrt(2)) * np.sqrt(np.abs(np.linalg.det(W))) \
                      * (-1)**(N*(N+1)//2) * pfaffian.pfaffian(M)

            middle = -M_inv + np.block([
                [np.zeros((N,N)), np.eye(N)],
                [np.zeros((N,N)), np.zeros((N,N))]
            ])

            right = np.vstack([W, V])

            cor = np.hstack([
                U0_p12[i,:].reshape(1,-1),
                U0_p11[i,:].reshape(1,-1)
            ]) @ middle @ right

            result = 1/np.sqrt(N) * phase_A * overlap * 1j * cor @ phi_list[l]
            spin_A = (result + result.conj()).real
            sigma_A_list.append(spin_A)

            # ======================
            # B 子格
            # ======================
            if l == 1:
                U_B = np.kron(np.eye(2), T_2) @ U_A
            elif l == 2:
                U_B = np.kron(np.eye(2), T_2) @ np.kron(np.eye(2), T_1.T) @ U_A
            else:
                U_B = U_A

            j = n1 + N1 * (n2+1)
            r_j = n1*a1 + (n2+1)*a2

            phase_B = np.exp(1j * np.dot(k, r_j - delta_list[l]))

            U_B_tilde = U0_dagger @ U_B
            W = U_B_tilde[:N, :N]
            V = U_B_tilde[N:, :N]

            F = V.conj() @ np.linalg.inv(W.conj())

            M = np.block([[F, -np.eye(N)],
                          [np.eye(N), np.zeros((N,N))]])

            M_inv = np.block([[np.zeros((N,N)), np.eye(N)],
                              [-np.eye(N), F]])

            overlap = (1/np.sqrt(2)) * np.sqrt(np.abs(np.linalg.det(W))) \
                      * (-1)**(N*(N+1)//2) * pfaffian.pfaffian(M)

            middle = -M_inv + np.block([
                [np.zeros((N,N)), np.eye(N)],
                [np.zeros((N,N)), np.zeros((N,N))]
            ])

            right = np.vstack([W, V])

            cor = np.hstack([
                U0_p22[j,:].reshape(1,-1),
                U0_p21[j,:].reshape(1,-1)
            ]) @ middle @ right

            result = 1/np.sqrt(N) * phase_B * overlap * cor @ phi_list[l]
            spin_B = (result + result.conj()).real
            sigma_B_list.append(spin_B)

# ==============================
# 3D 可视化（升级版）
# ==============================

Sx_A, Sy_A, Sz_A = sigma_A_list

# ===== (111) 平面基 =====
e1 = np.array([1,1,-2]) / np.sqrt(6)
e2 = np.array([-1,1,0]) / np.sqrt(2)
n_vec = np.array([1,1,1]) / np.sqrt(3)   # 法向量（磁场方向）

# ===== 投影 =====
S1 = Sx_A*e1[0] + Sy_A*e1[1] + Sz_A*e1[2]
S2 = Sx_A*e2[0] + Sy_A*e2[1] + Sz_A*e2[2]

# ===== 收集 =====
X,Y,Z,U,V,W = [],[],[],[],[],[]

window = 2

for nn1 in range(n1-window, n1+window+1):
    for nn2 in range(n2-window, n2+window+1):

        rA_2d = nn1*a1 + nn2*a2
        rB_2d = rA_2d + delta_x

        # ===== 嵌入 3D =====
        rA = rA_2d[0]*e1 + rA_2d[1]*e2
        rB = rB_2d[0]*e1 + rB_2d[1]*e2

        # ⭐ 关键：增加极小 out-of-plane（视觉增强）
        eps = 0.02
        rA = rA + eps * ((nn1+nn2)%2) * n_vec
        rB = rB - eps * ((nn1+nn2)%2) * n_vec

        SA = S1*e1 + S2*e2
        SB = -SA

        for r, S in [(rA,SA),(rB,SB)]:
            X.append(r[0]); Y.append(r[1]); Z.append(r[2])
            U.append(S[0]); V.append(S[1]); W.append(S[2])

X,Y,Z = map(np.array,(X,Y,Z))
U,V,W = map(np.array,(U,V,W))

# ===== 归一化 =====
norm = np.sqrt(U**2+V**2+W**2)
U/=norm; V/=norm; W/=norm

fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(111, projection='3d')

# ==============================
# bond
# ==============================
for nn1 in range(n1-window, n1+window+1):
    for nn2 in range(n2-window, n2+window+1):

        rA_2d = nn1*a1 + nn2*a2
        rA = rA_2d[0]*e1 + rA_2d[1]*e2

        for d in [delta_x, delta_y, delta_z]:
            rB_2d = rA_2d + d
            rB = rB_2d[0]*e1 + rB_2d[1]*e2

            ax.plot([rA[0],rB[0]],
                    [rA[1],rB[1]],
                    [rA[2],rB[2]],
                    'k-',alpha=0.4,lw=0.8)

# ==============================
# 自旋箭头（中点）
# ==============================
scale = 0.5
ax.quiver(X-0.5*scale*U,
          Y-0.5*scale*V,
          Z-0.5*scale*W,
          scale*U,scale*V,scale*W,
          linewidth=1.2)

# ==============================
# 格点
# ==============================
ax.scatter(X,Y,Z,s=10,color='black')

# ==============================
# ⭐ 加坐标轴（关键！！！）
# ==============================

origin = np.array([0,0,0])

# (111) 法向量（红色）
ax.quiver(*origin, *n_vec,
          length=2, linewidth=3, color='red')
ax.text(*(1.2*n_vec), '[111]', color='red')

# e1（蓝）
ax.quiver(*origin, *e1,
          length=2, linewidth=2, color='blue')
ax.text(*(1.2*e1), 'e1', color='blue')

# e2（绿）
ax.quiver(*origin, *e2,
          length=2, linewidth=2, color='green')
ax.text(*(1.2*e2), 'e2', color='green')

# ==============================
# 视角优化（关键）
# ==============================
ax.view_init(elev=20, azim=35)

ax.set_box_aspect([1,1,1])
ax.set_axis_off()

plt.title("3D Spin texture ⟂ [111]")
plt.show()