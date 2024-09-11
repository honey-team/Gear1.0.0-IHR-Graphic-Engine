class Gear1Exception(Exception): pass

class CoordsException(Gear1Exception): pass
class InvalidX(CoordsException): pass
class InvalidY(CoordsException): pass