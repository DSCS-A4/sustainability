import streamlit as st
import pandas as pd
import json
import requests

def test_financial_data(ticker):
    symbol = "?symbol=" + ticker
    symbol

    token = "&token=c0j6hdv48v6tlon085cg"
    r = requests.get('https://finnhub.io/api/v1/stock/profile2' + symbol + token)
    r = r.json()
    df = pd.DataFrame.from_dict(r, orient="index", columns=[''])
    return df
    
    # company_title = st.title(df.loc['name'][0])
    # company_title
    # st.table(df)

def app():
    st.title("Financial Data Access Port")
    st.write("Please enter the 'Ticker' or the 'Name' or the desired company, the results will be shown below:")
    st.write("So far, the API endpoint used is from Finnhub Company Profile 2, news sentiment and basic financials. Defo gotta extend this.")

#company profile
    symbol = "?symbol=" + st.text_input(label='Ticker')
    symbol

    token = "&token=c0j6hdv48v6tlon085cg"
    r = requests.get('https://finnhub.io/api/v1/stock/profile2' + symbol + token)
    r = r.json()
    df = pd.DataFrame.from_dict(r, orient="index", columns=[''])

    company_title = st.title(df.loc['name'][0])
    company_title
    st.table(df)

#news sentiment
    st.header("News Sentiment")
    r1 = requests.get('https://finnhub.io/api/v1/news-sentiment' + symbol + token)
    r1 = r1.json()
    df1 = pd.DataFrame.from_dict(r1)
    df1 = df1.drop(['symbol'], axis=1)
    st.table(df1)

#basic financials
    st.header("Basic Financials")
    r2 = requests.get('https://finnhub.io/api/v1/stock/metric' + symbol + "&metric=all" + token)
    r2 = r2.json()
    df2 = pd.DataFrame.from_dict(r2)
    df2 = df2.drop(['metricType', 'series', 'symbol'], axis=1)
    st.table(df2)
