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
from fit_scatter import fit_median


#fig, axs = plt.subplots(nrows=3, ncols=3, sharex=True, sharey=True, figsize=(9,9))
#fig.subplots_adjust(hspace=0)
#fig.subplots_adjust(wspace=0)


try: 
	redshift, DM_density = np.loadtxt('./binned_data/redshift_DMdensity.txt',unpack=True,comments='#')

except IOError:
	print("Missing data - will create")
	redshift      = []
	DM_density  = []
	
	for loop in range(0,9):
		df = fetch_lgalaxies(redshift=loop, data_path = '../prepare_output/',simulation='MR')
		#df = fetch_lgalaxies(redshift=loop,simulation='MR')
		df = make_selection(df,redshift=loop)
	
		SM = np.log10(df[df['Dust_Mass']>0.0]['StellarMass'])
	
		DM  = (df[df['Dust_Mass']>0.0]['Dust_Mass'].sum())

		volume = (480.279/0.673)**3.0

		redshift.append(loop)
		DM_density.append(np.log10(DM/volume))

	np.savetxt('./binned_data/redshift_DMdensity.txt',np.c_[redshift, DM_density])

fig = plt.figure(figsize=(7,7))
plt.xlabel(r'redshift', fontsize=18,labelpad=10)
plt.ylabel(r'log$_{10}$(dust mass density Msol/Mpc$^3$)', fontsize=18,labelpad=0)
plt.xlim(-1,10)

plt.tick_params(axis='both', which='major', labelsize=12,width=2)
plt.tick_params(axis='both', which='minor', labelsize=12,width=2)

plt.plot(redshift,DM_density , color='k',label='lgal',linewidth = 2)
plt.legend(loc='lower right')

axes = fig.get_axes()
for ax in axes:
    [i.set_linewidth(2.1) for i in ax.spines.values()]

pylab.savefig('./figs/redshift_DMdensity.png', bbox_inches=0)
plt.close()

