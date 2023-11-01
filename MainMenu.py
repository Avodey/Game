import pygame
from pygame.locals import *
import sys
import os
import time

pygame.init() #Initialises the program

screen = pygame.display.set_mode((800, 600)) #Setting The Resolution
pygame.display.set_caption('The Good, The Bad And The Drunk') #Gives the application it's window name

background = pygame.image.load('Assets/MainMenuV3.png') #Loads the background
settingsbackground = pygame.image.load('Assets/SettingsMenu.png') #Loads the settings background

# X, Y, Width, Height area of each button (not relying on an image for optimization and making the code more readable)
start_rect = pygame.Rect(305, 350, 175, 40)
exit_rect = pygame.Rect(305, 448, 175, 40)
setting_rect = pygame.Rect(305, 398, 175, 40)
#Settings Buttons V
back_rect = pygame.Rect(305, 448, 175, 40)
colour_rect = pygame.Rect(305, 340, 175, 40)

Click = pygame.mixer.Sound("Assets/Click3.mp3") #Gives click the value of that sound, can be called in each button.
MainMenu = pygame.mixer.Sound("Assets/MainMenu.mp3") #Grabs the MainMenu.mp3 and loads it so it can be played once called
screen.blit(background, (0, 0)) #Allows the screen to appear and set its co-ordinates

def HideMain(): #Optimized to make the Settings Button look more optimized
    screen.blit(background, (-15000, -15000)) #Hides the main background image
    screen.blit(settingsbackground, (0, 0)) #Shows the settings background image

def AudioSound(): #Optimized for playing the sound for each button press
    Click.play() #Plays sound effect click
    time.sleep(0.5) #Allows time for the sound effect to play and makes the game feel more premium, letting the player know if they've quit or started the game.

def Exit(): #Optimized so it doesn't need to be written out several times
    pygame.quit() #Quits the python file
    sys.exit() #Ensures it quits

MainMenu.play() #Plays the main menu theme out of the loop to avoid errors
MenuType = True #Variable to switch between Settings Menu and Main Menu

while True:

    pygame.display.update()

    for event in pygame.event.get():
            if event.type == QUIT: #if closed with the X button
                Exit()
            elif event.type == MOUSEBUTTONDOWN: #Makes it so buttons have to be pressed
                if MenuType == True: #Checks if MenuType is true, else go to Settings menu
                    if start_rect.collidepoint(event.pos): #Function for Start Button using collision point 
                        AudioSound() #plays sound effect and adds small delay for a premium feel of the game and allows time for the sound effect to play
                        pygame.mixer.fadeout(1000) #Stops the main menu music playing in game and closes off any extra sound effects by fading out the main menu music making the Cutscene transition seemless
                        os.system('python Cutscene.py') #Opens the cutscene to make it seemless
                        Exit()
                    elif exit_rect.collidepoint(event.pos):
                        AudioSound()
                        Exit() #Exits the application
                    elif setting_rect.collidepoint(event.pos):
                        Click.play() #No need for delay
                        HideMain() #Hides the main menu and displays setting menu
                        MenuType = False #Makes MenuType false which will allow it to go to settings
                        pygame.event.clear
                    
                if MenuType == False: #Checks if MenuType is false, else go to main menu
                    if colour_rect.collidepoint(event.pos):
                        AudioSound()
                        os.system('python ColourBlind.py') #Opens colourblind file
                    if back_rect.collidepoint(event.pos):
                        Click.play() #No need for delay
                        screen.blit(background, (0, 0)) #Displays the main menu
                        MenuType = True #Makes MenuType true to head back to the main menu
