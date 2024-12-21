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

def show_pie_chart(df: pd.DataFrame, column_name: str):
    """
    Displays a pie chart for the specified column in a pandas DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        column_name (str): The column name for which to create a pie chart.
    """
    if column_name not in df.columns:
        st.error(f"Column '{column_name}' not found in the DataFrame.")
        return

    # Count the occurrences of each unique value in the specified column
    value_counts = df[column_name].value_counts()

    if value_counts.empty:
        st.warning("The column has no data to display.")
        return

    # Create the pie chart
    fig, ax = plt.subplots()
    ax.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.

    # Display the chart in Streamlit
    st.pyplot(fig)

def show_line_chart(df: pd.DataFrame, column_name: str):

    """
    Displays a line chart for the specified column in a pandas DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        column_name (str): The column name for which to create a line chart.
    """
    if column_name not in df.columns:
        st.error(f"Column '{column_name}' not found in the DataFrame.")
        return

    # Check if the column contains numeric data
    if not pd.api.types.is_numeric_dtype(df[column_name]):
        st.error(f"Column '{column_name}' is not numeric and cannot be used for a line chart.")
        return

    # Create the line chart
    fig, ax = plt.subplots()
    ax.plot(df[column_name], marker='o')
    ax.set_title(f"Line Chart for {column_name}")
    ax.set_xlabel("Index")
    ax.set_ylabel(column_name)

    # Display the chart in Streamlit
    st.pyplot(fig)

def show_bar_chart(df: pd.DataFrame, column_name: str):
    """
    Displays a bar chart for the specified column in a pandas DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        column_name (str): The column name for which to create a bar chart.
    """
    if column_name not in df.columns:
        st.error(f"Column '{column_name}' not found in the DataFrame.")
        return

    # Count the occurrences of each unique value in the specified column
    value_counts = df[column_name].value_counts()

    if value_counts.empty:
        st.warning("The column has no data to display.")
        return

    # Create the bar chart
    fig, ax = plt.subplots()
    ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    return fig