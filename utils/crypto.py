from datetime import datetime

from pybit.unified_trading import HTTP


class Crypto:
    def __init__(self):
        self.__session = HTTP()
        self.__cache = 0.0
        self.__cache_time = 0.0

    def get_price(self, symbol):
        if self.__cache != 0.0 and (datetime.now().timestamp() - self.__cache_time) <= 1.0:
            return self.__cache

        data = self.__session.get_mark_price_kline(
            symbol=symbol,
            interval=1,
            limit=1
        )["result"]["list"][0][4]
        self.__cache = data
        self.__cache_time = datetime.now().timestamp()
        return data
