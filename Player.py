from Character import Character
from Shot import Shot
import pygame

class Player(Character):
    def __init__(self, x, y, name, width=50, height=50, lives=3, color=(0, 255, 0)):
        super().__init__(x, y, width, height, lives, color)
        self.name = name
        self.score = 0
        self.speed = 5
        self.shots = [] # List to hold shots fired by the player

    def shoot(self):
        print(f"{self.name} shoots!")
        new_shot = Shot(self.x + self.width // 2, self.y, width=5, height=10, color=(255, 255, 0))
        self.shots.append(new_shot) # Add the shot to the list

    def hit_by_enemy(self):
        self.lives -= 1
        self.is_alive = self.lives > 0
        if not self.is_alive:
            print(f"{self.name} has been defeated. Game over!")
            # Add logic to end the game here
        else:
            print(f"{self.name} was hit! Lives remaining: {self.lives}")
            # Add logic to respawn the player after a brief delay

    def move(self, direction):
        if direction == 'up':
            self.y -= self.speed
        elif direction == 'down':
            self.y += self.speed
        elif direction == 'left':
            self.x -= self.speed
        elif direction == 'right':
            self.x += self.speed

    def __str__(self):
        return f"Player(name={self.name}, score={self.score}, lives={self.lives})"
    
    def draw(self, screen):
        super().draw(screen) # Draw the player character
        for shot in self.shots:
            shot.draw(screen)