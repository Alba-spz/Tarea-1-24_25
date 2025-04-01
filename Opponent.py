from Character import Character

class Opponent(Character):
    def __init__(self, name, health, is_star=False):
        super().__init__(name, health)
        self.is_star = is_star

    def move(self, direction):
        print(f"{self.name} moves {direction}.")

    def shoot(self):
        print(f"{self.name} shoots!")

    def collide(self):
        """
        Handles collision logic. Reduces health and updates is_alive status.
        """
        self.health -= 1
        self.is_alive = self.health > 0
        print(f"{self.name} collided. Health remaining: {self.health}. Alive: {self.is_alive}")

    def hit_by_player(self, player_score):
        """
        Handles logic when hit by a player's shot. Reduces health, updates is_alive status,
        and increments the player's score.
        """
        self.health -= 1
        self.is_alive = self.health > 0
        player_score += 1
        print(f"{self.name} was hit by the player. Health remaining: {self.health}. Alive: {self.is_alive}. Player's score: {player_score}")
        return player_score