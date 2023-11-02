import math
import pygame

clock = pygame.time.Clock()
CurrentMS = 0
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
        global CurrentMS
        self.startTime = CurrentMS
        self.velocity = velocity
        self.angle = angle_rads

    def update(self):
        global CurrentMS
        if self.velocity > 0:
            CurrentMS = pygame.time.get_ticks()
            timechanged = (CurrentMS - self.startTime) / 200  # Gravity of the bottle
            if timechanged > 0:
                #  re-calculate the velocity
                half_gravity_time_squared = -9.8 * timechanged * timechanged / 2.0
                displacementx = self.velocity * math.sin(self.angle) * timechanged
                displacementy = self.velocity * math.cos(self.angle) * timechanged + half_gravity_time_squared
                # reposition sprite
                endshadow = self.y - int(displacementy)
                shadowsize = self.y - endshadow + 20
                if shadowsize < 0:  # Prevents negative int from crashing the game
                    shadowsize = 0
                self.image = pygame.transform.scale(pygame.image.load("Assets/shadow.png"),
                                                    (shadowsize, shadowsize))
                self.rect.center = (self.x + int(displacementx), self.y)
                # Stop at the edge of the window
                if self.rect.y >= WINDOW_HEIGHT:  # Gravity means we only need this for yAxis
                    self.velocity = 0  # This will set the bottle velocity to 0
                    self.kill()  # This will delete the bottle for performance
                if endshadow >= self.y:
                    self.velocity = 0
                    self.kill()
