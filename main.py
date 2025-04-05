import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable)
    player=Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in  shots:
                if asteroid.collision(shot) == True:
                    shot.kill()
                    asteroid.split()
            if asteroid.collision(player) == True:
                print("Game Over!")
                sys.exit()
        screen.fill("black")  # Fill screen every frame
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()  # Update the display
        delta = clock.tick(60)
        dt=delta/1000
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()