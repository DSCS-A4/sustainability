import yfinance as yf
import pandas as pd
import os


#function
ticker = "KO"

def get_ESG (ticker):
    ticker_y = yf.Ticker(ticker)
    esg_data = pd.DataFrame.transpose(ticker_y.sustainability)
    esg_data['company_ticker'] = str(ticker_y.ticker)

    return esg_data

get_ESG(ticker)
