from Entity import Entity
import pygame

class Shot(Entity):
    def __init__(self, x, y, color=(255, 0, 0), speed=10):
        super().__init__(x, y, width=5, height=10, color=color)
        self.speed = speed

    def move(self):
        """Move the shot upwards."""
        self.y -= self.speed

    def draw(self, screen):
        """Draw the shot on the screen."""
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))