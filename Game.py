from Player import Player
class Game:
    def __init__(self):
        self.score = 0
        self.player = None
        self.opponent = None
        self.is_running = False

    def start(self):
        self.is_running = True
        self.score = 0
        print("Game started!")

    def update(self):
        if self.is_running:
            print("Game is updating...")
            # Lógica para actualizar el estado del juego
        else:
            print("Game is not running. Please start the game first.")

    def end_game(self):
        self.is_running = False
        if self.player and self.player.lives > 0 and not self.opponent:
            print("Victory! You defeated the final boss and won the game!")
        else:
            print("Game ended! Better luck next time.")

    def convert_enemy_to_star(self, game):
        if game.is_running:
            game.score += 1
            print(f"Enemy converted to star! Current score: {game.score}")
        else:
            print("Cannot convert enemy to star. The game is not running.")

    def display_score_and_lives(self):
        if self.player:
            print(f"Score: {self.score} | Lives: {self.player.lives}")
        else:
            print("No player assigned to the game.")

    def remove_opponent(self):
        if self.opponent:
            print(f"Opponent {self.opponent.name} defeated!")
            self.opponent = None
            # Logic to spawn the final boss
            print("The final boss appears!")
        else:
            print("No opponent to remove.")

    def handle_enemy_conversion(self):
        if self.is_running and self.player:
            self.convert_enemy_to_star(self)
            if not self.opponent:  # If no opponent, spawn the final boss
                self.spawn_final_boss()
        else:
            print("Cannot handle enemy conversion. Either the game is not running or no player is assigned.")

    def handle_player_hit(self):
        if self.player and self.is_running:
            self.player.lives -= 1
            print(f"Player hit! Lives remaining: {self.player.lives}")
            if self.player.lives <= 0:
                print("Player has no lives left. Game over!")
                self.end_game()
        else:
            print("Cannot handle player hit. Either the game is not running or no player is assigned.")

    def spawn_final_boss(self):
        if self.is_running:
            self.opponent = Player(name="Final Boss", speed=2 * self.player.speed)
            print("The final boss has appeared! It moves twice as fast!")
        else:
            print("Cannot spawn final boss. The game is not running.")
       