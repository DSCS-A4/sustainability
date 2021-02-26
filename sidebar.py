import streamlit as st

# This function shows the basic sidebar and navigation sidebar and returns
# which page is selected by the radiobutton
def show(PAGES):
    # Show basic sidebar
    st.sidebar.title('Sidebar')
    st.sidebar.write('For navigation or extra info pagews')
    st.sidebar.write('Or required info')

    # Show navication sidebar and return active page
    st.sidebar.title('Navigation')
    return st.sidebar.radio("Go to", list(PAGES.keys()))
