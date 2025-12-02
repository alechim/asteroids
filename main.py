import sys, pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Initializes pygame
    pygame.init()

    # Get a new instance of GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()

    # Create two groups for player
    # - Updateable: hold all objects that can be updated
    # - Drawable: hold all objects that can be drawn
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # Generate the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    dt = 0      # Delta Time

    # Game Loop
    while True:
        # Logs the games frames once per second
        log_state()

        # Check if the user has closed the window, and exit the game loop if they do
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Use the groups to update and render player & objects
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots: 
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        # Fills the screen with a solid black color
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        # Refreshes the screen
        pygame.display.flip()

        # Pause the game loop until 1/60th of a second has passed and holds the amount of time passed since last frame
        dt = gameClock.tick(60) / 1000

if __name__ == "__main__":
    main()
