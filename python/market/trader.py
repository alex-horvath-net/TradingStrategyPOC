from market.aset_provider import AsetProvider
from market.startegy import Startegy
import pandas_ta as ta   # Version: 2.2.2
import plotly.graph_objects as go # Version: 5.22.0

class Trader:
    def __init__(self):
        self.strategy = Strategy()
        self.asset_provider = AsetProvider()
        self.df = None
        self.close_graph = None
        self.candlestick_graph = None

        self.sma_graphs =  {}
        self.ema_graphs =  {}
        self.adx_graphs =  {}

        self.rsi_graphs =  {}
    
    def asset(self, tickers):
        self.df = self.asset_provider.get_historical_data(asset=tickers, start="2024-01-01" , end="2024-05-31", interval="1d")
        return self
     
    def close(self):
        self.close_graph = go.Scatter(x=self.df.index, y=self.df["Close"], name='Close',  mode='lines', line=dict(color='blue', width=2),)        
        return self
    
    def candlestick(self):
        # The Body: abs(Open - Close)
        # The Wick (or Shadow): The upper wick shows the high, and the lower wick shows the low.
        # The Color: As mentioned, the color of the body indicates whether the closing price was higher or lower than the opening price.
        # Bulish: HCOL 
        # Berish: HOCL



        self.candlestick_graph = go.Candlestick( x=self.df.index, open=self.df['Open'], high=self.df['High'], low=self.df['Low'], close=self.df['Close'], name="Candlestick")
        return self
    

    ' TRend Indicators -------------------------------------------------------------'

    def sma(self, length):
        # Simple Moving Average: mesures direction of trend (trend, resistance or support leve)
        col_name = f"SMA_{length}"
        self.df[col_name] = ta.sma( self.df["Close"], length=length) 
        self.sma_graphs[length] =  go.Scatter(x=self.df.index,  y=self.df[col_name], name=col_name, mode='lines', line=dict(width=2))
        return self
    
    def ema(self, length):
        # Exponential Moving Average: mesures latest direction of trend (trend, resistance or support leve)
        col_name = f"EMA_{length}"
        self.df[col_name] = ta.ema( self.df["Close"], length=length) 
        self.ema_graphs[length] =  go.Scatter(x=self.df.index,  y=self.df[col_name], name=col_name, mode='lines', line=dict(width=2))
        return self
    
    def adx(self, length):
        # Average Directional Index: mesures strengt of trend ( 0week20moderate40strong60verystrong / 0ranging25trending100  ) 
        col_name = f"ADX_{length}" 
        ta.adx
        self.df.ta.adx(high='High', low='Low', close='Close', length=length, append=True) 
        self.adx_graphs[length] = go.Scatter(x= self.df.index,  y= self.df[col_name], name=col_name, yaxis='y2', line=dict( width=2))
        return self        
    
    def identify_rejection(self, data):
        # Create a new column for shooting star
        data['rejection'] = data.apply( self.rejection, axis=1 )
        return data
    
    def rejection(self, row):
        return 2 if self.has_shortHead_longTail_significantBody(row) else 1 if self.has_longHead_shortTail_and_significantBody(row) else 0


    def has_longHead_shortTail_and_significantBody(self, row):
        return self.head(row) > self.long_body(row) and self.tail(row) < self.short_body(row) and self.has_body(row)

    def has_shortHead_longTail_significantBody(self, row):
        return self.tail(row) > self.long_body(row) and self.head(row) < self.short_body(row) and  self.has_body(row)

    def head(self, row):
        return row['High'] - max(row['Close'], row['Open'])

    def tail(self, row):
        return min(row['Open'], row['Close']) - row['Low']

    def long_body(self, row):
        return 1.5 * self.body(row)
    
    
    def short_body(self, row):
        return 0.8 * self.body(row)

    def has_body(self, row):
        return self.body(row) > row['Open'] * 0.001

    def body(self, row):
        return abs(row['Close'] - row['Open'])

    ' Momentum Indicators -------------------------------------------------------------'
    def rsi(self, length):
        # Exponential Moving Average: mesures latest direction of trend (trend, resistance or support leve)
        col_name = f"RSI_{length}"
        self.df[col_name] = ta.rsi( self.df["Close"], length=length) 
        self.rsi_graphs[length] =  go.Scatter(x=self.df.index,  y=self.df[col_name], name=col_name, mode='lines', line=dict(width=2))
        return self
    
    def figure(self):
        #print(self.df)
        graphs = self.get_graphs()
        figure = self.get_figure(graphs)
        figure.show()

    def get_figure(self, data):
        figure = go.Figure(data=data)
        figure.update_layout( margin_l=0, margin_b=0, margin_r=0, margin_t=0 )
        figure.update_layout( paper_bgcolor="black", plot_bgcolor="black", font=dict(color="white") )  
        figure.update_layout( yaxis2=dict( color='red', anchor='free', overlaying='y',  side='right', title='ADX') )
        figure.update_yaxes( gridcolor='black')
        figure.update_xaxes( gridcolor='black')
        return figure

    def get_graphs(self):
        data = []
        
        if self.close_graph is not None:
            data.append( self.close_graph )

        if self.candlestick_graph is not None:
            data.append( self.candlestick_graph )
        
        for key in self.sma_graphs:
            data.append( self.sma_graphs[key] )

        for key in self.ema_graphs:
            data.append( self.ema_graphs[key] )

        for key in self.adx_graphs:
            data.append( self.adx_graphs[key] )

        for key in self.rsi_graphs:
            data.append( self.rsi_graphs[key] )

        return data

