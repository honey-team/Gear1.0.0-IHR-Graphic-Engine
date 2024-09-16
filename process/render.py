import rich.color
from utils.graphic import *
import time, os

def clear(): os.system("cls||clear")

def render(screen: Screen):
    string = ""
    for row in screen.elements:
        for element in row:
            if element.color == (0, 0, 0):
                string += "\033[40m" + " "
            elif element.color == (255, 255, 255):
                string += "\033[47m" + " "
        string += "\n"
    print(string + "\033[0m")

def sleep(FPS: int = 60): time.sleep(1/FPS)