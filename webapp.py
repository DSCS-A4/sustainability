# This is the main app that should be run from the terminal

import streamlit as st
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
