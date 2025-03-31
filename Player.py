from Character import Character

class Player(Character):
    def __init__(self, name, score=0, lives=3):
        """
        Initializes the Player with a score of 0 and 3 lives.
        """
        self.score = 0
        self.lives = 3

    def move(self, direction):
        """
        Overrides the move method to include player-specific behavior.
        """
        super().move(direction)
        print(f"Player moved {direction}.")

    def shoot(self):
        """
        Overrides the shoot method to include player-specific behavior.
        """
        super().shoot()
        print("Player fired a shot.")

# Example usage
if __name__ == "__main__":
    player = Player()
    player.move("up")
    player.shoot()
    print(f"Score: {player.score}, Lives: {player.lives}")