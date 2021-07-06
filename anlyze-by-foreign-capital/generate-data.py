# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5  2021

@author: TonyT
"""
import pandas as pd
import csv

FFund_path = './data/Foreign-Fund.csv'
TAIEX_path = './data/TAIEX.csv'
label_path = './data/label-2.csv'

with open(label_path, 'r') as f:
    df_label = pd.read_csv(f, index_col='Date')


with open(TAIEX_path, 'r') as f:
    df_TAIEX = pd.read_csv(f, index_col='Date')
    

with open(FFund_path, 'r') as f:
    df_FFund = pd.read_csv(f, index_col='Date')

diff = df_FFund['Difference']
    

f = open('./data/data.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(['Date', 'LastFFundDiff', 'LastFFundBuy', 'LastFFundSell', 'LastOpen', 'LastHigh', 'LastLow', 'LastClose', 'LastDiffOpenClose'])
for i in range(1, diff.shape[0]-1):
    tg_date = diff.index[i+1]
    print("date: {}, LastFFundDiff: {}, LastFFundBuy: {}, LastFFundSell: {}, LastOpen: {}, LastHigh: {}, LastLow: {}, LstClose:{}, LastDiffOpenClose: {}"
          .format(tg_date, diff.values[i], df_FFund['Buy'].values[i], df_FFund['Sell'].values[i],
                  df_TAIEX['Open'].values[i], df_TAIEX['High'].values[i], df_TAIEX['Low'].values[i],
                  df_TAIEX['Close'].values[i], df_label['DiffOpenClose'].values[i-1]))
    # input()
    writer.writerow([tg_date, diff.values[i], df_FFund['Buy'].values[i],
                     df_FFund['Sell'].values[i], df_TAIEX['Open'].values[i],
                     df_TAIEX['High'].values[i], df_TAIEX['Low'].values[i],
                     df_TAIEX['Close'].values[i]])

f.close()

print('==============================')


