import math
import random

import pygame
from Bottle import Bottle
from Player import Player
import time

from Shadow import Shadow

pygame.init()

# Set the size of the game window
screen = pygame.display.set_mode((800, 600))

# Name of the game window
pygame.display.set_caption("First Game")

# Timer
timer_font = pygame.font.SysFont('Verdana', 38)
timer_sec = 60
timer_text = timer_font.render(time.strftime('%M:%S', time.gmtime(timer_sec)), True, (255, 255, 255))

# Score code
score = 0
score_increment = 10
font = pygame.font.SysFont('Constansia', 30)
score_text = font.render(f'Score: {score}', True, (0, 255, 0))
angle = 0

# Userevent for timer
timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 1000)  # sets timer with USEREVENT and delay in milliseconds

# Userevent for bottle throw speed
bottleTimer = 0
pygame.time.set_timer(bottleTimer, 1000)  # sets timer with USEREVENT and delay in milliseconds


# Clock to allow for smooth movement
clock = pygame.time.Clock()

# Speed of the player
playerSpeed = 200
bottles = pygame.sprite.Group()
# Loads the player image and the size of the player
playerImage = pygame.transform.scale(pygame.image.load("Assets/Guy.png"), (100, 100))
backgroundImage = pygame.transform.scale(pygame.image.load("Assets/BackgroundV2.png"), (screen.get_width(), screen.get_height()))  # Renders the player
# Initiates 'Player.py' class and its starting location on the screen, x and y
player = Player(1, 1, playerImage)

run = True
while run:  # Checks for the user trying to quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == bottleTimer:
            speed = math.radians(random.randrange(3000, 5000))  # velocity of the throw
            angle = math.radians(random.randrange(15, 45))  # Angle of throw
            startingY = random.randint(1, screen.get_height())

            shadow = Shadow(0, startingY, random.randint(1, 360), time, speed, angle)
            bottle = Bottle(0, startingY, random.randint(1, 360), speed, angle)
            bottles.add(bottle)
            bottles.add(shadow)

        if event.type == timer:  # checks for timer event
            if timer_sec > 0:
                timer_sec -= 1
                timer_text = timer_font.render(time.strftime('%M:%S', time.gmtime(timer_sec)), True, (255, 255, 255))
            else:
                pygame.time.set_timer(timer, 0)  # turns off timer event

                # Merged loops to fix the stuttering FPS clock hence why it's all up here, if you're going to add a new event, add it to this rather than somewhere else in the code for compatability

    """
    To get smooth movement we need to limit screen updating
    to 60 pixels a second which will allow us to make the
    player go whatever speed we want it to.
    """
    timedelta = clock.tick(60)  # Limits screen updating to 60 pixels per second
    timedelta /= 1000  # Converts milliseconds to seconds
    screen.fill((0, 0, 0))

    # Detection of keyboard inputs
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= playerSpeed * timedelta  # x = x - speed * seconds

    if keys[pygame.K_RIGHT]:
        player.x += playerSpeed * timedelta  # x = x + speed * seconds

    if keys[pygame.K_UP]:
        player.y -= playerSpeed * timedelta  # y = y - speed * seconds

    if keys[pygame.K_DOWN]:
        player.y += playerSpeed * timedelta  # y = y + speed * seconds

    screen.fill((0, 0, 0))  # Fills the background screen with black
    screen.blit(backgroundImage, (0, 0))  # Renders the background
    screen.blit(playerImage, (player.x, player.y))  # Renders the player
    bottles.update()  # Draws bottle group
    bottles.draw(screen)  # Updates bottle group
    # add another "if timer_sec > 0" here if you want the timer to disappear after reaching 0
    screen.blit(timer_text, (300, 20))
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.update()  # Updates the screen rendering. Only one is needed at any time.

pygame.quit()
