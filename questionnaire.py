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
    sector_industries = qd.load_sectors_industries_csv('data/company_industry_sector.csv', 1, 3, 7)
    selected_sectors = []

    # Add checkbox for each category
    check_boxes = [questions.checkbox(sector, key=sector) for sector in [sector_industries[x][0] for x in range(len(sector_industries))]]

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
        selected_sectors = [sector for sector, checked in zip([sector[0] for sector in sector_industries], check_boxes) if checked]
        selected_industries = qd.get_industries_from_sectors(sector_industries, selected_sectors)

    # Add disclaimer (TO DO)
    st.title('Disclaimer!')
    st.write('Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. '
             'Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.'
             ' Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. ')
