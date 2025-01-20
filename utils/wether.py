from datetime import datetime

import requests


class Weather:
    def __init__(self, key):
        self.__endpoint = "https://api.openweathermap.org/data/2.5/weather"
        self.__key = key
        self.__cache: WeatherData = None
        self.__cache_time = 0.0

    def get_by_geo(self, lat, lon):
        if self.__cache is not None and (datetime.now().timestamp() - self.__cache_time) <= 1.0:
            return self.__cache

        url = f"{self.__endpoint}?lat={lat}&lon={lon}&units=metric&appid={self.__key}&lang=ja"
        data = WeatherData(requests.get(url).json())
        self.__cache = data
        self.__cache_time = datetime.now().timestamp()
        return data


class WeatherData:
    def __init__(self, data):
        self.__data = data

    def get_weather(self):
        return self.__data["weather"][0]["main"]  # or description

    def get_temp(self):
        return self.__data["main"]["temp"]

    def get_max_temp(self):
        return self.__data["main"]["temp_max"]

    def get_min_temp(self):
        return self.__data["main"]["temp_min"]
