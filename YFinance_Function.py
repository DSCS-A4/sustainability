#!/usr/bin/env python
# coding: utf-8

# In[12]:


import yfinance as yf
import pandas as pd
import os


# In[14]:


#cola = "KO"
#cola_y = yf.Ticker(cola)
#esg_data = pd.DataFrame.transpose(cola_y.sustainability)
#esg_data['company_ticker'] = str(cola_y.ticker)

#esg_data


# In[15]:


#function
ticker = "KO"
def get_ESG (ticker):
    cola_y = yf.Ticker(cola)
    esg_data = pd.DataFrame.transpose(cola_y.sustainability)
    esg_data['company_ticker'] = str(cola_y.ticker)

    return esg_data


# In[16]:


get_ESG(ticker)


# In[ ]:




