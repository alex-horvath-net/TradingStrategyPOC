from market.aset_provider import AsetProvider

class Trader:
    def __init__(self):
        self.v1=111
        self.asset_provider = AsetProvider()
    
    def acquire_asset(self):
        df = self.asset_provider.get_historical_data(asset="BTC-USD", start="2024-02-01" , end="2024-03-30", interval="1d")
        return df