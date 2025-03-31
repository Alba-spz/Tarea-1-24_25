from Entity import Entity

class Shot(Entity):
    def __init__(self, x, y, speed):
        super().__init__(x, y)
        self.speed = speed
        self.is_alive = True
        self.width = 1
        self.height = 1
        self.damage = 1

    def move(self):
        """Moves the shot upwards by its speed."""
        self.y -= self.speed

    def hit_target(self, target):
        """
        Checks if the shot hits a target.
        :param target: An object with x, y, width, and height attributes.
        :return: True if the shot hits the target, False otherwise.
        """
        return (self.x >= target.x and self.x <= target.x + target.width and
                self.y >= target.y and self.y <= target.y + target.height)
    
    def serialize(self):
        return {
            "x": self.x,
            "y": self.y,
            "speed": self.speed,
            "is_alive": self.is_alive
        }