
import requests
import os

def get_current_weather(place_name, format):
    try:
        geo_location_response = requests.get(
            "http://api.openweathermap.org/geo/1.0/direct?q=" + place_name + "&limit=1&APPID=" + os.getenv("WEATHER_API_KEY")
        )

        geo_location = geo_location_response.json()[0]
        
        weather_response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?lat=" + str(geo_location['lat']) + "&lon=" + str(geo_location['lon']) + "&units=" + format + "&APPID=" + os.getenv("WEATHER_API_KEY")
        )

        weather = weather_response.json()

        weather_data = weather['weather'][0]['description'] + ", " + str(weather['main']['temp']) + " in " + format

        return weather_data
    except Exception as e:
        print("Unable to generate get_current_weather response")
        print(f"Exception: {e}")
        return e