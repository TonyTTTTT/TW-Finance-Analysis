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
from RandomHeaderGenerator import getHeader

url = 'https://www.twse.com.tw/fund/BFI82U?response=csv&type=day&dayDate='


dir_path = './TW-Finance-Analysis/anlyze-by-foreign-capital/data'
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
# newline='' to avoid the redundant row
f = open('./TW-Finance-Analysis/anlyze-by-foreign-capital/data/Foreign-Fund.csv', 'a', newline='')
writer = csv.writer(f)

base = datetime.datetime.today()

date = str(base.date())
date = date.replace('-','')
print(date)
tmp_url = url + date
print(tmp_url)


try:
    headers = getHeader()
    res = requests.get(url=tmp_url, headers=headers)
    content = res.content.decode('big5')
    content = content.split('\r\n')
    # target:list
    target = content[5]
    print(target)
    target = target.split('"')
    target_buy = int(target[3].replace(',',''))
    target_sell = int(target[5].replace(',',''))
    target_delta = int(target[7].replace(',',''))
    writer.writerow([date, target_buy, target_sell, target_delta])
except:
    print(date, " not trading or data not available!")

print('============================')
    
f.close()