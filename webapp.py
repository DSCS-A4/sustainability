# This is the main app that should be run from the terminal

import streamlit as st
import questionnaire
import results
import sidebar
import SessionState

# Define pages
PAGES = {
    "Questionnaire": questionnaire,
    "Results": results
}

session_state = SessionState.get(selected_industries=[])

session_state.selected_industries = questionnaire.app(st)
results.app(session_state.selected_industries, st)
