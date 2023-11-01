import pygame
import random

class Powerup:
    def __init__(self, x, y, length, height, image):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.image = image
        self.image = pygame.transform.scale(image, (length, height))
        self.rect = (self.x + 30, self.y + 30, self.x - 50, self.y - 50)  # Bottle Powerup hitboxes

    def add(self):
        self.x = random.randint(100,700)
        self.y = random.randint(100,500)
        self.rect = (self.x + 30, self.y + 30, self.x - 50, self.y - 50)