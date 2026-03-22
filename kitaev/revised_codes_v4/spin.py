# -*- coding: utf-8 -*-

from kitaev_data_manager import KitaevDataManager
import numpy as np
import time
from pfapack import pfaffian
import matplotlib.pyplot as plt

def build_U0_prime_matrix(U0, N):
    I_N = np.eye(N, dtype=complex)
    U0_prime = np.block([
        [I_N, I_N],
        [-1j*I_N, 1j*I_N]
    ]) @ U0
    U0_prime_11 = U0_prime[:N, :N]
    U0_prime_12 = U0_prime[:N, N:]
    U0_prime_21 = U0_prime[N:, :N]
    U0_prime_22 = U0_prime[N:, N:]
    return U0_prime_11, U0_prime_12, U0_prime_21, U0_prime_22

def build_T_1_matrix(N1, N2):
    single_block = np.eye(N1, k=-1)
    single_block[0, N1-1] = -1
    T_1 = np.kron(np.eye(N2), single_block)
    return T_1

def build_T_2_matrix(N1, N2):
    single_block = np.eye(N2, k=-1)
    single_block[0, N2-1] = -1
    T_2 = np.kron(single_block, np.eye(N1))
    return T_2

manager = KitaevDataManager() # 不传参，默认 root 为 kitaev_data
N1, N2, bc1, bc2 = 20, 20, -1, -1
N = N1 * N2
n1, n2 = N1//2, N2//2

a1 = np.array([1.0, 0.0])
a2 = np.array([0.5, np.sqrt(3)/2])
i = n1 + N1 * n2
r_i = n1 * a1 + n2 * a2

Gamma = np.array([0.0, 0.0])
K = np.array([4*np.pi/3, 0.0])

delta_x = np.array([-0.5, -0.5/np.sqrt(3)])
delta_y = np.array([0.5, -0.5/np.sqrt(3)])
delta_z = np.array([0, 1/np.sqrt(3)])
delta_list = [None, delta_x, delta_y, delta_z]

T_1 = build_T_1_matrix(N1, N2)
T_2 = build_T_2_matrix(N1, N2)

for Kx, Ky, Kz in [(1, 1, 1),(-1, -1, -1)]:
    for kappa in np.linspace(0.04, 0.04, 1):
        sigma_A_list = []
        sigma_B_list = []
        U_A_list = [None,]
        U_B_list = [None,]
        params = {'Kx':Kx, 'Ky':Ky, 'Kz':Kz, 'kappa':kappa}
        
        h_c = manager.load_data('gap_closing_h', N1, N2, bc1, bc2, **params)
        phi = manager.load_data('gap_closing_vec', N1, N2, bc1, bc2, **params)
        phi_x = phi[0:N]
        phi_y = phi[N:2*N]
        phi_z = phi[2*N:3*N]
        phi_list = [None, phi_x, phi_y, phi_z]
        
        W_u_0 = manager.load_data('W_u_0', N1, N2, bc1, bc2, **params)
        V_u_0 = manager.load_data('V_u_0', N1, N2, bc1, bc2, **params)
        U0 = np.block([[W_u_0, V_u_0.conj()], [V_u_0, W_u_0.conj()]])
        U0_dagger = U0.T.conj()
        U0_prime_11, U0_prime_12, U0_prime_21, U0_prime_22 = build_U0_prime_matrix(U0, N)
        
        
        for l in [1, 2, 3]:
            if Kx == 1:
                k = Gamma
            elif Kx == -1:
                k = K
            phase_A = np.exp(1j * np.dot(k, r_i))
            
            W_A = manager.load_data(f'W_u_{l}', N1, N2, bc1, bc2, **params)
            V_A = manager.load_data(f'V_u_{l}', N1, N2, bc1, bc2, **params)
            U_A = np.block([[W_A, V_A.conj()], [V_A, W_A.conj()]])
            U_A_tilde = U0_dagger @ U_A
            W_A_tilde = U_A_tilde[:N, :N]
            V_A_tilde = U_A_tilde[N:, :N]
            F_A_tilde = V_A_tilde.conj() @ np.linalg.inv(W_A_tilde.conj())
            M_A = np.block([
                            [F_A_tilde, -np.eye(N)],
                            [np.eye(N), np.zeros((N, N))]
                        ])
            M_A_inv = np.block([
                            [np.zeros((N, N)), np.eye(N)],
                            [-np.eye(N), F_A_tilde]
                        ])
            N_0_tilde = 1/np.sqrt(2)
            N_A_tilde = np.sqrt(np.abs(np.linalg.det(W_A_tilde)))
            overlap_A = N_0_tilde * N_A_tilde * (-1)**(N*(N+1)/2) * pfaffian.pfaffian(M_A)
            
            middle_matrix = -M_A_inv + np.block([ [np.zeros((N, N)), np.eye(N)], [np.zeros((N, N)), np.zeros((N, N))] ])
            right_WV = np.vstack([W_A_tilde, V_A_tilde])
            cor_c_i_A_alpha_2_dag = np.hstack([U0_prime_12[i,:].reshape(1,-1), U0_prime_11[i,:].reshape(1,-1) ]) @ middle_matrix @ right_WV
            
            result_A = 1/np.sqrt(N) * phase_A * overlap_A * 1j * cor_c_i_A_alpha_2_dag @ phi_list[l]
            spin_A = result_A + result_A.conj()
            sigma_A_list.append(spin_A)
            print(f"A sigma_{l}:{spin_A}")
            # B spin
            
            if l == 1:
                U_B = np.kron(np.eye(2), T_2) @ U_A
                j = (n1) + N1 * (n2+1) 
                r_j = (n1) * a1 + (n2+1) * a2
            elif l == 2:
                U_B = np.kron(np.eye(2), T_2) @ np.kron(np.eye(2), T_1.T) @ U_A
                j = (n1) + N1 * (n2+1) 
                r_j = (n1) * a1 + (n2+1) * a2
            elif l == 3:
                U_B = U_A
                j = (n1) + N1 * (n2+1) 
                r_j = (n1) * a1 + (n2+1) * a2
                
            phase_B = np.exp(1j * np.dot(k, (r_j - delta_list[l])))
            
            U_B_tilde = U0_dagger @ U_B
            W_B_tilde = U_B_tilde[:N, :N]
            V_B_tilde = U_B_tilde[N:, :N]
            F_B_tilde = V_B_tilde.conj() @ np.linalg.inv(W_B_tilde.conj())
            M_B = np.block([
                            [F_B_tilde, -np.eye(N)],
                            [np.eye(N), np.zeros((N, N))]
                        ])
            M_B_inv = np.block([
                            [np.zeros((N, N)), np.eye(N)],
                            [-np.eye(N), F_B_tilde]
                        ])
            N_0_tilde = 1/np.sqrt(2)
            N_B_tilde = np.sqrt(np.abs(np.linalg.det(W_B_tilde)))
            overlap_B = N_0_tilde * N_B_tilde * (-1)**(N*(N+1)/2) * pfaffian.pfaffian(M_B)
            
            middle_matrix = -M_B_inv + np.block([ [np.zeros((N, N)), np.eye(N)], [np.zeros((N, N)), np.zeros((N, N))] ])
            right_WV = np.vstack([W_B_tilde, V_B_tilde])
            cor_c_j_B_alpha_2_dag = np.hstack([U0_prime_22[j,:].reshape(1,-1), U0_prime_21[j,:].reshape(1,-1) ]) @ middle_matrix @ right_WV
            
            result_B = 1/np.sqrt(N) * phase_B * overlap_B * cor_c_j_B_alpha_2_dag @ phi_list[l]
            spin_B = result_B + result_B.conj()
            sigma_B_list.append(spin_B)
            print(f"B sigma_{l}:{spin_B}")
            
        print(f"sigma_A:{sigma_A_list}")
        print(f"sigma_B:{sigma_B_list}")
        sigma_A_list = np.array(sigma_A_list)
        sigma_B_list = np.array(sigma_B_list)
        sum_A = np.sum(sigma_A_list)
        sum_B = np.sum(sigma_B_list)
        print(sum_A)
        print(sum_B)
        
Sx_A, Sy_A, Sz_A = sigma_A_list[0], sigma_A_list[1], sigma_A_list[2]

e1 = np.array([1,1,-2]) / np.sqrt(6)
e2 = np.array([-1,1,0]) / np.sqrt(2)

S1_A = Sx_A*e1[0] + Sy_A*e1[1] + Sz_A*e1[2]
S2_A = Sx_A*e2[0] + Sy_A*e2[1] + Sz_A*e2[2]

S1_B = -S1_A
S2_B = -S2_A

x, y, u, v = [], [], [], []

for n1 in range(N1):
    for n2 in range(N2):
        rA = n1*a1 + n2*a2
        rB = rA + delta_x

        # A
        x.append(rA[0])
        y.append(rA[1])
        u.append(S1_A)
        v.append(S2_A)

        # B
        x.append(rB[0])
        y.append(rB[1])
        u.append(S1_B)
        v.append(S2_B)

x = np.array(x)
y = np.array(y)
u = np.array(u)
v = np.array(v)

norm = np.sqrt(u**2 + v**2)
u = u / (norm + 1e-8)
v = v / (norm + 1e-8)

plt.figure(figsize=(12,12))

# ===== 画 honeycomb bond（底层）=====
for n1 in range(N1):
    for n2 in range(N2):
        rA = n1*a1 + n2*a2

        neighbors = [
            rA + delta_x,
            rA + delta_y,
            rA + delta_z
        ]

        for rB in neighbors:
            plt.plot([rA[0], rB[0]],
                     [rA[1], rB[1]],
                     'k-', lw=0.8, alpha=0.4)

# ===== 缩小箭头 =====
scale_factor = 0.5
u_plot = scale_factor * u
v_plot = scale_factor * v

# ===== 画箭头 =====
plt.quiver(x, y, u_plot, v_plot,
           angles='xy',
           scale_units='xy',
           scale=1,
           width=0.004,
           headwidth=2.5,
           headlength=5,
           headaxislength=4.5)

# ===== 画格点 =====
plt.scatter(x, y, s=8, color='black', zorder=3)

plt.gca().set_aspect('equal')
plt.title(r"Spin texture in plane $\perp (111)$")

plt.axis('off')

plt.show()
