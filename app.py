import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# import plotly.express as px

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

def generate_line_chart(dataframe, column_name):
    """
    Generates a line chart based on a given column.
    :param dataframe: pandas DataFrame.
    :param column_name: Column to generate line chart for.
    """
    fig, ax = plt.subplots()
    ax.plot(dataframe[column_name])
    ax.set_xlabel('Index')
    ax.set_ylabel(column_name)
    return fig

# def generate_pie_chart(df, column_for_values, column_for_labels, title="Pie Chart"):
#     """
#     Function to generate a pie chart using Plotly and display it in a Streamlit app.

#     Parameters:
#     - df (pd.DataFrame): The input DataFrame.
#     - column_for_values (str): The column name to use for values in the pie chart.
#     - column_for_labels (str): The column name to use for labels in the pie chart.
#     - title (str): Title of the pie chart. Default is "Pie Chart".
#     """
#     try:
#         # Validate inputs
#         if column_for_values not in df.columns or column_for_labels not in df.columns:
#             st.error("Selected columns are not available in the DataFrame.")
#             return

#         # Generate the pie chart using Plotly
#         fig = plt.pie(
#             df,
#             values=column_for_values
#             # names=column_for_labels,
#             # title=title,
#         )
#         # Display the chart
#         st.plotly_chart(fig)
#     except Exception as e:
#         st.error(f"An error occurred: {e}")