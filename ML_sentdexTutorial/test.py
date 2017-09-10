# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 21:23:40 2017

@author: yc
"""

import pandas_datareader.data as web
DAX = web.DataReader(name='^GDAXI', data_source='yahoo',start = '2000-1-1')

f = open('test.txt','w')
f.write(DAX)
f.close()
