import math
import random
import pygame
from pygame import Rect

clock = pygame.time.Clock()
# milliseconds since start
NOW_MS = 0
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


class Bottle(pygame.sprite.Sprite):
    def __init__(self, x, y, randomrotation, screen, velocity=0, angle=0):
        pygame.sprite.Sprite.__init__(self)
        self.velocity = velocity  # velocity of the throw
        self.angle = angle
        self.x = x
        self.screen = screen
        self.randomrotation = randomrotation
        self.y = y
        self.image = pygame.Surface((50, 50))
        self.image = [pygame.transform.scale(pygame.image.load("Assets/Alcohol.png"), (50, 50)),
                      pygame.transform.scale(pygame.image.load("Assets/AlcoholBlue.png"), (50, 50)),
                      pygame.transform.scale(pygame.image.load("Assets/AlcoholClear.png"), (50, 50)),
                      pygame.transform.scale(pygame.image.load("Assets/AlcoholGreen.png"), (50, 50)),
                      pygame.transform.scale(pygame.image.load("Assets/AlcoholWhite.png"), (50, 50))]
        self.image = self.image[random.randint(0, 4)]
        self.rect = self.image.get_rect()

        self.hitbox = (self.x + 50, self.y, 50, 50)
        self.image = pygame.transform.rotate(self.image, randomrotation)
        self.rect.center = (1, self.y)
        self.setInitialVelocityRadians(velocity, angle)

    def setInitialVelocityRadians(self, velocity, angle_rads):
        global NOW_MS
        self.start_time = NOW_MS
        self.velocity = velocity
        self.angle = angle_rads

    def update(self):
        global NOW_MS
        if self.velocity > 0:
            NOW_MS = pygame.time.get_ticks()

            time_change = (NOW_MS - self.start_time) / 200  # Gravity of the bottle (probably don't change)
            self.randomrotation += 100
            if time_change > 0:
                #  re-calculate the velocity
                half_gravity_time_squared = -9.8 * time_change * time_change / 2.0
                displacement_x = self.velocity * math.sin(self.angle) * time_change
                displacement_y = self.velocity * math.cos(self.angle) * time_change + half_gravity_time_squared
                # reposition sprite
                self.rect.center = (self.x + int(displacement_x), self.y - int(displacement_y))
                if self.y-displacement_y > self.y-55:
                    bottle_rect = Rect(displacement_x-10, self.y-displacement_y-10, 40, 40)
                    pygame.draw.rect(self.screen, (255, 0, 0), bottle_rect, 2)
                # Stop at the edge of the window
                if self.rect.y >= WINDOW_HEIGHT:  # Gravity means we only need this for yAxis
                    self.velocity = 0  # This will set the bottle velocity to 0
                    self.kill()  # This will delete the bottle at the bottom of the screen for performance
                if self.rect.y >= self.y-15:
                    self.velocity = 0
                    self.kill()  # This will delete the on the ground
