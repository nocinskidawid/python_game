import pygame.font

class Scoreboard:
    """class to show player score in real time"""

    def __init__(self, aigame):
        self.screen = aigame.screen
        self.screen_rect = self.screen.get_rect()
        self.setings = aigame.settings
        self.stats=aigame.stats

        #score font color
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        """converting score number into image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,
            self.text_color, self.setings.bg_color)
        
        #displaying score in top right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """displaying score on screen"""
        self.screen.blit(self.score_image, self.score_rect)