# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 18:30:03 2021

@author: Tony Tsou
"""
import pandas as pd
import csv

FFund_path = './data/Foreign-Fund.csv'
with open(FFund_path, 'r') as f:
    df_FFund = pd.read_csv(f, index_col='Date')
    
f = open('./data/data-new.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(['Date', '1thFFundDiff', '2thFFundDiff', '3thFFundDiff', '4thFFundDiff', '5thFFundDiff', '6thFFundDiff', '7thFFundDiff'])
diff = df_FFund['Difference']
for i in range(6, diff.shape[0]-1):
    tg_date = diff.index[i]
    print('date: {}, 1thFFundDiff: {}, 2thFFundDiff: {}, 3thFFundDiff: {}, 4thFFundDiff: {}, 5thFFundDiff: {}, 6thFFundDiff: {}, 7thFFundDiff: {}'
          .format(tg_date, diff.values[i-6], diff.values[i-5], diff.values[i-4], diff.values[i-3], diff.values[i-2], diff.values[i-1], diff.values[i]))
    
    writer.writerow([tg_date, diff.values[i-6], diff.values[i-5], diff.values[i-4], diff.values[i-3], diff.values[i-2], diff.values[i-1], diff.values[i]])
    
f.close()