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
        print("Game ended!")
        # Lógica para finalizar el juego, como mostrar el puntaje final


# Ejemplo de uso
if __name__ == "__main__":
    game = Game()
    game.start()
    game.update()
    game.end_game()