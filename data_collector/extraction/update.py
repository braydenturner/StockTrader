from data_collector.extraction.ticker import get_nasdaq_tickers, get_sp500_tickers

class Updater:
    
    def __init__(self):
        pass
    
    
    async def run(self):
        ticker_retrieval: dict = {
            "S&P 500": get_sp500_tickers, 
            "NASDAQ": get_nasdaq_tickers
        }
        
        for name, function in ticker_retrieval.items():
            
            tickers = function()
            
            
            
        
        
        
        