import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")

df = pd.read_csv("C:/Users/asukh/Documents/WeatherForecast/data/happy.csv")
col = tuple(df.columns)

x = st.selectbox("Select the data for teh X-axis:",col)
x = x.lower()
y = st.selectbox("Select the data for teh Y-axis:",col)
y = y.lower()

def get_data(x,y):
    x_value = df[x]
    y_value = df[y]
    fig = px.scatter(x=x_value,y=y_value,labels={"x":x.title(),"y":y.title()})
    return  fig

st.header(f"{x.title()} and {y.title()}")
st.plotly_chart(get_data(x,y))