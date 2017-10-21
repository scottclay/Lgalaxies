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


def bin_data2(var1,var2,redshift,filename,nbins=10, sim = 'MR'):
    df = fetch_lgalaxies(redshift=redshift, data_path = '../prepare_output/',simulation=sim)
    #df = fetch_lgalaxies(redshift=redshift,simulation='MR')
    df = make_selection(df,redshift=redshift)

    x = df[var1]
    y = df[var2]

    x = x.as_matrix()
    y = y.as_matrix()

    median, bin_centres, per_50, per_16, per_84, per_25, per_75 = fit_median(x,y,nbins)
    return bin_centres,median,per_50,per_16,per_84,per_25,per_75


def plot_SM_DM(redshift_low, redshift_high, filename):
	#fig, axs = plt.subplots(nrows=3, ncols=3, sharex=True, sharey=True, figsize=(9,9))
	#ax = axs.reshape(-1)
	plt.figure(figsize=(9,9))
	redshift = 0
	normalize=0

	df = fetch_lgalaxies(redshift=redshift, data_path = '../prepare_output/',simulation='MR')
	df = make_selection(df,redshift=redshift)
	x = df[df.SM > 9].SM
	y = df[df.SM > 9].DM

	df2 = fetch_lgalaxies(redshift=redshift, data_path = '../prepare_output/',simulation='MRII')
	df2 = make_selection(df2,redshift=redshift)
	x2 = df2['SM']
	y2 = df2['DM']

	bin_centres,median,per_50,per_16,per_84,per_25,per_75 = bin_data2('SM','DM',redshift,filename,nbins=30, sim='MR')
	bin_centres2,median2,per_502,per_162,per_842,per_252,per_752 = bin_data2('SM','DM',redshift,filename,nbins=30, sim='MRII')


	hb = plt.hexbin(x2,y2,gridsize=150,bins='log',mincnt=1,cmap='gist_gray')
	min = hb.norm.vmin
	max = hb.norm.vmax
	normalize = matplotlib.colors.Normalize(vmin=min, vmax=max)
	#ax[redshift].hexbin(x,y,gridsize=150,bins='log',mincnt=5,cmap='gist_gray')#,norm=normalize)
	
	print(min,max)
	
	#normalize  = matplotlib.colors.Normalize(vmin=0, vmax=4)
	plt.hexbin(x,y,gridsize=150,bins='log',mincnt=1,cmap='gist_gray',norm=normalize)	




	#plt.hexbin(x2,y2,gridsize=150,bins='log',mincnt=1,cmap='gist_gray')#,norm=normalize)	
	  
	plt.xlim([6,11.97])
	plt.ylim([0,9.98])
	
	#fig.text(8.2,0.3,"z = "+str(loop), fontsize = 16)
	
	#plot_params(ax[loop],loop,'SM','DM')
	#plot_observations(ax[loop],loop,"SM_DM")
	

	plt.plot(bin_centres,per_50,c='k',zorder=10,linewidth=2,label='L-Galaxies')
	plt.plot(bin_centres,per_16,'k--',zorder=10,linewidth=2)
	plt.plot(bin_centres,per_84,'k--',zorder=10,linewidth=2)
	
	plt.plot(bin_centres2,per_502,c='r',zorder=10,linewidth=2,label='L-Galaxies')
	plt.plot(bin_centres2,per_162,'r--',zorder=10,linewidth=2)
	plt.plot(bin_centres2,per_842,'r--',zorder=10,linewidth=2)
	
	
	
	#[i.set_linewidth(2.1) for i in ax[loop].spines.values()]

	pylab.savefig('./figs/'+filename+'.png', bbox_inches=0)

plot_SM_DM(0,9,'SM_DM')
