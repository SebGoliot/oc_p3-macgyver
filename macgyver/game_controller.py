import pygame
import pygame.freetype
from macgyver.constants import *
from macgyver.board import Board
from macgyver.enums import Tile, State


class GameController():
    """This class handles the data and rendering of the game
    """
    board = Board()
    player_pos = (0,0)
    picked_items = []
    n_picked_items = 0
    screen = pygame.display.set_mode((LEVEL_SIZE * TILE_SIZE, LEVEL_SIZE * TILE_SIZE))
    game_state = None
    game_font = None

    wall_img = pygame.image.load(WALL_IMG)
    macgyver_img = pygame.image.load(MACGYVER_IMG)
    guardian_img = pygame.image.load(GUARDIAN_IMG)
    needle_img = pygame.transform.scale(pygame.image.load(NEEDLE_IMG), (TILE_SIZE,TILE_SIZE))
    tube_img = pygame.transform.scale(pygame.image.load(TUBE_IMG), (TILE_SIZE,TILE_SIZE))
    ether_img = pygame.transform.scale(pygame.image.load(ETHER_IMG), (TILE_SIZE,TILE_SIZE))
    syringe_img = pygame.transform.scale(pygame.image.load(ETHER_IMG), (TILE_SIZE,TILE_SIZE))

    def __init__(self):
        pygame.init()
        self.game_font = pygame.freetype.Font(UI_FONT, UI_FONT_SIZE)
        pygame.display.set_icon(self.macgyver_img)
        pygame.display.set_caption(WINDOW_TITLE)
        pygame.key.set_repeat(75, 50)
        self.game_state = State.RUNNING
        self.render_level()

    def render_level(self):
        """Renders the level with the data from Board()
        """
        self.screen.fill((175,175,175))

        for position, tile in self.board.tiles.items():
            sprite_pos = (position[0] * TILE_SIZE, position[1] * TILE_SIZE)
            blit_area = (0, 0, TILE_SIZE, TILE_SIZE)
            
            if tile == Tile.WALL:
                self.screen.blit(self.wall_img, sprite_pos, blit_area)
            elif tile == Tile.MACGYVER:
                self.player_pos = (position[0], position[1])
                self.screen.blit(self.macgyver_img, sprite_pos, blit_area)
            elif tile == Tile.GUARDIAN:
                self.screen.blit(self.guardian_img, sprite_pos, blit_area)
            elif tile == Tile.NEEDLE:
                self.screen.blit(self.needle_img, sprite_pos)
            elif tile == Tile.TUBE:
                self.screen.blit(self.tube_img, sprite_pos)
            elif tile == Tile.ETHER:
                self.screen.blit(self.ether_img, sprite_pos)

        # render the ui
        self.render_ui()    
        pygame.display.flip()


    def move(self, direction):
        """This method handles the player's movements and items retrieval
        """
        # Keep the player in bounds
        dest_pos = (
            min(max(self.player_pos[0] + direction.value[0], 0), LEVEL_SIZE - 1),
            min(max(self.player_pos[1] + direction.value[1], 0), LEVEL_SIZE - 1)
            )
        
        # Handle the object retrieval
        if self.board.tiles.get(dest_pos) != Tile.WALL:
            if self.board.tiles.get(dest_pos) == Tile.NEEDLE:
                self.pick_item(Tile.NEEDLE)
            elif self.board.tiles.get(dest_pos) == Tile.TUBE:
                self.pick_item(Tile.TUBE)
            elif self.board.tiles.get(dest_pos) == Tile.ETHER:
                self.pick_item(Tile.ETHER)

            # Handle the guardian encounter & set the final state
            elif self.board.tiles.get(dest_pos) == Tile.GUARDIAN:
                if all(item in self.picked_items for item in [Tile.NEEDLE, Tile.TUBE, Tile.ETHER]):
                    self.game_state = State.WIN
                else:
                    self.game_state = State.LOSE

            self.board.tiles[self.player_pos] = None

            # If the player is not dead, draw him on his destination position
            if self.game_state != State.LOSE:
                self.board.tiles[dest_pos] = Tile.MACGYVER
            
        self.render_level()

        if self.game_state == State.WIN:
            print("Win")
        elif self.game_state == State.LOSE:
            print("Lose")

    def pick_item(self, item):
        """This method updates the picked_items list
        """
        self.picked_items.append(item)
        # storing the lenght of the list for performance reasons
        self.n_picked_items = len(self.picked_items)

    def render_ui(self):
        """This method renders the ui to the screen
        You must call it last in the render process, right before a display.flip()
        """
        value = self.n_picked_items
        if value == 0:
            value = 'no'
        elif value == 3:
            value = 'all'

        ui_text = f'You have found {value} items'
        self.game_font.render_to(self.screen, UI_OFFSET, ui_text, UI_COLOR)
