import matplotlib.pyplot as plt
def plot_params(redshift, x_axis = 'SM', y_axis = 'DM'):
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
	
	#if(redshift==8):
	#	plt.xlim([8,12.0])
		
	if redshift==7:
		if x_axis == "SM":
			plt.xlabel(r'log$_{10}$(M$_{*}$/M$_{\odot}$)', fontsize=18)
		if x_axis == "O":
			plt.xlabel(r'12 + log$_{10}$(O/H)', fontsize=18)
	if redshift==3:
		if y_axis == "DM":
			plt.ylabel(r'log$_{10}$(M$_{\rm{D}}$/M$_{\odot}$)', fontsize=18)
		if y_axis == "DTG":
			plt.ylabel(r'log$_{10}$(M$_{\rm{D}}$/M$_{\rm{CG}}$)', fontsize=18)
		if y_axis == "DTM":
			plt.ylabel(r'log$_{10}$(M$_{\rm{D}}$/M$_{\rm{M}}$)', fontsize=18)
		if y_axis == "O":
			plt.ylabel(r'12 + log$_{10}$(O/H)', fontsize=18)
		if y_axis == "CG":
			plt.ylabel(r'log$_{10}$(M$_{\rm{CG}}$/M$_{\odot}$)', fontsize=18)
		if y_axis == "DRate":
			plt.ylabel(r'Dust production rate M$_{\odot}$yr$^{-1}$', fontsize=18)			
	return