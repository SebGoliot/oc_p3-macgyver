from macgyver.enums import Tile
from macgyver.constants import LEVEL_FILE
from random import sample


class Board():
    """This class generates and stores the board data
    """
    tiles = {}
    
    def __init__(self):
        level = None
        x, y = 0, 0
        floor_tiles = []
        items = [Tile.NEEDLE, Tile.TUBE, Tile.ETHER]

        with open(LEVEL_FILE) as f:
            level = f.read().replace('\n', '')

        for pos, tile in enumerate(level):
            x, y = pos % 15, pos // 15
            if tile == '#':
                self.tiles[x, y] = Tile.WALL
            elif tile == ' ':
                self.tiles[x, y] = Tile.FLOOR
                floor_tiles.append((x, y))
            elif tile == '-':
                self.tiles[x, y] = Tile.GUARDIAN
            elif tile == '+':
                self.tiles[x, y] = Tile.MACGYVER
            
        for item in sample(floor_tiles, 3):
            self.tiles[item] = items.pop()
