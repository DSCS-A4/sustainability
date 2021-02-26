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
import sidebar

# Define pages
PAGES = {
    "Questionnaire": questionnaire,
    "Results": results
}

# Load active page
page = PAGES[sidebar.show(PAGES)]
page.app()
