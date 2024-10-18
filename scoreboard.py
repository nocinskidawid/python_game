import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    """class to show player score in real time"""

    def __init__(self, aigame):
        self.ai_game=aigame
        self.screen = aigame.screen
        self.screen_rect = self.screen.get_rect()
        self.setings = aigame.settings
        self.stats=aigame.stats

        #score font color
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_ships()

    def prep_score(self):
        """converting score number into image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "SCORE:"+"{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,
            self.text_color, self.setings.bg_color)
        
        #displaying score in top right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """converting high score into image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "HIGH SCORE: "+"{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True,
            self.text_color, self.setings.bg_color)
        
        #displaying score in top right corner
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game, 0)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def check_high_score(self):
        if self.stats.score>self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """displaying score on screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.ships.draw(self.screen)