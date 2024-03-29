# This script will get the currency price data from the yfinance library and store it as csv

import yfinance as yf

currencies = [ "EURUSD=X", "GBPUSD=X", "JPYUSD=X" ]
timeframe = "1h" 
from_date = '2023-01-23'
to_date = '2023-04-24'

for currency in currencies:
    df_currency = yf.download(tickers=currency, start=from_date,end=to_date,interval=timeframe);
    df_currency.to_csv(currency.split('=')[0] + '.csv')
    print(df_currency.head())

