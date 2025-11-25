import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    # Initializes pygame
    pygame.init()

    # Get a new instance of GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # Logs the games frames once per second
        log_state()

        # Check if the user has closed the window, and exit the game loop if they do
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Fills the screen with a solid black color
        screen.fill("black")

        # Refreshes the screen
        pygame.display.flip()

    # print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
