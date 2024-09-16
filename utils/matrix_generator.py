from __future__ import annotations
from typing import Any
from utils.graphic import *
from PIL import Image as _Image

class MatrixGenerator(Matrix):
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.elements):
            self.index += 1
            return self.elements[self.index - 1]
        else:
            raise StopIteration()
    
class RectWidth(int): pass
class RectHeight(int): pass
class Color(tuple): pass
class PathToImage(str): pass

class Rect(MatrixGenerator):
    def __init__(self, width: RectWidth, height: RectHeight, color: Color):
        self.width, self.height = RectWidth(width), RectHeight(height)
        self.color = color
        super().__init__([[Element(x, y, self.color) for x in range(self.width)] for y in range(self.height)])

class Image(MatrixGenerator):
    def __init__(self, path_to_image: PathToImage[str]):
        self.path = path_to_image
        image = _Image.open(path_to_image)
        rgb_image = image.convert("RGB")
        super().__init__([[Element(x, y, rgb_image.getpixel((x, y))) for x in range(rgb_image.size[0])] for y in range(rgb_image.size[1])])
