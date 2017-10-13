import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pylab
import sys
import numpy as np
import cloudpickle
import pandas as pd

sys.path.append('../data/')
sys.path.append('../src/')

from fetch_observations import plot_observations
from fit_scatter import fit_scatter
from read_pickled_data import produce_df
from read_pickled_data import fetch_lgalaxies
from read_pickled_data import make_selection
from plot_params import plot_params
from fit_scatter import fit_median

fig, axs = plt.subplots(nrows=2, ncols=2, sharex=False, sharey=False, figsize=(9,9))
ax = axs.reshape(-1)
fig.subplots_adjust(hspace=0.5)
fig.subplots_adjust(wspace=0.5)

dfs = []
DR = []
DMdensity = []
z=[]

for loop in range(9,14):

    df = fetch_lgalaxies(redshift=loop, data_path = '../prepare_output/',simulation='MR')
    df = make_selection(df,redshift=loop)
    
    new_df = pd.DataFrame()
    
    new_df['SM'] = df['SM']
    new_df['DM'] = df['DM']
    new_df['OX_Z'] = df['OX_Z']
    new_df['SFR'] = df['Sfr']
    new_df['DR_AGB'] = df['DustRate_AGB']
    new_df['DR_SNII'] = df['DustRate_SNII']
    new_df['DR_SNIA'] = df['DustRate_SNIA']
    new_df['DR_GROW'] = df['DustRate_GROW']
    new_df['DR_DEST'] = df['DustRate_DEST']
    
    
    
    dfs.append(new_df)
    
colours = ['r','b','g','y','k']    
for loop, redshift in enumerate(list(range(9,14))):
	
	#ax[0] - SM vs DM
	
	df = dfs[loop]
	
	median, bin_centres, per_50, per_16, per_84, per_25, per_75 = fit_median(df['SM'].as_matrix(),df['DM'].as_matrix(),20)
	ax[0].plot(bin_centres,per_50,c=colours[loop],zorder=10,linewidth=2,label='z = '+str(redshift))
	ax[0].plot(bin_centres,per_16,c=colours[loop],linestyle='--',zorder=10,linewidth=2)
	ax[0].plot(bin_centres,per_84,c=colours[loop],linestyle='--',zorder=10,linewidth=2)
	ax[0].legend()
	
	#ax[1] = DM vs. Oxy
	
	median, bin_centres, per_50, per_16, per_84, per_25, per_75 = fit_median(df['OX_Z'].as_matrix(),df['DM'].as_matrix(),20)
	ax[1].plot(bin_centres,per_50,c=colours[loop],zorder=10,linewidth=2,label='z = '+str(redshift))
	ax[1].plot(bin_centres,per_16,c=colours[loop],linestyle='--',zorder=10,linewidth=2)
	ax[1].plot(bin_centres,per_84,c=colours[loop],linestyle='--',zorder=10,linewidth=2)
	ax[1].legend()
	
	
	z.append(redshift)
	DR.append([df['DR_AGB'].sum(),df['DR_AGB'].sum(),df['DR_AGB'].sum(),df['DR_AGB'].sum(),df['DR_AGB'].sum(),df['SFR'].sum()])
	DMdensity.append(df['DM'].sum())
	
volume = (480.279/0.673)**3.0
ax[2].plot(z, np.log10([row[0] for row in DR]/volume), label='AGB')	
	
	
	
	

pylab.savefig('./figs/first_gals.png', bbox_inches=0)

















