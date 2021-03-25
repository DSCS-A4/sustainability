import streamlit as st
import numpy as np
import pandas as pd
import json
import requests

# API KEY
token = "&token=c0j6hdv48v6tlon085cg"


def financial_data(tickers: list) -> pd.DataFrame:

    # Getting the CompanyProfile2 endpoint from finnhub and taking certain ones out

    responses1 = list()

    for ticker in tickers:
        r1 = requests.get('https://finnhub.io/api/v1/stock/profile2?symbol={}'.format(ticker) + token)
        data1 = json.loads(r1.text)
        responses1.append(data1)

    df1 = pd.DataFrame.from_dict(responses1)
    df1 = df1.drop(columns=['phone', 'logo'])
    df1 = df1.rename(columns={'country':'Country', 'currency':'Currency', 'exchange':'Exchange',
                              'finnhubIndustry':'Industry', 'ipo':'IPO', 'marketCapitalization':'Market Capitalization',
                              'name':'Name', 'shareOutstanding':'Share Outstanding', 'ticker':'Ticker', 'weburl':'URL'})

    #only select CompanyNewsScore from the sentiment score endpoint

    responses3 = list()

    for ticker in tickers:
        r3 = requests.get('https://finnhub.io/api/v1/news-sentiment?symbol={}'.format(ticker) + token)
        data3 = json.loads(r3.text)
        responses3.append(data3)


    df3 = pd.DataFrame.from_dict(responses3)
    df3 = pd.DataFrame(df3['companyNewsScore'])
    df3 = df3.rename(columns={'companyNewsScore':'Company News Score'})

    # select current stock price from the quote endpoint

    responses4 = list()

    for ticker in tickers:
        r4 = requests.get('https://finnhub.io/api/v1/quote?symbol={}'.format(ticker) + token)
        data4 = json.loads(r4.text)
        responses4.append(data4)

    df4 = pd.DataFrame.from_dict(responses4)
    df4 = df4.drop(columns=['h', 'l', 'o', 'pc', 't'])
    df4 = df4.rename(columns={'c': 'Current Stock Price'})

    # adding everything together, rearranging the columns

    finaldf = pd.concat([df1, df3, df4], axis=1)
    finaldf = finaldf[['Ticker', 'Name', 'Country', 'Currency', 'Exchange', 'Industry', 'IPO', 'Current Stock Price', 'Market Capitalization', 'Share Outstanding', 'Company News Score', 'URL']]
    return finaldf
