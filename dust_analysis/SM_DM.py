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

from bin_data import bin_data

def plot_SM_DM(redshift_low, redshift_high, filename):
	fig, axs = plt.subplots(nrows=3, ncols=3, sharex=True, sharey=True, figsize=(9,9))
	ax = axs.reshape(-1)
	normalize=0
	fig.subplots_adjust(hspace=0)
	fig.subplots_adjust(wspace=0)


	redshift_range = list(range(redshift_low, redshift_high))
	for loop, redshift in enumerate(redshift_range):
		try: 
			bin_centres,median,per_50,per_16,per_84,per_25,per_75 = np.loadtxt('./binned_data/'+filename+'_z'+str(redshift)+'.txt',unpack=True,comments='#')
			ax[loop] = cloudpickle.load(open('./pkl_hists/'+filename+'_z'+str(redshift)+'.pkl','rb'))
		except IOError:
			bin_centres,median,per_50,per_16,per_84,per_25,per_75,normalize = bin_data('SM','DM',ax,normalize,redshift,filename,nbins=30)
		  
		ax[loop].set_xlim([8,11.97])
		ax[loop].set_ylim([0,9.98])
		ax[loop].text(8.2,0.3,"z = "+str(loop), fontsize = 16)
		
		plot_params(ax[loop],loop,'SM','DM')
		plot_observations(ax[loop],loop,"SM_DM")
	
		ax[loop].plot(bin_centres,per_50,c='k',zorder=10,linewidth=2,label='L-Galaxies')
		ax[loop].plot(bin_centres,per_16,'k--',zorder=10,linewidth=2)
		ax[loop].plot(bin_centres,per_84,'k--',zorder=10,linewidth=2)
	
	axes = fig.get_axes()
	for ax in axes:
		[i.set_linewidth(2.1) for i in ax.spines.values()]

	pylab.savefig('./figs/'+filename+'.png', bbox_inches=0)

plot_SM_DM(0,9,'SM_DM')
