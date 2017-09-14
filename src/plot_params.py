import matplotlib.pyplot as plt
def plot_params(redshift):
	if(redshift==1 or redshift==2 or redshift==4 or redshift==5):
		plt.tick_params(axis='both', which='major', labelsize=12,width=2,length=6, labelleft ='off', labelbottom='off', direction='inout')
		plt.tick_params(axis='both', which='minor', labelsize=12,width=2,length=6, labelleft ='off', labelbottom='off', direction='inout')

	if(redshift==0 or redshift==3):
		plt.tick_params(axis='both', which='major', labelsize=12,width=2,length=6, labelleft ='on', labelbottom='off', direction='inout')
		plt.tick_params(axis='both', which='minor', labelsize=12,width=2,length=6, labelleft ='on', labelbottom='off', direction='inout')

	if(redshift==7 or redshift==8):
		plt.tick_params(axis='both', which='major', labelsize=12,width=2,length=6, labelleft ='off', labelbottom='on', direction='inout')
		plt.tick_params(axis='both', which='minor', labelsize=12,width=2,length=6, labelleft ='off', labelbottom='on', direction='inout')
	
	if(redshift==6):
		plt.tick_params(axis='both', which='major', labelsize=12,width=2,length=6, labelleft ='on', labelbottom='on', direction='inout')
		plt.tick_params(axis='both', which='minor', labelsize=12,width=2,length=6, labelleft ='on', labelbottom='on', direction='inout')
	
	if(redshift==8):
		plt.xlim([6,12.0])
		
	if redshift==7:
		plt.xlabel(r'log$_{10}$(M$_{*}$/M$_{\odot}$)', fontsize=18)
	if redshift==3:
		plt.ylabel(r'log$_{10}$(M$_{\rm{d}}$/M$_{\odot}$)', fontsize=18)
	return