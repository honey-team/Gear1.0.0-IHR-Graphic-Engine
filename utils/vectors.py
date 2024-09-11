from __future__ import annotations

__all__ = (
    "Vector2D",
)

class Vector2D:
    def __init__(
        self,
        x: int = 0,
        y: int = 0
    ):
        self.x = x
        self.y = y

    # Operators
    ## Math operations - + *

    def __add__(self, vector: Vector2D) -> Vector2D:
        return Vector2D(self.x + vector.x, self.y + vector.y)
    
    def __radd__(self, vector: Vector2D) -> Vector2D:
        return Vector2D(self.x + vector.x, self.y + vector.y)
    
    def __iadd__(self, vector: Vector2D) -> Vector2D:
        return Vector2D(self.x + vector.x, self.y + vector.y)
    
    def __sub__(self, vector: Vector2D) -> Vector2D:
        return Vector2D(self.x - vector.x, self.y - vector.y)
    
    def __rsub__(self, vector: Vector2D) -> Vector2D:
        return Vector2D(self.x - vector.x, self.y - vector.y)
    
    def __isub__(self, vector: Vector2D) -> Vector2D:
        return Vector2D(self.x - vector.x, self.y - vector.y)
    
    def __mul__(self, vector: Vector2D) -> Vector2D:
        return Vector2D(self.x * vector.x, self.y * vector.y)
    
    def __rmul__(self, vector: Vector2D) -> Vector2D:
        return Vector2D(self.x * vector.x, self.y * vector.y)
    
    def __imul__(self, vector: Vector2D) -> Vector2D:
        return Vector2D(self.x * vector.x, self.y * vector.y)
    
    ## Conversations > < >= <=

    def __lt__(self, vector: Vector2D) -> Vector2D: # <
        return self.x < vector.y and self.y < vector.y
    
    def __le__(self, vector: Vector2D) -> Vector2D: # <
        return self.x <= vector.y and self.y <= vector.y
    
    def __gt__(self, vector: Vector2D) -> Vector2D: # <
        return self.x > vector.y and self.y > vector.y
    
    def __gt__(self, vector: Vector2D) -> Vector2D: # <
        return self.x >= vector.y and self.y >= vector.y