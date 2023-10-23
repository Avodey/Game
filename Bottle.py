import pygame

class Bottle(pygame.sprite.Sprite):
    def __init__(self, col, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50, 50))
            self.image = pygame.transform.scale(pygame.image.load("Assets/Alcohol.png"), (100, 100))
            # self.image.fill(col)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

    def update(self):
            self.rect.move_ip(0, 5)
            # check if sprite has gone off screen
            #if self.rect.top > :
              #  self.kill()