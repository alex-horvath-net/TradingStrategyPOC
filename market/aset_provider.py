import yfinance as yf
import pandas as pd
import pandas_ta as ta

class AsetProvider:

    def __init__(self):
        selvv2=2222

    def get_historical_data(self, asset, start, end, interval): 
      
#print(df)
        #df.reset_index(inplace=True)
        #df = df[ df["Volume"]!=0 ] # clean empty volumes
        ##df = df[:500]
        #df = df.copy()
        #Download historical data
        
        #tickers = yf.Ticker(tickers)
        #historical_data = ticker.history(start=start, end=end, interval=interval) #1m-7d / <1d-60d
        #historical_data = ticker.history(period=period, interval=interval)
        #historical_data = yf.download(tickers=ticker_symbol, period=period, interval=interval )
        #historical_data = pd.read_csv(raw_data_file_path)
        df = yf.download(tickers=asset, start=start, end=end, interval=interval)
        df.reset_index(inplace=True)
        df = df[ df["Volume"]!=0 ] # clean empty volumes
        return df