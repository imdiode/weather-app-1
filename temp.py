import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()

# Open weathermap API BASE URL for HTTP request
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"


def weather(city):
    # Request construction
    apikey = os.getenv('APIKEY')
    URL = BASE_URL + "q=" + city + "&appid=" + str(apikey)
    
    # Getting response
    response = requests.get(URL)

    # Checking response
    if response.status_code == 200:
        # Parsing response to JSON
        data = response.json()

        # Extracting required information
        main = data['main']
        tempk = main['temp']
        
        # Temperature calculations
        tempf = (((tempk-273.15)*9)/5)+32
        tempc = tempk-273.15
        return tempf
    else:
        print(response.content)
        return 0

# Usage
# weather('Ottawa')
# weather('Waterloo')