import pygame
from macgyver.constants import *
from macgyver.board import Board
from macgyver.enums import Tile, State


class GameController():
    """This class handles the data and rendering of the game
    """
    board = Board()
    player_pos = (0,0)
    picked_items = []
    screen = pygame.display.set_mode((LEVEL_SIZE * TILE_SIZE, LEVEL_SIZE * TILE_SIZE))
    game_state = None

    wall_img = pygame.image.load(WALL_IMG)
    macgyver_img = pygame.image.load(MACGYVER_IMG)
    guardian_img = pygame.image.load(GUARDIAN_IMG)
    needle_img = pygame.transform.scale(pygame.image.load(NEEDLE_IMG), (TILE_SIZE,TILE_SIZE))
    tube_img = pygame.transform.scale(pygame.image.load(TUBE_IMG), (TILE_SIZE,TILE_SIZE))
    ether_img = pygame.transform.scale(pygame.image.load(ETHER_IMG), (TILE_SIZE,TILE_SIZE))
    syringe_img = pygame.transform.scale(pygame.image.load(ETHER_IMG), (TILE_SIZE,TILE_SIZE))

    def __init__(self):
        pygame.init()
        pygame.display.set_icon(self.macgyver_img)
        pygame.display.set_caption(WINDOW_TITLE)
        pygame.key.set_repeat(75, 50)
        self.game_state = State.RUNNING

    def render_level(self):
        """Renders the level with the data from Board()
        """
        self.screen.fill((175,175,175))

        for pos, tile in self.board.tiles.items():
            sprite_pos = (pos[0] * TILE_SIZE, pos[1] * TILE_SIZE)
            blit_area = (0, 0, TILE_SIZE, TILE_SIZE)
            
            if tile == Tile.WALL:
                self.screen.blit(self.wall_img, sprite_pos, blit_area)
            elif tile == Tile.MACGYVER:
                self.player_pos = (pos[0], pos[1])
                self.screen.blit(self.macgyver_img, sprite_pos, blit_area)
            elif tile == Tile.GUARDIAN:
                self.screen.blit(self.guardian_img, sprite_pos, blit_area)
            elif tile == Tile.NEEDLE:
                self.screen.blit(self.needle_img, sprite_pos)
            elif tile == Tile.TUBE:
                self.screen.blit(self.tube_img, sprite_pos)
            elif tile == Tile.ETHER:
                self.screen.blit(self.ether_img, sprite_pos)

        pygame.display.flip()

    def move(self, direction):
        """This method handles the player's movements
        """
        # Keep the player in bounds
        dest_pos = (
            min(max(self.player_pos[0] + direction.value[0], 0), LEVEL_SIZE - 1),
            min(max(self.player_pos[1] + direction.value[1], 0), LEVEL_SIZE - 1)
            )
        
        # Handle the object retrieval
        if self.board.tiles.get(dest_pos) != Tile.WALL:
            if self.board.tiles.get(dest_pos) == Tile.NEEDLE:
                self.picked_items.append(Tile.NEEDLE)
            elif self.board.tiles.get(dest_pos) == Tile.TUBE:
                self.picked_items.append(Tile.TUBE)
            elif self.board.tiles.get(dest_pos) == Tile.ETHER:
                self.picked_items.append(Tile.ETHER)

            # Handle the guardian encounter & set the final state
            elif self.board.tiles.get(dest_pos) == Tile.GUARDIAN:
                if all(item in self.picked_items for item in [Tile.NEEDLE, Tile.TUBE, Tile.ETHER]):
                    self.game_state = State.WIN
                else:
                    self.game_state = State.LOSE

            self.board.tiles[self.player_pos] = None
            if self.game_state != State.LOSE:
                self.board.tiles[dest_pos] = Tile.MACGYVER
            
        self.render_level()

        if self.game_state == State.WIN:
            print("Win")
        elif self.game_state == State.LOSE:
            print("LOSE")
