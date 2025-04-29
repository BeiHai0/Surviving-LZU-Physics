import numpy as np

L = np.array([100.20, 100.30, 100.30, 100.20, 100.15])*1e-2 # 单位 m
d = np.array([2.776, 2.770, 2.778, 2.776, 2.770]) * 1e-2 # 单位 m
t = np.array([1.9287, 1.8991, 1.9175, 1.9194, 1.9364]) # 单位 s

L_bar = np.average(L)
d_bar = np.average(d)
t_bar = np.average(t)

print(L_bar)
print(d_bar)
print(t_bar)

g_bar = 4 * np.pi**2 * (L_bar+d_bar/2)/t_bar**2
print(f"g_bar : {g_bar}")

t_factor = 2.78 # t因子

def u_A(t_factor, array, N, average):
    u_A = t_factor * np.sqrt( np.sum( (array-average)**2 ) / (N*(N-1)) )
    return u_A

print("u_As : ")
u_A_L = u_A(t_factor, L, 5, L_bar)
u_A_d = u_A(t_factor, d, 5, d_bar)
u_A_t = u_A(t_factor, t, 5, t_bar)


print(f"u_A for L,d,t")
print(u_A_L)
print(u_A_d)
print(u_A_t)

E_g = np.sqrt( ( (8.5*1e-4)**2 + (4.9*1e-5)**2/4 )/(1.0023+2.774*1e-2/2)**2 + ( 4*(1.9*1e-2)**2 )/(1.92022**2) )

print(E_g)