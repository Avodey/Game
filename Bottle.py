import pygame


class Bottle:
    def __init__(self, x, y, length, height, image):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.image = image
        self.image = pygame.transform.scale(image, (length, height))
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)