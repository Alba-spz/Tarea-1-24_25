import pygame
class Entity:
    def __init__(self, x, y, width=50, height=50, color=(255, 255, 255)):
        """
        Inicializa la entidad con la posición, dimensiones y color.
        :param x: Posición X en la pantalla.
        :param y: Posición Y en la pantalla.
        :param width: Ancho del rectángulo.
        :param height: Alto del rectángulo.
        :param color: Color del rectángulo (por defecto blanco).
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        
    def move(self, dx, dy):
        """
        Mueve la entidad por un desplazamiento dado.
        :param dx: Desplazamiento en el eje X.
        :param dy: Desplazamiento en el eje Y.
        """
        self.x += dx
        self.y += dy

    def draw(self, screen, color = (255, 255, 255)):
        """
        Dibuja la entidad en la pantalla.
        :param screen: La superficie de Pygame donde se dibuja la entidad.
        :param color: Color de la entidad (por defecto blanco).
        """
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))


