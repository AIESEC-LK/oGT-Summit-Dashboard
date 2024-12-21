import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from team1 import page as team1_page
from team2 import page as team2_page
from team3 import page as team3_page
from team4 import page as team4_page
from team5 import page as team5_page
from team6 import page as team6_page

#import from team files

def main():

    st.image("./White-Black-Logo.png")
    st.title("oGT Summit - Data Analytics")
    st.write("Data dashboard for the year 2024")


    try:
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Team 1", "Team 2", "Team 3", "Team 4", "Team 5", "Team 6"])
        with tab1:
            team1_page()

        with tab2:
            team2_page()

        with tab3:
            team3_page()

        with tab4:
            team4_page()

        with tab5:
            team5_page()

        with tab6:
            team6_page()

    except Exception as e:
        st.error(f"Error fetching or processing data: {e}")

# Run the app
if __name__ == "__main__":
    main()
