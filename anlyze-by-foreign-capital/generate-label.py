# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 21:35:12 2021

@author: TonyT
"""
import pandas as pd
import csv

TAIEX_path = './data/TAIEX.csv'

with open(TAIEX_path, 'r') as f:
    df = pd.read_csv(f, index_col='Date')

open_points = df['Open']
close_points = df['Close']
    

f = open('./data/label.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(['Date', 'DiffBtwOpen'])
for i in range(1, open_points.shape[0]):
    diff = round(open_points.values[i] - open_points.values[i-1], 2)
    print("date: {}, open: {}, diff: {}"
          .format(open_points.index[i], open_points.values[i], diff))
    # input()
    writer.writerow([open_points.index[i], diff])

f.close()

print('==============================')

f = open('./data/label-2.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(['Date', 'DiffOpenClose'])
for i in range(1, open_points.shape[0]):
    diff = round(open_points.values[i] - close_points.values[i-1], 2)
    print("date: {}, open: {}, close: {}, diff: {}"
          .format(open_points.index[i], open_points.values[i], close_points.values[i] ,diff))
    # input()
    writer.writerow([open_points.index[i], diff])

f.close()
