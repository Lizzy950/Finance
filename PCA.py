import pandas as pd
import numpy as np
import math as mh

pd.options.display.float_format = '{:.6f}'.format
pd.set_option('display.min_rows', 10)
pd.set_option('display.max_columns', 100)
np.set_printoptions(formatter={'float': '{: 0.8f}'.format})

data = pd.read_excel(r'A:\Lekan\Miscellaneous\python\data\Case Study_III.2.xls', sheet_name='Prices')
date = data['Date']

del data['Date']

returns = np.log((data/data.shift(periods=1)))
returns = returns.dropna()

PL = data - data.shift(periods=1)
PL = PL.dropna()

cov_data = returns.cov()
corr_data = returns.corr()

#np.set_printoptions(precision=3)

eigen = np.linalg.eig(cov_data)
eigenVal = (np.array(eigen[0]).T)
eigenVec = (np.array(eigen[1]))

#Get percentage ranking of EigneValues
hold = []
for i in eigenVal:
    val = i * 100 / eigenVal.sum()
    hold.append(val)

#sort columns in terms of eigenValues    
result = pd.DataFrame(data=eigenVec, columns=hold, index=cov_data.index)
list = result.columns
result = result.reindex(columns=list)

print(result)