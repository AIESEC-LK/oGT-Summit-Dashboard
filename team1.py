from app import fetch_google_sheet_data, calculate_column_sums, generate_pie_chart
import streamlit as st

# add a title to your section
title = 'Team 1'
# add a published csv link from google sheets
google_sheet_link = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vR-cEIAKQ26fGRkvr8hnBqkmuWfzverObjQdgcC3mdbdmIx7P0QOauwzXcC0Uz_aWDfDnaKAhhp3BST/pub?output=csv'

#############################################################
google_sheet_data = fetch_google_sheet_data(google_sheet_link)

def page():   
    st.subheader(title)
    st.write(google_sheet_data)
