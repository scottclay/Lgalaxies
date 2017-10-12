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

fig, axs = plt.subplots(nrows=3, ncols=3, sharex=True, sharey=True, figsize=(9,9))
#ax = axs.reshape(-1)
ax = axs.ravel()
normalize=0
fig.subplots_adjust(hspace=0)
fig.subplots_adjust(wspace=0)

from fetch_observations import fetch_observations
RR_2014, RR_2015, Santini_2014, daCunha_2015, Mancini_2015, Bourne_2012, Ciesla_2014, Wiseman_2017, Clemens_2013, VlahakisA_2005, VlahakisB_2005 = fetch_observations()



for loop in range(0,9):
    try: 
        bin_centres,median,per_50,per_16,per_84,per_25,per_75 = np.loadtxt('./binned_data/DM_OX_z'+str(loop)+'.txt',unpack=True,comments='#')
        ax[loop] = cloudpickle.load(open('./pkl_hists/DM_OX_z'+str(loop)+'.pkl','rb'))
    except IOError:
        bin_centres,median,per_50,per_16,per_84,per_25,per_75,normalize = bin_data('OX_Z','DM',ax,normalize,loop,'DM_OX',nbins=30)



    #plt.subplot(3,3,loop+1)
    ax[loop].set_xlim([6.,9.98])
    ax[loop].set_ylim([0,9.98])

    plot_params(ax[loop], loop,'O','DM')

    #plot_observations(loop,"DTG_Oxy")
    
    #if loop == 0:
    #    ax[0].scatter(RR_2015['Oxygen'], RR_2015['DM_1'], color='g')

    ax[loop].plot(bin_centres,per_50,c='k',zorder=10,linewidth=2,label='L-Galaxies')
    ax[loop].plot(bin_centres,per_16,'k--',zorder=10,linewidth=2)
    ax[loop].plot(bin_centres,per_84,'k--',zorder=10,linewidth=2)
    if loop == 0:
    	#ax[loop].scatter(RR_2015['Oxygen'], RR_2015['DM_1'], color='g')
        ax[loop].errorbar(RR_2015['Oxygen'], RR_2015['DM_1'], yerr = (RR_2015['DM_1_down'], RR_2015['DM_1_up']),color='g',label='Remy-Ruyer2015',fmt='.')

    #print (RR_2015.head(5))
    print(ax)
    print(axs)
    print(axs.ravel())


    #if loop==8:
    #    plt.legend(loc='lower right',fontsize = 8)

axes = fig.get_axes()
for ax in axes:
    [i.set_linewidth(2.1) for i in ax.spines.values()]

pylab.savefig('./figs/DM_oxygen.png', bbox_inches=0)
plt.close()
    

