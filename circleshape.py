import pygame
import sys
# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        # pygame.draw.polygon(screen, "white", self.triangle)
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def check_collision(self, CircleShape):
        dist = pygame.math.Vector2.distance_to(self.position, CircleShape.position)
        if dist <= self.radius + CircleShape.radius:
            print('Game Over!')
            sys.exit()
        