#!/bin/bash
#SBATCH --job-name=PyCronoGPU_CPU
#SBATCH --output=%x.o%j
#SBATCH --error=%x.e%j
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=21
#SBATCH --gres=gpu:tesla:1
#SBATCH --mem=16G
#SBATCH --time=10:05:00
#SBATCH --partition=gpu
#
# Edit next line
##SBATCH --account<SimoneBenatti>
#

source activate pychrono
python ./PPO/train_parallel.py ChronoAnt -n 20000

