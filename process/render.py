from utils import graphic
import time, os

def clear(): os.system("cls||clear")

def render(screen: graphic.Screen):
    string = str()
    for row in screen.matrix:
        row: list = row
        for pixel in row:
            pixel: graphic.Element = pixel
            if pixel.color.list == (0, 0, 0):
                string += " "
            if pixel.color.list == (255, 255, 255):
                string += "#"
        string += "\n"
    print(string)

def sleep(FPS: int = 60):
    time.sleep(1/FPS)