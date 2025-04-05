import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player=Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")  # Fill screen every frame
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()  # Update the display
        delta = clock.tick(60)
        dt=delta/1000
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()