from Character import Character

class Player(Character):
    def __init__(self, name, score=0, lives=3):
        super().__init__(name)
        self.score = score
        self.lives = lives

    def hit_by_enemy(self):
        self.lives -= 1
        if self.lives <= 0:
            print(f"{self.name} has been defeated. Game over!")
            # Add logic to end the game here
        else:
            print(f"{self.name} was hit! Lives remaining: {self.lives}")
            # Add logic to respawn the player after a brief delay

    def move(self, direction):
        print(f"{self.name} moves {direction}.")

    def shoot(self):
        print(f"{self.name} shoots!")

    def __str__(self):
        return f"Player(name={self.name}, score={self.score}, lives={self.lives})"