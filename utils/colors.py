from __future__ import annotations

class Color:
    def __init__(self):
        pass

class HEX(Color):
    def __init__(
        self,
        hex: str = "#000000"
    ):
        self.hex = hex
        self.hex.rstrip("#")
    
    def to_rgb(self) -> RGB:
        return RGB(list=tuple(int(self.hex[i:i+2], 16) for i in (0, 2, 4)))


class RGB(Color):
    def __init__(
        self,
        r: int = 0,
        g: int = 0,
        b: int = 0,
        list: tuple | list = ()
    ):
        self.r, self.g, self.b = r, g, b
        self.list = tuple(list) or (self.r, self.g, self.b)

    def to_hex(self) -> HEX:
        return HEX(f'#{self.r:02x}{self.g:02x}{self.b:02x}')
    
def rgb_to_hex(rgb: RGB) -> HEX:
    return HEX(f'#{rgb.r:02x}{rgb.g:02x}{rgb.b:02x}')

def hex_to_rgb(hex: HEX) -> RGB:
    return RGB(list=tuple(int(hex[i:i+2], 16) for i in (0, 2, 4)))