
import yfinance as yf
import pandas as pd


# Retrieve Yahoo! Finance Sustainability Scores for each ticker
# tickers=['AAPL', 'TSLA', 'XRX', 'R']

def get_sustainability_score(tickers):
    result = pd.DataFrame()
    for ticker in tickers:
        print("TRYING FOR THIS TICKER", ticker)
        i_y = yf.Ticker(ticker)
        try:
            if i_y.sustainability is not None:
                temp = pd.DataFrame.transpose(i_y.sustainability)
                temp['company_ticker'] = str(i_y.ticker)
                result = result.append(temp)
        except IndexError:
            pass
        except KeyError:
            pass
    return result
