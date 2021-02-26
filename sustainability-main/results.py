# This is the results page (to be completed)

import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO

def app():
    st.title('Sustainable Investment Service')
    st.write('Results (Top 10 of selected investements)')

    #sidebar is fixed call using sidebar
    st.sidebar.title('Sidebar')
    st.sidebar.write('For navigation or extra info pages')
    st.sidebar.write('Or required info')


    TESTDATA = u"""\
                Industry  Price  ESG_Score
        Name                   
        Fake-Inc      Telecom   2.0   A++
        CompanyZ    Retail   5.0   A++
        MyCorp    Telecom   8.0   A+
        NewCompany  Banking  11.0  A+
        DSCS    Banking  14.0  A+
        Fake-Inc      Communications   2.0   A
        CompanyZ    Insurance   5.0   A
        MyCorp    Telecom   8.0   A
        NewCompany  Communications  11.0  B+
        DSCS    Communications  14.0  B
    """

    df = pd.read_csv(StringIO(TESTDATA), index_col=0, sep=r"\s+", engine='python')
    st.table(df)

    st.write('Market Trends for the selected industries')
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns = ['a', 'b', 'c'])
    st.line_chart(chart_data)
