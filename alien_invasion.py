import sys
from time import sleep
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

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

        #creating game stats and scoreboard instance
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        #creating player ship instance
        self.ship = Ship(self)

        #creating alien fleet
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        #crating start button
        self.play_button=Button(self,self.screen,'play')

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """starting new game after clicking play button"""
        if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
            self._start_game()        

    def _start_game(self):
        self.stats.reset_stats()
        self.stats.game_active = True

        self.sb.prep_score()

        self.aliens.empty()
        self.bullets.empty()

        self._create_fleet()
        self.ship.center_ship()

        self.settings.initialize_dynamic_settings()

        pygame.mouse.set_visible(False)

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
        elif event.key == pygame.K_RETURN:
            self._start_game()

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

        self._check_bullet_alien_colision()

    def _check_bullet_alien_colision(self):
        #checking bullets colisions
        colisions = pygame.sprite.groupcollide(
            self.bullets,self.aliens,True,True)
        
        if colisions:
            for aliens in colisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()

        if not self.aliens:
            #creating new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.biltme()
        
        #displaying bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #displaying aliens
        self.aliens.draw(self.screen)

        #displaying score
        self.sb.show_score()

        #displaying start button if game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

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

    def _update_aliens(self):
        """updating aliens position"""
        self._check_fleet_edges()
        self.aliens.update()

        #ship-alien colision check
        if pygame.sprite.spritecollide(self.ship,self.aliens,False):
            self._ship_hit()

        #alien-screen bottom colision check
        self._check_alien_bottom()

    def _ship_hit(self):

        if self.stats.ships_left>0:

            #changing ships_left after hit
            self.stats.ships_left-=1

            #deleting items in lists
            self.aliens.empty()
            self.bullets.empty()

            #creating new fleet and ship
            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.stats.game_active=False
            ##sys.exit()
            pygame.mouse.set_visible(True)


    def _check_alien_bottom(self):
        """if alien gets to screen bottom"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >=screen_rect.bottom:
                self._ship_hit()
                break
        
    def _check_fleet_edges(self):
        """when alien reach screen edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """moving fleet down and changing direction"""
        for alien in self.aliens.sprites():
            alien.rect.y+=self.settings.fleet_drop_speed
        self.settings.fleet_direction*=-1

    def run_game(self):
        """main game loop start"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()