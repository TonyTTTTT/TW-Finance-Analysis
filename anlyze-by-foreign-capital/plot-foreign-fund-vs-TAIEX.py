# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 12:08:35 2021

@author: user
"""
import pandas as pd
import matplotlib.pyplot as plt

TAIEX_path = './data/TAIEX.csv'
foreign_fund_path = './data/Foreign-Fund.csv'


with open(foreign_fund_path, 'r') as f:
    df_fund = pd.read_csv(f, index_col='Date')
    
with open(TAIEX_path, 'r') as f:
    df_TAIEX = pd.read_csv(f, index_col='Date')


parameters = {'axes.labelsize':8, 'axes.titlesize':16,
              'xtick.labelsize':7, 'ytick.labelsize':7}

plt.rcParams.update(parameters)
fig = plt.figure()
plt.plot(df_TAIEX['Open'].index.values[-5:].astype('str'), df_TAIEX['Open'].values[-5:],
         df_fund['Difference'].index.values[-5:].astype('str'), df_fund['Difference'].values[-5:],
         marker='o')
plt.title('TAIEX')
plt.xlabel('Date')
plt.ylabel('point')




        