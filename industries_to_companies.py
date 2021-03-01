import pandas as pd

data=pd.read_csv(r"data/companies_industries_US.csv")

def get_companies_from_industries(industry):
    return data[data["Industry Group"].isin(industry)].loc[:,"Ticker"].sample(n=10)
