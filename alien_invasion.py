import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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

        #creating alien fleet
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

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
        
        #displaying bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #displaying aliens
        self.aliens.draw(self.screen)

        # screen refreshing in every frame
        pygame.display.flip()

    def _fire_bullet(self):
        """creating new bullet and adding it into group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """creating alein fleet"""

        alien = Alien(self)
        #number of aliens in row
        alien_width, alien_height=alien.rect.size
        avaliable_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = avaliable_space_x//(2*alien_width)

        #number of aliens rows
        ship_height = self.ship.rect.height
        avaliable_space_y = (self.settings.screen_height - (3*alien_width) - ship_height)
        number_rows = avaliable_space_y // (2*alien_height)

        #creating alien fleet
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                #creating one alien in row
                self._crate_alien(alien_number,row_number)

    def _crate_alien(self, alien_number,row_number):
        alien = Alien(self)
        alien_width=alien.rect.width
        alien.x = alien_width+2*alien_width*alien_number
        alien.rect.x=alien.x
        alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
        self.aliens.add(alien)
        

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