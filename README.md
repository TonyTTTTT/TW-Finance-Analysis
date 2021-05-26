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
