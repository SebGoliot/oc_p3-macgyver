import pygame
from macgyver.constants import *
from macgyver.board import Board
from macgyver.enums import Tile


class GameController():
    """This class handles the data and rendering of the game
    """
    board = Board()
    player_pos = (0,0)
    screen = pygame.display.set_mode((15*TILE_SIZE, 15*TILE_SIZE))

    wall_img = pygame.image.load(WALL_IMG)
    macgyver_img = pygame.image.load(MACGYVER_IMG)
    guardian_img = pygame.image.load(GUARDIAN_IMG)
    needle_img = pygame.transform.scale(pygame.image.load(NEEDLE_IMG), (32,32))
    tube_img = pygame.transform.scale(pygame.image.load(TUBE_IMG), (32,32))
    ether_img = pygame.transform.scale(pygame.image.load(ETHER_IMG), (32,32))
    syringe_img = pygame.transform.scale(pygame.image.load(ETHER_IMG), (32,32))

    def __init__(self):
        pygame.init()
        pygame.display.set_icon(self.macgyver_img)
        pygame.display.set_caption(WINDOW_TITLE)
        pygame.key.set_repeat(75, 50)

    def render_level(self):
        """Renders the level with the data from Board()
        """
        self.screen.fill((175,175,175))

        for pos, tile in self.board.tiles.items():
            if tile == Tile.WALL:
                self.screen.blit(self.wall_img, (pos[0] * TILE_SIZE, pos[1] * TILE_SIZE), (0,0,32,32))
            elif tile == Tile.MACGYVER:
                self.player_pos = (pos[0], pos[1])
                self.screen.blit(self.macgyver_img, (pos[0] * TILE_SIZE, pos[1] * TILE_SIZE), (0,0,32,32))
            elif tile == Tile.GUARDIAN:
                self.screen.blit(self.guardian_img, (pos[0] * TILE_SIZE, pos[1] * TILE_SIZE), (0,0,32,32))
            elif tile == Tile.NEEDLE:
                self.screen.blit(self.needle_img, (pos[0] * TILE_SIZE, pos[1] * TILE_SIZE))
            elif tile == Tile.TUBE:
                self.screen.blit(self.tube_img, (pos[0] * TILE_SIZE, pos[1] * TILE_SIZE))
            elif tile == Tile.ETHER:
                self.screen.blit(self.ether_img, (pos[0] * TILE_SIZE, pos[1] * TILE_SIZE))

        pygame.display.flip()

    def move(self, direction):
        """This method handles the player's movements
        """
        dest_pos = (self.player_pos[0] + direction.value[0], self.player_pos[1] + direction.value[1])
        if self.board.tiles.get(dest_pos) != Tile.WALL:

            self.board.tiles[self.player_pos] = None
            self.board.tiles[dest_pos] = Tile.MACGYVER

        self.render_level()

