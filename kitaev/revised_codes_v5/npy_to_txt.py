import numpy as np

kappas = [0.000, 0.020, 0.040, 0.060]

for kappa in kappas:

    npy_name = (
        f"spins_N1_60_N2_60_bc1_-1_bc2_-1_"
        f"Kx_1_Ky_1_Kz_1_kappa_{kappa:.3f}.npy"
    )

    dat_name = (
        f"spins_kappa_{kappa:.3f}.dat"
    )

    spins = np.load(npy_name)

    np.savetxt(dat_name, spins)

    print(f"saved -> {dat_name}")