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

class Direction(Enum):
    """This Enum class stores the direction the player is going
    """
    UP = (0,-1)
    DOWN = (0,1)
    LEFT = (-1,0)
    RIGHT = (1,0)

class State(Enum):
    """This Enum class stores the game state
    """
    RUNNING = 0
    WIN = 1
    LOSE = 2
