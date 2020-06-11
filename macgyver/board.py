from macgyver.enums import Tile
from macgyver.constants import LEVEL_FILE


class Board():
    """This class generates and stores the board data
    """
    tiles = {}
    
    def __init__(self):
        level = None

        with open(LEVEL_FILE) as f:
            level = f.read().replace('\n', '')

        x, y = 0, 0
        for pos, tile in enumerate(level):
            x, y = pos % 15, pos // 15
            if tile == '#':
                self.tiles[x, y] = Tile.WALL
            elif tile == ' ':
                self.tiles[x, y] = Tile.FLOOR
            elif tile == '-':
                self.tiles[x, y] = Tile.GUARDIAN
            elif tile == '+':
                self.tiles[x, y] = Tile.MACGYVER
            elif tile == '/':
                self.tiles[x, y] = Tile.NEEDLE
            elif tile == '|':
                self.tiles[x, y] = Tile.TUBE
            elif tile == '*':
                self.tiles[x, y] = Tile.ETHER
