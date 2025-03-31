class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        """
        Mueve la entidad por un desplazamiento dado.
        :param dx: Desplazamiento en el eje X.
        :param dy: Desplazamiento en el eje Y.
        """
        self.x += dx
        self.y += dy

    def draw(self):
        """
        Representa la entidad en la pantalla (simulado con un print).
        """
        print(f"Entity at position ({self.x}, {self.y})")

    def update(self):
        print("Entity updated")
    def get_position(self):
        return self.x, self.y
    def set_position(self, x, y):
        self.x = x
        self.y = y
    

# Ejemplo de uso
if __name__ == "__main__":
    entity = Entity(0, 0)
    entity.draw()
    entity.move(5, 3)
    entity.draw()