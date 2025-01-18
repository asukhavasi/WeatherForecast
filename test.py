# dates = ["2024-12-01","2024-12-02","2024-12-03","2024-12-04","2024-12-05"]
# temp = [20,22,30,18,25]
# days = 4
# selected_days = []
# temp_dynamic = []
# for i in range(days):
#     selected_days.append(dates[i])
#     temp_dynamic.append(temp[i])
# print(selected_days)
# print(temp_dynamic)

import pandas as pd

df = pd.read_csv("C:/Users/asukh/Documents/WeatherForecast/data/happy.csv")

df1 = df["gdp"]
df2 = df['happiness']

print(df1)