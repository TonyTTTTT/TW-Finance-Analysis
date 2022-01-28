# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 12:08:35 2021

@author: user
"""
import pandas as pd
from flask import Flask, request
from flask_cors import CORS
from flask import jsonify


app = Flask(__name__)
cors = CORS(app)

data_num = 365
TAIEX_path = '../anlyze-by-foreign-capital/data/TAIEX.csv'
foreign_fund_path = '../anlyze-by-foreign-capital/data/Foreign-Fund.csv'


@app.route('/get-TAIEX')
def getTAIEX():
    with open(TAIEX_path, 'r') as f:
        df_TAIEX = pd.read_csv(f, index_col='Date')
    # res = {'x' : df_TAIEX['Open'].index.values[-5:].astype('str').tolist(),
           # 'y' : df_TAIEX['Open'].values[-5:].tolist()}
    res = jsonify(x = df_TAIEX['Open'].index.values[-1*data_num:].astype('str').tolist(),
                  y = df_TAIEX['Open'].values[-1*data_num:].tolist())
    
    return res


@app.route('/get-Foreign-Fund')
def getForeignFund():
    with open(foreign_fund_path, 'r') as f:
        df_fund = pd.read_csv(f, index_col='Date')
    res = jsonify(x = df_fund['Difference'].index.values[-1*data_num:].astype('str').tolist(),
                  y = df_fund['Difference'].values[-1*data_num:].tolist())
    
    return res

@app.route('/test')
def test():
    return "Hello World!\n"
