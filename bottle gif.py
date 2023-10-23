import pygame
import os
from PIL import Image

pygame.init()

sprite1 = pygame.image.load('bottle1.png')
sprite2 = pygame.image.load('bottle2.png')

def save_surface_to_gif(surface, file_name):
    pygame.image.save(surface, file_name)

    img = Image.open(file_name)
    img.save(file_name, save_all=True, append_images=[img]*99, duration=100, loop=0)

    os.remove(file_name)

    def update_display(surface, clock):
    pygame.display.flip()
    clock.tick(4)

    # Create a surface to draw on
surface = pygame.Surface((100, 100))

# Create a clock object
clock = pygame.time.Clock()

# Animation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the sprite on the surface
    surface.blit(sprite1, (0, 0))
    update_display(surface, clock)

    # Save the surface to a gif file
    save_surface_to_gif(surface, 'animation.gif')

    # Change the sprite to simulate the animation
    sprite1 = sprite2

pygame.quit()