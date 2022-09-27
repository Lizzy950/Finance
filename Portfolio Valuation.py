# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:02:02 2018

@author: lekan
"""

#Portfolio Valuation

import datetime
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

df = pdr.get_data_yahoo(['AAPL', 'GE', 'GOOG', 'IBM', 'ADM','ABF','AAL'], 
                               start=datetime.datetime(2012, 7, 10), 
                               end=datetime.datetime(2013, 7, 10))['Adj Close']

returns = df / df.shift(1) - 1  # to obtain the returns of the stock
mean = returns.mean() # average of returns
VarianceCo = df.cov() # Variance Covariance of returns
Components = np.array([0.143, 0.143, 0.143, 0.143, 0.143, 0.143, 0.143])
TransComponent = Components.transpose()
PortReturn = np.dot(TransComponent, means)

 # Portfolio Return
PortVariance = np.dot(np.dot(TransComponent, VarianceCo),TransComponent)
 #Portfolio Variance
PortVolatility = PortVariance ** 0.5
print(PortReturn, PortVariance, PortVolatility)