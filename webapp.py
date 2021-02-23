import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import datetime
import plotly.graph_objects as go

#default titles for now - can use st.markup rather than st.write to add web features (and also define css for it)
st.title('Sustainable Investment Service')
st.write('Explanatory text..')

#sidebar is fixed call using sidebar
st.sidebar.title('Sidebar')
st.sidebar.write('For navigation or extra info pages')
st.sidebar.write('Or required info')


#beta_container is horizontal section of page
questionnaire = st.beta_container()

#beta_column splits the page into vertical sections - this is two columns with the right hand side one 3x the size of the left
require, questions = st.beta_columns([1,3])


#write lets you write anything (including dataframes and figures)
require.write('Required input nav')

questions.write('Select from the following fields:')

#beta_expander expands the field on click 
fields=questions.beta_expander('Industries you would NOT invest in:')

#checkboxs for filters - can use buttons or radio buttons 
energy=fields.checkbox('Energy')
materials=fields.checkbox('Materials')
industrials=fields.checkbox('Industrials')
healthcare=fields.checkbox('Healthcare')
telec=fields.checkbox('Telecommunications')
finance=fields.checkbox('Financials')

#for commands of these buttons use if, else statements - can do the same with if 'view'
if energy=='Energy':
    st.write('You have selected energy')


#other button examples
buttons=questions.radio("Select Company Size:", ['FTSE100', 'Large Enterprise', 'Medium Enterprise', 'SME'])   

if buttons=='FTSE100':
    questions.write('FTSE100 is selected')
elif buttons=='Large Enterprise':
    questions.write('Large Enterprise is selected')
    
    
if questions.button("Confirm Selection"):
    questions.write('Selection confirmed')


