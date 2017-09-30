#!/bin/bash

# To check to log files to see if the batch jobs completed successfully

echo Number of log files is `ls dust/logs/Clay17_Dust_MR_*.log | wc -l`

for file in `ls dust/logs/Clay17_Dust_MR_*.log`
do
    if ! grep -q "done tree file" $file 
    then
	echo File $file failed to complete properly
    fi
done


# echo Number of log files is `ls MRIIlogs/Hen14_MRII_*.log | wc -l`
# 
# for file in `ls MRIIlogs/Hen14_MRII_*.log`
# do
#     if ! grep -q "done tree file" $file 
#     then
# 	echo File $file failed to complete properly
#     fi
# done

