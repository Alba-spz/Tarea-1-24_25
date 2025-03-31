class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

class Opponent(Character):
    def __init__(self, name, health, is_star=False):
        super().__init__(name, health)
        self.is_star = is_star

    def move(self, direction):
        print(f"{self.name} moves {direction}.")

    def shoot(self):
        print(f"{self.name} shoots!")

    def reset(self):
        print(f"{self.name} resets position.")
    
    def serialize(self):
        return {
            "name": self.name,
            "health": self.health,
            "is_star": self.is_star
        }
    
    def deserialize(data):
        return Opponent(data["name"], data["health"], data["is_star"])
    
    def __str__(self):
        return f"{self.name} ({self.health} HP)"