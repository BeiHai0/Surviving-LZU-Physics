import numpy as np

def u_matrix(N1, N2, bc1="PBC", bc2="PBC"):
    N = N1 * N2 # N1 为 a_1 方向 unit cell 数量
    M = np.zeros((2 * N, 2 * N)) # M 储存 u_jk(j 为 A 子格，k 为 B 子格)构型
    u = np.zeros((2 * N, 2 * N))
    
    if bc1 == "PBC":
        sign1 = 1
    elif bc1 == "APBC":
        sign1 = -1
    if bc2 == "PBC":
        sign2 = 1
    elif bc2 == "APBC":
        sign2 = -1
    
    def index(n1, n2, sub):
        return n1 + n2 * N1 + N1 * N2 * sub # A子格对应 sub=0,B子格对应 sub=1
    
    for n2 in range(N2):
        for n1 in range(N1):
            j = index(n1, n2, 0) # j 为(n1, n2)unit cell 内 A 子格格点的单指标
            
            kx = index(n1, n2, 1) # kx 为(n1, n2)unit cell 内 B 子格格点的单指标
            M[j, kx] = 1 # j 与 kx 由 x-bond 相连，一定不跨越边界
            
            plus_a1_n1 = (n1 + 1) % N1 # (n1, n2) 往 a1 方向走一步得到的 unit cell
            plus_a1_n2 = n2
            ky = index(plus_a1_n1, plus_a1_n2, 1)
            if n1 == N1 - 1:
                M[j, ky] = sign1
            else:
                M[j, ky] = 1

            plus_a2_n1 = n1
            plus_a2_n2 = (n2 + 1) % N2
            kz = index(plus_a2_n1, plus_a2_n2, 1)
            if n2 == N2 - 1:
                M[j, kz] = sign2
            else:
                M[j, kz] = 1
      
    u = M - M.T                        
    return u

def A3_kappa(N1, N2, u):
    N = N1 * N2
    M = np.zeros((2 * N, 2 * N))
    
    def index(n1, n2, sub):
        return n1 + n2 * N1 + N1 * N2 * sub # A子格对应 sub=0,B子格对应 sub=1
    
    for n2 in range(N2):
        for n1 in range(N1):
            plus_a1_n1 = (n1 + 1) % N1
            plus_a1_n2 = n2
            
            plus_a2_n1 = n1
            plus_a2_n2 = (n2 + 1) % N2
            
            plus_a1_plus_a2_n1 = plus_a1_n1
            plus_a1_plus_a2_n2 = plus_a2_n2
            for sub in [0, 1]:
                if sub == 0:
                    j = index(plus_a1_n1, plus_a1_n2, sub)
                    k = index(n1, n2, sub)
                    l = index(plus_a1_n1, plus_a1_n2, 1-sub)
                    if M[j, k] == 0 and M[k, j] == 0: # 防止当 N1 == 2 或 N2 == 2 时次近邻相互作用重复计算
                        M[j, k] = u[j, l] * u[k, l]
                    
                    j = index(n1, n2, sub)
                    k = index(plus_a2_n1, plus_a2_n2, sub)
                    l = index(plus_a2_n1, plus_a2_n2, 1-sub)
                    if M[j, k] == 0 and M[k, j] == 0:
                        M[j, k] = u[j, l] * u[k, l]
                    
                    j = index(plus_a2_n1, plus_a2_n2, sub)
                    k = index(plus_a1_n1, plus_a1_n2, sub)
                    l = index(plus_a1_plus_a2_n1, plus_a1_plus_a2_n2, 1-sub)
                    if M[j, k] == 0 and M[k, j] == 0:
                        M[j, k] = u[j, l] * u[k, l]
                else: # sub == 1
                    j = index(n1, n2, sub)
                    k = index(plus_a1_n1, plus_a1_n2, sub)
                    l = index(n1, n2, 1-sub)
                    if M[j, k] == 0 and M[k, j] == 0:
                        M[j, k] = u[j, l] * u[k, l]
                    
                    j = index(plus_a2_n1, plus_a2_n2, sub)
                    k = index(n1, n2, sub)
                    l = index(n1, n2, 1-sub)
                    if M[j, k] == 0 and M[k, j] == 0:
                        M[j, k] = u[j, l] * u[k, l]
                    
                    j = index(plus_a1_n1, plus_a1_n2, sub)
                    k = index(plus_a2_n1, plus_a2_n2, sub)
                    l = index(n1, n2, 1-sub)
                    if M[j, k] == 0 and M[k, j] == 0:
                        M[j, k] = u[j, l] * u[k, l]                  

    return (M - M.T) / 2.0
                
N1, N2 = 2, 2 
for bc1 in ["PBC", "APBC"]:
    for bc2 in ["PBC", "APBC"]:
        print("bc1=", bc1, ",bc2=", bc2, "\n")
        u = u_matrix(N1, N2, bc1, bc2)
        print("u_matrix:\n", u)
        A3 = A3_kappa(N1, N2, u)
        print("A3：\n", A3)
    
    
    
    


