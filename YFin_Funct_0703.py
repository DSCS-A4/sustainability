#!/usr/bin/env python
# coding: utf-8

# In[7]:


import yfinance as yf
import pandas as pd
import os


# In[9]:


# Retrieve Yahoo! Finance Sustainability Scores for each ticker
tickers=['AAPL', 'TSLA', 'XRX', 'R']

def ESG_tick(tickers):
    for i in tickers:
    # print(i)
        i_y = yf.Ticker(i)
        try:
            if i_y.sustainability is not None:
                temp = pd.DataFrame.transpose(i_y.sustainability)
                temp['company_ticker'] = str(i_y.ticker)
                print(temp)
                #esg= esg.append(temp)
            
        except IndexError:
            pass
        


# In[10]:


ESG_tick(tickers)


# In[ ]:




