import streamlit as st
import plotly.express as px
from matplotlib.pyplot import figure

st.title("Weather Forecast for Next Days")

place = st.text_input("Place:",placeholder="enter city name",value="Windsor")
days = st.slider("Forecast Days",min_value=1,max_value=5,value=2,
                 help="Select number of days to forecast weather")

selector = st.selectbox("Select data to view",
                        ("Temperature","Sky")
                        )


st.header(f"{selector} for the next {days} days in {place}", divider="orange")

def get_data(days):
    dates = ["2024-12-01","2024-12-02","2024-12-03","2024-12-04","2024-12-05"]
    temp = [20,22,30,18,25]

    selected_days = []
    temp_dynamic = []
    for i in range(days):
        selected_days.append(dates[i])
        temp_dynamic.append(temp[i])
    fig = px.line(x=selected_days,y=temp_dynamic,labels={"x":"Date","y":"Temperature(C)"})
    return fig
st.plotly_chart(get_data(days))