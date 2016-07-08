__author__ = 'diwesh'
import requests


def get_weather_forecast():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Wonju&APPID=3acc16ffae9e45df92a064e41646355f&units=metric'
    request_weather = requests.get(url)
    weather_json = request_weather.json()

    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    forecast = 'The Circus forecast for today is ' + description + ' with a low of ' + str(temp_min) + ' and a high of ' + str(temp_max)
    return forecast
