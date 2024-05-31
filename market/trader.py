from market.aset_provider import AsetProvider
import pandas_ta as ta   # Version: 2.2.2

class Trader:
    def __init__(self):
        self.asset_provider = AsetProvider()
        #self.df = None
    
    def asset(self, tickers):
        self.df = self.asset_provider.get_historical_data(asset=tickers, start="2024-01-01" , end="2024-05-31", interval="1d")
        return self
    
    def sma(self, length):
        self.df[f"SMA{length}"] = ta.sma( self.df["Close"], length=length) # base direction of trend: trend, resistance or support leve
        return self
    
    def df(self):
        return self.df
