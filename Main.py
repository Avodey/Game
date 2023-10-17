import os
# Import and initialize the pygame library
import pygame
from Player import Player
from Bottle import Bottle

def main():
    pygame.init()

    # Set 'constants' for max X and Y size for the drawing window
    SCREEN_X = 800
    SCREEN_Y = 600

    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))

    # 1.0 instantiate Player class
    player = Player((SCREEN_X / 2) - (35 / 2), (SCREEN_Y - 100), 350, 300, pygame.image.load("Assets/Guy.png"))
    player.x = 1
    player.y = 1
    # 1.1 instantiate Bottle class
    bottle = Bottle(50, 100, 30, 30, pygame.image.load("Assets/Alcohol.png"))

    # Fill the background with black

    # Run until the user asks to quit
    running = True
    while running:
        screen.fill((0, 0, 0))  # Fills the screen with black

        screen.blit(player.image, (player.x, player.y))

        player.__init__(player.x, player.y, 100, 110, player.image)

        # pygame.draw.rect(screen, (0, 255, 0), (player.x, 20, 20, 20))
        # pygame.display.update()

        # Did the user click the window close button?
        for event in pygame.event.get():
            screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
            if event.type == pygame.QUIT:
                running = False

        # 1.0 detect keypress
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # screen.blit(player.image, (player.x, player.y))
                player.x -= 0.35
            if event.key == pygame.K_RIGHT:
                # screen.blit(player.image, (player.x, player.y))
                player.x += 0.35
            if event.key == pygame.K_UP:
                # screen.blit(player.image, (player.x, player.y))
                player.y -= 0.35

            if event.key == pygame.K_DOWN:
                # screen.blit(player.image, (player.x, player.y))
                player.y += 0.35



        # Flip the display
        pygame.display.flip()

    # End
    pygame.quit()

if __name__ == "__main__":
    run = main()
    run