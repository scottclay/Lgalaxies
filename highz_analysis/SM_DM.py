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

from bin_data import bin_highz_data
plt.figure(figsize=(9,9))
plt.xlim([6,11])
plt.ylim([0,9.98])


redshift_range = list(range(9,14))
filename = 'SM_DM'
for loop, redshift in enumerate(redshift_range):
	print(redshift)
	try: 
		bin_centres,median,per_50,per_16,per_84,per_25,per_75 = np.loadtxt('./binned_data/'+filename+'_z'+str(redshift)+'.txt',unpack=True,comments='#')
	except IOError:
		bin_centres,median,per_50,per_16,per_84,per_25,per_75 = bin_highz_data('SM','DM',redshift,filename,nbins=30)
	  
	#plt.text(8.2,0.3,"z = "+str(loop), fontsize = 16)
	
	#plot_params(ax[loop],loop,'SM','DM')
	#plot_observations(ax[loop],loop,"SM_DM")

	plt.plot(bin_centres,per_50,zorder=10,linewidth=2,label=str(redshift))
	plt.plot(bin_centres,per_16,zorder=10,linewidth=2)
	plt.plot(bin_centres,per_84,zorder=10,linewidth=2)
'''	
axes = fig.get_axes()
for ax in axes:
	[i.set_linewidth(2.1) for i in ax.spines.values()]
'''
plt.legend()
pylab.savefig('./figs/'+filename+'.png', bbox_inches=0)

