import numpy as np
from itertools import product
from kitaev_data_manager import KitaevDataManager

manager = KitaevDataManager()

N1,N2,bc1,bc2 = 20,20,-1,-1

K_list = [(1,1,1), (-1,-1,-1),]

kappa_list = [0.0,]

step = 0.1

with open("SF_tasks_test_2.txt","w") as f:

    for (Kx,Ky,Kz), kappa in product(K_list, kappa_list):

        params = {
            "Kx":Kx,
            "Ky":Ky,
            "Kz":Kz,
            "kappa":kappa
        }

        h_c = manager.load_data( "h_c", N1,N2,bc1,bc2, **params)

        h_list = list(np.arange(0, h_c, step))
        h_list.append(h_c)

        for h in h_list:

            f.write(
                f"{Kx} {Ky} {Kz} {kappa} {h}\n"
            )