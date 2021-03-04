
import requests
import pandas as pd


def get_esg_scores(tickers):
    tickers = ["AAPL", "TSLA", "XRX"]
    qts = ','.join(tickers)
    # print(qts)

    url = 'https://tf689y3hbj.execute-api.us-east-1.amazonaws.com/prod/authorization/search?&token=4cb3eee013a380a2ac987066c4f1721c'
    query = {"q": qts}

    response = requests.request("GET", url, params=query)
    print(response.json())

    data = response.text
    df = pd.read_json(data, orient='records')

    # tickers list to dataframe
    tickers_df = pd.DataFrame(tickers, columns=['tickers'])

    # print(tickers_df, tickers_df.info())

    esg_scores = pd.concat([tickers_df, df], axis=1)
    # esg_scores

    # dropped not needed columns from final dataset
    esg_scores.drop(['environment_level', 'social_level', 'governance_level', 'total_level',
                     'disclaimer', 'last_processing_date'], axis=1)
    return esg_scores
