import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pylab
import sys
import numpy as np
import cloudpickle

sys.path.append('../data/')
sys.path.append('../src/')

from fetch_observations import plot_observations
from fit_scatter import fit_scatter
from read_pickled_data import produce_df
from read_pickled_data import fetch_lgalaxies
from read_pickled_data import make_selection
from plot_params import plot_params
from fit_scatter import fit_median

fig, axs = plt.subplots(nrows=3, ncols=3, sharex=True, sharey=True, figsize=(9,9))
ax = axs.reshape(-1)
fig.subplots_adjust(hspace=0)
fig.subplots_adjust(wspace=0)

for loop in range(0,9):

	try: 
		AGB_bin_centres,AGB_median,AGB_50,AGB_16,AGB_84,AGB_25,AGB_75  = np.loadtxt('./binned_data/SM_DRate_AGB_'+str(loop)+'.txt',unpack=True,comments='#')
		SNII_bin_centres,SNII_median,SNII_50,SNII_16,SNII_84,SNII_25,SNII_75 = np.loadtxt('./binned_data/SM_DRate_SNII_'+str(loop)+'.txt',unpack=True,comments='#')
		SNIA_bin_centres,SNIA_median,SNIA_50,SNIA_16,SNIA_84,SNIA_25,SNIA_75 = np.loadtxt('./binned_data/SM_DRate_SNIA_'+str(loop)+'.txt',unpack=True,comments='#')
		GROW_bin_centres,GROW_median,GROW_50,GROW_16,GROW_84,GROW_25,GROW_75 = np.loadtxt('./binned_data/SM_DRate_GROW_'+str(loop)+'.txt',unpack=True,comments='#')
		DEST_bin_centres,DEST_median,DEST_50,DEST_16,DEST_84,DEST_25,DEST_75 = np.loadtxt('./binned_data/SM_DRate_DEST_'+str(loop)+'.txt',unpack=True,comments='#')
	
	except IOError:
		print("Missing data - will create")
		#df = fetch_lgalaxies(redshift=loop, data_path = '../prepare_output/',simulation='MR')
		df = fetch_lgalaxies(redshift=loop,simulation='MR')
		df = make_selection(df,redshift=loop)
		
		SM = np.log10(df[df['Dust_Mass']>0.0]['StellarMass'])
		
		AGB_DustRate  = np.log10(df[df['Dust_Mass']>0.0]['DustRate_AGB'])
		SNII_DustRate = np.log10(df[df['Dust_Mass']>0.0]['DustRate_SNII'])
		SNIA_DustRate = np.log10(df[df['Dust_Mass']>0.0]['DustRate_SNIA'])
		GROW_DustRate = np.log10(df[df['Dust_Mass']>0.0]['DustRate_GROW'])
		DEST_DustRate = np.log10(df[df['Dust_Mass']>0.0]['DustRate_DEST'])

		AGB_DustRate  = AGB_DustRate.as_matrix()
		SNII_DustRate = SNII_DustRate.as_matrix()
		SNIA_DustRate = SNIA_DustRate.as_matrix()
		GROW_DustRate = GROW_DustRate.as_matrix()
		DEST_DustRate = DEST_DustRate.as_matrix()
		

		AGB_median,AGB_bin_centres,AGB_50,AGB_16,AGB_84,AGB_25,AGB_75 = fit_median(SM,AGB_DustRate,10)
		np.savetxt('./binned_data/SM_DRate_AGB_'+str(loop)+'.txt',np.c_[AGB_bin_centres,AGB_median,AGB_50,AGB_16,AGB_84,AGB_25,AGB_75])

		SNII_median,SNII_bin_centres,SNII_50,SNII_16,SNII_84,SNII_25,SNII_75 = fit_median(SM,SNII_DustRate,10)
		np.savetxt('./binned_data/SM_DRate_SNII_'+str(loop)+'.txt',np.c_[SNII_bin_centres,SNII_median,SNII_50,SNII_16,SNII_84,SNII_25,SNII_75])

		SNIA_median,SNIA_bin_centres,SNIA_50,SNIA_16,SNIA_84,SNIA_25,SNIA_75 = fit_median(SM,SNIA_DustRate,10)
		np.savetxt('./binned_data/SM_DRate_SNIA_'+str(loop)+'.txt',np.c_[SNIA_bin_centres,SNIA_median,SNIA_50,SNIA_16,SNIA_84,SNIA_25,SNIA_75])

		GROW_median,GROW_bin_centres,GROW_50,GROW_16,GROW_84,GROW_25,GROW_75 = fit_median(SM,GROW_DustRate,10)
		np.savetxt('./binned_data/SM_DRate_GROW_'+str(loop)+'.txt',np.c_[GROW_bin_centres,GROW_median,GROW_50,GROW_16,GROW_84,GROW_25,GROW_75])

		DEST_median,DEST_bin_centres,DEST_50,DEST_16,DEST_84,DEST_25,DEST_75 = fit_median(SM,DEST_DustRate,10)
		np.savetxt('./binned_data/SM_DRate_DEST_'+str(loop)+'.txt',np.c_[DEST_bin_centres,DEST_median,DEST_50,DEST_16,DEST_84,DEST_25,DEST_75])


	plt.subplot(3,3,loop+1)
	plt.xlim([6,12])
	plt.ylim([-10,2.5])
	
	        
	plot_params(loop,'SM','DRate')
	#plot_observations(loop,"SM_DM")
	
	
	plt.plot(AGB_bin_centres,AGB_median,c='b',zorder=10,linewidth=2,label='AGB')
	plt.plot(SNII_bin_centres,SNII_median,c='r',zorder=10,linewidth=2,label='SNII')
	plt.plot(SNIA_bin_centres,SNIA_median,c='y',zorder=10,linewidth=2,label='SNIA')
	plt.plot(GROW_bin_centres,GROW_median,c='g',zorder=10,linewidth=2,label='GROW')
	plt.plot(DEST_bin_centres,DEST_median,c='k',zorder=10,linewidth=2,label='DEST')
	
	plt.plot(AGB_bin_centres,AGB_16,'b--',zorder=10,linewidth=2)
	plt.plot(AGB_bin_centres,AGB_84,'b--',zorder=10,linewidth=2)
	plt.plot(SNII_bin_centres,SNII_16,'r--',zorder=10,linewidth=2)
	plt.plot(SNII_bin_centres,SNII_84,'r--',zorder=10,linewidth=2)
	plt.plot(SNIA_bin_centres,SNIA_16,'y--',zorder=10,linewidth=2)
	plt.plot(SNIA_bin_centres,SNIA_84,'y--',zorder=10,linewidth=2)
	plt.plot(GROW_bin_centres,GROW_16,'g--',zorder=10,linewidth=2)
	plt.plot(GROW_bin_centres,GROW_84,'g--',zorder=10,linewidth=2)
	plt.plot(DEST_bin_centres,DEST_16,'k--',zorder=10,linewidth=2)
	plt.plot(DEST_bin_centres,DEST_84,'k--',zorder=10,linewidth=2)
	

	
	
	
	plt.text(8.2,1.0,"z = "+str(loop), fontsize = 16)
	if loop==8:
		plt.legend(loc='lower right',fontsize = 8)

axes = fig.get_axes()
for ax in axes:
    [i.set_linewidth(2.1) for i in ax.spines.values()]

pylab.savefig('./figs/SM_DRate.png', bbox_inches=0)
plt.close()
    




plt.show()
