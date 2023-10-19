import pygame
from Player import Player

pygame.init()
# Set the size of the game window
screen = pygame.display.set_mode((800, 600))
# Name of the game window
pygame.display.set_caption("First Game")
#  Clock to allow for smooth movement
clock = pygame.time.Clock()
# Speed of the player
playerSpeed = 200
# Loads the player image and the size of the player
playerImage = pygame.transform.scale(pygame.image.load("Assets/Guy.png"), (100, 100))
backgroundImage = pygame.transform.scale(pygame.image.load("Assets/TempBackgr.png"), (screen.get_width(), screen.get_height()))  # Renders the player

# Initiates 'Player.py' class and its starting location on the screen, x and y
player = Player(1, 1, playerImage)

run = True
while run:  # Checks for the user trying to quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    """
    To get smooth movement we need to limit screen updating
    to 60 pixels a second which will allow us to make the
    player go whatever speed we want it to.
    """
    timedelta = clock.tick(60)  # Limits screen updating to 60 pixels per second
    timedelta /= 1000  # Converts milliseconds to seconds

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

    pygame.display.update()  # Updates the screen rendering. Only one is needed at any time.

pygame.quit()
