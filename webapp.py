# This is the main app that should be run from the terminal

import streamlit as st
import questionnaire
import results
import SessionState
import time
from stqdm import stqdm

#just random fonts for now can change
st.markdown("""
    <style>
    .maintitle {
        font-size: 42px;
        font-weight:900;
        font-family: "Lucida Grande", Verdana, Helvetica, Arial, sans-serif;;
        text-transform: uppercase;
        color: #124712;
        background-color:  white;
        line-height: 90%;
        letter-spacing: 2px;
        text-align: left;
        padding: 0px 0px 0px 0px;

    }
    .info {
        color: #111
        font-family: "Lucida Grande", Verdana, Helvetica, Arial, sans-serif;
        font-size: 18px;
        font-weight:200;
        letter-spacing: 1px;
        color: #444444;

    }
    .text {
        letter-spacing: 1px;
        color: #124712;
        font-size: 22px;
        font-family: "Lucida Grande", Verdana, Helvetica, Arial, sans-serif;
        font-weight: 900;
        padding-top:40px;
     }
     .tagline{
     font-weight:600;
     text-transform:uppercase;
     font-size:18px;
     }

     .results{
        font-family: "Lucida Grande", Verdana, Helvetica, Arial, sans-serif;
        font-size: 18px;
        font-weight:200;
        letter-spacing: 1px;
        color: #444444;
     }
    </style>
    """, unsafe_allow_html=True)

# Input title
st.markdown('<p class="maintitle">GreenBear Investment</p>', unsafe_allow_html=True)

# Create empty placeholders to put in results and questionnaire
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
    #loading spinner
    with st.spinner("Searching for your portfolio.."):
     time.sleep(20)
     st.success("Found your matches!")

    #progress bar
    #my_bar = st.progress(0)
    for _ in stqdm(range(100), desc="Verifying results"):
     time.sleep(0.5)
    # Launch the results and give the selected industries as argument
    results.app(session_state.selected_industries, session_state.selected_priority, container_results, session_state.status)


    # Launch the results and give the selected industries as argument
    results.app(session_state.selected_industries,
        session_state.selected_priority, container_results, session_state.status)


# Add disclaimer (TO DO)
info_url="<a href='https://corpgov.law.harvard.edu/2017/07/27/esg-reports-and-ratings-what-they-are-why-they-matter/'>More on ESG Reports and Ratings</a>"
st.title('Disclaimer!')
st.markdown('<p class="info"> Green Bear Investment do not calculate these scores. The sustainability scores are provided by an external service (Yahoo Finance), who calculate a total Environmental, Social and Governance (ESG) score for each company. Green Bear Investment provide a recommendation service based on your interests. We do not guarantee suggested stocks will provide a decent return, nor if they carry out truly sustainable practices.</p>', unsafe_allow_html=True)
st.markdown(info_url, unsafe_allow_html=True)
