from rgbmatrix import RGBMatrix, RGBMatrixOptions


class Matrix:
    def __init__(self, options: RGBMatrixOptions = None):
        self.matrix = RGBMatrix(options = options)

    def Fill(self):
        self.matrix.Fill(255, 255, 255)


if __name__ == "__main__":
    options = RGBMatrixOptions()
    options.rows = 40
    options.cols = 80
    options.disable_hardware_pulsing = True
    # options.chain_length = 1
    # options.parallel = 1
    # options.hardware_mapping = 'regular'

    matrix = Matrix(options)
    matrix.Fill()

