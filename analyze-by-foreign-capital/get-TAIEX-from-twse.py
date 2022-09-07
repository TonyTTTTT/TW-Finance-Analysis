# -*- coding: utf-8 -*-
"""
Created on Thur 0701 11:13 2021

@author: TonyT
"""
import requests
import time
import csv
import os
import datetime
import random
from RandomHeaderGenerator import getHeader

url = 'https://www.twse.com.tw/indicesReport/MI_5MINS_HIST?response=csv&date='

delay_choices = [8, 5, 10, 6, 13, 7, 11, 4, 9 ]
dir_path = './data'
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
# newline='' to avoid the redundant row
f = open('./data/TAIEX-tmp.csv', 'a', newline='')
writer = csv.writer(f)

# the data needed from now to numdays days ago
numdays = 240
base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(numdays,-1,-30)]
for i in date_list:
    tmp_date = str(i.date())
    tmp_date = tmp_date.replace('-','')
    print(tmp_date)
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
        # print(target)
        for day_info in target:
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
            print(day_info_write)

            writer.writerow(day_info_write)
    except:
        print(tmp_date, " not trading or data not available!")
    delay = random.choice(delay_choices)
    print("delay {} sec.".format(delay))
    print('============================')
    time.sleep(delay)
    
f.close()