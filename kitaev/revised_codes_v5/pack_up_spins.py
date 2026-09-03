# -*- coding: utf-8 -*-

from kitaev_data_manager import KitaevDataManager

manager = KitaevDataManager()

N1, N2, bc1, bc2 = 60, 60, -1, -1
K_list = [(1,1,1)]
kappa_list = [0.0, 0.02, 0.04, 0.06]
sub_type_list = ['A','B']
bond_list = [1, 2, 3]

for Kx,Ky,Kz in K_list:  
    for kappa in kappa_list:
        
        spin_list = []
        
        for sub_type in sub_type_list:
            for bond in bond_list:
                
                params = {'bond':bond, 'Kx':Kx, 'Ky':Ky, 'Kz':Kz, 'kappa':kappa}
                
                spin = manager.load_data(f'sigma_{sub_type}_beta_k_1_dag_GS_exp', N1, N2, bc1, bc2, **params)
                spin_list.append(spin)
                
        params_to_save = {'Kx':Kx, 'Ky':Ky, 'Kz':Kz, 'kappa':kappa}
        manager.save_data('spins', spin_list, N1, N2, bc1, bc2, **params_to_save)                

                
                