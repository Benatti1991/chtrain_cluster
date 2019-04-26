#!/bin/bash
#SBATCH --job-name=PyCronoGPU_CPU
#SBATCH --output=%x.o%j
#SBATCH --error=%x.e%j
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=21
#SBATCH --gres=gpu:tesla:1
#SBATCH --mem=32G
#SBATCH --time=10:05:00
#SBATCH --partition=gpu
#
# Edit next line
##SBATCH --account<SimoneBenatti>
#

source activate myenv
python ./PPO/train_parallel.py ChronoRacer3 -n 10000

