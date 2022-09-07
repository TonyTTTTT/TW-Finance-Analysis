# -*- coding: utf-8 -*-
"""
Created on Mon May 24 12:42:41 2021

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

delay_choices = [8, 5, 10, 6, 13, 7, 11, 4, 9 ]
dir_path = './data'
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
# newline='' to avoid the redundant row
f = open('./data/Foreign-Fund.csv', 'a', newline='')
writer = csv.writer(f)

# the data needed from now to numdays days ago
numdays = 5
base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(numdays,0,-1)]
for i in date_list:
    date = str(i.date())
    date = date.replace('-','')
    print(date)
    tmp_url = url + date
#    print(tmp_url)


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
    delay = random.choice(delay_choices)
    print("delay {} sec.".format(delay))
    print('============================')
    time.sleep(delay)
    
f.close()