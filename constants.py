from enum import Enum

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS
# 3 possible amount of pieces: 6, 13, 19
PIECES = 6
# MODES: COMPvsCOMP, COMPvsPLAYER, PLAYERvsPLAYER
MODE = 'COMPvsCOMP'

Color = Enum('Color', {"RED": (255, 0, 0), "GREEN": (0, 204, 0)})

BROWN = (188, 170, 164)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
