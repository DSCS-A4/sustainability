# This is the questionnaire page (to be completed)

import streamlit as st
import questionnaire_data as qd


def app(container, status):

    # Only run this if the app is in the questionnaire phase
    if status == 0:
        # Introduction
        container.markdown('<p class="tagline">Sustainable investment suggestions in 2 steps</p>', unsafe_allow_html=True)
        container.markdown('<p class="info">We know that finding suitable sustainable stocks to invest in can be a daunting task. That’s why we offer GreenBear. Fill in your preferred sectors and priorities and we will provide you with a list of stocks to match. Start below:</p>', unsafe_allow_html=True)
        # question container
        questions = container.beta_container()

        # Question 1: select industries
        questions.markdown('<p class="text">STEP 1. Select sectors you have affinity with:</p>', unsafe_allow_html=True)

        # Option 1: load categories from csv file
        sector_industries = qd.load_sectors_industries_csv('data/company_industry_sector.csv', 1, 3, 7)
        selected_sectors = []

        #split sectors into 2 lists for 2 columns
        s1, s2, s3 =qd.split_list(sector_industries, 3)
        #split into 2 columns
        c1, c2, c3 = questions.beta_columns(3)
        # Add checkbox for each category
        #category_boxes = [questions.checkbox(sector, key=sector) for sector in [sector_industries[x][0] for x in range(len(sector_industries))]]


        check1=[c1.checkbox(s1, key=s1) for s1 in [s1[x][0] for x in range(len(s1))] ]
        check2=[c2.checkbox(s2, key=s2) for s2 in [s2[x][0] for x in range(len(s2))] ]
        check3=[c3.checkbox(s3, key=s3) for s3 in [s3[x][0] for x in range(len(s3))] ]

        category_boxes=[check1, check2, check3]
        # Question 2: select sustainability priorities
        questions.markdown('<p class="text">STEP 2. Select your sustainability priorities:</p>', unsafe_allow_html=True)
        # Add options for question 2
        selected_priority = questions.radio('',['Environmental sustainability',
            'Social sustainability', 'Governance sustainability', 'Total sustainability'])

        # Translate selected option to table column name
        if selected_priority == 'Environmental sustainability':
            selected_priority = 'environmentScore'
        elif selected_priority == 'Social sustainability':
            selected_priority = 'socialScore'
        elif selected_priority == 'Governance sustainability':
            selected_priority = 'governanceScore'
        elif selected_priority == 'Total sustainability':
            selected_priority = 'totalEsg'

        # Add confirm button
        if questions.button('Confirm Selection'):
            questions.write('Selection confirmed')
            selected_sectors = [sector for sector, checked in zip([sector[0] for sector in sector_industries], category_boxes) if checked]
            selected_industries = qd.get_industries_from_sectors(sector_industries, selected_sectors)

            # If the confirm button is clicked return status 1, so that the
            # app moves on to the results
            return selected_industries, selected_priority, 1
        else:
            return [], '', 0
