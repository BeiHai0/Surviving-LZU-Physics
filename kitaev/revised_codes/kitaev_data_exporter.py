# -*- coding: utf-8 -*-
import os
import numpy as np
from scipy import sparse

class KitaevDataExporter:
    def __init__(self, root="kitaev_data"):
        self.root = root
        if not os.path.exists(self.root):
            os.makedirs(self.root)
    def _generate_path_grid(self, N1, N2, bc1, bc2):
        folder_name = f"N1_{N1}_N2_{N2}_bc1_{bc1}_bc2_{bc2}"
        return os.path.join(self.root, folder_name)
    
    def _generate_path_grid_kappa(self, N1, N2, bc1, bc2, kappa):
        folder_name = f"kappa_{kappa:.3f}"
        return os.path.join(self._generate_path_grid(N1, N2, bc1, bc2), folder_name)
        
    def save_nonsparse_matrix_grid(self, matrix, matrix_name, N1, N2, bc1, bc2):
        path = self._generate_path_grid(N1, N2, bc1, bc2)
        os.makedirs(path, exist_ok=True)
        
        file_path = os.path.join(path, f"{matrix_name}.npy")
        np.save(file_path, matrix)
        print(f"{matrix_name}已导出至:{path}")
        
    def save_nonsparse_matrix_grid_kappa(self, matrix, matrix_name, N1, N2, bc1, bc2, kappa):
        path = self._generate_path_grid_kappa(N1, N2, bc1, bc2, kappa)
        os.makedirs(path, exist_ok=True)
        
        file_path = os.path.join(path, f"{matrix_name}.npy")
        np.save(file_path, matrix)
        print(f"{matrix_name}已导出至:{path}")

    def save_sparse_matrix_grid(self, matrix, matrix_name, N1, N2, bc1, bc2):
        path = self._generate_path_grid(N1, N2, bc1, bc2)
        os.makedirs(path, exist_ok=True)
        
        sparse_mat = sparse.csc_matrix(matrix)
        file_path = os.path.join(path, f"{matrix_name}.npz")
        sparse.save_npz(file_path, sparse_mat)
        print(f"{matrix_name} (稀疏压缩) 已导出至: {path}")    
    
    def save_sparse_matrix_grid_kappa(self, matrix, matrix_name, N1, N2, bc1, bc2, kappa):
        path = self._generate_path_grid_kappa(N1, N2, bc1, bc2, kappa)
        os.makedirs(path, exist_ok=True)
        
        sparse_mat = sparse.csc_matrix(matrix)
        file_path = os.path.join(path, f"{matrix_name}.npz")
        sparse.save_npz(file_path, sparse_mat)
        print(f"{matrix_name} (稀疏压缩) 已导出至: {path}")  

    def load_nonsparse_matrix_grid(self, matrix_name, N1, N2, bc1, bc2):
        path = self._generate_path_grid(N1, N2, bc1, bc2)
        file_path = os.path.join(path, f"{matrix_name}.npy")
        if os.path.exists(file_path):
            matrix_loaded = np.load(file_path)
            print(f"已从{path}读取{matrix_name}")
            return matrix_loaded
        else:
            raise FileNotFoundError(f"找不到文件 {matrix_name}.npy")         
        
    def load_sparse_matrix_grid(self, matrix_name, N1, N2, bc1, bc2):
        path = self._generate_path_grid(N1, N2, bc1, bc2)
        file_path = os.path.join(path, f"{matrix_name}.npz")
        if os.path.exists(file_path):
            sparse_matrix_loaded = sparse.load_npz(file_path)
            print(f"已从 {path} 读取 {matrix_name}")
            return sparse_matrix_loaded.toarray() # 返回普通 numpy 矩阵
        else:
            return FileNotFoundError(f"找不到文件: {file_path}")
        
    def load_sparse_matrix_grid_kappa(self, matrix_name, N1, N2, bc1, bc2, kappa):
        path = self._generate_path_grid_kappa(N1, N2, bc1, bc2, kappa)
        file_path = os.path.join(path, f"{matrix_name}.npz")
        if os.path.exists(file_path):
            sparse_matrix_loaded = sparse.load_npz(file_path)
            print(f"已从 {path} 读取 {matrix_name}")
            return sparse_matrix_loaded.toarray() # 返回普通 numpy 矩阵
        else:
            return FileNotFoundError(f"找不到文件: {file_path}") 
        
    def load_nonsparse_matrix_grid_kappa(self, matrix_name, N1, N2, bc1, bc2,kappa):
        path = self._generate_path_grid_kappa(N1, N2, bc1, bc2)
        file_path = os.path.join(path, f"{matrix_name}.npy")
        if os.path.exists(file_path):
            matrix_loaded = np.load(file_path)
            print(f"已从{path}读取{matrix_name}")
            return matrix_loaded
        else:
            raise FileNotFoundError(f"找不到文件 {matrix_name}.npy")