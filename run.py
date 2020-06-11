import pygame
from macgyver.game_controller import GameController
from macgyver.enums import Direction, State

def main():

    game_ctrl = GameController()
    game_ctrl.render_level()

    running = True

    # main loop
    while running:

        # event handling
        for event in pygame.event.get():

            # Quit if the event is of type QUIT
            if event.type == pygame.QUIT:
                running = False

            # Handle the keyboard inputs
            elif event.type == pygame.KEYDOWN:

                # Handling the game controls
                if game_ctrl.game_state == State.RUNNING:
                    if event.key == pygame.K_UP:
                        game_ctrl.move(Direction.UP)
                    elif event.key == pygame.K_DOWN:
                        game_ctrl.move(Direction.DOWN)
                    elif event.key == pygame.K_LEFT:
                        game_ctrl.move(Direction.LEFT)
                    elif event.key == pygame.K_RIGHT:
                        game_ctrl.move(Direction.RIGHT)

                # Escape = Quit
                if event.key == pygame.K_ESCAPE:
                    running = False



if __name__=="__main__":
    main()
