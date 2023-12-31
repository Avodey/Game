import pygame
from pygame import Rect

import spritesheet


class Player:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.hitbox = (self.x + 50, self.y, 50, 50)
        Black = (0, 0, 0)

        # Sprites
        sprite_sheet_image = pygame.image.load("Assets/CowBoySheet.png").convert_alpha()
        sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

        # create animation list
        animation_list = []
        animation_steps = [4, 6, 3, 4]
        step_counter = 0

        for animation in animation_steps:
            temp_img_list = []
            for _ in range(animation):
                temp_img_list.append(sprite_sheet.get_image(step_counter, 64, 64, Black))
                step_counter += 1
            animation_list.append(temp_img_list)
            
