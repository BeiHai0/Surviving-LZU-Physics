# -*- coding: utf-8 -*-
import os
import numpy as np
from scipy import sparse

class KitaevDataManager:
    def __init__(self, root="kitaev_data"):
        self.root = root
        # 定义严格的文件名参数排序优先级
        self.param_priority = [
            'N1', 'N2', 'bc1', 'bc2',
            'Kx', 'Ky', 'Kz', 
            'kappa', 
            'hx', 'hy', 'hz'
        ]
        if not os.path.exists(self.root):
            os.makedirs(self.root)

    def _get_dir(self, N1, N2, bc1, bc2):
        """核心文件夹：按尺寸和边界条件分类"""
        path = os.path.join(self.root, f"N1_{N1}_N2_{N2}_bc1_{bc1}_bc2_{bc2}")
        os.makedirs(path, exist_ok=True)
        return path

    def _make_filename(self, name, N1, N2, bc1, bc2, **params):
        """
        按照预设的优先级构造文件名。
        尺寸参数 (N1, N2, bc1, bc2) 被强制放在文件名的最前面。
        """
        # 1. 首先整合所有参数到一个临时字典
        all_args = {'N1': N1, 'N2': N2, 'bc1': bc1, 'bc2': bc2}
        all_args.update(params)
        
        # 2. 按照严格的优先级列表提取并拼接
        parts = []
        for key in self.param_priority:
            if key in all_args:
                val = all_args[key]
                # 对浮点数保留 3 位
                if isinstance(val, (float, np.float64)):
                    parts.append(f"{key}_{val:.3f}")
                else:
                    parts.append(f"{key}_{val}")
        
        param_str = "_".join(parts)
        return f"{name}_{param_str}"

    def save_data(self, name, data, N1, N2, bc1, bc2, **params):
        """
        保存数据：
        - 文件夹名带尺寸
        - 文件名也带尺寸 + 物理参数
        """
        folder = self._get_dir(N1, N2, bc1, bc2)
        base_name = self._make_filename(name, N1, N2, bc1, bc2, **params)

        if sparse.issparse(data):
            # 稀疏矩阵 -> .npz
            file_path = os.path.join(folder, f"{base_name}.npz")
            sparse.save_npz(file_path, data.tocsc())
            print(f"  [已存稀疏] {os.path.basename(file_path)}")
        else:
            # 数组/标量 -> .npy
            file_path = os.path.join(folder, f"{base_name}.npy")
            np.save(file_path, data)
            print(f"  [已存稠密/标量] {os.path.basename(file_path)}")

    def load_data(self, name, N1, N2, bc1, bc2, **params):
        """
        读取数据：使用同样的优先级规则定位文件
        """
        folder = self._get_dir(N1, N2, bc1, bc2)
        base_name = self._make_filename(name, N1, N2, bc1, bc2, **params)
        
        sparse_path = os.path.join(folder, f"{base_name}.npz")
        dense_path = os.path.join(folder, f"{base_name}.npy")

        if os.path.exists(sparse_path):
            return sparse.load_npz(sparse_path)
        elif os.path.exists(dense_path):
            val = np.load(dense_path, allow_pickle=True)
            return val.item() if val.ndim == 0 else val
        else:
            print(f"  [错误] 未找到文件: {base_name}")
            return None