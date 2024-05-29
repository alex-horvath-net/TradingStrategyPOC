class aset_store:
    def __init__(self):
        import yfinance as yf
        import pandas as pd
        import pandas_ta as ta
        import plotly.graph_objects as go
        from plotly.subplots import make_subplots
        import matplotlib.pyplot as pp

    def cell_0(self):
        import pandas as pd

        # create a dataframe with sample data
        df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Gender': ['F', 'M', 'M']})
        print(df)

    def cell_2(self):
        import yfinance as yf
        import pandas as pd

        #Download historical data
        ticker_symbol = "BTC-USD"
        period= "100d"
        start = "2024-02-01"
        end = "2024-03-28"
        interval = "1d"
        raw_data_file_path= "BTCUSD_Candlestick_1_Hour_BID_01.01.2024-31.01.2024.csv"
        ticker = yf.Ticker(ticker_symbol)
        #historical_data = ticker.history(start=start, end=end, interval=interval) #1m-7d / <1d-60d
        #historical_data = ticker.history(period=period, interval=interval)
        #historical_data = yf.download(tickers=ticker_symbol, period=period, interval=interval )
        #historical_data = pd.read_csv(raw_data_file_path)
        historical_data = yf.download(tickers='BTC-USD', period='max', interval='1d')

    def cell_3(self):
        import pandas as pd

        # cleaning historical_data
        historical_data.reset_index(inplace=True)
        historical_data = historical_data[ historical_data["Volume"]!=0 ] # clean empty volumes
        df = historical_data[:500]
        df = df.copy()