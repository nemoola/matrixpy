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
        self.open_weather_api_key = open_weather_api_key
        self.news_api_key = news_api_key
        self.Crypto = Crypto()
        self.Weather = Weather(self.open_weather_api_key)
        self.News = News(self.news_api_key)
        self.font.LoadFont("./fonts/jp12.bdf")

    def run(self):
        news_pos = 160
        while (True):
            self.canvas.Clear()

            now = datetime.now()
            year = now.strftime("%Y")
            day = now.strftime("%m/%d")
            time_ = now.strftime("%H:%M:%S")

            graphics.DrawText(self.canvas, self.font, 0, 10, graphics.Color(0, 0, 255), year)
            graphics.DrawText(self.canvas, self.font, 0, 21, graphics.Color(0, 0, 255), day)
            graphics.DrawText(self.canvas, self.font, 0, 32, graphics.Color(0, 0, 255), time_)

            graphics.DrawText(self.canvas, self.font, 80, 10, graphics.Color(0, 0, 255),
                              f"BTC: {self.Crypto.get_price('BTCUSDT')}")
            graphics.DrawText(self.canvas, self.font, 80, 21, graphics.Color(0, 0, 255),
                              f"天気: {self.Weather.get_by_geo(36.1039866, 140.1955721).get_weather()}")
            graphics.DrawText(self.canvas, self.font, news_pos, 32, graphics.Color(0, 0, 255),
                              f"ニュース: {self.News.get_top_headlines().get_title()}")

            news_pos -= 1
            if news_pos <= 80:
                news_pos = 160

            self.canvas = self.matrix.SwapOnVSync(self.canvas)


if __name__ == "__main__":
    # load_dotenv()

    options = RGBMatrixOptions()
    options.rows = 40
    options.cols = 80
    options.disable_hardware_pulsing = True
    options.pwm_lsb_nanoseconds = 80
    options.chain_length = 2
    options.pixel_mapper_config = "V-mapper"

    matrix = Matrix(options, "REMOVED", "REMOVED")
    matrix.run()
