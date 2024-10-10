import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """class to menage bullets fired by player"""

    def __init__(self, ai_game):
        """creating bullet on ship position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        #creating bullet on (0,0), then moving it
        #to ship position

        self.rect = pygame.Rect(0,0,
                                self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #bullet y position as float number
        self.y = float(self.rect.y)

    def update(self):
        """bullet movement"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """displaying bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)