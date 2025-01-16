from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time
from datetime import datetime

class Matrix:
    def __init__(self, options: RGBMatrixOptions = None):
        self.matrix = RGBMatrix(options = options)

    def Fill(self):
        self.matrix.Fill(0, 255, 0)

    def RunText(self):
        canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("./fonts/9x18.bdf")
        text_color = graphics.Color(200, 255, 255)
        
        while(True):
            canvas.Clear()
            graphics.DrawText(canvas, font, 0, 10, text_color, datetime.now().strftime("%Y"))
            graphics.DrawText(canvas, font, 0, 21, text_color, datetime.now().strftime("%m/%d"))
            graphics.DrawText(canvas, font, 0, 32, text_color, datetime.now().strftime("%H:%M:%S"))
            time.sleep(0.05)
            canvas = self.matrix.SwapOnVSync(canvas)


if __name__ == "__main__":
    options = RGBMatrixOptions()
    options.rows = 40
    options.cols = 80
    options.disable_hardware_pulsing = True
    options.pwm_lsb_nanoseconds = 80
    # options.chain_length = 1
    # options.parallel = 1
    # options.hardware_mapping = 'regular'

    matrix = Matrix(options)
    # matrix.Fill()
    matrix.RunText()
    
