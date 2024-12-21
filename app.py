import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------- Fetch Data from Google Sheets -------------------------

@st.cache_data
def fetch_google_sheet_data(sheet_url):
    """
    Fetches data from a public Google Sheet and returns it as a DataFrame.
    :param sheet_url: URL of the public Google Sheet CSV export link.
    :return: pandas DataFrame.
    """
    return pd.read_csv(sheet_url)

# ------------------------- Functions for Data Operations -------------------------

def calculate_column_sums(dataframe):
    """
    Calculates the sum of each column.
    Replace 'column1', 'column2', etc., with actual column names from the sheet.
    """
    column_sums = {
        'Sum of Column 1': dataframe['column1'].sum(),  # Replace 'column1' with actual column name
        'Sum of Column 2': dataframe['column2'].sum(),  # Replace 'column2' with actual column name
        'Sum of Column 3': dataframe['column3'].sum(),  # Replace 'column3' with actual column name
        'Sum of Column 4': dataframe['column4'].sum()   # Replace 'column4' with actual column name
    }
    return column_sums

def generate_pie_chart(dataframe, column_name):
    """
    Generates a pie chart based on a given column.
    :param dataframe: pandas DataFrame.
    :param column_name: Column to generate pie chart for.
    """
    pie_data = dataframe[column_name].value_counts()
    fig, ax = plt.subplots()
    ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    return fig