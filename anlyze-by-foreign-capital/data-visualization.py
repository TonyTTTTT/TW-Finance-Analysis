# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 20:17:30 2021

@author: user
"""
import pandas as pd
import matplotlib.pyplot as plt

data_path = './data/data.csv'
label_path = './data/label-2.csv'

with open(data_path, 'r') as f:
    df_data = pd.read_csv(f,  index_col='Date')

with open(label_path, 'r') as f:
    df_label = pd.read_csv(f,  index_col='Date')
    

parameters = {'axes.labelsize':8, 'axes.titlesize':16,
              'xtick.labelsize':7, 'ytick.labelsize':7}

plt.rcParams.update(parameters)
fig = plt.figure()
plt.scatter(df_data.values, df_label.values, s=5)
plt.title('data distribution')
plt.xlabel('LastFFundDiff')
plt.ylabel('DiffOpenClose')