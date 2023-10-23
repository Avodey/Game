import pygame
from pygame.locals import *
import sys
import os

pygame.init() #Initialises the program

screen = pygame.display.set_mode((800, 600)) #Setting The Resolution
pygame.display.set_caption('The Good, The Bad And The Drunk') #Gives the application it's window name

background = pygame.image.load('Assets/MainMenu V3.png') #Loads the background

# X, Y, Width, Height area of each button (not relying on an image for optimization and making the code more readable)
start_rect = pygame.Rect(305, 350, 175, 40)
exit_rect = pygame.Rect(305, 448, 175, 40)
setting_rect = pygame.Rect(305, 398, 175, 40)

while True:
    screen.blit(background, (0, 0)) #Allows the screen to appear and set its co-ordinates

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT: #if closed with the X button
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos): #Function for Start Button using collision point   
                pygame.quit() #Quits MainMenu.py
                os.system('python Main.py') #Opens the main game
            elif exit_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
            elif setting_rect.collidepoint(event.pos):
                print("Testing")
                # Not implemented Setting functionality just yet.
