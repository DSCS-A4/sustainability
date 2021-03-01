
import requests
import pandas as pd


#LIST TICKERS 2 QUERY STRING TO QUERY -- YESSS!!!!
##might need adapting based on how the list looks like (of companies;)

tickers=["AAPL", "TSLA", "XRX"]
qts = ','.join(tickers)
#print(qts)

url='https://tf689y3hbj.execute-api.us-east-1.amazonaws.com/prod/authorization/search?&token='
query = {"q":qts}

response = requests.request("GET", url, params=query)
print(response.json())


data = response.text
df = pd.read_json(data, orient='records')


print(df)

#todo
#get tickers into list format
#add tickers to this (from company stuff part)
#keep only grades and scores per row
