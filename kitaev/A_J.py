import numpy as np

def index(i, j):
    return i + j * N1

def kitaev_honeycomb_A(N1, N2, Jx, Jy, Jz, bc1, bc2):
    N = N1 * N2 # 总 unit cell 数
    M = np.zeros((N, N), dtype=float) # A 的右上角block
    
    def index(i, j):
        return i + j * N1
    
    if bc1 == "PBC":
        sign1 = 1.0
    elif bc1 == "APBC":
        sign1 = -1.0
    
    if bc2 == "PBC":
        sign2 = 1.0
    elif bc2 == "APBC":
        sign2 = -1.0    
    
    for j in range(N2):
        for i in range(N1):
            r = index(i, j) # 单指标标记 unit cell
            M[r, r] = 2*Jx  # 对 unit cell 求和，每个 unit cell 一一对应一条 x-bond
            
            plus_a1_i = (i + 1) % N1 
            plus_a1_j = j
            if i == N1-1:
                M[index(i, j), index(plus_a1_i, plus_a1_j)] = 2 * Jy * sign1
            else:
                M[index(i, j), index(plus_a1_i, plus_a1_j)] = 2 * Jy 

            plus_a2_i = i
            plus_a2_j = (j + 1) % N2
            if j == N2-1:
                M[index(i, j), index(plus_a2_i, plus_a2_j)] = 2 * Jz * sign2
            else:
                M[index(i, j), index(plus_a2_i, plus_a2_j)] = 2 * Jz 
            
    A = np.zeros((2*N, 2*N), dtype=float)
    A[:N, N:] = M
    A[N:, :N] = -M.T
    
    return A

N1, N2, Jx, Jy, Jz = 2, 2, 1, 1, 1
            
A_PP = kitaev_honeycomb_A(N1, N2, Jx, Jy, Jz, "PBC", "PBC")
A_AP = kitaev_honeycomb_A(N1, N2, Jx, Jy, Jz, "APBC", "PBC")
A_PA = kitaev_honeycomb_A(N1, N2, Jx, Jy, Jz, "PBC", "APBC")
A_AA = kitaev_honeycomb_A(N1, N2, Jx, Jy, Jz, "APBC", "APBC")

print("matrix A_PP:\n", A_PP)
print("matrix A_AP:\n", A_AP)
print("matrix A_PA:\n", A_PA)
print("matrix A_AA:\n", A_AA)
            
            
            
                
            
            
            
            
            
            
    