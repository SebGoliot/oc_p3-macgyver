import pygame
from macgyver.game_controller import GameController

def main():

    game_ctrl = GameController()
    game_ctrl.render_level()

    running = True

    # main loop
    while running:

        # event handling
        for event in pygame.event.get():

            # do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                running = False


if __name__=="__main__":
    main()
