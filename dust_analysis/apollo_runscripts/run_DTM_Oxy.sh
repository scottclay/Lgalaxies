#!/bin/bash -l

# Tell SGE that we are using the bash shell
#$ -S /bin/bash

# Say which queue you want to submit to
#$ -q mps.q

# Give the job a name
#$ -N DTM_Oxy_plot

source /etc/profile
shopt -s expand_aliases
module load mps/software/
module load python/3.4.3
source /lustre/scratch/astro/ds381/yt-x86_64/bin/activate

cd /home/s/sc/sc558/Lgalaxies_Analysis/dust_analysis/
rm -f /home/s/sc/sc558/Lgalaxies_Analysis/dust_analysis/logs/DTM_Oxy_plot.log
rm -f /home/s/sc/sc558/Lgalaxies_Analysis/dust_analysis/logs/DTM_Oxy_plot.elog
#$ -o /home/s/sc/sc558/Lgalaxies_Analysis/dust_analysis/logs/DTM_Oxy_plot.log
#$ -e /home/s/sc/sc558/Lgalaxies_Analysis/dust_analysis/logs/DTM_Oxy_plot.elog
python DTM_oxygen.py
