import numpy as np
import matplotlib.pyplot as plt

# 手动求平均的参数

D_mean = 6.406 * 1e-2 # 量筒内径的平均值，单位：m
h_mean = 3.131 * 1e-1 # 液体深度的平均值，单位：m
g = 9.793 # 榆中重力加速度
rho = 1.1305 * 1e4 # 小球密度，单位：kg/m^3
rho_0 = 9.65 * 1e2 # 液体密度，单位：kg/m^3
L_mean = 1.227 * 1e-1 # 环线间距，单位：m
d1_mean = 2.145 * 1e-3 #
d2_mean = 2.143 * 1e-3 #
d3_mean = 1.949 * 1e-3 #

# 数组参数,为了计算不确定度

T = 1.14 # N=5时，t因子=1.14

D = np.array([0.06440, 0.06420, 0.06374, 0.06424, 0.06374]) # 量筒内径，单位：m
L = np.array([0.1227, 0.1227, 0.1225, 0.1230, 0.1228]) # 环线间距，单位：m
h = np.array([0.3111, 0.3114, 0.3109, 0.3110, 0.3119]) # 液体深度，单位：m

d_1 = np.array([2.135*1e-3, 2.191*1e-3, 2.145*1e-3, 2.135*1e-3, 2.110*1e-3]) # 小球1的直径，单位：m
d_2 = np.array([2.010*1e-3, 2.010*1e-3, 2.304*1e-3, 2.410*1e-3, 1.980*1e-3]) #小球2的直径，单位：m
d_3 = np.array([1.851*1e-3, 2.092*1e-3, 1.720*1e-3, 2.280*1e-3, 1.800*1e-3]) #小球3的直径，单位：m

t_1 = 4.91 # 小球1的下落时间，单位：s
t_2 = 4.69 # 小球2的下落时间，单位：s
t_3 = 5.28 # 小球3的下落时间，单位：s


d_mean = np.array([2.145*1e-3, 2.143*1e-3, 1.949*1e-3]) # 把三个小球直径的平均值组装成一个数组
t_array = np.array([t_1, t_2, t_3]) # 把三个小球下落时间组装成一个数组

def compute_yita(d_mean, g, D_mean, h_mean, rho, rho_0, L_mean, t_array):
    return 1/18 * t_array * (rho - rho_0)/( L_mean * (1 + 2.4 * d_mean / D_mean)*(1 + 3.3 * (d_mean/(2*h_mean))) ) *d_mean**2 * g

print(f"黏性系数yita的平均值为:{compute_yita(d_mean, g, D_mean, h_mean, rho, rho_0, L_mean, t_array)}")

# 不确定度计算

def u_A(T, N, array, average):
    return T*np.sqrt(  np.sum((array-average)**2)/(N*(N-1)) )



u_A_D = u_A(T=T, N=5, array=D, average=D_mean)
u_A_L = u_A(T=T, N=5, array=L, average=L_mean)
u_A_h = u_A(T=T, N=5, array=h, average=h_mean)
u_A_d1 = u_A(T=T, N=5, array=d_1, average=d1_mean)
u_A_d2 = u_A(T=T, N=5, array=d_2, average=d2_mean)
u_A_d3 = u_A(T=T, N=5, array=d_3, average=d3_mean)

print(f"u_A of D:{u_A(T=T, N=5, array=D, average=D_mean)}")
print(f"u_A of L:{u_A(T=T, N=5, array=L, average=L_mean)}")
print(f"u_A of h:{u_A(T=T, N=5, array=h, average=h_mean)}")
print(f"u_A of d1:{u_A(T=T, N=5, array=d_1, average=d1_mean)}")
print(f"u_A of d2:{u_A(T=T, N=5, array=d_2, average=d2_mean)}")
print(f"u_A of d3:{u_A(T=T, N=5, array=d_3, average=d3_mean)}")

u_D = 1.56*1e-4
u_L = 2.85*1e-4
u_h = 1.22*1e-3
u_d1 = 1.63*1e-5
u_d2 = 1.02*1e-3
u_d3 = 1.18*1e-4
u_t = 0.2

delta = 1e-8

p_yita1_p_D = ( compute_yita(d1_mean, g, D_mean+delta, h_mean, rho, rho_0, L_mean, t_1)-compute_yita(d1_mean, g, D_mean+delta, h_mean, rho, rho_0, L_mean, t_1) ) / delta
p_yita1_p_L = ( compute_yita(d1_mean, g, D_mean, h_mean, rho, rho_0, L_mean+delta, t_1)-compute_yita(d1_mean, g, D_mean, h_mean, rho, rho_0, L_mean, t_1)  ) / delta
p_yita1_p_h = ( compute_yita(d1_mean, g, D_mean, h_mean+delta, rho, rho_0, L_mean, t_1)-compute_yita(d1_mean, g, D_mean, h_mean, rho, rho_0, L_mean, t_1) ) / delta
p_yita1_p_d1 = ( compute_yita(d1_mean+delta, g, D_mean, h_mean, rho, rho_0, L_mean, t_1)-compute_yita(d1_mean, g, D_mean, h_mean, rho, rho_0, L_mean, t_1) ) / delta
p_yita1_p_t1 = ( compute_yita(d1_mean, g, D_mean, h_mean, rho, rho_0, L_mean, t_1+delta)-compute_yita(d1_mean, g, D_mean, h_mean, rho, rho_0, L_mean, t_1) ) / delta

p1_array = np.array([p_yita1_p_D, p_yita1_p_L, p_yita1_p_h, p_yita1_p_d1, p_yita1_p_t1])
u1_array = np.array([u_D, u_L, u_h, u_d1, u_t])

u1 = np.sqrt( np.sum(p1_array * u1_array)**2 )
print(f"u of yita1: {u1}")

p_yita2_p_D = ( compute_yita(d2_mean, g, D_mean+delta, h_mean, rho, rho_0, L_mean, t_2)-compute_yita(d2_mean, g, D_mean+delta, h_mean, rho, rho_0, L_mean, t_2) ) / delta
p_yita2_p_L = ( compute_yita(d2_mean, g, D_mean, h_mean, rho, rho_0, L_mean+delta, t_2)-compute_yita(d2_mean, g, D_mean, h_mean, rho, rho_0, L_mean, t_2)  ) / delta
p_yita2_p_h = ( compute_yita(d2_mean, g, D_mean, h_mean+delta, rho, rho_0, L_mean, t_2)-compute_yita(d2_mean, g, D_mean, h_mean, rho, rho_0, L_mean, t_2) ) / delta
p_yita2_p_d2 = ( compute_yita(d2_mean+delta, g, D_mean, h_mean, rho, rho_0, L_mean, t_2)-compute_yita(d2_mean, g, D_mean, h_mean, rho, rho_0, L_mean, t_2) ) / delta
p_yita2_p_t2 = ( compute_yita(d2_mean, g, D_mean, h_mean, rho, rho_0, L_mean, t_2+delta)-compute_yita(d2_mean, g, D_mean, h_mean, rho, rho_0, L_mean, t_2) ) / delta

p2_array = np.array([p_yita2_p_D, p_yita2_p_L, p_yita2_p_h, p_yita2_p_d2, p_yita2_p_t2])
u2_array = np.array([u_D, u_L, u_h, u_d1, u_t])

u2 = np.sqrt( np.sum(p2_array * u2_array)**2 )
print(f"u of yita2: {u2}")

p_yita3_p_D = ( compute_yita(d3_mean, g, D_mean+delta, h_mean, rho, rho_0, L_mean, t_3)-compute_yita(d3_mean, g, D_mean+delta, h_mean, rho, rho_0, L_mean, t_3) ) / delta
p_yita3_p_L = ( compute_yita(d3_mean, g, D_mean, h_mean, rho, rho_0, L_mean+delta, t_3)-compute_yita(d3_mean, g, D_mean, h_mean, rho, rho_0, L_mean, t_3)  ) / delta
p_yita3_p_h = ( compute_yita(d3_mean, g, D_mean, h_mean+delta, rho, rho_0, L_mean, t_3)-compute_yita(d3_mean, g, D_mean, h_mean, rho, rho_0, L_mean, t_3) ) / delta
p_yita3_p_d3 = ( compute_yita(d3_mean+delta, g, D_mean, h_mean, rho, rho_0, L_mean, t_3)-compute_yita(d3_mean, g, D_mean, h_mean, rho, rho_0, L_mean, t_3) ) / delta
p_yita3_p_t3 = ( compute_yita(d3_mean, g, D_mean, h_mean, rho, rho_0, L_mean, t_3+delta)-compute_yita(d3_mean, g, D_mean, h_mean, rho, rho_0, L_mean, t_3) ) / delta

p3_array = np.array([p_yita3_p_D, p_yita3_p_L, p_yita3_p_h, p_yita3_p_d3, p_yita3_p_t3])
u3_array = np.array([u_D, u_L, u_h, u_d3, u_t])

u3 = np.sqrt( np.sum(p3_array * u3_array)**2 )
print(f"u of yita3: {u3}")
