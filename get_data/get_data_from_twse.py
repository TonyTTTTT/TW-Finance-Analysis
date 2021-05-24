# -*- coding: utf-8 -*-
"""
Created on Mon May 24 12:42:41 2021

@author: user
"""
import requests
import json
import time

url = 'https://www.twse.com.tw/fund/BFI82U?response=json&type=day&dayDate='
#data = {'response': 'json', 'dayDate': None}
#data['dayDate'] = '20210521'
#res = requests.get(url)
#content = res.content.decode('utf8')
#content = json.loads(content)
##print(content)
#print(content['data'])
##target:list
#target = content['data'][3]
#target_buy = int(target[1].replace(',',''))
#target_sell = int(target[2].replace(',',''))
#target_delta = int(target[3].replace(',',''))

delta_ary = []
for i in range(1,32):
    if(i<10):
        date = '2021050'+str(i)
    else:
        date = '202105'+str(i)
    print(date)
    tmp_url = url + date
#    print(tmp_url)
    res = requests.get(tmp_url)
    content = res.content.decode('utf8')
    content = json.loads(content)
    #print(content)
    try:
        print(content['data'][3])
        #target:list
        target = content['data'][3]
        target_buy = int(target[1].replace(',',''))
        target_sell = int(target[2].replace(',',''))
        target_delta = int(target[3].replace(',',''))
    except:
        print(data, " not trading!")
    time.sleep(2)