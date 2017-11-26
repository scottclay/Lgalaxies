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
from bin_data import get_data_dir

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
        data_path = get_data_dir()
        df = fetch_lgalaxies(redshift=loop, data_path = data_path,simulation='MR')
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


    ax[loop].set_xlim([9.,11.3])
    ax[loop].set_ylim([-6.,2.0])
    
    if loop == 0:
    	ax[loop].set_ylim([-6.,2.0])
    if loop == 8:
        ax[loop].set_xlim([9.0,11.3])
            
    plot_params(ax[loop], loop,'SM','DRate')
    #plot_observations(loop,"SM_DM")
    
    
    ax[loop].plot(AGB_bin_centres,AGB_median,c='b',zorder=10,linewidth=2,label='AGB')
    ax[loop].plot(SNII_bin_centres,SNII_median,c='r',zorder=10,linewidth=2,label='SNII')
    ax[loop].plot(SNIA_bin_centres,SNIA_median,c='y',zorder=10,linewidth=2,label='SNIA')
    ax[loop].plot(GROW_bin_centres,GROW_median,c='g',zorder=10,linewidth=2,label='Grain Growth')
    ax[loop].plot(DEST_bin_centres,DEST_median,c='k',zorder=10,linewidth=2,label='Destruction')
    
    ax[loop].plot(AGB_bin_centres,AGB_16,'b--',zorder=10,linewidth=2)
    ax[loop].plot(AGB_bin_centres,AGB_84,'b--',zorder=10,linewidth=2)
    ax[loop].plot(SNII_bin_centres,SNII_16,'r--',zorder=10,linewidth=2)
    ax[loop].plot(SNII_bin_centres,SNII_84,'r--',zorder=10,linewidth=2)
    ax[loop].plot(SNIA_bin_centres,SNIA_16,'y--',zorder=10,linewidth=2)
    ax[loop].plot(SNIA_bin_centres,SNIA_84,'y--',zorder=10,linewidth=2)
    ax[loop].plot(GROW_bin_centres,GROW_16,'g--',zorder=10,linewidth=2)
    ax[loop].plot(GROW_bin_centres,GROW_84,'g--',zorder=10,linewidth=2)
    ax[loop].plot(DEST_bin_centres,DEST_16,'k--',zorder=10,linewidth=2)
    ax[loop].plot(DEST_bin_centres,DEST_84,'k--',zorder=10,linewidth=2)
    

    
    
    
    ax[loop].text(9.4,-5.5,"z = "+str(loop), fontsize = 16)
    if loop==8:
        ax[loop].legend(loc='lower right',fontsize = 8)

    [i.set_linewidth(2.1) for i in ax[loop].spines.values()]

pylab.savefig('./figs/SM_DRate.eps', bbox_inches=0)
plt.close()
    




plt.show()
