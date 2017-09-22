import numpy as np
import matplotlib.pyplot as plt
import pylab
import sys
import matplotlib

sys.path.append('../data/')
sys.path.append('../src/')

from fetch_observations import plot_observations
from fit_scatter import fit_scatter
from read_pickled_data import produce_df
from read_pickled_data import fetch_lgalaxies
from read_pickled_data import make_selection
from plot_params import plot_params

#col_maps=['afmhot','autumn','bone','cool','copper','gist_heat','gray','spring','winter']

#for map in col_maps:
fig, axs = plt.subplots(nrows=3, ncols=3, sharex=True, sharey=True, figsize=(9,9))
fig.subplots_adjust(hspace=0)
fig.subplots_adjust(wspace=0)

for loop in range(0,9):
#for loop in range(0,1):


    #df = produce_df(redshift=loop, data_path = '../prepare_output/')
    df = fetch_lgalaxies(redshift=loop, data_path = '../prepare_output/',simulation='MR')
    df = make_selection(df,redshift=loop)
    
    plt.subplot(3,3,loop+1)
    plt.xlim([6.,9.98])
    plt.ylim([-5.98,-1.])
    
    plot_params(loop)

    '''
    DM = np.log10(df[df['Dust_Mass']>0.0]['Dust_Mass'])
    SM = np.log10(df[df['Dust_Mass']>0.0]['StellarMass'])
    CG = np.log10(df[df['Dust_Mass']>0.0]['ColdGas'])
    
    OX_D = df[df['Dust_Mass']>0.0]['O_Dust']
    OX_M = df[df['Dust_Mass']>0.0]['O']
    OX = np.log10(OX_D + OX_M)
    #OX = np.log10(OX_M)
    '''    
    DM = np.log10(df['Dust_Mass'])
    SM = np.log10(df['StellarMass'])
    CG = np.log10(df['ColdGas'])
    
    OX_D = df['O_Dust']
    OX_M = df['O']
    #OX = np.log10(OX_D + OX_M)
    Hyd = df['H']
    
    
    OX_Z = np.log10   (( (OX_D + OX_M) /Hyd) * (1.0/16.0)) + 12.0

    
    DTG = DM - CG
    
    DTG = DTG.as_matrix()
    
    
    from fit_scatter import fit_median
    median, bin_centres, per_50,per_16,per_84,per_25,per_75 = fit_median(OX_Z,DTG,10)
    
    '''
    if loop == 0: 
        hb = plt.hexbin(OX_Z,DTG,gridsize=150,bins='log',mincnt=5,cmap='gist_heat')
    
        min = hb.norm.vmin
        max = hb.norm.vmax
        normalize = matplotlib.colors.Normalize(vmin=min, vmax=max)
        print(min,max)
    else:
        plt.hexbin(OX_Z,DTG,gridsize=150,bins='log',mincnt=5,cmap='gist_heat',norm=normalize)
    '''
    plot_observations(loop,"DTG_Oxy")
    #plt.errorbar(x_bins,y_median,yerr=(y_mederr),color='k',label='L-Galaxies Median',linewidth=2)
    
    plt.plot(bin_centres,per_50,c='k',zorder=10,linewidth=2,label='L-Galaxies')
    plt.plot(bin_centres,per_16,'k--',zorder=10,linewidth=2)
    plt.plot(bin_centres,per_84,'k--',zorder=10,linewidth=2)
    
    
    #plt.text(8.2,1.0,"z = "+str(loop), fontsize = 16)
    if loop==8:
        plt.legend(loc='lower right',fontsize = 8)

axes = fig.get_axes()
for ax in axes:
    [i.set_linewidth(2.1) for i in ax.spines.values()]

pylab.savefig('./figs/DTG_oxygen.png', bbox_inches=0)
plt.close()
    




plt.show()


#        plt.text(10,2.5,"z = "+str(loop), fontsize = 16)
        #plt.text(9,1,"z = "+str(loop)+"\nN = "+str(sum(count)),fontsize=16)
        
       # if loop==8:
       #     plt.legend(loc='lower right')
        
# 
