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

# ------------------------- Main Streamlit UI -------------------------

def main():
    st.title("Google Sheets Data Viewer")
    st.write("This app fetches data from a publicly published Google Sheet and displays insights.")

    # Hardcoded Google Sheet URL - Change the export link accordingly
    google_sheet_url = "YOUR_GOOGLE_SHEET_URL"  # Replace this with your Google Sheet export CSV URL

    try:
        # Fetch data
        st.info("Fetching data...")
        df = fetch_google_sheet_data(google_sheet_url)
        st.success("Data fetched successfully!")

        # Section 1: Display Column Sums
        st.header("Section 1: Column Sums")
        column_sums = calculate_column_sums(df)
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Sum of Column 1", column_sums['Sum of Column 1'])
        col2.metric("Sum of Column 2", column_sums['Sum of Column 2'])
        col3.metric("Sum of Column 3", column_sums['Sum of Column 3'])
        col4.metric("Sum of Column 4", column_sums['Sum of Column 4'])

        # Section 2: Display Table
        st.header("Section 2: Data Table")
        st.dataframe(df)

        # Section 3: Pie Chart
        st.header("Section 3: Pie Chart")
        pie_column = st.selectbox("Select a column for the pie chart:", df.columns)
        pie_chart = generate_pie_chart(df, pie_column)
        st.pyplot(pie_chart)

    except Exception as e:
        st.error(f"Error fetching or processing data: {e}")

# Run the app
if __name__ == "__main__":
    main()
