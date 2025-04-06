from Opponent import Opponent
import pygame

class Boss(Opponent):
    def __init__(self, x, y, image, lives=10, speed=10, special_attack_power=50):
        super().__init__(x, y, image, lives)
        self.speed = speed
        self.special_attack_power = special_attack_power
    
    def move(self, direction):
        if direction == 'left':
            self.x -= self.speed
        elif direction == 'right':
            self.x += self.speed
        elif direction == 'up':
            self.y -= self.speed
        elif direction == 'down':
            self.y += self.speed
        self.rect.topleft = (self.x, self.y)

    def shoot(self):
        print("Boss uses special attack!")

    def take_damage(self, damage):
        # Boss takes reduced damage
        reduced_damage = int(damage * 0.75)
        self.lives -= reduced_damage
        self.is_alive = self.lives > 0
        print(f"Boss took {reduced_damage} damage. Lives left: {self.lives}")
        return self.is_alive

    def __str__(self):
        return f"Boss {self.x}, {self.y}, Lives {self.lives}, Speed {self.speed}, Special Attack Power {self.special_attack_power}"
