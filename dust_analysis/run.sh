#!/bin/bash -l

# Tell SGE that we are using the bash shell
#$ -S /bin/bash

# Say which queue you want to submit to
#$ -q mps.q

# Give the job a name
#$ -N run1

source /etc/profile
shopt -s expand_aliases
module load mps/software/
module load python/2.7.8
source /home/s/sc/sc558/my_python_stack/bin/activate

cd /home/s/sc/sc558/lgal_clay17/Analysis/python2/apollo/
#$ -o /home/s/sc/sc558/lgal_clay17/Analysis/python2/apollo/logs/run1.log
#$ -e /home/s/sc/sc558/lgal_clay17/Analysis/python2/apollo/logs/run1.elog
python stellar_dust_masses.py

