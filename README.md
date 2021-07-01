# TW_finance_analysis
This project aim to analysis&amp;predict the trend of Taiwan's finance

## 2021/5/24
- directly get data from the twse website, but been banned due to frequently requesting.
- Should download the file to local and read the csv file, instead of directly get the data from web url.
## 2021/5/25
- add the auto download data from twse function by file "get_data_from_twse.py"
## 2021/5/26
- coplete the auto dowload data file, add many anti-reptile detection method
	- random delay
	- add header
	- random user-agent

## 2021/7/1
- add get-TAIEX-from-twse.py to get TAIEX from 20200601 ~ 20210630
- Plan to build a Web APP that can visualize some analysis of TW finace
	- add main.py for the backend
