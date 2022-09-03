# -*- coding: utf-8 -*-
"""
Created on 2021/7/20

@author: TonyT
"""
import requests
import time
import csv
import os
import datetime
import random
import pandas as pd
from RandomHeaderGenerator import getHeader

url = 'https://www.twse.com.tw/indicesReport/MI_5MINS_HIST?response=csv&date='

dir_path = './data'
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# newline='' to avoid the redundant row
f = open('./data/TAIEX-diff.csv', 'r+', newline='')
df = pd.read_csv(f)
writer = csv.writer(f)

# the data needed from now to numdays days ago
numdays = 1
base = datetime.datetime.today()

# concate today's date into url
tmp_date = str(base.date())
tmp_date = tmp_date.replace('-','')
print(tmp_date)
tmp_date = '20220902'
tmp_url = url + tmp_date
print(tmp_url)


try:
    headers= getHeader()
    res = requests.get(url=tmp_url, headers=headers)
    content = res.content.decode('big5')
    content = content.split('\r\n')
    # print(content)
    # target:list
    target = content[2:-1]
    print(target[-1])
    day_info = target[-1]
    day_info_write = []
    day_info = day_info.replace(',', '')
    day_info = day_info.split('"')
    
    # convert ROC Era to AD
    day_info[1] = day_info[1].split('/')
    day_info[1][0] = str(int(day_info[1][0])+1911)
    day_info[1] = day_info[1][0] + day_info[1][1] + day_info[1][2]
    
    day_info_write.append(day_info[1])
    day_info_write.append(day_info[3])
    day_info_write.append(day_info[5])
    day_info_write.append(day_info[7])
    day_info_write.append(day_info[9])

    diff = round(float(day_info_write[1]) - df.iloc[-1]['Open'], 2)
    day_info_write.append(diff)

    print(day_info_write)
    
    writer.writerow(day_info_write)

except:
    print(tmp_date, " not trading or data not available!")
print('============================')

f.close()