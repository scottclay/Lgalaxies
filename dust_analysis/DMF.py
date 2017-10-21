import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pylab
import sys
import numpy as np



sys.path.append('../data/')
sys.path.append('../src/')

from fetch_observations import plot_observations
from fit_scatter import fit_scatter
from read_pickled_data import produce_df
from read_pickled_data import fetch_lgalaxies
from read_pickled_data import make_selection
from plot_params import plot_params

fig, axs = plt.subplots(nrows=3, ncols=3, sharex=True, sharey=True, figsize=(9,9))
ax = axs.reshape(-1)
fig.subplots_adjust(hspace=0)
fig.subplots_adjust(wspace=0)

for loop in range(0,9):

	try: 
		bin_centers,hist = np.loadtxt('./binned_data/DMF_z'+str(loop)+'.txt',unpack=True,comments='#')
	except IOError:
		print("Missing data - will create")
		#df = fetch_lgalaxies(redshift=loop, data_path = '../prepare_output/',simulation='MR')
		df = fetch_lgalaxies(redshift=loop,simulation='MR')
		df = make_selection(df,redshift=loop)
		DM = np.log10(df[df['Dust_Mass']>0.0]['Dust_Mass'])
		
		hist, bin_edges = np.histogram(DM,bins=50)
		bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
		binsize = (bin_centers[-1] - bin_centers[0])/len(bin_centers)
		volume_MR = (480.279/0.673)**3.0
		hist = hist/(volume_MR*binsize)

		np.savetxt('./binned_data/DMF_z'+str(loop)+'.txt',np.c_[bin_centers,hist])


	ax[loop].set_xlim([6.,9.99])
	ax[loop].set_ylim([-6.,-0.02])
	#if loop == 0:
	#	ax[loop].set_ylim([-6,0.05])
	#if loop == 8:
	#	ax[loop].set_xlim([6.0,10.0])	
	
	
	plot_params(ax[loop],loop, 'DMF','DMF')

	plot_observations(ax[loop],loop,"DMF")
	
	ax[loop].plot(bin_centers,np.log10(hist),c='k',zorder=10,linewidth=2,label='L-Galaxies')
	ax[loop].text(8.5,-2,"z = "+str(loop),fontsize=16)

	[i.set_linewidth(2.1) for i in ax[loop].spines.values()]

pylab.savefig('./figs/DMF.eps', bbox_inches=0)
plt.close()
    




plt.show()
