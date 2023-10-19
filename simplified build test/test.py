import time
from datetime import datetime

import pygame
import random
import math
import schedule

# Window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60
clock = pygame.time.Clock()
# milliseconds since start
NOW_MS = 0


class ProjectileSprite(pygame.sprite.Sprite):
    GRAVITY = -9.8

    def __init__(self, bitmap, velocity=0, angle=0):
        pygame.sprite.Sprite.__init__(self)
        self.endPos = random.randint(0, WINDOW_HEIGHT)
        self.velocity = None
        self.image = bitmap
        self.rect = bitmap.get_rect()
        self.start_x = 1
        self.start_y = random.randint(1, WINDOW_HEIGHT)
        self.rect.center = (self.start_x, self.start_y)
        # Physics
        self.setInitialVelocityRadians(velocity, angle)

    def setInitialVelocityRadians(self, velocity, angle_rads):
        global NOW_MS
        self.start_time = NOW_MS
        self.velocity = velocity
        self.angle = angle_rads

    def update(self):
        global NOW_MS
        if self.velocity > 0:
            time_change = (NOW_MS - self.start_time) / 200  # Speed of bottle / gravity
            if time_change > 0:

                # re-calcualte the velocity
                half_gravity_time_squared = self.GRAVITY * time_change * time_change / 2.0
                displacement_x = self.velocity * math.sin(self.angle) * time_change
                displacement_y = self.velocity * math.cos(self.angle) * time_change + half_gravity_time_squared

                # reposition sprite
                self.rect.center = (self.start_x + int(displacement_x), self.start_y - int(displacement_y))

                # Stop at the bottom of the window
                if self.rect.y >= self.endPos:
                    self.velocity = 0
                    self.kill()


### MAIN
pygame.init()
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 1)
pygame.display.set_caption("Projectile Motion Example")

# Load resource image(s)
# sprite_image = pygame.image.load( "Assets/Alcohol.png" )#.convert_alpha()
sprite_image = pygame.transform.scale(pygame.image.load("Assets/Alcohol.png"), (50, 50))

# Make some sprites
NOW_MS = pygame.time.get_ticks()
SPRITES = pygame.sprite.Group()
timedelta = clock.tick(60)  # Limits screen updating to 60 pixels per second
timedelta /= 1000

for i in range(100):  # amount that spawn <----- thing that doesn't work
    speed = math.radians(random.randrange(3000, 5000))  # velocity of the throw
    angle = math.radians(random.randrange(1, 45))  # Angle of throw
    new_sprite = ProjectileSprite(sprite_image, speed, angle)
    SPRITES.add(new_sprite)



done = False
while not done:
    NOW_MS = pygame.time.get_ticks()

    # Handle user-input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Repaint the screen
    WINDOW.fill((0, 255, 0))
    SPRITES.update()  # re-position the sprites
    SPRITES.draw(WINDOW)  # draw the sprites

    pygame.display.flip()
    # Update the window, but not more than 60fps
    clock.tick_busy_loop(FPS)

pygame.quit()
