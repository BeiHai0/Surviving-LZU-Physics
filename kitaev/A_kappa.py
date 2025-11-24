import numpy as np

def kitaev_A3(N1, N2, kappa, bc1, bc2):
    N = N1 * N2 # 总unit cell数
    A3 = np.zeros((2 * N, 2 * N))
    left_dash_arrow_matrix = np.zeros((2 * N, 2 * N))
    
    if bc1 == "APBC":
        sign1 = 1
    elif bc1 == "PBC":
        sign1 = -1
    
    if bc2 == "APBC":
        sign2 = -1
    elif bc2 == "PBC":
        sign2 = 1
    
    def index(n1, n2, sub):
        return n1 + n2 * N1 + sub * N
    
    for n2 in range(N2):
        for n1 in range(N1):
            j = index(n1, n2, 0) # A子格
            
            plus_a1_n1 = (n1 + 1) % N1
            plus_a1_n2 = n2
            k1 = index(plus_a1_n1, plus_a1_n2, 0)
            if n1 == N1-1:
                left_dash_arrow_matrix[j, k1] = sign1
            else:
                left_dash_arrow_matrix[j, k1] = -1
                
            plus_a2_n1 = n1
            plus_a2_n2 = (n2 + 1) % N2
            k2 = index(plus_a2_n1, plus_a2_n2, 0)
            if n2 == N2-1:
                left_dash_arrow_matrix[j, k2] = sign2
            else:
                left_dash_arrow_matrix[j, k2] = 1
            
            minus_a1_plus_a2_n1 = (n1 - 1 + N1) % N1
            minus_a1_plus_a2_n2 = (n2 + 1) % N2
            k3 = index(minus_a1_plus_a2_n1, minus_a1_plus_a2_n2, 0)
            
            if n1 == 0 and n2 != N2-1 or n2 == N2-1 and n1 != 0:
                left_dash_arrow_matrix[j, k3] = sign1
            else:
                left_dash_arrow_matrix[j, k3] = -1 # 跨过两次边界贡献两个-1，与内部情况一致        
            
    left_dash_arrow_matrix[N:, N:] = -left_dash_arrow_matrix[:N, :N]
    A3 = 2 * kappa * (left_dash_arrow_matrix - left_dash_arrow_matrix.T)
    return A3
            
N1, N2, kappa = 2, 2, 1

A3_PP = kitaev_A3(N1, N2, kappa, "PBC", "PBC")
A3_AP = kitaev_A3(N1, N2, kappa, "APBC", "PBC")    
A3_PA = kitaev_A3(N1, N2, kappa, "PBC", "APBC")
A3_AA = kitaev_A3(N1, N2, kappa, "APBC", "APBC")

print("matrix A3_PP:\n", A3_PP)
print("matrix A3_AP:\n", A3_AP)
print("matrix A3_PA:\n", A3_PA)
print("matrix A3_AA:\n", A3_AA)  
            
            
            