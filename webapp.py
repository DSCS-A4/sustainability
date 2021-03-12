# This is the main app that should be run from the terminal

import streamlit as st
import questionnaire
import results
import SessionState
from PIL import Image

# Input title
logo = Image.open('Green Bear Logo.png')
st.image(logo, width=250)
st.title('Welcome to Green Bear Investment Home Page!')
st.write('This website is devoted to **_aspiring_ investors** out there who put sustainability at the top priority. '
         'The functionality of the website is very simple. You tell us which sectors you have an affinity with, '
         'and we will show you the best companies to invest in with the highest ESG (Environment, Social and Governance) '
         'scores within the selected industries along with relevant information about the companies.')
st.write('**_Happy_ Investing!**')

# Create empty placeholders to put in results and questionnaire
st.header('The Questionnaire')
holder_results = st.empty()
holder_questionnaire = st.empty()

# Create containers in these holders for the controls
container_questionnaire = holder_questionnaire.beta_container()
container_results = holder_results.beta_container()

# Use the SessionState to save the list of selected industries and status
# Status 0: questionnaire phase
# Status 1: results phase
session_state = SessionState.get(selected_industries=[], selected_priority='',
    status=0)

# Launch the questionnaire and save the returned industries in the session state
# and save the new status (1) in session state so that the results are launched
session_state.selected_industries, session_state.selected_priority, \
    session_state.status = questionnaire.app(container_questionnaire, \
    session_state.status)

# Launch the results if the status is 1
if session_state.status == 1:
    # Empty the questionnaire placeholder to show the results placeholder
    holder_questionnaire.empty()

    # Launch the results and give the selected industries as argument
    results.app(session_state.selected_industries,
        session_state.selected_priority, container_results, session_state.status)


# Add disclaimer (TO DO)
st.header('Disclaimer!')
st.write("*The financial data that is used within this website is pulled from Finnhub and \
Yahoo Finance API's. Under no circumstance that the creators of the website can he held accountable \
for any financial decisions that the user might take. *")
