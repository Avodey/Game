import pygame 

class Bottle:
    def __init__(self, x, y, length, height, image):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.image = image

        # Initializing surface
        surface = pygame.display.set_mode((400, 300))

        # Initializing Color
        color = (255, 0, 0)

        self.image = pygame.transform.scale(image, (length, height))
    