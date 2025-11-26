import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print("DEBUG: entered main()")

    # Initializes pygame
    pygame.init()
    gameClock = pygame.time.Clock()
    dt = 0      # Delta Time

    # Create two groups for player
    # - Updateable: hold all objects that can be updated
    # - Drawable: hold all objects that can be drawn
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # Generate the player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # Explicitly add player instanced object into the groups
    updatable.add(player)
    drawable.add(player)

    # Get a new instance of GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game Loop
    while True:
        # Logs the games frames once per second
        log_state()

        # Check if the user has closed the window, and exit the game loop if they do
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Fills the screen with a solid black color
        screen.fill("black")

        # Use the groups to update and render player & objects
        updatable.update(dt)

        for obj in drawable:
            obj.draw(screen)

        # Refreshes the screen
        pygame.display.flip()

        # Pause the game loop until 1/60th of a second has passed and holds the amount of time passed since last frame
        dt = gameClock.tick(60) / 1000

    # print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
