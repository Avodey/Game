import pygame 

class Player:
    def __init__(self, x, y, length, height, image):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.image = image
        self.image = pygame.transform.scale(image, (length*5, height*5))

