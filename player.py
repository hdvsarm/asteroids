import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt, direction):
        self.rotation = self.rotation + (direction * (PLAYER_TURN_SPEED * dt))
    
    def update(self, dt):
        self.timer = max(self.timer-dt,0)
        keys = pygame.key.get_pressed()
        negative = -1
        positive = 1
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_a]:
            self.rotate(dt, negative)
        if keys[pygame.K_d]:
            self.rotate(dt, positive)
        if keys[pygame.K_w]:
            self.move(dt, positive)
        if keys[pygame.K_s]:
            self.move(dt, negative)
    
    def move(self, dt, direction):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += direction * (forward * PLAYER_SPEED * dt)
    
    def shoot(self):
        if self.timer == 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN
