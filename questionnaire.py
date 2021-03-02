# This is the questionnaire page (to be completed)

import streamlit as st
import questionnaire_data as qd

def app():
    # Title and introduction
    st.title('Sustainable Investment Service')
    st.write('Questionnaire (further explanation...)')

    # Split page into vertical sections, 1 to 3
    require, questions = st.beta_columns([1,3])

    # Question 1: select industries
    questions.markdown('**1. Select industries you have affinity with:**')

    # Option 1: load categories from csv file
    categories = qd.load_categories_csv('data/global_alphabetical.csv', 1, 2)
    selected_industries = []

    # Add checkbox for each category
    check_boxes = [questions.checkbox(category, key=category) for category in categories]

    # Question 2: select sustainability priorities
    questions.markdown('**2. Select sustainability priorities:**')

    # Add options for question 2
    energy=questions.checkbox('Social sustainability')
    materials=questions.checkbox('Environmental sustainability')

    # Question 3: input stock price indication 
    questions.markdown('**3. Input stock price indication:**')
    price_indication = questions.number_input('', value=50.0, min_value=0.0, step=10.0)    
    
    # Add confirm button
    if questions.button("Confirm Selection"):
        questions.write('Selection confirmed')
        selected_industries = [category for category, checked in zip(categories, check_boxes) if checked]

    # Add disclaimer (TO DO)
    st.title('Disclaimer!')
    st.write('Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. '
             'Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.'
             ' Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. ')
