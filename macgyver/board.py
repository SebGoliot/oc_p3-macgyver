from macgyver.enums import Tile
from macgyver.constants import LEVEL_FILENAME, LEVEL_SIZE
from random import sample


class Board():
    """This class generates and stores the board data
    """
    tiles = {}
    
    def __init__(self):
        floor_tiles = []
        items = [Tile.NEEDLE, Tile.TUBE, Tile.ETHER]

        with open(LEVEL_FILENAME) as f:
            level = f.read().replace('\n', '')

        for position, tile in enumerate(level):
            x, y = position % LEVEL_SIZE, position // LEVEL_SIZE
            if tile == '#':
                self.tiles[x, y] = Tile.WALL
            elif tile == '-':
                self.tiles[x, y] = Tile.GUARDIAN
            elif tile == '+':
                self.tiles[x, y] = Tile.MACGYVER
            else:
                self.tiles[x, y] = Tile.FLOOR
                floor_tiles.append((x, y))

        for position in sample(floor_tiles, len(items)):
            self.tiles[position] = items.pop()
