from __future__ import annotations

class XCoords(float): pass
class YCoords(float): pass

__all__ = (
    "Vector2D",
)

class Vector2D:
    def __init__(
        self,
        x: XCoords[float] = XCoords(),
        y: YCoords[float] = YCoords()
    ):
        self.x = XCoords(x)
        self.y = YCoords(y)

    # Operators
    ## Math operations - + *

    def __add__(self, vector: Vector2D[XCoords, YCoords]) -> Vector2D[XCoords, YCoords]:
        return Vector2D(self.x + vector.x, self.y + vector.y)
    
    def __radd__(self, vector: Vector2D[XCoords, YCoords]) -> Vector2D[XCoords, YCoords]:
        return Vector2D(self.x + vector.x, self.y + vector.y)
    
    def __sub__(self, vector: Vector2D[XCoords, YCoords]) -> Vector2D[XCoords, YCoords]:
        return Vector2D(self.x - vector.x, self.y - vector.y)
    
    def __rsub__(self, vector: Vector2D[XCoords, YCoords]) -> Vector2D[XCoords, YCoords]:
        return Vector2D(self.x - vector.x, self.y - vector.y)
    
    def __mul__(self, vector: Vector2D[XCoords, YCoords]) -> Vector2D[XCoords, YCoords]:
        return Vector2D(self.x * vector.x, self.y * vector.y)
    
    def __rmul__(self, vector: Vector2D[XCoords, YCoords]) -> Vector2D[XCoords, YCoords]:
        return Vector2D(self.x * vector.x, self.y * vector.y)
    
    ## Conversations > < >= <=

    def __lt__(self, vector: Vector2D[XCoords, YCoords]) -> Vector2D[XCoords, YCoords]:
        return self.x < vector.y and self.y < vector.y
    
    def __le__(self, vector: Vector2D[XCoords, YCoords]) -> Vector2D[XCoords, YCoords]:
        return self.x <= vector.y and self.y <= vector.y
    
    def __gt__(self, vector: Vector2D[XCoords, YCoords]) -> Vector2D[XCoords, YCoords]:
        return self.x > vector.y and self.y > vector.y
    
    def __gt__(self, vector: Vector2D[XCoords, YCoords]) -> Vector2D[XCoords, YCoords]:
        return self.x >= vector.y and self.y >= vector.y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vector2D(x={self.x}, y={self.y})"

    def __bool__(self) -> bool:
        return self.x != 0 and self.y != 0

    def __eq__(self, vector: Vector2D[XCoords, YCoords]) -> bool:
        return self.x == vector.x and self.y == vector.y

    def __truediv__(self, vector: Vector2D[XCoords, YCoords]) -> Vector2D[XCoords, YCoords]:
        return Vector2D(self.x / vector.x, self.y / vector.y)
    
