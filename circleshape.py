import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collision(self, circle):
        distance = self.position.distance_to(circle.position)
        if circle.radius + self.radius > distance:
            return True
        else:
            return False

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass
