import quandl
import pandas as pd

pd.set_option('display.max_columns', 15)
pd.set_option('display.min_rows', 10)
pd.set_option('max_colwidth', 150)

quandl.ApiConfig.api_key = "QWsV414KPVcnomvyon-i"
data = quandl.get("EOD/AAPL")

#data = quandl.get_table('ZACKS/FC', paginate=True, ticker=['AAPL', 'MSFT'], per_end_date={'gte': '2015-01-01'}, qopts={'columns':['ticker', 'per_end_date']})
print(data)