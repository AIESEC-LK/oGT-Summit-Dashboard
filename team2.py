from app import fetch_google_sheet_data, show_pie_chart, show_line_chart, show_bar_chart
import streamlit as st
import matplotlib.pyplot as plt

# add a title to your section
title = 'Team 2'

# add a published csv link from google sheets
google_sheet_link = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQvZjeq6jPoMOfeJIS11esCTGpE92W7QvC7XwLyGlZi23TYjgBL1aImsn_dW8iUxKSw_qhEDA_be59y/pub?gid=1847193799&single=true&output=csv'
#############################################################
google_sheet_data = fetch_google_sheet_data(google_sheet_link)

def page():   
    st.subheader(title)
    st.write(google_sheet_data)

    # google_sheet_data = df[google_sheet_data]

    show_pie_chart(google_sheet_data, 'Home LC')
    show_bar_chart(google_sheet_data, 'Home LC')
    # show_line_chart(google_sheet_data, 'Home LC')
