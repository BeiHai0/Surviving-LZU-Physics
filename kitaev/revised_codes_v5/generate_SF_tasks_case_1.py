import numpy as np
from kitaev_data_manager import KitaevDataManager

manager = KitaevDataManager()

N1, N2, bc1, bc2 = 60, 60, -1, -1
step = 0.1

with open("SF_tasks_case_3.txt", "w") as f:

    # # =========================
    # # Case 1: K = -1, kappa = 0, only h = 0
    # # =========================
    # K_list_1 = [(-1, -1, -1)]
    # kappa = 0.0

    # for Kx, Ky, Kz in K_list_1:
    #     f.write(f"{Kx} {Ky} {Kz} {kappa} 0.0\n")


    # =========================
    # Case 2: K = +1, kappa = 0, sweep h
    # =========================
    Kx = Ky = Kz = 1
    kappa = 0.0

    params = {
        "Kx": Kx,
        "Ky": Ky,
        "Kz": Kz,
        "kappa": kappa
    }

    h_c = manager.load_data("h_c", N1, N2, bc1, bc2, **params)

    h_list = np.arange(0.0, h_c, step)
    h_list = np.append(h_list, h_c)

    # for h in h_list:
    f.write(f"{Kx} {Ky} {Kz} {kappa} {h_list[1]}\n")