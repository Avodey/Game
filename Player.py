import pygame
import spritesheet

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Black = (0, 0, 0)

        # Sprites
        sprite_sheet_image = pygame.image.load("Assets/CowBoySheet.png").convert_alpha()
        sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

        # create animation list
        animation_list = []
        animation_steps = [4, 6, 3, 4]
        action = 0
        last_update = pygame.time.get_ticks()
        animation_cooldown = 300
        frame = 0
        step_counter = 0

        for animation in animation_steps:
            temp_img_list = []
            for _ in range(animation):
                temp_img_list.append(sprite_sheet.get_image(step_counter, 64, 64, Black))
                step_counter += 1
            animation_list.append(temp_img_list)
            
            
            