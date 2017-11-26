# L-Galaxies Dust Analysis
This repo holds the data analysis pipeline used to obtain all the plots in Clay17 from the detailed dust implemenation of L-Galaxies available here: https://github.com/scottclay/Lgalaxies_Dust

To use this pipeline, you should first go to https://github.com/scottclay/Lgalaxies_Dust and follow the instructions for running the model. 

# Running the pipeline

A step by step series of instructions to run this pipeline is given below. 

* ```git clone https://github.com/scottclay/Lgalaxies_Analysis.git```


## Sorting the output data

If you have run the model on the full millennium box, you will have an output directory with a very large amount of files. The first thing you should do is run the tools in ```/prepare_output/tools/``` to sort these files into their respective snapshot directories. 

```./rehome.sh snaplist_file model_output_dir where_you_want_the_files```

* ```rehome.sh``` and the ```snaplist_file``` for MR/MRII Planck is available in ```/prepare_output/tools/```
* ```model_output_dir``` is the location of the L-Galaxies Dust output files from running the model at https://github.com/scottclay/Lgalaxies_Dust
* ```where_you_want_the_files``` is the directory you want to store the files

## Pickling the data (Python)

You should now pickle the data. 
* ```cd Lgalaxies_Analysis/prepare_output/```
* edit the file paths in ```script_read_allz_apollo.py``` to match the ```where_you_want_the_files``` from above and for where you want the pickled data to go
* run ```run_script.sh```

```run_script.sh``` sends ```script_read_allz_apollo.py``` to apollo and pickles the data for redshifts z=0-15. 

NOTES:
* You can change what information is in the pickled output in ```script_read_allz_apollo.py```
* You can see all available information from the L-Galaxies dust output in the snap_template located at ```/data/snap_template.py```
* This pipeline assumes the data is stored in the following format:
```
Clay2018 (this can be named anything)
└───MR
│   │   Pickled
│   
└───MRII
    │   Pickled
```

### Plotting the graphs

You should first edit the file path in the get_data_dir function in ```/src/bin_data.py``` to match that of the top output data directory (in the case above, that would be ```Clay2018``` (don't include MR or MRII or pickled in this directory as the pipeline can be used to call MR or MRII or both itself). 

* Change to the ```/prepare_output/``` subdirectory
* ```python script_read_allz_local.py MR```
* Change to the ```/dust_analysis/``` subdirectory
* ```python SM_DM.py``` will output the SM_DM.eps to ```/dust_analysis/figs/``` and the binned data to ```/dust_analysis/binned_data/```
* Alternatively, ```./produce_all.sh``` will create all plots


 
