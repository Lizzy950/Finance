# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 13:36:56 2018
@author: lekan
"""
##def MonteCall(StockPrice, Exercise, Interest, Volatility, Time, Iteration):

from math import exp,sqrt
import numpy as np

StockPrice = 50
Exercise = 47
Interest = 0.04
tim = 0.75
Volatility = 0.3
Iteration = 10000


Simulated = []
StockSimulate = []
StockSimulate.append(StockPrice)
count = 0

for i in range(1, Iteration):
     z = np.random.standard_normal(Iteration)

     #StockSimulate.append(StockSimulate[i-1] * exp((Interest - 0.5 * Volatility**2 * tim) + (Volatility *sqrt(tim) * z))      
     StockSimulate.append(StockSimulate[0] * exp((Interest - 0.5 * Volatility**2 * tim) + (Volatility *sqrt(tim) * z[count])))
     
     payof = exp(-Interest * tim) * max(StockSimulate[i] - Exercise, 0)
     #print(StockSimulate[count])
     count = count + 1

     Simulated.append(payof)
callMonte = sum(Simulated)/len(Simulated)
print(callMonte)
