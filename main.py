import streamlit as st
import plotly.express as px
from altair import condition
from matplotlib.pyplot import figure
from backend import get_data
from streamlit import image

st.title("Weather Forecast for Next Days")

place = st.text_input("Place:",placeholder="enter city name",value="Windsor")
days = st.slider("Forecast Days",min_value=1,max_value=5,value=2,
                 help="Select number of days to forecast weather")

selector = st.selectbox("Select data to view",
                        ("Temperature","Sky")
                        )

try:
    st.header(f"{selector} for the next {days} days in {place}",
              divider="orange")
    data = get_data(place, days)
    if selector == "Temperature":
        dates = [item["dt_txt"] for item in data]
        temp = [round((item["main"]["temp"])/10,1) for item in data]
        fig = px.line(x=dates,y=temp,labels={"x":"Date","y":"Temperature(C)"})
        st.plotly_chart(fig)
    elif selector == "Sky":
        sky = {item["dt_txt"]:item["weather"][0]["main"] for item in data}
        images = {"Snow": "data/images/snow.png",
                  "Clouds": "data/images/cloud.png",
                  "Clear": "data/images/clear.png",
                  "Rain": "data/images/rain.png"}
        txt = []
        image_path = []
        for date, condition in sky.items():
            txt.append(date)
            image_path.append(condition)
        final_image = [images[condition] for condition in image_path]
        st.image(final_image,caption=txt,width=115)
except KeyError:
    st.write("Please Enter City name with no mistakes")



# def get_data(days):
#     dates = ["2024-12-01","2024-12-02","2024-12-03","2024-12-04","2024-12-05"]
#     temp = [20,22,30,18,25]
#
#     selected_days = []
#     temp_dynamic = []
#     for i in range(days):
#         selected_days.append(dates[i])
#         temp_dynamic.append(temp[i])
#
#
#     return fig
