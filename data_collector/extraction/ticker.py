import pandas as pd
from enum import Enum

class TickerSources(Enum):
    SP500 = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    NASDAQ = "https://en.wikipedia.org/wiki/NASDAQ-100"

class TickerUtility:
    
    def __init__(self):
        pass
    
    
    def get_sp500_tickers(self) -> list:
        """Get the list of S&P 500 tickers."""
        tables = pd.read_html(TickerSources.SP500.value)
        df = tables[0]
        tickers = df['Symbol'].tolist()
        # Some tickers may include dots instead of hyphens for certain stocks,
        # adjust if necessary for yfinance (e.g., BRK.B -> BRK-B)
        tickers = [ticker.replace('.', '-') for ticker in tickers]
        return tickers
    
    
    def get_nasdaq_tickers(self) -> list:
        """Get the list of NASDAQ tickers."""
        tables = pd.read_html(TickerSources.NASDAQ.value)
            # Find the first table that has a 'Ticker' column.
        ticker_table = None
        for table in tables:
            if 'Ticker' in table.columns:
                ticker_table = table
                break
                
        if ticker_table is None:
            raise ValueError("No table with a 'Ticker' column was found on the NASDAQ-100 Wikipedia page.")
        
        tickers = ticker_table['Ticker'].tolist()
        # Replace dots with hyphens if necessary (e.g., BRK.B -> BRK-B)
        tickers = [ticker.replace('.', '-') for ticker in tickers]
        return tickers
    

    
    def get_data(ticker: str) -> pd.DataFrame:
        pass