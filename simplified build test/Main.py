import os
# Import and initialize the pygame library
import pygame
from Player import Player
from Bottle import Bottle

# define colours
white = (255, 255, 255)

def main():
    pygame.init()

    # Set 'constants' for max X and Y size for the drawing window
    screen_length = 600
    screen_height = 800

    screen = pygame.display.set_mode((screen_height, screen_length))

    # define fonts (though unused in this version)
    font30 = pygame.font.SysFont('Constantia', 30)
    font40 = pygame.font.SysFont('Constantia', 40)

    # Background image
    bg = pygame.image.load("Assets/TempBackgr.png")

    # 1.0 instantiate Player class
    player = Player((screen_height / 2) - (35 / 2), (screen_length - 100), 175, 150, pygame.image.load("Assets/Guy.png"))
    player.x = 1 #<-- Starting X position of the player
    player.y = 1 #<-- Starting Y position of the player
    #^ we could potentially make this have different starting positions for the player per level
    # Main loop
    running = True
    while running:
        keys = pygame.key.get_pressed()

        # 2.0 movement system, now with diagonal movement
        if keys[pygame.K_LEFT]:
            player.x -= 1.35
        if keys[pygame.K_RIGHT]:
            player.x += 1.35
        if keys[pygame.K_UP]:
            player.y -= 1.35
        if keys[pygame.K_DOWN]:
            player.y += 1.35

        # Handle events
        for event in pygame.event.get(): #removed display.set_mode as it was causing the flickering issues
            # Did the user click the window close button?
            if event.type == pygame.QUIT:
                running = False

        # Fills the screen with background image
        screen.blit(bg, (0, 0))

        # Draw the player
        screen.blit(player.image, (player.x, player.y))

        # Update the screen (Flip the display)
        pygame.display.flip()

    # End
    pygame.quit()

if __name__ == "__main__":
    run = main()
    run
