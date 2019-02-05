#!/bin/bash
#SBATCH -n 1
#SBATCH -p gpu
#SBATCH -t 00:40:00
#SBATCH --mem=10000
#SBATCH -J gpu_job
#SBATCH -o gpu_job.out.%j
#SBATCH -e gpu_job.err.%j
#SBATCH --gres=gpu:k80:1
#SBATCH                                                                                                                                   
ONMTTRAIN=~/OpenNMT-py/train.py
                                           
module purge
module load python-env/intelpython3.6-2018.3 gcc/5.4.0 cuda/9.0 cudnn/7.1-cuda9

DATA=tur-track2

echo $DATA
python $ONMTTRAIN -data onmt-data/$DATA -train_steps 10000 -valid_steps 1000 -save_model models/$DATA.model -world_size 1 -gpu_ranks 0 1 -encoder_type brnn

