import requests


API_KEY = "a049f767e378dc942f8fdfe9b411ac41"

def get_data(place, forecast_days):
    url = (f"https://api.openweathermap.org/data/2.5/forecast?q={place}"
           f"&appid={API_KEY}")
    response = requests.get(url)
    data = response.json()
    filtered_data = forecast_days*8
    forecast_data = data["list"][:filtered_data]
    return forecast_data
if __name__ == "__main__":
    result = get_data(place='michigan',forecast_days=2)
    print(result)
    print(type(result))

    # temp = [item["main"]["temp"] for item in forecast_data]
    # sky = [item["weather"][0]["main"] for item in forecast_data]

