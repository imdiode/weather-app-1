# Weather App
A weather app to display temperature difference chart between two cities.

## Building Materials
- Flask
- OpenWeatherMap API
- Fetch API
- Chart.js

## Usage
1. Change the API Key
2. Run script.py
3. Open http://127.0.0.1:8080

## Changing the API key
1. Go to https://openweathermap.org
2. Sign-up for free and verify account
3. Click on your username and go to My API keys
4. Type the name of key and click generate
5. Copy the key
6. Make a .env file in the root folder
7. Add "APIKEY={yourAPIKEYwithoutcurlybraces}"

## Folder Structure
--Root
 |- temp.py (Gets temperature)
 |- keep_alive.py (Flask server)
 |- templates
   |- public
     |- index.html (View)
     |- data.json (Database)
 |- script.py (Main file that runs everything)
 |- LICENSE
 |_ README.md