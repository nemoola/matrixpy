from datetime import datetime

import requests


class News:
    def __init__(self, key):
        self.__endpoint = "https://newsapi.org/v2"
        self.__key = key
        self.__cache: NewsData = None
        self.__cache_time = 0.0

    def get_top_headlines(self):
        if self.__cache is not None and (datetime.now().timestamp() - self.__cache_time) <= 90.0:
            return self.__cache

        url = f"{self.__endpoint}/top-headlines?country=us&pageSize=1&apiKey={self.__key}"
        data = NewsData(requests.get(url).json())
        self.__cache = data
        self.__cache_time = datetime.now().timestamp()
        return data


class NewsData:
    def __init__(self, data):
        self.__data = data

    def raw(self):
        return self.__data

    def get_source(self):
        return self.__data["articles"][0]["source"]["name"]

    def get_title(self):
        if len(self.__data["articles"]) != 0:
            return self.__data["articles"][0]["title"]
        else:
            return "None"

    def get_description(self):
        return self.__data["articles"][0]["description"]
