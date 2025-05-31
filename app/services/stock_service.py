from typing import List, Optional
import yfinance as yf
from cachetools import TTLCache
from datetime import datetime, timedelta
import pandas as pd

cache = TTLCache(maxsize=100, ttl=900)  # Cache for 15 minutes

async def get_stock_data(tickers: List[str], period: str, start_date: Optional[str] = None, end_date: Optional[str] = None):
    cache_key = f"{','.join(tickers)}_{period}_{start_date}_{end_date}"
    
    if cache_key in cache:
        return cache[cache_key]
    
    yf_period_map = {
        "1D": "1d",
        "1W": "5d",
        "1M": "1mo",
        "3M": "3mo",
        "1Y": "1y",
        "YTD": "ytd",
        "MTD": "1mo",
        "CUSTOM": None
    }
    
    interval = "1d"  # default interval
    yf_period = yf_period_map.get(period)
    
    if period == "CUSTOM" and start_date and end_date:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        delta = end - start
        if delta.days <= 7:
            interval = "60m"
        elif delta.days <= 30:
            interval = "1d"
    
    try:
        result = {}
        for ticker in tickers:
            print(f"Fetching data for {ticker} with period {period} ({yf_period}), interval {interval}")
            stock = yf.Ticker(ticker)
            if period == "CUSTOM" and start_date and end_date:
                df = stock.history(start=start_date, end=end_date, interval=interval)
            else:
                if yf_period is None:
                    raise Exception(f"Unsupported period: {period}")
                df = stock.history(period=yf_period, interval=interval)
            
            print(f"DataFrame shape for {ticker}: {df.shape}")
            if df.empty:
                print(f"No data returned for {ticker}")
                continue
                
            df = df.reset_index()
            df['Date'] = df['Date'].astype(str)
            result[ticker] = df[['Date', 'Close']].to_dict('records')
        
        cache[cache_key] = result
        return result
    except Exception as e:
        raise Exception(f"Error fetching stock data: {str(e)}")
