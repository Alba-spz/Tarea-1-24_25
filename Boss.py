from Opponent import Opponent

class Boss(Opponent):
    def __init__(self, name, health, attack_power, special_attack_power):
        super().__init__(name, health, attack_power)
        self.special_attack_power = special_attack_power

    def attack(self):
        # Boss has a stronger attack
        return self.attack_power * 2

    def special_attack(self):
        # Boss can perform a special attack
        return self.special_attack_power

    def take_damage(self, damage):
        # Boss takes reduced damage
        reduced_damage = damage * 0.75
        return super().take_damage(reduced_damage)

    def __str__(self):
        return f"Boss {self.name}: {self.health} HP, {self.attack_power} Attack, {self.special_attack_power} Special Attack"

# Ejemplo de uso
if __name__ == "__main__":
    boss = Boss("Final Boss", 500, 50, 100)
    print(boss)
    print(boss.attack())
    print(boss.special_attack())
    print(boss.take_damage(100))