import numpy as np

def index(n1, n2, sub, N1, N2):
    return n1 + n2 * N1 + N1 * N2 * sub # A子格对应 sub=0,B子格对应 sub=1

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
    elif bc1 == "APBC":
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
                M[j, ky] = 1
      
    u = M - M.T                        
    return u



