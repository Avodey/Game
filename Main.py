import math
import random
import time
from Powerup import Powerup
import pygame
from pygame import Rect
from Bottle import Bottle
from Player import Player
import spritesheet
from Shadow import Shadow
import os

pygame.init()
screen_width = 600
screen_height = 800
# Set the size of the game window
screen = pygame.display.set_mode((screen_height, screen_width))

# Name of the game window
pygame.display.set_caption("The Good, The Bad and The Drunk")

# Icon image
new_icon = pygame.image.load("Assets/cowboy_v2.png")
pygame.display.set_icon(new_icon)

# Music
MainMusic = pygame.mixer.Sound("Assets/MainMusic.mp3")
MainMusic.play()

# Sprites
sprite_sheet_image = pygame.image.load("Assets/CowBoySheet.png").convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
Black = (0, 0, 0)

# create animation list
animation_list = []
animation_steps = [4, 6, 3, 4]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 300
frame = 0
step_counter = 0
health = 3

ended = False  # for the variable to go back to the main menu

player_hit = False
FLOOR_HEIGHT = 50
floor_y_position = screen_height - FLOOR_HEIGHT

for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, 64, 64, Black))
        step_counter += 1
    animation_list.append(temp_img_list)

# Timer
timer_font = pygame.font.SysFont('Verdana', 38)
timer_sec = 60
timer_text = timer_font.render(time.strftime('%M:%S', time.gmtime(timer_sec)), True, (255, 255, 255))

# Score code
score = 0
score_increment = 10
font = pygame.font.SysFont('Constansia', 30)
bigfont = pygame.font.SysFont('Constansia', 130)
angle = 0

# Userevent for timer2
timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 1000)  # sets timer with USEREVENT and delay in milliseconds

# Userevent for bottle throw speed
bottleTimer = 0
pygame.time.set_timer(bottleTimer, 300)  # sets timer with USEREVENT and delay in milliseconds

# Clock to allow for smooth movement
clock = pygame.time.Clock()

# Speed of the player
playerSpeed = 200
bottles = pygame.sprite.Group()
# Loads the player image and the size of the player
playerImage = pygame.transform.scale(pygame.image.load("Assets/Guy.png"), (100, 100))
backgroundImage = pygame.transform.scale(pygame.image.load("Assets/BackgroundV2.png"),
                                         (screen.get_width(), screen.get_height()))

powerup = Powerup(100, 100, 100, 100, pygame.image.load("Assets/PowerUp.png"))

drunk_increase = 0  # Creates the variable and value for the drunk increase
drunkenness = 0  # Creates the drunkness value
last_drunkenness_update = pygame.time.get_ticks()
drunkenness_cooldown = 3000  # Cooldown for the drunkness (needs fixing ASAP)

# backgroundImage.fill(((213, 255, 0), (0, 100, 17), (255, 102, 0)) + (0,), None, pygame.BLEND_RGBA_ADD) # COLORBLIND ACCESSABILITY CONCEPT - DO NOT DELETE
# Initiates 'Player.py' class and its starting location on the screen, x and y
player = Player(screen, screen.get_width() / 2, screen.get_height() / 2)  # Spawns player in the middle of the screen
run = True
while run:  # Checks for the user trying to quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == bottleTimer:
            speed = math.radians(random.randrange(3000, 5000))  # velocity of the throw
            angle = math.radians(random.randrange(15, 45))  # Angle of the throw
            startingY = random.randint(1, screen.get_height())  # Picks a random height to spawn in the bottle
            shadow = Shadow(0, startingY, speed, angle)  # New shadow class under the bottle class
            bottle = Bottle(0, startingY, random.randrange(1, 360), screen, speed,
                            angle)  # New random bottle class above the shadow class
            if health <= 0 or timer_sec <= 0:
                pass
            else:
                bottles.add(shadow)  # Spawns in a shadow
                bottles.add(bottle)  # Spawns in a bottle

        if event.type == timer:  # checks for timer event
            if timer_sec > 0:
                score += 5
                timer_sec -= 1
                timer_text = timer_font.render(time.strftime('%M:%S', time.gmtime(timer_sec)), True, (255, 255, 255))
            else:
                pygame.time.set_timer(timer, 0)  # turns off timer event

                # Merged loops to fix the stuttering FPS clock hence why it's all up here, if you're going to add a new event, add it to this rather than somewhere else in the code for compatability
    # update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list):
            frame = 0
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
        if player_rect.left <= 0:
            pass
        else:
            player.x -= playerSpeed * timedelta  # x = x - speed * seconds
    if keys[pygame.K_RIGHT]:
        if player_rect.right >= 800:
            pass
        else:
            player.x += playerSpeed * timedelta  # x = x + speed * seconds

    if keys[pygame.K_UP]:
        if player_rect.top <= 0:
            pass
        else:
            player.y -= playerSpeed * timedelta  # y = y - speed * seconds

    if keys[pygame.K_DOWN]:
        if player_rect.bottom >= 600:
            pass
        else:
            player.y += playerSpeed * timedelta  # y = y + speed * seconds

    screen.fill((0, 0, 0))  # Fills the background screen with black
    screen.blit(backgroundImage, (0, 0))  # Renders the background
    screen.blit(animation_list[action][frame], (player.x, player.y))
    bottles.update()  # Draws bottle group
    bottles.draw(screen)  # Updates bottle group
    player_rect = Rect(player.x + 10, player.y, 45, 70)
    #  pygame.draw.rect(screen, (255, 0, 0), player_rect, 2)

    for bottle in bottles.sprites():
        if isinstance(bottle, Bottle):
            if not player_hit and player_rect.colliderect(bottle.rect):
                # Check if the bottle is above the floor before considering it a player hit
                if floor_y_position > bottle.rect.bottom >= bottle.y - 10:
                    player_hit = True
                    health -= 1
                    break  # Exit the loop
            if not player_hit and player_rect.colliderect(powerup.rect):
                player_hit = True
                score += 10
                timer_sec += 2
                drunk_increase += 1  # Increases 1 to the drunkness counter which increases the player random movement
                drunkenness += drunk_increase
                powerup.add()
                break  # Exit the loop

    if player_hit:
        # Perform actions for when the player is hit.
        bottle.kill()
        shadow.kill()
        player_hit = False  # Reset the flag
    screen.blit(powerup.image, (powerup.x, powerup.y))  # Powerup image renderer
    screen.blit(timer_text, (300, 20))  # Timer Text
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    healthtext = font.render(f'Health: {health}/3', True, (255, 102, 25))
    gameover = bigfont.render(f'Game Over', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(healthtext, (50, screen.get_height() - 65))
    if health <= 0 or timer_sec <= 0: # If health is zero or time runs out
        timer_sec = 0
        screen.blit(gameover, (
            screen.get_width() / 2 - gameover.get_width() / 2, screen.get_height() / 2 - gameover.get_height() / 2))
        ended = True  # allows all other functionality with the ending screen to play out
    pygame.display.update()  # Updates the screen rendering. Only one is needed at any time.
    if ended == True:  # Allows pygame.display to update
        time.sleep(1)  # waits 1 second
        pygame.mixer.fadeout(1000)  # fades the music out
        os.system('python NextMainMenu.py')  # goes back to home screen
        pygame.quit()

    if drunkenness > 0:
        current_time = pygame.time.get_ticks()
    if current_time - last_drunkenness_update >= drunkenness_cooldown:  # Using previously declared delay to ensure that the drunkness deducter won't just make the player never drunk
        drunkenness -= 1  # Deducts -1 drunk status from the counter over time to make the game more fair for the player ensuring they balance time with points/drunkness
        last_drunkenness_update = current_time
        print(
            drunkenness)  # Just a testing line to see the current status of the drunk level, the higher the number the quicker the random movements.

    if random.random() < (1 * drunkenness):  # adjust probability based on drunkenness level
        directions = [(-2, 0), (2, 0), (0, -2), (
        0, 2)]  # Each direction and the speed on which it goes (set it to 2 as it adds more dramatic effect.)
        dx, dy = random.choice(directions)  # randomizes directions
        player.x += dx * (playerSpeed * timedelta)  # X direction
        player.y += dy * (playerSpeed * timedelta)  # Y direction

pygame.quit()
