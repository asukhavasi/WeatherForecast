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

# import pandas as pd
#
# df = pd.read_csv("C:/Users/asukh/Documents/WeatherForecast/data/happy.csv")
#
# df1 = df["gdp"]
# df2 = df['happiness']
#
# print(df1)


# with open("data/happy.csv","r") as file:
#     data = file.read()
#
# print(data)


# print(image)


sky = {'2025-01-20 00:00:00': 'Snow', '2025-01-20 03:00:00': 'Snow',
     '2025-01-20 06:00:00': 'Snow', '2025-01-20 09:00:00': 'Snow', '2025-01-20 12:00:00': 'Snow', '2025-01-20 15:00:00': 'Snow', '2025-01-20 18:00:00': 'Snow', '2025-01-20 21:00:00': 'Snow', '2025-01-21 00:00:00': 'Snow', '2025-01-21 03:00:00': 'Snow', '2025-01-21 06:00:00': 'Clouds', '2025-01-21 09:00:00': 'Clouds', '2025-01-21 12:00:00': 'Clouds', '2025-01-21 15:00:00': 'Clouds', '2025-01-21 18:00:00': 'Snow', '2025-01-21 21:00:00': 'Snow', '2025-01-22 00:00:00': 'Clouds', '2025-01-22 03:00:00': 'Clouds', '2025-01-22 06:00:00': 'Snow', '2025-01-22 09:00:00': 'Clouds', '2025-01-22 12:00:00': 'Clouds', '2025-01-22 15:00:00': 'Clouds', '2025-01-22 18:00:00': 'Snow', '2025-01-22 21:00:00': 'Snow', '2025-01-23 00:00:00': 'Clouds', '2025-01-23 03:00:00': 'Snow', '2025-01-23 06:00:00': 'Snow', '2025-01-23 09:00:00': 'Snow', '2025-01-23 12:00:00': 'Snow', '2025-01-23 15:00:00': 'Snow', '2025-01-23 18:00:00': 'Snow', '2025-01-23 21:00:00': 'Snow', '2025-01-24 00:00:00': 'Snow', '2025-01-24 03:00:00': 'Snow', '2025-01-24 06:00:00': 'Snow', '2025-01-24 09:00:00': 'Clouds', '2025-01-24 12:00:00': 'Snow', '2025-01-24 15:00:00': 'Clouds', '2025-01-24 18:00:00': 'Clouds', '2025-01-24 21:00:00': 'Snow'}
print(sky)
date= []
condition= []
for x, y in sky.items():
    date.append(x)
    condition.append(y)
print(date)
print(condition)


