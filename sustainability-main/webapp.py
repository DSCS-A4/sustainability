# This is the main app that should be run from the terminal

import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# import plotly.express as px
# import datetime
# import plotly.graph_objects as go
import questionnaire
import results
import financial_data

PAGES = {
    "Questionnaire": questionnaire,
    "Results": results,
    "Financial Data": financial_data
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
