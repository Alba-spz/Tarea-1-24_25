from Entity import Entity

class Character(Entity):
    def __init__(self, lives):
        super().__init__()
        self.lives = lives
        self.is_alive = lives > 0

    def move(self, direction):
        """
        Moves the character in the specified direction.
        :param direction: A string indicating the direction ('up', 'down', 'left', 'right').
        """
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
    
    