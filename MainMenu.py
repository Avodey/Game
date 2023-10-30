import pygame
from pygame.locals import *
import sys
import os
import time

pygame.init() #Initialises the program

screen = pygame.display.set_mode((800, 600)) #Setting The Resolution
pygame.display.set_caption('The Good, The Bad And The Drunk') #Gives the application it's window name

background = pygame.image.load('Assets/MainMenu V3.png') #Loads the background
settingsbackground = pygame.image.load('Assets/Main Menu V2.png')

# X, Y, Width, Height area of each button (not relying on an image for optimization and making the code more readable)
start_rect = pygame.Rect(305, 350, 175, 40)
exit_rect = pygame.Rect(305, 448, 175, 40)
setting_rect = pygame.Rect(305, 398, 175, 40)

Click = pygame.mixer.Sound("Assets/Click3.mp3") #Gives click the value of that sound, can be called in each button.
numtest = True
screen.blit(background, (0, 0)) #Allows the screen to appear and set its co-ordinates

def HideMain(): #Optimized to make the Settings Button look more optimized
    screen.blit(background, (-500, -150))
    screen.blit(settingsbackground, (0, 0))

def AudioSound(): #Optimized for playing the sound for each button press
    Click.play() #Plays sound effect click
    time.sleep(0.5) #Gives time for the sound effect to play and makes it feel more premium

def Exit(): #Optimized so it doesn't need to be written out several times
    pygame.quit() #Quits the python file
    sys.exit() #Ensures it quits

while True:

    pygame.display.update()

    for event in pygame.event.get():
        if numtest == True:
            if event.type == QUIT: #if closed with the X button
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos): #Function for Start Button using collision point 
                    AudioSound()
                    os.system('python Main.py') #Opens the main game
                elif exit_rect.collidepoint(event.pos):
                    AudioSound()
                    Exit()
                elif setting_rect.collidepoint(event.pos):
                    AudioSound()
                    numtest = False
                    HideMain()
                    # Not implemented Setting functionality just yet.

    else: #Settings options if numtest is false
        if event.type == QUIT:
                Exit()
        elif event.type == MOUSEBUTTONDOWN and setting_rect.collidepoint(event.pos):
                numtest = True #This will call back to the primary function as it changes numtest to true which brings you back to the main screen.
                screen.blit(background, (0, 0))
