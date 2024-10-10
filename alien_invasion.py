import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """main class to run the game and manage resources"""

    def __init__(self):
        """game and resources initialization"""
        pygame.init()
        self.settings = Settings()

        #display settings windowed
        self.screen = pygame.display.set_mode(
                       (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        #display settings fullscreen
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        #pygame.display.set_caption('Alien Invasion')

        #background color
        self.bg_color = self.settings.bg_color

        #creating player ship instance
        self.ship = Ship(self)

        #bullet group
        self.bullets = pygame.sprite.Group()

    def _check_events(self):
        """method to deal with events in game"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """method to deal with keydown events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """method to deal with keyup events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_bullets(self):
        """updating bullets and deleting off screen bullets"""
        #bullets updating
        self.bullets.update()

        #deleting off screen bullets
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <=0:
                    self.bullets.remove(bullet)

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.biltme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # screen refreshing in every frame
        pygame.display.flip()

    def _fire_bullet(self):
        """creating new bullet and adding it into group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def run_game(self):
        """main game loop start"""
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            self._update_bullets()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()