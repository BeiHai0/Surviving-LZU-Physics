import os
import numpy as np
from scipy import sparse
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class KitaevDataManager:
    def __init__(self, root="kitaev_data"):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.param_priority = [
            'bond',
            'N1', 'N2', 'bc1', 'bc2',
            'Kx', 'Ky', 'Kz',
            'kappa',
            'hx', 'hy', 'hz'
        ]

    def _get_dir(self, N1, N2, bc1, bc2):
        path = self.root / f"N1_{N1}_N2_{N2}_bc1_{bc1}_bc2_{bc2}"
        path.mkdir(parents=True, exist_ok=True)
        return path

    def _make_filename(self, name, N1, N2, bc1, bc2, **params):
        forbidden = {'N1', 'N2', 'bc1', 'bc2'}
        duplicates = forbidden & params.keys()
        if duplicates:
            raise ValueError(f"尺寸参数 {duplicates} 不应以关键字参数重复提供。")

        all_args = {'N1': N1, 'N2': N2, 'bc1': bc1, 'bc2': bc2, **params}
        parts = []
        extra = []
        for key in self.param_priority:
            if key in all_args:
                val = all_args[key]
                if isinstance(val, (float, np.floating)):
                    parts.append(f"{key}_{val:.3f}")
                else:
                    parts.append(f"{key}_{val}")

        # 处理未在优先列表中的参数（放在末尾）
        for k, v in all_args.items():
            if k not in self.param_priority:
                extra.append(f"{k}_{v}")
        if extra:
            logger.debug("文件名中追加了非优先参数: %s", extra)
            parts.extend(sorted(extra))   # 保证顺序可复现

        return f"{name}_{'_'.join(parts)}"

    def save_data(self, name, data, N1, N2, bc1, bc2, **params):
        folder = self._get_dir(N1, N2, bc1, bc2)
        base_name = self._make_filename(name, N1, N2, bc1, bc2, **params)

        if sparse.issparse(data):
            file_path = folder / f"{base_name}.npz"
            sparse.save_npz(str(file_path), data.tocsc())
            logger.info("已存稀疏: %s", file_path.name)
        else:
            file_path = folder / f"{base_name}.npy"
            np.save(str(file_path), data)
            logger.info("已存稠密/标量: %s", file_path.name)

    def load_data(self, name, N1, N2, bc1, bc2, **params):
        folder = self._get_dir(N1, N2, bc1, bc2)
        base_name = self._make_filename(name, N1, N2, bc1, bc2, **params)

        sparse_path = folder / f"{base_name}.npz"
        dense_path = folder / f"{base_name}.npy"

        if sparse_path.exists():
            return sparse.load_npz(str(sparse_path))
        elif dense_path.exists():
            data = np.load(str(dense_path))
            return data.item() if data.ndim == 0 else data
        else:
            raise FileNotFoundError(f"未找到文件: {sparse_path} 或 {dense_path}")