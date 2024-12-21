from app import fetch_google_sheet_data, calculate_column_sums, generate_pie_chart, generate_line_chart
import streamlit as st

# add a title to your section
title = 'Team 1'
# add a published csv link from google sheets
google_sheet_link = ''

#############################################################
google_sheet_data = fetch_google_sheet_data(google_sheet_link)

def page():   
    st.subheader(title)
    st.write(google_sheet_data)
