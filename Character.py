from Entity import Entity
import pygame

class Character(Entity):
    def __init__(self, x, y, width, height, lives=3, color=(255, 255, 0)):
        super().__init__(x,y, width, color)
        self.width = width
        self.height = height
        self.lives = lives
        self.is_alive = lives > 0

    def move(self, direction):
        """
        Moves the character in the specified direction.
        :param direction: A string indicating the direction ('up', 'down', 'left', 'right').
        """
        if direction == 'up':
            self.y -= 3
        elif direction == 'down':
            self.y += 3
        elif direction == 'left':
            self.x -= 3
        elif direction == 'right':
            self.x += 3
        print(f"Character moves {direction}.")

    def shoot(self):
        """
        Simulates the character shooting.
        """
        print("Character shoots.")

    def collide(self):
        """
        Handles collision logic. Reduces lives and updates is_alive status.
        """
        self.lives -= 1
        self.is_alive = self.lives > 0
        print(f"Character collided. Lives remaining: {self.lives}. Alive: {self.is_alive}")
    
    