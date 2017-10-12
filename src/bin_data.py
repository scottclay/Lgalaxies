import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pylab
import sys
import numpy as np
import cloudpickle


from fetch_observations import plot_observations
from fit_scatter import fit_scatter
from read_pickled_data import produce_df
from read_pickled_data import fetch_lgalaxies
from read_pickled_data import make_selection
from plot_params import plot_params
from fit_scatter import fit_median


def bin_data(var1,var2,ax,normalize,redshift,filename,nbins=10):
    df = fetch_lgalaxies(redshift=redshift, data_path = '../prepare_output/',simulation='MR')
    #df = fetch_lgalaxies(redshift=redshift,simulation='MR')
    df = make_selection(df,redshift=redshift)

    x = df[var1]
    y = df[var2]
    
    x = x.as_matrix()
    y = y.as_matrix()

    median, bin_centres, per_50, per_16, per_84, per_25, per_75 = fit_median(x,y,nbins)
    np.savetxt('./binned_data/'+filename+'_z'+str(redshift)+'.txt',np.c_[bin_centres,median,per_50,per_16,per_84,per_25,per_75])
    
    if redshift == 0: 
        hb = ax[redshift].hexbin(x,y,gridsize=150,bins='log',mincnt=5,cmap='gist_gray')
        min = hb.norm.vmin
        max = hb.norm.vmax
        #normalize = matplotlib.colors.Normalize(vmin=min, vmax=max)
        #print (normalize)
    else:
        ax[redshift].hexbin(x,y,gridsize=150,bins='log',mincnt=5,cmap='gist_gray')#,norm=normalize)

    import pickle   
    fout = open('./pkl_hists/'+filename+'_z'+str(redshift)+'.pkl','wb')
    cloudpickle.dump(ax[redshift],fout)
    
    return bin_centres,median,per_50,per_16,per_84,per_25,per_75,normalize


def bin_highz_data(var1,var2,redshift,filename,nbins=10):
    df = fetch_lgalaxies(redshift=redshift, data_path = '../prepare_output/',simulation='MR')
    #df = fetch_lgalaxies(redshift=redshift,simulation='MR')
    df = make_selection(df,redshift=redshift)

    x = df[var1]
    y = df[var2]
    
    x = x.as_matrix()
    y = y.as_matrix()

    median, bin_centres, per_50, per_16, per_84, per_25, per_75 = fit_median(x,y,nbins)
    np.savetxt('./binned_data/'+filename+'_z'+str(redshift)+'.txt',np.c_[bin_centres,median,per_50,per_16,per_84,per_25,per_75])

    return bin_centres,median,per_50,per_16,per_84,per_25,per_75
