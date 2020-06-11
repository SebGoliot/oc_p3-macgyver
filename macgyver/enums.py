from enum import Enum

class Tile(Enum):
    """This Enum class stores the kind of the tiles
    """
    WALL = 0
    FLOOR = 1
    GUARDIAN = 2
    MACGYVER = 3
    NEEDLE = 4
    TUBE = 5
    ETHER = 6
