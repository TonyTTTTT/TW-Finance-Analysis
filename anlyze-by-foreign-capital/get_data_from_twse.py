# -*- coding: utf-8 -*-
"""
Created on Mon May 24 12:42:41 2021

@author: TonyT
"""
import requests
import time
import csv
import os
from datetime import date
import datetime
from fake_useragent import UserAgent
import random

user_agent = UserAgent()
url = 'https://www.twse.com.tw/fund/BFI82U?response=csv&type=day&dayDate='
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Host": "www.twse.com.tw",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66"
    }
delay_choices = [8, 5, 10, 6, 13, 7, 11, 4, 9 ]
delta_ary = []
dir_path = './data'
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
# newline=='' to avoid the redundant row
f = open('./data/foreign_investment.csv', 'a', newline='')
writer = csv.writer(f)
numdays = 320
base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(numdays,0,-1)]
for i in date_list:
    date = str(i.date())
    date = date.replace('-','')
    print(date)
    tmp_url = url + date
#    print(tmp_url)


    try:
        headers["User-Agent"] = user_agent.random
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
    time.sleep(delay)
    
f.close()