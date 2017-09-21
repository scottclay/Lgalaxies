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


datadir   = '../../Hen15_Dustmodel/output/'
output_dir = './MRII/'

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
	0.00:"058",
	1.04:"038",
	2.07:"030",
	3.11:"025",
	3.95:"022",
	5.03:"019",
	5.92:"017",
	6.97:"015",
	8.22:"013",
	8.93:"012",	
	9.72:"011",	
	10.57:"010",	
	11.51:"009",	
	12.53:"008",		
	13.66:"007",
	14.90:"006"
	}

min_redshift = 0.00
max_redshift = 15.00

# Define which files you want to read in
#firstfile = 0
#lastfile = 511

desired_redshifts = {}
for redshift in file_prefix.keys():
	if redshift>=min_redshift and redshift <= max_redshift+0.5:
		#print(redshift,file_prefix[redshift])
		desired_redshifts.update({redshift:file_prefix[redshift]})

print(desired_redshifts)


for j in range(0,5):
	if j == 0:
		firstfile = 0
		lastfile = 100
	elif j==1:
		firstfile = 101
		lastfile = 200
	elif j==2:
		firstfile = 201
		lastfile = 300
	elif j==3:
		firstfile = 301
		lastfile = 400
	elif j==4:
		firstfile = 401
		lastfile = 511

	firstfile = 40
	lastfile = 40
		
	for i, redshift in enumerate(sorted(desired_redshifts.keys()),int(round(min_redshift))):
		print (i,redshift)
		snapshot = desired_redshifts[redshift]
		file_prefix = "SA_z"+str("%.2f" % redshift)
		#output_file = "../data/MR/lgal_z"+str(i)+".pkl"
		output_file = output_dir+"lgal_z"+str(i)+"_N"+str(j)
		#snapdir = datadir+"snapdir_"+snapshot
		snapdir = datadir
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
	



