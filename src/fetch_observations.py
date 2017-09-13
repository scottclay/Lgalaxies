def fetch_observations():
	import numpy as np
	import pandas as pd

	#-------------Path to observational datasets
	observation_path = '../observational_data/'

	#-------------Remy-Ruyer 2014 z=0
	RR_2014 = pd.read_table(observation_path+'Remy_Ruyer_2014_KINGFISH_z0.txt',sep='\t',comment='#',names=['DM', 'DM_err', 'SM', 'HI', 'HI_err', 'Metals', 'H2_mw', 'H2_z'])
	RR_2014['DM_err_actual'] = RR_2014['DM']*(RR_2014['DM_err']/100.0)
	RR_2014['DTG'] = RR_2014['DM'] / (RR_2014['HI'] + RR_2014['H2_mw'])
	RR_2014['DTM'] = RR_2014['DM'] / (((10**(RR_2014['Metals'] - 8.69))*0.0134)*(RR_2014['HI'] + RR_2014['H2_mw']))

	#-------------RR2015 z=0
	RR_2015 = pd.read_table(observation_path+'RR2015.txt',sep='\t',comment='#',index_col=False,names=['SM','SM_err','DM_1','DM_1_up','DM_1_down','DM_2', 'DM_2_up', 'DM_2_down', 'HI', 'HI_err', 'Oxygen', 'H2_mw','H2_z'])

	RR_2015['DTG_1A'] = RR_2015['DM_1'] - np.log10(RR_2015['HI'] + RR_2015['H2_z'])
	RR_2015['DTG_1B'] = RR_2015['DM_1'] - np.log10(RR_2015['HI'] + RR_2015['H2_mw'])
	RR_2015['DTG_2A'] = RR_2015['DM_2'] - np.log10(RR_2015['HI'] + RR_2015['H2_z'])
	RR_2015['DTG_2B'] = RR_2015['DM_2'] - np.log10(RR_2015['HI'] + RR_2015['H2_mw'])

	RR_2015['DTM_1A'] = RR_2015['DM_1'] - np.log10((10**(RR_2015['Oxygen'] - 8.69 - 1.87289520164))*(RR_2015['HI'] + RR_2015['H2_z']))
	RR_2015['DTM_1B'] = RR_2015['DM_1'] - np.log10((10**(RR_2015['Oxygen'] - 8.69 - 1.87289520164))*(RR_2015['HI'] + RR_2015['H2_mw']))
	RR_2015['DTM_2A'] = RR_2015['DM_2'] - np.log10((10**(RR_2015['Oxygen'] - 8.69 - 1.87289520164))*(RR_2015['HI'] + RR_2015['H2_z']))
	RR_2015['DTM_2B'] = RR_2015['DM_2'] - np.log10((10**(RR_2015['Oxygen'] - 8.69 - 1.87289520164))*(RR_2015['HI'] + RR_2015['H2_mw']))

	#-------------Santini 2014 z=0,1,2
	Santini_2014_z0 = pd.read_table(observation_path+'Santini_2014_z0.txt',sep='\t',comment='#',index_col=False,names=['SM_z0', 'DM_z0', 'DM_up_err_z0', 'DM_down_err_z0'])
	Santini_2014_z1 = pd.read_table(observation_path+'Santini_2014_z1.txt',sep='\t',comment='#',index_col=False,names=['SM_z1', 'DM_z1', 'DM_up_err_z1', 'DM_down_err_z1'])
	Santini_2014_z2 = pd.read_table(observation_path+'Santini_2014_z2.txt',sep='\t',comment='#',index_col=False,names=['SM_z2', 'DM_z2', 'DM_up_err_z2', 'DM_down_err_z2'])

	Santini_2014 = pd.concat((Santini_2014_z0,Santini_2014_z1,Santini_2014_z2),axis=1)

	#-------------daCunha 2015
	daCunha_z2 = pd.read_table(observation_path+'daCunha_2015_z_2.txt',sep='\t',comment='#',index_col=False,names=['z_z2','z_up_err_z2','z_down_err_z2','SM_z2','SM_up_err_z2','SM_down_err_z2','DM_z2','DM_up_err_z2','DM_down_err_z2'])
	daCunha_z3 = pd.read_table(observation_path+'daCunha_2015_z_3.txt',sep='\t',comment='#',index_col=False,names=['z_z3','z_up_err_z3','z_down_err_z3','SM_z3','SM_up_err_z3','SM_down_err_z3','DM_z3','DM_up_err_z3','DM_down_err_z3'])
	daCunha_z4 = pd.read_table(observation_path+'daCunha_2015_z_4.txt',sep='\t',comment='#',index_col=False,names=['z_z4','z_up_err_z4','z_down_err_z4','SM_z4','SM_up_err_z4','SM_down_err_z4','DM_z4','DM_up_err_z4','DM_down_err_z4'])
	daCunha_z5 = pd.read_table(observation_path+'daCunha_2015_z_5.txt',sep='\t',comment='#',index_col=False,names=['z_z5','z_up_err_z5','z_down_err_z5','SM_z5','SM_up_err_z5','SM_down_err_z5','DM_z5','DM_up_err_z5','DM_down_err_z5'])
	daCunha_z6 = pd.read_table(observation_path+'daCunha_2015_z_6.txt',sep='\t',comment='#',index_col=False,names=['z_z6','z_up_err_z6','z_down_err_z6','SM_z6','SM_up_err_z6','SM_down_err_z6','DM_z6','DM_up_err_z6','DM_down_err_z6'])

	daCunha_2015 = pd.concat((daCunha_z2,daCunha_z3,daCunha_z4,daCunha_z5,daCunha_z6),axis=1)

	#-------------Mancini2015
	Mancini_2015 = pd.read_table(observation_path+'Mancini_2015_z6_z7.txt',sep='\t',comment='#',index_col=False,names=['z', 'SM', 'SM_err', 'DM', 'DM_err'])

	#-------------Bourne2012
	Bourne_2012 = pd.read_table(observation_path+'Bourne2012_z0.txt',sep='\t',comment='#',index_col=False,names=['MEDZ','MEDM','MEDC','MLIMITS_DOWN','MLIMITS_UP','MEDMSTAR','MEDMSTARERR','MEDMDUST','MEDMDUSTERR','MEDDMS','MEDDMSERR','NBIN'])

	#-------------Ciesla2014
	Ciesla_2014 = pd.read_table(observation_path+'Ciesla_2014_z0.txt',sep='\t',comment='#',index_col=False,names=['ID1','DM','DM_err','ID2','SM'])

	#-------------Wiseman2016
	Wiseman_z2 = pd.read_table(observation_path+'wiseman2016_z2.txt',sep='\t',comment='#',index_col=False,names=['z_z2','SM_z2','SM_uperr_z2','SM_downerr_z2','SFR_z2','SFR_err_z2','Metals_z2','Metals_err_z2','DTM_z2','DTM_err_z2'])
	Wiseman_z3 = pd.read_table(observation_path+'wiseman2016_z3.txt',sep='\t',comment='#',index_col=False,names=['z_z3','SM_z3','SM_uperr_z3','SM_downerr_z3','SFR_z3','SFR_err_z3','Metals_z3','Metals_err_z3','DTM_z3','DTM_err_z3'])
	Wiseman_z4 = pd.read_table(observation_path+'wiseman2016_z4.txt',sep='\t',comment='#',index_col=False,names=['z_z4','SM_z4','SM_uperr_z4','SM_downerr_z4','SFR_z4','SFR_err_z4','Metals_z4','Metals_err_z4','DTM_z4','DTM_err_z4'])

	Wiseman_2017 = pd.concat((Wiseman_z2,Wiseman_z3,Wiseman_z4),axis=1)
	
	#-------------Return 
	return RR_2014, RR_2015, Santini_2014, daCunha_2015, Mancini_2015, Bourne_2012, Ciesla_2014, Wiseman_2017


