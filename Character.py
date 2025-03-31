from Entity import Entity

class Character(Entity):
    def __init__(self, name, position, health):
        super().__init__(name, position, health)

    def move(self, direction, distance):
        """
        Moves the character in the specified direction by the given distance.
        :param direction: A tuple (dx, dy) representing the direction vector.
        :param distance: A float representing the distance to move.
        """
        dx, dy = direction
        self.position = (self.position[0] + dx * distance, self.position[1] + dy * distance)

    def shoot(self, target):
        """
        Simulates shooting at a target.
        :param target: The target entity to shoot at.
        """
        print(f"{self.name} shoots at {target.name}!")

    def collide(self, other):
        """
        Handles collision with another entity.
        :param other: The other entity involved in the collision.
        """
        print(f"{self.name} collides with {other.name}!")
        self.health -= 10  # Example: reduce health on collision
    
    def reset(self):
        """
        Resets the character's position to the origin.
        """
        self.position = (0, 0)
    
    