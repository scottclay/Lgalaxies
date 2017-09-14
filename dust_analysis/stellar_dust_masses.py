import numpy as np
import matplotlib.pyplot as plt
import pylab
import sys

sys.path.append('../data/')
sys.path.append('../src/')

from fetch_observations import plot_observations
from fit_scatter import fit_scatter
from read_pickled_data import produce_df
from plot_params import plot_params

col_maps=['afmhot','autumn','bone','cool','copper','gist_heat','gray','spring','winter']

#for map in col_maps:
fig, axs = plt.subplots(nrows=3, ncols=3, sharex=True, sharey=True, figsize=(9,9))
fig.subplots_adjust(hspace=0)
fig.subplots_adjust(wspace=0)

for loop in range(0,9):
#for loop in range(0,1):


	df = produce_df(redshift=loop, data_path = '../prepare_output/')
	plt.subplot(3,3,loop+1)
	plt.xlim([8,11.97])
	plt.ylim([0,9.98])
	
	plot_params(loop)

	#df2 = df[(df != 0).all(1)]


	DM = np.log10(df[df['Dust_Mass']>0.0]['Dust_Mass'])
	SM = np.log10(df[df['Dust_Mass']>0.0]['StellarMass'])




	x_bins,y_bins,y_std_dev,y_std_err,count,y_median, y_mederr = fit_scatter(SM, DM, ret_n=True, ret_sterr=True, ret_median=True, nbins=10)


	#plt.scatter(log_SM,log_DM)
	#

	#print(SM.describe())
	#print(DM.describe())
	#from scipy.stats import gaussian_kde

	plt.hexbin(SM,DM,gridsize=150,bins='log',mincnt=5,cmap='gist_heat')

	plot_observations(loop)
	plt.errorbar(x_bins,y_median,yerr=(y_mederr),color='k',label='L-Galaxies Median',linewidth=2)
	#print("end")

plt.show()



#         
#     #Stellar_Mass_Condition = 1.0E9
#     Stellar_Mass_Condition = 0.0
#     Dust_Mass_Condition = 0.0 
#     Hubble_time = 28.0/3*(1+(1+loop)**2)*1.0E9 #years
#     sSFR_cut = 1 / (3 * Hubble_time)
#     condition = np.logical_and(sSFR > sSFR_cut, np.logical_and(Dust_Mass > 0, Type == 0))
#     
#     log_Stellar_Mass = np.log10(Stellar_Mass[condition==1])
#     log_Dust_Mass = np.log10(Dust_Mass[condition==1])
#     
#     
#     SM_bins,Dust_bins,Dust_std_dev,Dust_std_err,count,Dust_median,Dust_mederr = fit_scatter(log_Stellar_Mass, log_Dust_Mass, ret_n=True, ret_sterr=True,ret_median=True, nbins=20)
#     #np.savetxt('./binned/stellar_dust_mass_'+str(loop)+'_BOTH.txt',np.c_[SM_bins,Dust_median,Dust_mederr,count])
# 
#     if(sum(count)>0):  
      
#        if loop==0:
            #fig = plt.figure(figsize=(9,9))

      
        #plt.tick_params(axis='both', which='major', labelsize=12,width=2)
        #plt.tick_params(axis='both', which='minor', labelsize=12,width=2)
#        plt.text(10,2.5,"z = "+str(loop), fontsize = 16)
        #plt.text(9,1,"z = "+str(loop)+"\nN = "+str(sum(count)),fontsize=16)
        
        
        #plt.errorbar(SM_bins,Dust_bins,yerr=(Dust_std_err),color='k',label='L-Galaxies Mean',linewidth=2)
#        plt.errorbar(SM_bins,Dust_median,yerr=(Dust_mederr),color='k',linewidth=2,zorder=10)
#        print SM_bins, Dust_median
        
#        plt.legend(loc='lower right')
       # if loop==8:
       #     plt.legend(loc='lower right')
        
# 
# axes = fig.get_axes()
# for ax in axes:
#     [i.set_linewidth(2.1) for i in ax.spines.itervalues()]
# 
# 
# pylab.savefig('./stellar_dust_mass_ALL.png', bbox_inches=0)
# plt.close()
#     
# 
# 
# 
# 
