import matplotlib.pyplot as plt
def plot_params(ax, redshift, x_axis = 'none', y_axis = 'none'):
	if(redshift==1 or redshift==2 or redshift==4 or redshift==5):
		ax.tick_params(axis='both', which='major', labelsize=12,width=2,length=6, labelleft ='off', labelbottom='off', direction='inout')
		ax.tick_params(axis='both', which='minor', labelsize=12,width=2,length=6, labelleft ='off', labelbottom='off', direction='inout')

	if(redshift==0 or redshift==3):
		ax.tick_params(axis='both', which='major', labelsize=12,width=2,length=6, labelleft ='on', labelbottom='off', direction='inout')
		ax.tick_params(axis='both', which='minor', labelsize=12,width=2,length=6, labelleft ='on', labelbottom='off', direction='inout')

	if(redshift==7 or redshift==8):
		ax.tick_params(axis='both', which='major', labelsize=12,width=2,length=6, labelleft ='off', labelbottom='on', direction='inout')
		ax.tick_params(axis='both', which='minor', labelsize=12,width=2,length=6, labelleft ='off', labelbottom='on', direction='inout')
	
	if(redshift==6):
		ax.tick_params(axis='both', which='major', labelsize=12,width=2,length=6, labelleft ='on', labelbottom='on', direction='inout')
		ax.tick_params(axis='both', which='minor', labelsize=12,width=2,length=6, labelleft ='on', labelbottom='on', direction='inout')
	
	#if(redshift==8):
	#	ax.xlim([8,12.0])
		
	if redshift==7:
		if x_axis == "SM":
			ax.set_xlabel(r'log$_{10}$(M$_{*}$/M$_{\odot}$)', fontsize=18)
		if x_axis == "O":
			ax.set_xlabel(r'12 + log$_{10}$(O/H)', fontsize=18)
	if redshift==3:
		if y_axis == "DM":
			ax.set_ylabel(r'log$_{10}$(M$_{\rm{D}}$/M$_{\odot}$)', fontsize=18)
		if y_axis == "DTG":
			ax.set_ylabel(r'log$_{10}$(M$_{\rm{D}}$/M$_{\rm{CG}}$)', fontsize=18)
		if y_axis == "DTM":
			ax.set_ylabel(r'log$_{10}$(M$_{\rm{D}}$/M$_{\rm{M}}$)', fontsize=18)
		if y_axis == "O":
			ax.set_ylabel(r'12 + log$_{10}$(O/H)', fontsize=18)
		if y_axis == "CG":
			ax.set_ylabel(r'log$_{10}$(M$_{\rm{CG}}$/M$_{\odot}$)', fontsize=18)
		if y_axis == "DRate":
			ax.set_ylabel(r'Dust production rate M$_{\odot}$yr$^{-1}$', fontsize=18)			
	return