import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from team1 import page as team1_page

#import from team files

def main():

    st.title("oGT Summit - Data Analytics")
    st.write("Data dashboard for the year 2024")

    st.image("./White-Black-Logo.png")

    try:
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Team 1", "Team 2", "Team 3", "Team 4", "Team 5", "Team 6"])
        with tab1:
            team1_page()

        with tab2:
            st.subheader("Team 2")
            st.write("This is the data for Team 2")

        with tab3:
            st.subheader("Team 3")
            st.write("This is the data for Team 3")

        with tab4:
            st.subheader("Team 4")
            st.write("This is the data for Team 4")

        with tab5:
            st.subheader("Team 5")
            st.write("This is the data for Team 5")

        with tab6:
            st.subheader("Team 6")
            st.write("This is the data for Team 6")
        

    except Exception as e:
        st.error(f"Error fetching or processing data: {e}")

# Run the app
if __name__ == "__main__":
    main()
