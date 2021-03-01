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


    #beta_container is horizontal section of page
    #questionnaire = st.beta_container()

    #beta_column splits the page into vertical sections - this is two columns with the right hand side one 3x the size of the left
    require, questions = st.beta_columns([1,3])

    questions.write('Select from the following fields:')

    #beta_expander expands the field on click
    fields=questions.beta_expander('Industries you have an affinity with:')

    #checkboxs for filters - can use buttons or radio buttons
    energy=fields.checkbox('Energy')
    materials=fields.checkbox('Materials')
    industrials=fields.checkbox('Industrials')
    healthcare=fields.checkbox('Healthcare')
    telec=fields.checkbox('Telecommunications')
    finance=fields.checkbox('Financials')

    #for commands of these buttons use if, else statements - can do the same with if 'view'
    if energy==1:
        st.write('You have selected energy')
    if materials==1:
        st.write('You have selected materials')
    if industrials==1:
        st.write('You have selected industrials')
    if healthcare==1:
        st.write('You have selected healthcare')
    if telec==1:
        st.write('You have selected telec')
    if finance==1:
        st.write('You have selected finance')


    #other button examples
    buttons=questions.radio("Select Company Size:", ['FTSE100', 'Large Enterprise', 'Medium Enterprise', 'SME'])

    if buttons=='FTSE100':
        questions.write('FTSE100 is selected')
    elif buttons=='Large Enterprise':
        questions.write('Large Enterprise is selected')
    elif buttons=='Medium Enterprise':
        questions.write('Medium Enterprise is selected')
    elif buttons=='SME':
        questions.write('SME is selected')

    if questions.button("Confirm Selection"):
        questions.write('Selection confirmed')

    st.title('Disclaimer!')
    st.write('Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. '
             'Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.'
             ' Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. ')
