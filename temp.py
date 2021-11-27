import requests
import json

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"


def weather(city):
    URL = BASE_URL + "q=" + city + "&appid=" + "8f8694694d0b936470289037ead9a9df"
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        tempk = main['temp']
        tempf = (((tempk-273.15)*9)/5)+32
        tempc = tempk-273.15
        print(tempf)
        return tempf
    else:
        print(response.content)
        return 0

# weather('Ottawa')
# weather('Waterloo')
