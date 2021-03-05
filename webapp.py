# This is the main app that should be run from the terminal

import streamlit as st
import questionnaire
import results
import sidebar
import SessionState

# Input title
st.title('Sustainable Investment Service')

# Create empty placeholders to put in results and questionnaire
holder_results = st.empty()
holder_questionnaire = st.empty()

# Create containers in these holders for the controls
container_questionnaire = holder_questionnaire.beta_container()
container_results = holder_results.beta_container()

# Use the SessionState to save the list of selected industries and status
# Status 0: questionnaire phase
# Status 1: results phase
session_state = SessionState.get(selected_industries=[], status=0)

# Launch the questionnaire and save the returned industries in the session state
# and save the new status (1) in session state so that the results are launched
session_state.selected_industries, session_state.status = questionnaire.app(container_questionnaire, session_state.status)

# Launch the results if the status is 1
if session_state.status == 1:
    # Launch the results and give the selected industries as argument
    results.app(session_state.selected_industries, container_results, session_state.status)

    # Empty the questionnaire placeholder to show the results placeholder
    holder_questionnaire.empty()

# Add disclaimer (TO DO)
st.title('Disclaimer!')
st.write('Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. '
         'Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.'
         ' Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. ')