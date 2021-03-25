# This is the results page (to be completed)

import pandas as pd
import plotly.express as px
import streamlit as st

from combine_results import combine_dfs
from financial_data import financial_data
from industries_to_companies import get_companies_from_industries
from YFin_Funct_0703 import get_sustainability_score


def app(selected_industries, selected_priority, container, status):
    # Only run this if the app is in the results phase
    if status == 1:
        # Introduction
        container.markdown('<p class="info">Here is what we found! See below the results</p>', unsafe_allow_html=True)

        industry = selected_industries  # put in selected industries

        if industry:
            companies = get_companies_from_industries(industry).tolist()
            print(companies)
            # Remove nans
            companies = [x for x in companies if str(x) != 'nan']
            print("GETTING SUSTAINABILITY DATA")
            df2 = get_sustainability_score(companies)
            # Clean up dataframe
            columns_to_drop = ['palmOil', 'controversialWeapons',
                               'gambling', 'nuclear', 'furLeather',
                               'alcoholic', 'alcoholic', 'gmo', 'catholic', 'pesticides',
                               'pesticides', 'percentile', 'smallArms', 'governancePercentile',
                               'militaryContract', 'peerCount', 'environmentPercentile', 'animalTesting',
                               'tobacco', 'highestControversy', 'coal', 'socialPercentile',
                               'esgPerformance', 'adult', 'peerGroup']
            df2 = df2.drop(columns_to_drop, axis=1)
            print(df2)
            print("GETTING FINANCIAL DATA")
            df1 = financial_data(df2['Ticker'])
            columns_to_drop = ['Exchange', 'Share Outstanding',
                               'Company News Score', 'URL', 'Currency', 'IPO']
            df1 = df1.drop(columns_to_drop, axis=1)
            print(df1)
            # Check that both dataframes are not empty before attempting to join
            if not df1.empty and not df2.empty:
                final_result = combine_dfs(df1, df2, "Ticker", selected_priority)
                print(final_result)
                print(final_result.columns)
                final_result.rename(columns={'socialScore': 'Social Score',
                                             'governanceScore': 'Governance Score',
                                             'environmentScore': 'Environment Score',
                                             'totalEsg': 'Total ESG Score'}, inplace=True)

                container.markdown('<p class="text">1. Suggested stocks for you</p>', unsafe_allow_html=True)

                container.table(final_result.style.format({'Total ESG Score': '{:.2f}',
                                                           'Current Stock Price': '{:.2f}',
                                                           'Market Capitalization': '{:.2f}',
                                                           'Social Score': '{:.2f}',
                                                           'Governance Score': '{:.2f}',
                                                           'Environment Score': '{:.2f}'}))

                container.markdown('<p class="text">2. The make-up of your portfolio based on the stock suggestions:</p>', unsafe_allow_html=True)
                fig = px.pie(final_result, values='Total ESG Score', names='Ticker')
                fig.update_traces(textposition='inside', textinfo='percent+label')
                container.plotly_chart(fig)
