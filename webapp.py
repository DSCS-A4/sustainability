# This is the main app that should be run from the terminal

import streamlit as st
import questionnaire
import results
import sidebar
import SessionState

st.title('Sustainable Investment Service')

holder_results = st.empty()
holder_questionnaire = st.empty()

container_questionnaire = holder_questionnaire.beta_container()
container_results = holder_results.beta_container()

session_state = SessionState.get(selected_industries=[])
session_state.selected_industries = questionnaire.app(container_questionnaire)
results.app(session_state.selected_industries, container_results)

holder_questionnaire.empty()