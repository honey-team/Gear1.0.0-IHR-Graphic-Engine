from __future__ import annotations
from utils.vectors import *

class XCoords(int): pass
class YCoords(int): pass
class Color(tuple): pass
class ScreenWidth(int): pass
class ScreenHeight(int): pass
class _FPS(int): pass

class Element:
    def __init__(self, x: XCoords, y: YCoords, color: Color = (0, 0, 0, 0)):
        self.x, self.y = XCoords(x), YCoords(y)
        self.color = color

class Matrix:
    def __init__(self, elements: list[list]) -> None:
        self.elements = elements
    
    def get(self, x: XCoords, y: YCoords) -> Element:
        x, y = int(x), int(y)
        return self.elements[y][x]

    def set(self, x: XCoords, y: YCoords, element: Element):
        x, y = int(x), int(y)
        if y < len(self.elements) and x < len(self.elements[y]):
            self.elements[y][x] = element
        return self

class Screen(Matrix):
    def __init__(self, width: ScreenWidth, height: ScreenHeight, FPS: _FPS, elements: list[list] = [[]]):
        super().__init__(elements)
        self.width, self.height = width, height
        self.elements = [[Element(x, y, (0, 0, 0)) for x in range(self.width)] for y in range(self.height)]
        self.FPS = FPS
    
    def __copy__(self) -> Screen:
        return Screen(self.width, self.height, self.FPS)