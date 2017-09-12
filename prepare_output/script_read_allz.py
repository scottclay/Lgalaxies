#=========================================================================
#
#  Script to read in L-galaxies snapshot data
#
#  To force a re-read of the data do Gal=None
#
#-------------------------------------------------------------------------

# Imports
# 
import sys

#datadir = '../../Hen15_Dustmodel/output/'
datadir   = '../../Hen15_Dustmodel/output/'
output_dir = './'

sys.path.insert(0,datadir)

# Template structure for L-Galaxies data
sys.path.append('../data/')
sys.path.append('../src/')
import snap_template   # structure temple for data
import read_lgal       # function to read in data
# 
#-------------------------------------------------------------------------
import time 
start_all = time.time()
# Parameters

# Snaplist file
#snaplist_file = '../MRPlancksnaplist.txt'


file_prefix = {
	0.00:58,
	1.04:38,
	2.07:30,
	3.11:25,
	3.95:22,
	5.03:19,
	5.92:17,
	6.97:15,
	8.22:13,
	8.93:12,	
	9.72:11,	
	10.57:10,	
	11.51:9,	
	12.53:8,		
	13.66:7,
	14.90:6
	}

min_redshift = 0.00
max_redshift = 15.00

# Define which files you want to read in
firstfile = 5
lastfile = 5

desired_redshifts = {}
for redshift in file_prefix.keys():
	if redshift>=min_redshift and redshift <= max_redshift+0.5:
		#print(redshift,file_prefix[redshift])
		desired_redshifts.update({redshift:file_prefix[redshift]})

print(desired_redshifts)

for i, redshift in enumerate(desired_redshifts.keys(),int(round(min_redshift))):
	snapshot = desired_redshifts[redshift]
	file_prefix = "SA_z"+str("%.2f" % redshift)
	#output_file = "../data/MR/lgal_z"+str(i)+".pkl"
	output_file = output_dir+"lgal_z"+str(i)
	snapdir = datadir+"snapdir_0"+str(snapshot)
	#snapdir = datadir
	#print(i,snapshot, file_prefix, output_file)
	

	# Define what properties you want to read in
	props = snap_template.properties_used

	props['Type'] = True
	props['ColdGas'] = True
	props['StellarMass'] = True
	props['BulgeMass'] = True
	props['DiskMass'] = True
	props['HotGas'] = True
	props['ICM'] = True
	props['MetalsColdGas'] = True
	props['MetalsBulgeMass'] = True
	props['MetalsDiskMass'] = True
	props['MetalsHotGas'] = True
	props['MetalsEjectedMass'] = True
	props['MetalsICM'] = True
	props['Sfr'] = True
	props['SfrBulge'] = True
	props['DiskMass_elements'] = True
	props['BulgeMass_elements'] = True
	props['ColdGas_elements'] = True
	props['HotGas_elements'] = True
	#props['DustMassISM'] = True
	props['DustRatesISM'] = True
	props['Dust_elements'] = True
	props['Attenuation_Dust'] = True
	props['Mag'] = True
	props['MagDust'] = True
	props['GasDiskRadius'] = True
	# 
	#-------------------------------------------------------------------------

	# Working body of the program

	# Read in galaxy output
	(nTrees,nHalos,nTreeHalos,gals) = \
		read_lgal.read_snap(snapdir,file_prefix,firstfile,lastfile,\
								props,snap_template.struct_dtype)

	
	if str(sys.argv[1]) == 'MR': 
		mass_limit = 10**8.5
	elif str(sys.argv[1]) == 'MRII': 
		mass_limit = 10**6.5
		
	gals_to_save =gals[gals['StellarMass']*1.0E10/0.673>mass_limit]
	
	
	import pickle as cPickle
	fout = open(output_file+".pkl",'wb')
	cPickle.dump(gals_to_save,fout,cPickle.HIGHEST_PROTOCOL)
	fout.close()
	



