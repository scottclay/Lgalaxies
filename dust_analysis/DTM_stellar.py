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
ax = axs.reshape(-1)
normalize=0
fig.subplots_adjust(hspace=0)
fig.subplots_adjust(wspace=0)


for loop in range(0,9):
    try: 
        bin_centres,median,per_50,per_16,per_84,per_25,per_75 = np.loadtxt('./binned_data/SM_DTM_z'+str(loop)+'.txt',unpack=True,comments='#')
        ax[loop] = cloudpickle.load(open('./pkl_hists/SM_DTM_z'+str(loop)+'.pkl','rb'))
    except IOError:
        bin_centres,median,per_50,per_16,per_84,per_25,per_75,normalize = bin_data('SM','DTM',ax,normalize,loop,'SM_DTM',nbins=30)


    ax[loop].set_xlim([8.,11.98])
    ax[loop].set_ylim([-3.98,2])
    
    plot_params(ax[loop],loop,'SM','DTM')
    
    plot_observations(ax[loop],loop,"DTM_SM")
    #ax[loop].errorbar(x_bins,y_median,yerr=(y_mederr),color='k',label='L-Galaxies Median',linewidth=2)
    
    ax[loop].plot(bin_centres,per_50,c='k',zorder=10,linewidth=2,label='L-Galaxies')
    ax[loop].plot(bin_centres,per_16,'k--',zorder=10,linewidth=2)
    ax[loop].plot(bin_centres,per_84,'k--',zorder=10,linewidth=2)
    
    
axes = fig.get_axes()
for ax in axes:
    [i.set_linewidth(2.1) for i in ax.spines.values()]

pylab.savefig('./figs/DTM_stellar.png', bbox_inches=0)
plt.close()
    




plt.show()

