import math
import random
import pygame

clock = pygame.time.Clock()
# milliseconds since start
NOW_MS = 0
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

class Shadow(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity=0, angle=0):
        pygame.sprite.Sprite.__init__(self)
        self.velocity = velocity  # velocity of the throw
        self.angle = angle
        self.x = x
        self.y = y
        self.image = pygame.Surface((50, 50))
        self.image = pygame.transform.scale(pygame.image.load("Assets/shadow.png"), (50, 50))
        self.rect = self.image.get_rect()
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
            if time_change > 0:
                #  re-calculate the velocity
                half_gravity_time_squared = -9.8 * time_change * time_change / 2.0
                displacement_x = self.velocity * math.sin(self.angle) * time_change
                displacement_y = self.velocity * math.cos(self.angle) * time_change + half_gravity_time_squared
                # reposition sprite
                endshadow = self.y - int(displacement_y)
                self.rect.center = (self.x + int(displacement_x), self.y)
                # Stop at the edge of the window
                if self.rect.y >= WINDOW_HEIGHT:  # Gravity means we only need this for yAxis
                    self.velocity = 0  # This will set the bottle velocity to 0
                    self.kill()  # This will delete the bottle for performance
                if endshadow >= self.y:
                    self.velocity = 0
                    self.kill()