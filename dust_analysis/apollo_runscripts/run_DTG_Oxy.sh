#!/bin/bash -l

# Tell SGE that we are using the bash shell
#$ -S /bin/bash

# Say which queue you want to submit to
#$ -q mps.q

# Give the job a name
#$ -N DTG_Oxy_plot

source /etc/profile
shopt -s expand_aliases
module load mps/software/
module load python/3.4.3
source /lustre/scratch/astro/sc558/my_python/bin/activate

cd /home/s/sc/sc558/Lgalaxies_Analysis/dust_analysis/
#$ -o /home/s/sc/sc558/Lgalaxies_Analysis/dust_analysis/logs/DTG_Oxy_plot.log
#$ -e /home/s/sc/sc558/Lgalaxies_Analysis/dust_analysis/logs/DTG_Oxy_plot.elog
python DTG_oxygen.py
