import pygame

from settings import Settings

class Ship:
    def __init__(self, ai_game):
        """class to manage ship controlled by player"""
        self.settings = Settings()

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #loading ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #ship appearing at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #ship position stored as float number
        self.x = float(self.rect.x)

        #ship movement control
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ship position update on player input"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        #ship rect update based on ship position update
        self.rect.x = self.x

    def biltme(self):
        """ship displaying in its actual position"""
        self.screen.blit(self.image, self.rect)