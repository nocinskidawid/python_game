import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """class of one alien ship"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        #alien image load
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #positioning alien in left top corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #alien x position
        self.x = float(self.rect.x)