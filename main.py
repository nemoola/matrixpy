# import os
from datetime import datetime

# from dotenv import load_dotenv
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

from utils.crypto import Crypto
from utils.news import News
from utils.wether import Weather


class Matrix:
    def __init__(self, options: RGBMatrixOptions = None, open_weather_api_key: str = None, news_api_key: str = None):
        self.matrix = RGBMatrix(options=options)
        self.canvas = self.matrix.CreateFrameCanvas()
        self.font = graphics.Font()
        self.font_small = graphics.Font()
        self.open_weather_api_key = open_weather_api_key
        self.news_api_key = news_api_key
        self.Crypto = Crypto()
        self.Weather = Weather(self.open_weather_api_key)
        self.News = News(self.news_api_key)
        self.font.LoadFont("./fonts/9x18.bdf")
        self.font_small.LoadFont("./fonts/6x13.bdf")

    def run(self):
        news_pos = 160
        count = 0
        news_len = 0

        while (True):
            self.canvas.Clear()

            now = datetime.now()
            year = now.strftime("%Y")
            day = now.strftime("%m/%d")
            time_ = now.strftime("%H:%M:%S")

            wether = self.Weather.get_by_geo(36.1039866, 140.1955721)

            graphics.DrawText(self.canvas, self.font_small, 0, 10, graphics.Color(255, 255, 255), year)
            graphics.DrawText(self.canvas, self.font, 0, 20, graphics.Color(255, 255, 255), day)
            graphics.DrawText(self.canvas, self.font, 0, 30, graphics.Color(255, 255, 255), time_)

            graphics.DrawText(self.canvas, self.font_small, 80, 10, graphics.Color(255, 200, 0),
                              f"BTC: {self.Crypto.get_price('BTCUSDT')}")
            graphics.DrawText(self.canvas, self.font_small, 80, 20, graphics.Color(0, 200, 255),
                              f"Wether: {wether.get_weather()}")
            graphics.DrawText(self.canvas, self.font_small, 80, 30, graphics.Color(255, 50, 50),
                              f"Temp: {wether.get_temp()}")
            news_len = graphics.DrawText(self.canvas, self.font_small, news_pos, 39, graphics.Color(200, 0, 255),
                              f"News: {self.News.get_top_headlines().get_title()}")

            if count == 2:
                news_pos -= 1
                count = 0
            else:
                count += 1
    
            if news_pos <= 0 - news_len:
                news_pos = 160

            self.canvas = self.matrix.SwapOnVSync(self.canvas)


if __name__ == "__main__":
    # load_dotenv()

    options = RGBMatrixOptions()
    options.rows = 40
    options.cols = 80
    options.disable_hardware_pulsing = True
    options.pwm_lsb_nanoseconds = 50
    options.gpio_slowdown = 3
    options.chain_length = 2
    # options.pixel_mapper_config = "V-mapper"

    matrix = Matrix(options, "REMOVED", "REMOVED")
    matrix.run()
