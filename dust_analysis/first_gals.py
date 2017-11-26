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
from bin_data import get_data_dir

fig, axs = plt.subplots(nrows=2, ncols=2, sharex=False, sharey=False, figsize=(9,9))
ax = axs.reshape(-1)
fig.subplots_adjust(hspace=0.3)
fig.subplots_adjust(wspace=0.3)

dfs = []
DR = []
DMdensity = []
z=[]

for loop in range(9,14):
    
    data_path = get_data_dir()
    df = fetch_lgalaxies(redshift=loop, data_path = data_path,simulation='MR')
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
    
    #ax[2+3]
    
    volume = (480.279/0.673)**3.0
    z.append(redshift)
    DR.append([np.log10(df['DR_AGB'].sum()/volume),np.log10(df['DR_SNII'].sum()/volume),np.log10(df['DR_SNIA'].sum()/volume),np.log10(df['DR_GROW'].sum()/volume),np.log10(df['DR_DEST'].sum()/volume),np.log10(df['SFR'].sum()/volume)])
    DMdensity.append(np.log10(df['DM'].sum()/volume))
    
    
    
    
ax[2].plot(z,[row[0] for row in DR], label='AGB',linewidth=2)    
ax[2].plot(z,[row[1] for row in DR], label='SNII',linewidth=2)    
ax[2].plot(z,[row[2] for row in DR], label='SNIA',linewidth=2)    
ax[2].plot(z,[row[3] for row in DR], label='Grain Growth',linewidth=2)    
ax[2].plot(z,[row[4] for row in DR], label='Destruction',linewidth=2)    
ax[2].legend()

ax[3].plot(z,DMdensity,linewidth=2)    

ax[0].set_xlabel(r'log$_{10}$(M$_{*}$/M$_{\odot}$)', fontsize=18)
ax[0].set_ylabel(r'log$_{10}$(M$_{\rm{D}}$/M$_{\odot}$)', fontsize=18)
ax[1].set_xlabel(r'12 + log$_{10}$(O/H)', fontsize=18)
ax[1].set_ylabel(r'log$_{10}$(M$_{\rm{D}}$/M$_{\odot}$)', fontsize=18)
ax[2].set_xlabel(r'z', fontsize=18,labelpad=10)
ax[2].set_ylabel(r'log$_{10}$($\phi_{DR}$) [M$_{\odot}$yr$^{-1}$Mpc$^{-3}$]', fontsize=18,labelpad=0)
ax[3].set_xlabel(r'z', fontsize=18,labelpad=10)
ax[3].set_ylabel(r'log$_{10}$($\rho_{DM}$)[M$_{\odot}$Mpc$^{-3}$]', fontsize=18,labelpad=0)

for count in range(0,4):
    ax[count].tick_params(axis='both', which='major', labelsize=12,width=2)
    ax[count].tick_params(axis='both', which='minor', labelsize=12,width=2)
    [i.set_linewidth(2.1) for i in ax[count].spines.values()]


pylab.savefig('./figs/first_gals.eps', bbox_inches=0)

















