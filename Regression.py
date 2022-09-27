import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 100)

col_nam = ['Date','SX5P','SX5E','SXXP','SXXE','SXXF','SXXA','DK5F','DKXF']
df = pd.read_csv(r'A:\Lekan\Miscellaneous\python\data\Indices.txt', names=col_nam,delim_whitespace=False, sep=';')
df['Date'] = pd.to_datetime(df['Date']) #converting the date column to a date format
df = df.set_index(df['Date']) #setting the index of the dataframe to the date column
del df['Date'] # to delete the now redundant Date Column\

dn = pd.read_csv(r'A:\Lekan\Miscellaneous\python\data\vstoxx.txt')
dn['Date'] = pd.to_datetime(dn['Date']) # converting the date column to a date format
dn = dn.set_index(dn['Date']) # setting the index of the dataframe to the date column
del dn['Date'] # to delete the now redundant Date Column

#VSTOXX data is only available from the beginning of January 1999, we only take data from that date on

#data = pd.DataFrame({'EUROSTOXX' : df['SX5E'][df.index > dt.datetime(1999, 1, 1)]})

df = df.merge(dn, how='outer', left_index=True, right_index=True)

df = df.fillna(method='ffill')

df['SX5E_ret'] = np.log(df['SX5E'] / df['SX5E'].shift(1))

df['V2TX_ret'] = np.log(df['V2TX'] / df['V2TX'].shift(1))

df2 = df['04.01.1999':'12.02.2016'] # this is to split the dataframe at the dates shown.
df2 = df2.fillna(method='ffill')

plt.figure()
plt.plot(df['SX5E_ret'])
plt.plot(df['V2TX_ret'])

plt.show()

df2.to_csv(r'A:\Lekan\Miscellaneous\python\data\regr.csv')

model = sm.OLS(y,x).fit()
predictions = model.predict(x) 
print(model.summary())