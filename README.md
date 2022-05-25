# TW-finance-analysis
This project aim to analysis&amp;predict the trend of Taiwan's finance

## 2022/5/25
- Fail to call api to backend by directly embed url in homepage without setupProxy

## 2022/2/8
- Setup the scratching routine for scratching TAIEX and Foreign-Fund on linux8
- No need to deploy advanced server on linux8, npm start is sufficient

## 2022/1/31
- Know how to automatically build and run the frontend
- Switch the server code(included jenkins server) to linux8.
- Next to do
	- deploy the server using advanced server tools(e.g. Apache).

## 2022/1/28
- Sucessful deal with webhook that emission when push to repo and trigger the build on jinken server.

## 2022/1/27
- Finish the deployment of Jenkins pipeline on Oasis3 server that can automatic update the git repo. when run the pipeline.

## 2021/9/9
- Use last 7 days diff as features to predict (tommorow's open - today's close), result still not good

## 2021/7/6
- try to train a linear regression model for predicting the difference btw today's Close and tmr's Open, but performance not good yet
	- need to collect more featrues

## 2021/7/2
- build the TAIEX-Open vs. Foreign-Fund-Diff figure on frontend 
- generate the label for predicting tommorow Open

## 2021/7/1
- add get-TAIEX-from-twse.py to get TAIEX from 20200601 ~ 20210630
- Plan to build a Web APP that can visualize some analysis of TW finace
	- add main.py for the backend

## 2021/5/26
- coplete the auto dowload data file, add many anti-reptile detection method
	- random delay
	- add header
	- random user-agent

## 2021/5/25
- add the auto download data from twse function by file "get_data_from_twse.py"

## 2021/5/24
- directly get data from the twse website, but been banned due to frequently requesting.
- Should download the file to local and read the csv file, instead of directly get the data from web url.