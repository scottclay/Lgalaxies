#!/bin/bash

FILENAME=$1
count0=
exec 3<&0
exec 0< $FILENAME

trap "exit" INT
while read LINE
do
	    a=( $LINE )
        if ls $2/SA_z${a[1]}_* &> /dev/null; then
    
    	    echo "Creating directory snapdir_${a[0]}"
    	    mkdir -p $3/snapdir_${a[0]}
			echo "Moving files at redshift ${a[1]}"
			mv $2/SA_z${a[1]}_* $3/snapdir_${a[0]}/
			echo "Files at redshift ${a[1]} moved succesfully "
		
		else
			echo "No files exist at redshift ${a[1]} "
		fi
done

exec 0<&3