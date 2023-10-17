import os
# Import and initialize the pygame library
import pygame
from Player import Player
from Bottle import Bottle



#define colours
white = (255, 255, 255)


def main():
    pygame.init()
    #define fonts
    font30 = pygame.font.SysFont('Constantia', 30)
    font40 = pygame.font.SysFont('Constantia', 40)

    # Set 'constants' for max X and Y size for the drawing window
    screen_length = 600
    screen_height = 800

    screen = pygame.display.set_mode((screen_height, screen_length))

        #defne function for creating text
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    #define game variables
    countdown = 3
    last_count = pygame.time.get_ticks()

    #countdown code
    if countdown > 0:
        draw_text('GET READY!', font40, white, (screen_height / 2 - 110), int(screen_length / 2 + 50))
        draw_text(str(countdown), font40, white, int(screen_height / 2 - 10), int(screen_length / 2 + 110))
        count_timer = pygame.time.get_ticks()
        if count_timer - last_count > 1000:
            countdown -= 1
            last_count = count_timer
            
    # 1.0 instantiate Player class
    player = Player((screen_height / 2) - (35 / 2), (screen_length - 100), 350, 300, pygame.image.load("Assets/Guy.png"))
    player.x = 1
    player.y = 1
    # 1.1 instantiate Bottle class
    bottle = Bottle(50, 100, 30, 30, pygame.image.load("Assets/Alcohol.png"))

    # Background image
    bg = pygame.image.load("Assets/TempBackgr.png")
 
    
    # Run until the user asks to quit
    running = True
    while running:
        screen.blit(bg, (0, 0))  # Fills the screen with black

        screen.blit(player.image, (player.x, player.y))

        player.__init__(player.x, player.y, 100, 110, player.image)

        # pygame.draw.rect(screen, (0, 255, 0), (player.x, 20, 20, 20))
        # pygame.display.update()

        # Did the user click the window close button?
        for event in pygame.event.get():
            screen = pygame.display.set_mode((screen_height, screen_length))
            if event.type == pygame.QUIT:
                running = False

        # 1.0 detect keypress
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # screen.blit(player.image, (player.x, player.y))
                player.x -= 1.35
            if event.key == pygame.K_RIGHT:
                # screen.blit(player.image, (player.x, player.y))
                player.x += 1.35
            if event.key == pygame.K_UP:
                # screen.blit(player.image, (player.x, player.y))
                player.y -= 1.35
            if event.key == pygame.K_DOWN:
                # screen.blit(player.image, (player.x, player.y))
                player.y += 1.35



        # Flip the display
        pygame.display.flip()

    # End
    pygame.quit()

if __name__ == "__main__":
    run = main()
    run