import streamlit as st


st.title("Weather Forecast for Next Days")

place = st.text_input("Place:",placeholder="enter city name",value="Windsor")
days = st.slider("Forecast Days",min_value=1,max_value=5,value=2,
                 help="Select number of days to forecast weather")

selector = st.selectbox("Select data to view",
                        ("Temperature","Sky")
                        )


st.header(f"{selector} for the next {days} days in {place}", divider="orange")

