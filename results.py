# This is the results page (to be completed)

import streamlit as st
import pandas as pd
from combine_results import combine_dfs
import plotly.express as px
from industries_to_companies import get_companies_from_industries
from financial_data import financial_data
from YFin_Funct_0703 import get_sustainability_score


def app(selected_industries, container, status):

    # Only run this if the app is in the results phase
    if status == 1:
        # Introduction
        container.write('Find below your results')

        industry = selected_industries  # put in selected industries

        if industry:
            # container.write(industry)
            companies = get_companies_from_industries(industry).tolist()
            print("GETTING FINANCIAL DATA")
            df1 = financial_data(companies)
            print(df1)
            print("GETTING SUSTAINABILITY DATA")
            df2 = get_sustainability_score(companies)
            print(df2)

        container.write('Results (Top 10 of selected investements)')

        # Hardcoded dataframes to simulate input from previous steps (To be removed)
        df1 = pd.DataFrame({'ticker': ["APPL", "GOOGL", "MSFT"], 'overall_score': [98.7, 56.2, 76],
                            'E_score': [10, 30, 20], 'S_score': [15, 30, 60], 'G_score': [80, 25, 38]},
                           columns=['ticker', 'overall_score', "E_score", "S_score", "G_score"])
        df2 = pd.DataFrame({'ticker': ["APPL", "GOOGL", "MSFT"], 'Price_per_share': [112, 78, 230]},
                           columns=['ticker', 'Price_per_share'])

        # Combine the results and show in a table
        df = combine_dfs(df1, df2, "ticker", 'overall_score')
        container.table(df.style.format({'overall_score': '{:.2f}'}))

        container.write('Market Trends for the selected industries')

        fig = px.pie(df, values='overall_score', names='ticker')
        fig.update_traces(textposition='inside', textinfo='percent+label')
        container.plotly_chart(fig)
