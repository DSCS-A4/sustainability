# This is the questionnaire page (to be completed)

import streamlit as st

def app():
    #default titles for now - can use st.markup rather than st.write to add web features (and also define css for it)
    st.title('Sustainable Investment Service')
    st.write('Questionnaire (further explanation...)')

    #sidebar is fixed call using sidebar
    st.sidebar.title('Sidebar')
    st.sidebar.write('For navigation or extra info pages')
    st.sidebar.write('Or required info')

    #beta_column splits the page into vertical sections - this is two columns with the right hand side one 3x the size of the left
    require, questions = st.beta_columns([1,3])

    #questions.write('Select from the following fields:')

    #beta_expander expands the field on click 
    questions.markdown('**1. Select industries you have affinity with:**')

    #checkboxs for filters - can use buttons or radio buttons 
    energy=questions.checkbox('Energy')
    materials=questions.checkbox('Materials')
    industrials=questions.checkbox('Industrials')
    healthcare=questions.checkbox('Healthcare')
    telec=questions.checkbox('Telecommunications')
    finance=questions.checkbox('Financials')


    #beta_expander expands the field on click
    questions.markdown('**2. Select sustainability priorities:**')

    #checkboxs for filters - can use buttons or radio buttons 
    energy=questions.checkbox('Social sustainability')
    materials=questions.checkbox('Environmental sustainability')

    questions.markdown('**3. Select sustainability priorities:**')
    price_indication = questions.number_input('', value=50.0, min_value=0.0, step=10.0)    
        
    if questions.button("Confirm Selection"):
        questions.write('Selection confirmed')

    st.title('Disclaimer!')
    st.write('Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. '
             'Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.'
             ' Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. ')
