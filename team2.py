from app import fetch_google_sheet_data, show_pie_chart, show_line_chart, show_bar_chart
import streamlit as st
import matplotlib.pyplot as plt

# add a title to your section
title = 'Team 2'

# add a published csv link from google sheets
google_sheet_link = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTu6uF64b8Q-OXMSndIY_0a2jVZJjFnKFCgAtoRZ_XUhaianjQ30tdNBMfMUpRRrGxWc7FUVyNaK_1Y/pub?gid=2113157642&single=true&output=csv'
#############################################################
google_sheet_data = fetch_google_sheet_data(google_sheet_link)

def page():   
    st.subheader(title)
    st.write(google_sheet_data)

    # google_sheet_data = df[google_sheet_data]

    show_pie_chart(google_sheet_data, 'Home LC')
    show_bar_chart(google_sheet_data, 'Home LC')
    # show_line_chart(google_sheet_data, 'Home LC')
