# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 19:50:03 2025

@author: ZhuanZ（无密码）
"""

import numpy as np

def kitaev_A3(N1, N2, kappa=1, bc1="PBC", bc2="PBC"):
    N = N1 * N2 # 总unit cell数
    A3 = np.zeros((2 * N, 2 * N))
    
    if bc1 == "APBC":
        sign1 = -1
    elif bc1 == "PBC":
        sign1 = 1
    
    if bc2 == "APBC":
        sign2 = -1
    elif bc2 == "PBC":
        sign2 = 1
    
    def index(n1, n2, sub):
        return n1 + n2 * N1 + sub * N
    
    for n2 in range(N2):
        for n1 in range(N1):
            j = index(n1, n2, 0)
            
            plus_a1_n1 = (n1 + 1) % N1
            plus_a1_n2 = n2
            k = index(plus_a1_n1, plus_a1_n2)
            
            if n1 == N1-1:
                A3[j, k] = -sign1
            else:
                A3[j, k] = -1
                
            plus_a2_n1 = n1
            plus_a2_n2 = (n2 + 1) % N2
            k = index(plus_a2_n1, plus_a2_n2)
            
            if n2 == N2-1:
                A3[j, k] = sign2
            else:
                A3[j, k] = 1
            
            
            
            
            
            