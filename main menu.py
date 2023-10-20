import pygame
from pygame.locals import *
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('The Good, The Bad And The Drunk')

background = pygame.image.load('Assets/background.jpg')
start_button = pygame.image.load('Assets/Alcohol.png')
exit_button = pygame.image.load('Assets/Guy.png')

while True:
    screen.blit(background, (0, 0))
    screen.blit(start_button, (250, 250))
    screen.blit(exit_button, (250, 350))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 250 < x < 550 and 250 < y < 300: # Coordinates of start button
                print("Start button clicked")
                # Add code here to start the game
            elif 250 < x < 550 and 350 < y < 400: # Coordinates of exit button
                print("Exit button clicked")
                pygame.quit()
                sys.exit()