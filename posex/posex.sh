#!/bin/sh

#$ -N posex    
#$ -wd /exports/eddie/scratch/s2520601/references/                  
#$ -l h_rt=05:00:00 
#$ -l h_rss=4G
#$ -pe sharedmem 4
#$ -P roslin_prendergast_cores
#$ -l rl9=true

# initialize environment
. /etc/profile.d/modules.sh

# activate cactus environment
source /exports/applications/apps/RL9/anaconda/2024.02/etc/profile.d/conda.sh
conda activate snake


WORKDIR="/exports/eddie/scratch/s2520601/references/codebase_master/posEx/"
cd ${WORKDIR}

snakemake --cores 4