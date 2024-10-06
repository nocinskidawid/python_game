import pygame

class Ship:
    def __init__(self, ai_game):
        """class to manage ship controlled by player"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #loading ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #ship appearing at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def biltme(self):
        """ship displaying in its actual position"""
        self.screen.blit(self.image, self.rect)