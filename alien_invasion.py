import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """main class to run the game and manage resources"""

    def __init__(self):
        """game and resources initialization"""
        pygame.init()
        self.settings = Settings()

        #display settings
        self.screen = pygame.display.set_mode(
                       (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        #background color
        self.bg_color = (120,120,120)

        #creating player ship instance
        self.ship = Ship(self)

    def run_game(self):
        """main game loop start"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.ship.biltme()

            # screen refreshing in every frame
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()