
import yfinance as yf
import pandas as pd


# Retrieve Yahoo! Finance Sustainability Scores for each ticker
# tickers=['AAPL', 'TSLA', 'XRX', 'R', 'SBUX','TLRY' 'MYOR', 'NVDA', 'BNII', 'PGIS', 'MS', 'JNJ', 'FB', 'TMO','JPM' 'BA', 'BRKB', 'MO',  'QCOMM', 'TXN', 'SNBR', 'AZN', 'HSBA','GOGL35' 'JNJ', 'FAPA', 'RIO.L'  ]


def get_sustainability_score(tickers):
    result = pd.DataFrame()

    for ticker in tickers:
        print("TRYING FOR THIS TICKER", ticker)
        i_y = yf.Ticker(ticker)
        try:
            if i_y.sustainability is not None and len(result.index) < 6:
                temp = pd.DataFrame.transpose(i_y.sustainability)
                temp['Ticker'] = str(i_y.ticker)
                result = result.append(temp)
                print(len(result.index))
            elif len(result.index) == 5:
                break
        except IndexError:
            pass
        except KeyError:
            pass

    return result
