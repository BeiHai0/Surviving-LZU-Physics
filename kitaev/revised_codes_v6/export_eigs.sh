#!/bin/bash
#SBATCH -p amd_512
#SBATCH --job-name=kitaev_60_eigs
#SBATCH --array=0-31
#SBATCH --time=00:40:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G

# ===== 环境 =====
source /public1/soft/modules/module.sh
module load miniforge/24.11
source $(conda info --base)/etc/profile.d/conda.sh
conda activate kitaev

cd $SLURM_SUBMIT_DIR

mkdir -p logs

# ===== 参数列表 =====
BONDS=(0 1 2 3)
KS=(1 -1)
KAPPAS=(0.0 0.02 0.04 0.06)

# ===== 用 task_id 映射参数 =====
task_id=$SLURM_ARRAY_TASK_ID

bond_index=$((task_id / 8))
rem=$((task_id % 8))
k_index=$((rem / 4))
kappa_index=$((rem % 4))

bond=${BONDS[$bond_index]}
K=${KS[$k_index]}
kappa=${KAPPAS[$kappa_index]}

Kx=$K
Ky=$K
Kz=$K

# ===== 日志文件名=====
OUT_FILE="logs/bond=${bond}_K=${K}_kappa=${kappa}.out"
ERR_FILE="logs/bond=${bond}_K=${K}_kappa=${kappa}.err"

echo "Running: bond=$bond K=$K kappa=$kappa"

# ===== 运行 =====
python export_eigs.py \
    --bond $bond \
    --Kx $Kx \
    --Ky $Ky \
    --Kz $Kz \
    --kappa $kappa
    > $OUT_FILE 2> $ERR_FILE
