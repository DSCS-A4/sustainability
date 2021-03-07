# This is the results page (to be completed)

import streamlit as st
import pandas as pd
import numpy as np
from combine_results import combine_dfs
import plotly.express as px
<<<<<<< Updated upstream
=======
from industries_to_companies import get_companies_from_industries
from financial_data import financial_data
#from Get_ESGScores_FromList import get_esg_scores
#from YFinance_Function import get_ESG
from YFin_Funct_0703 import ESG_tick

>>>>>>> Stashed changes


def app():
    st.title('Sustainable Investment Service')
<<<<<<< Updated upstream
=======

    industry=["Advertising", "Trucking"] #put in selected industries

    companies=get_companies_from_industries(industry).tolist()
    print(companies, type(companies))

    df2=test_financial_data(companies[0])
    print(df2)

<<<<<<< Updated upstream
    df3=get_esg_scores(companies)
    print(df3)


=======
        if industry:
            container.write(industry)
            companies = get_companies_from_industries(industry).tolist()

        container.write(companies)
        #print(companies, type(companies))

        #df2 = financial_data(companies)
        #print(df2)


        df3 = ESG_tick(companies)
        print(df3)
>>>>>>> Stashed changes

>>>>>>> Stashed changes
    st.write('Results (Top 10 of selected investements)')

    # Hardcoded dataframes to simulate input from previous steps (To be removed)
    df1 = pd.DataFrame({'ticker': ["APPL", "GOOGL", "MSFT"], 'overall_score': [98.7, 56.2, 76],
                        'E_score': [10, 30, 20], 'S_score': [15, 30, 60], 'G_score': [80, 25, 38]},
                       columns=['ticker', 'overall_score', "E_score", "S_score", "G_score"])
    df2 = pd.DataFrame({'ticker': ["APPL", "GOOGL", "MSFT"], 'Price_per_share': [112, 78, 230]},
                       columns=['ticker', 'Price_per_share'])

    # Combine the results and show in a table
    df = combine_dfs(df1, df2, "ticker", 'overall_score')
    st.table(df.style.format({'overall_score': '{:.2f}'}))

    st.write('Market Trends for the selected industries')

    fig = px.pie(df, values='overall_score', names='ticker')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig)
