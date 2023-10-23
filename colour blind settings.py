import pygame
import sys

# Initialize Pygame
pygame.init()

# Colors for different types of color blindness
protanopia_colors = [(213, 255, 0), (0, 100, 17), (255, 102, 0)]
deuteranopia_colors = [(110, 130, 225), (102, 11, 200), (119, 136, 181)]
tritanopia_colors = [(255, 114, 0), (200, 111, 0), (120, 220, 120)]

# Default settings
color_blindness_type = "normal"
color_blindness_colors = []

def main():
    global color_blindness_type, color_blindness_colors

    # Set up the display
    screen = pygame.display.set_mode((300, 200))

    # Main event loop
    while True:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Change the color blindness type
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    color_blindness_type = "protanopia"
                    color_blindness_colors = protanopia_colors
                elif event.key == pygame.K_d:
                    color_blindness_type = "deuteranopia"
                    color_blindness_colors = deuteranopia_colors
                elif event.key == pygame.K_t:
                    color_blindness_type = "tritanopia"
                    color_blindness_colors = tritanopia_colors
                