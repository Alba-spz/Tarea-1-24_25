class Entity:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        
    def move(self, dx, dy):
        """
        Mueve la entidad por un desplazamiento dado.
        :param dx: Desplazamiento en el eje X.
        :param dy: Desplazamiento en el eje Y.
        """
        self.x += dx
        self.y += dy

    def get_image(self):
        """
        Devuelve la imagen de la entidad.
        """
        return self.image
    
    def set_image(self, image):
        """
        Establece la imagen de la entidad.
        """
        self.image = image

    def draw(self):
        """
        Representa la entidad en la pantalla (simulado con un print).
        """
        print(f"Entity at position ({self.x}, {self.y})")


