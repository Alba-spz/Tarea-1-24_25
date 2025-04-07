from Character import Character
import pygame

class Opponent(Character):
    def __init__(self, x, y, width=50, height=50, color=(255,255,0), lives=1, is_star=False):
        super().__init__(x, y, width, height, lives, color)
        self.is_star = is_star

    def move(self, direction):
        if direction == 'left':
            self.x -= 1
        elif direction == 'right':
            self.x += 1
        elif direction == 'up':
            self.y -= 1
        elif direction == 'down':
            self.y += 1

    def shoot(self):
        print("Opponent shoots!")

    def collide(self):
        """
        Handles collision logic. Reduces health and updates is_alive status.
        """
        self.lives -= 1
        self.is_alive = self.lives > 0
        print(f"Opponent collided. Lives remaining: {self.lives}. Alive: {self.is_alive}")

    def hit_by_player(self, player):
        """
        Handles logic when hit by a player's shot. Reduces health, updates is_alive status,
        and increments the player's score.
        """
        self.collide()
        player.score += 1
        if not self.is_alive:
            self.is_star = True
            print("Opponent was defeated and turned into a star!")
        print(f"{player.name}'s score: {player.score}")
        