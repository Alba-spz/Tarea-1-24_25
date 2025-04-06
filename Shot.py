from Entity import Entity
import pygame

class Shot(Entity):
    def __init__(self, x, y, image, speed=10):
        super().__init__(x, y, image)
        self.speed = speed
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def move(self):
        """Move the shot upwards."""
        self.y -= self.speed
        self.rect.y = self.y

    def hit_target(self, target):
        """
        Check if the shot hits a target.
        :param target: An object with x, y, width, and height attributes.
        :return: True if the shot hits the target, False otherwise.
        """
        return self.rect.colliderect(target.rect)