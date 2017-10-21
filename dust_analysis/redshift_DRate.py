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
	redshift, DustRate_AGB, DustRate_SNII, DustRate_SNIA, DustRate_GROW, DustRate_DEST, DustRate_ALL, SFR_density = np.loadtxt('./binned_data/redshift_DRate.txt',unpack=True,comments='#')

except IOError:
	print("Missing data - will create")
	redshift      = []
	DustRate_AGB  = []
	DustRate_SNII = []
	DustRate_SNIA = []
	DustRate_GROW = []
	DustRate_DEST = []
	DustRate_ALL  = []
	SFR_density  = []
	for loop in range(0,9):
		#df = fetch_lgalaxies(redshift=loop, data_path = '../prepare_output/',simulation='MR')
		df = fetch_lgalaxies(redshift=loop,simulation='MR')
		df = make_selection(df,redshift=loop)
	
		SM = np.log10(df[df['Dust_Mass']>0.0]['StellarMass'])
		
		SFR = (df[df['Dust_Mass']>0.0]['Sfr'].sum())
	
		AGB_DustRate  = (df[df['Dust_Mass']>0.0]['DustRate_AGB'].sum())
		SNII_DustRate = (df[df['Dust_Mass']>0.0]['DustRate_SNII'].sum())
		SNIA_DustRate = (df[df['Dust_Mass']>0.0]['DustRate_SNIA'].sum())
		GROW_DustRate = (df[df['Dust_Mass']>0.0]['DustRate_GROW'].sum())
		DEST_DustRate = (df[df['Dust_Mass']>0.0]['DustRate_DEST'].sum())
	
		ALL_DustRate = AGB_DustRate + SNII_DustRate + SNIA_DustRate + GROW_DustRate - DEST_DustRate 
	
		volume = (480.279/0.673)**3.0

		redshift.append(loop)
		DustRate_AGB.append(np.log10(AGB_DustRate/volume))
		DustRate_SNII.append(np.log10(SNII_DustRate/volume))
		DustRate_SNIA.append(np.log10(SNIA_DustRate/volume))
		DustRate_GROW.append(np.log10(GROW_DustRate/volume))
		DustRate_DEST.append(np.log10(DEST_DustRate/volume))
		DustRate_ALL.append(np.log10(ALL_DustRate/volume))
		SFR_density.append(np.log10(SFR/volume))

	np.savetxt('./binned_data/redshift_DRate_z.txt',np.c_[redshift, DustRate_AGB, DustRate_SNII, DustRate_SNIA, DustRate_GROW, DustRate_DEST, DustRate_ALL,SFR_density])

fig = plt.figure(figsize=(7,7))
plt.xlabel(r'z', fontsize=18,labelpad=10)
plt.ylabel(r'log$_{10}$($\phi_{DR}$) [M$_{\odot}$yr$^{-1}$Mpc$^{-3}$]', fontsize=18,labelpad=0)
plt.xlim(-0.2,9.0)

plt.tick_params(axis='both', which='major', labelsize=12,width=2)
plt.tick_params(axis='both', which='minor', labelsize=12,width=2)

plt.plot(redshift,DustRate_AGB , color='b',label='AGB',linewidth = 2)
plt.plot(redshift,DustRate_SNII, color='r',label='SNII',linewidth = 2)
plt.plot(redshift,DustRate_SNIA, color='y',label='SNIA',linewidth = 2)
plt.plot(redshift,DustRate_GROW, color='g',label='GG',linewidth = 2)
plt.plot(redshift,DustRate_DEST, color='k',label='DEST',linewidth = 2)
plt.plot(redshift,DustRate_ALL,  color='orange',label='NET',linewidth = 2)
#plt.plot(DustRate_z,DustRate_GROW_z+DustRate_AGB_z+DustRate_SNIA_z+DustRate_SNII_z-DustRate_DEST_z, color='cyan', linestyle='--', linewidth=2,label='Net')
plt.plot(redshift,SFR_density, color='cyan', linestyle='--', linewidth=2,label='SFR')
plt.legend(loc='lower right')

axes = fig.get_axes()
for ax in axes:
    [i.set_linewidth(2.1) for i in ax.spines.values()]

pylab.savefig('./figs/redshift_DRate.eps', bbox_inches=0)
plt.close()

