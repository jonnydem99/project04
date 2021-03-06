from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
import yfinance as yf

print('end of progam')
startDate = '2012-01-01'
endDate = str( datetime.now().strftime('%Y-%m-%d'))
print('endDate=', endDate)
def get_stats( stock_data):
    return {
        'last': np.mean( stock_data.tail(1)),
        'short_mean': np.mean( stock_data.tail(20)),
        'long_mean': np.mean( stock_data.tail(200)),
        'short_rolling': stock_data.rolling( window=20).mean,
        'long_rolling': stock_data.rolling( window=200).mean
    }

def clean_data( stock_data, col):
    weekdays = pd.date_range( start=startDate, end=endDate)
    clean_data = stock_data[col].reindex( weekdays)
    return clean_data.fillna( method='ffill')

def create_plot( stock_data, ticker):
    stats = get_stats( stock_data)
    #print( stats['last'])
    fig, ax = plt.subplots( figsize=(12,8))
    plt.plot( stock_data, label=ticker)
    plt.xlabel('Date')
    plt.ylabel('Adj Close')
    plt.legend();
    plt.title('Stock Price over Time')
    #plt.show();
    fig.savefig('stock.png')
    plt.close(fig);

def get_data( ticker):
    try:
        stock_data = data.DataReader( ticker, 'yahoo', startDate, endDate)
        adj_close = clean_data( stock_data, 'Adj Close')
        print('adj_close=', adj_close)
        create_plot (adj_close, ticker)


    except RemoteDataError:
        print('no data found for {}'.format(ticker))