from typing import TypeVar
from utils.vectors import *
from utils.colors import *
from utils.errors import *

class Element:
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        color: Color | HEX | RGB = RGB(0, 0, 0)
    ):
        self.x = x
        self.y = y
        self.color = color
        self.vector = Vector2D(self.x, self.y)

class Screen:
    def __init__(
        self,
        width: int,
        height: int
    ):
        self.width = width
        self.height = height
        # matrix - двухмерный массив, содержащий пиксели (Element)
        self.matrix = [[Element(x, y) for x in range(self.width)] for y in range(self.height)]

    def get(
        self,
        x: int = 0,
        y: int = 0,
        vector: Vector2D = Vector2D(0, 0)
    ) -> Element:
        # Get x, y
        x, y = Screen.getXY(x, y, vector)
        if self.validX(x):
            if self.validY(y):
                return self.matrix[y][x]
            else:
                raise InvalidY(f"Got: {y}, max: {self.height}")
        else:
            raise InvalidX(f"Got: {x}, max: {self.width}")
    
    def set(
        self,
        x: int = 0,
        y: int = 0,
        color: Color = RGB(0, 0, 0),
        vector: Vector2D = Vector2D(0, 0),
        element: Element = None
    ) -> Element:
        x, y = Screen.getXY(x, y, vector)
        if self.validX(x):
            if self.validY(y):
                e = element or Element(x, y, color) # Create Element
                self.matrix[y][x] = e
                return e
            else:
                raise InvalidY(f"Got: {y}, max: {self.height - 1}")
        else:
            raise InvalidX(f"Got: {x}, max: {self.width - 1}")
    
    # Validating

    def validX(self, x: int) -> bool:
        return x <= self.width - 1
    
    def validY(self, y: int) -> bool:
        return y <= self.height - 1
    
    def validXY(self,
        x: int = 0,
        y: int = 0,
        vector: Vector2D = Vector2D(0, 0)
    ) -> bool:
        x, y = Screen.getXY(x, y, vector)
        return self.validX(x) and self.validY(y)
    
    @staticmethod
    def getXY(
        x: int = 0,
        y: int = 0,
        vector: Vector2D = Vector2D(0, 0)
    ) -> list:
        return [x or vector.x, y or vector.y]