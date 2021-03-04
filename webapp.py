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


#placeholder = st.empty()

# Replace the placeholder with some text:
#placeholder.text("Hello")

# Replace the text with a chart:
#placeholder.line_chart({"data": [1, 5, 2, 6]})

# Replace the chart with several elements:
#with placeholder.beta_container():
#     st.write("This is one element")
#     st.write("This is another")

# Clear all those elements:
#placeholder.empty()

session_state = SessionState.get(selected_industries=[])

session_state.selected_industries = questionnaire.app(st)
results.app(session_state.selected_industries, st)
