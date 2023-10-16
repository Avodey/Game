import os
# Import and initialize the pygame library
import pygame
from Player import Player
from Bottle import Bottle

pygame.init()

# Set 'constants' for max X and Y size for the drawing window
SCREEN_X = 500
SCREEN_Y = 700
screen = pygame.display.set_mode([SCREEN_X, SCREEN_Y])

# 1.0 instantiate Player class
player = Player((SCREEN_X/2)-(35/2), (SCREEN_Y - 100), 35, 30, pygame.image.load("Assets/Guy.png"))

# 1.1 instantiate Bottle class
bottle = Bottle(50, 100, 30, 30, pygame.image.load("Assets/Alcohol.png"))

# Fill the background with black
screen.fill((0, 0, 0))


# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #1.0 detect keypress
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            #screen.blit(player.img, (player.x, player.y)) 
            player.x -= 0.15
            
        if event.key == pygame.K_RIGHT:
            player.x += 0.15
    
    screen.blit(player.image, (player.x, player.y))
    
    # Flip the display
    pygame.display.flip()

# End
pygame.quit()