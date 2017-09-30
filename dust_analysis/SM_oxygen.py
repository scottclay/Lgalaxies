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

fig, axs = plt.subplots(nrows=3, ncols=3, sharex=True, sharey=True, figsize=(9,9))
ax = axs.reshape(-1)
fig.subplots_adjust(hspace=0)
fig.subplots_adjust(wspace=0)

for loop in range(0,9):

	try: 
		bin_centres,median,per_50,per_16,per_84,per_25,per_75 = np.loadtxt('./binned_data/SM_oxygen_'+str(loop)+'.txt',unpack=True,comments='#')
	except IOError:
		print("Missing data - will create")
		#df = fetch_lgalaxies(redshift=loop, data_path = '../prepare_output/',simulation='MR')
		df = fetch_lgalaxies(redshift=loop,simulation='MR')
		df = make_selection(df,redshift=loop)
		SM = np.log10(df['StellarMass'])
		OX_M = df['O']
		Hyd = df['H']
        
		OX_Z = np.log10   (( (OX_M) /Hyd) * (1.0/16.0)) + 12.0
		
		OX_Z = OX_Z.as_matrix()

    
		from fit_scatter import fit_median
		median, bin_centres, per_50,per_16,per_84,per_25,per_75 = fit_median(SM,OX_Z,10)
		np.savetxt('./binned_data/SM_oxygen_'+str(loop)+'.txt',np.c_[bin_centres,median,per_50,per_16,per_84,per_25,per_75])
		try: 
			ax[loop] = cloudpickle.load(open('./pkl_hists/SM_oxygen_z'+str(loop)+'.pickle','rb'))
		except:
			print("generating hists")
			if loop == 0: 
				hb = plt.hexbin(SM,OX_Z,gridsize=150,bins='log',mincnt=5,cmap='gist_heat')
				min = hb.norm.vmin
				max = hb.norm.vmax
				normalize = matplotlib.colors.Normalize(vmin=min, vmax=max)
				print(min,max)
			else:
				plt.hexbin(SM,OX_Z,gridsize=150,bins='log',mincnt=5,cmap='gist_heat',norm=normalize)
			import pickle   
	
			fout = open('./pkl_hists/SM_oxygen_z'+str(loop)+'.pkl','wb')
			cloudpickle.dump(ax[loop],fout)

	plt.subplot(3,3,loop+1)
	plt.ylim([6.,9.98])
	plt.xlim([8,11.97])

	plot_params(loop,'SM','O')

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

	#plot_observations(loop,"DTG_Oxy")

	plt.plot(bin_centres,per_50,c='k',zorder=10,linewidth=2,label='L-Galaxies')
	plt.plot(bin_centres,per_16,'k--',zorder=10,linewidth=2)
	plt.plot(bin_centres,per_84,'k--',zorder=10,linewidth=2)


	if loop==8:
		plt.legend(loc='lower right',fontsize = 8)

axes = fig.get_axes()
for ax in axes:
    [i.set_linewidth(2.1) for i in ax.spines.values()]

pylab.savefig('./figs/SM_oxygen.png', bbox_inches=0)
plt.close()
    

