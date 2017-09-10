# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 21:05:17 2017

@author: yc
"""
import numpy as np
import pandas as pd
import quandl, math
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import pandas_datareader.data as web

DAX = web.DataReader(name='BRK-B', data_source='yahoo')
data = DAX[['Open', 'High', 'Low', 'Close', 'Volume']]
data['HL_PCT'] = (data['High'] - data['Low']) / data['Close'] * 100
data['PCT_change'] = (data['Close'] - data['Open']) / data['Open'] * 100

data = data[['Open','Close', 'HL_PCT', 'PCT_change', 'Volume']]

forecast_col = 'Close'
data.fillna(-99999, inplace=True)
forecast_out = int(math.ceil(0.001*len(df)))
data['lable'] = data[forecast_col].shift(-forecast_out)
data.dropna(inplace=True)

X = np.array(data.drop(['lable'],1))
y = np.array(data['lable'])
X = preprocessing.scale(X)
y = np.array(data['lable'])

X_train, X_test, y_train, y_test =cross_validation.train_test_split(X, y, test_size = 0.01)

clf = LinearRegression()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)

print(accuracy)