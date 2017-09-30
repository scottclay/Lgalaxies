#!/bin/bash -l

# Tell SGE that we are using the bash shell
#$ -S /bin/bash

# Say which queue you want to submit to
#$ -q mps.q

# Give the job a name
#$ -N SM_DM_plot

source /etc/profile
shopt -s expand_aliases
module load mps/software/
module load python/3.4.3
source /lustre/scratch/astro/ds381/yt-x86_64/bin/activate

cd /home/s/sc/sc558/Lgalaxies_Analysis/dust_analysis/
rm /home/s/sc/sc558/Lgalaxies_Analysis/dust_analysis/apollo/SM_DM_plot.log
rm /home/s/sc/sc558/Lgalaxies_Analysis/dust_analysis/apollo/SM_DM_plot.elog
#$ -o /home/s/sc/sc558/Lgalaxies_Analysis/dust_analysis/apollo/SM_DM_plot.log
#$ -e /home/s/sc/sc558/Lgalaxies_Analysis/dust_analysis/apollo/SM_DM_plot.elog
python SM_DM.py
