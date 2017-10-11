#!/usr/bin/python
# encoding=utf8

import pickle as cPickle
import numpy as np
import pandas as pd

def read_pickled_data(redshift=0, data_path = '/lustre/scratch/astro/sc558/Clay17_Sept/MR/Pickled/'):

    file_N0 = open(data_path +'lgal_z'+str(redshift)+'_N0.pkl','rb')
    gals_N0 = cPickle.load(file_N0)
    file_N0.close()

    file_N1 = open(data_path +'lgal_z'+str(redshift)+'_N1.pkl','rb')
    gals_N1 = cPickle.load(file_N1)
    file_N1.close()

    file_N2 = open(data_path +'lgal_z'+str(redshift)+'_N2.pkl','rb')
    gals_N2 = cPickle.load(file_N2)
    file_N2.close()

    file_N3 = open(data_path +'lgal_z'+str(redshift)+'_N3.pkl','rb')
    gals_N3 = cPickle.load(file_N3)
    file_N3.close()

    file_N4 = open(data_path +'lgal_z'+str(redshift)+'_N4.pkl','rb')
    gals_N4 = cPickle.load(file_N4)
    file_N4.close()

    gals = np.hstack((gals_N0, gals_N1, gals_N2, gals_N3, gals_N4))
    
    return gals


def produce_df(redshift=0, data_path = '/lustre/scratch/astro/sc558/Clay17_Sept/MR/Pickled/'):
        
    gals = read_pickled_data(redshift, data_path)

    df = pd.DataFrame()

    df['Type'] = gals['Type']
    df['ColdGas'] = gals['ColdGas']*1.0E10/0.673
    df['StellarMass'] = gals['StellarMass']*1.0E10/0.673
    df['Sfr'] = gals['Sfr']

    df['Dust_Mass'] = np.sum(gals['Dust_elements'], axis=1)
    df['Metal_Mass'] = np.sum(gals['ColdGas_elements'][:,2:11], axis=1)

    df['DustRate_AGB']  = gals['DustRatesISM'][:,0]
    df['DustRate_SNII'] = gals['DustRatesISM'][:,1]
    df['DustRate_SNIA'] = gals['DustRatesISM'][:,2]
    df['DustRate_GROW'] = gals['DustRatesISM'][:,3]
    df['DustRate_DEST'] = gals['DustRatesISM'][:,4]
    
    df['H']  = gals['ColdGas_elements'][:,0]
    df['He'] = gals['ColdGas_elements'][:,1]
    df['Cb'] = gals['ColdGas_elements'][:,2]
    df['N']  = gals['ColdGas_elements'][:,3]
    df['O']  = gals['ColdGas_elements'][:,4]
    df['Ne'] = gals['ColdGas_elements'][:,5]
    df['Mg'] = gals['ColdGas_elements'][:,6]
    df['Si'] = gals['ColdGas_elements'][:,7]
    df['S']  = gals['ColdGas_elements'][:,8]
    df['Ca'] = gals['ColdGas_elements'][:,9]
    df['Fe'] = gals['ColdGas_elements'][:,10]

    df['H_Dust']  = gals['Dust_elements'][:,0]
    df['He_Dust'] = gals['Dust_elements'][:,1]
    df['Cb_Dust'] = gals['Dust_elements'][:,2]
    df['N_Dust']  = gals['Dust_elements'][:,3]
    df['O_Dust']  = gals['Dust_elements'][:,4]
    df['Ne_Dust'] = gals['Dust_elements'][:,5]
    df['Mg_Dust'] = gals['Dust_elements'][:,6]
    df['Si_Dust'] = gals['Dust_elements'][:,7]
    df['S_Dust']  = gals['Dust_elements'][:,8]
    df['Ca_Dust'] = gals['Dust_elements'][:,9]
    df['Fe_Dust'] = gals['Dust_elements'][:,10]
    
    df['SM'] = np.log10(df['StellarMass'])
    df['DM'] = np.log10(df['Dust_Mass'])
    df['MM'] = np.log10(df['Metal_Mass'])
    df['CG'] = np.log10(df['ColdGas'])
    df['OX_Z'] = np.log10((df['O']/df['H']) * (1.0/16.0)) + 12.0
    df['DTG'] = df['DM'] - df['CG']   
    df['DTM'] = df['DM'] - df['MM']   
    
    return df

def fetch_lgalaxies(redshift = 0, data_path = '/lustre/scratch/astro/sc558/Clay17_Sept',simulation='MR'):
    
    if simulation=='MR':
        df   = produce_df(redshift=redshift, data_path = data_path + '/MR/Pickled/')
    elif simulation == 'MRII':
        df = produce_df(redshift=redshift, data_path = data_path + '/MRII/Pickled/')
    elif simulation =='both':
        df_MR   = produce_df(redshift=redshift, data_path = data_path + '/MR/Pickled/')
        df_MRII = produce_df(redshift=redshift, data_path = data_path + '/MRII/Pickled/')
        df = pd.concat([df_MR,df_MRII], axis=0)

    return df
    
def make_selection(df,redshift=0):
    sSFR = df['Sfr'] / df['StellarMass']
    Hubble_time = 28.0/3*(1+(1+redshift)**2)*1.0E9 #years
    sSFR_cut = 1 / (3 * Hubble_time)
    
    df_cut = df[( (df['Type']==0) & (sSFR > sSFR_cut) & (df['Dust_Mass']>0.0) )]
    #df_cut = df[df['Dust_Mass']>0.0]
    return df_cut
    
    
        
#df = fetch_lgalaxies(redshift=5, data_path = '../prepare_output/',simulation = 'both')
#print(df.shape)
#df = make_selection(df,redshift=5)

#print(df.shape)
#X_zero = X.loc[y['Class'] ==0]
#X_one  = X.loc[y['Class'] ==1]


#df = fetch_lgalaxies(redshift = 0, data_path = '../prepare_output/',simulation='MR')
#print(df['O'].min())
#print(df['O_Dust'].min())
#print( (df['O'] + df['O_Dust']).min())





















