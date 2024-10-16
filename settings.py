class Settings:
    def __init__(self):
        """game settings initialization"""

        #screen settings
        self.screen_width = 1600
        self.screen_height = 989
        self.bg_color = (120,120,120)

        #ship movement settings
        #self.ship_speed = 0.9
        self.ship_limit=3

        #bullets settings
        #self.bullet_speed=1.0
        self.bullet_width=3
        self.bullet_height=15
        self.bullets_allowed=3
        self.bullet_color=(60,60,60)

        #aliens settings
        #self.alien_speed=0.5
        self.fleet_drop_speed=5
        #fleet direction 1=right -1=left
        self.fleet_direction=1

        self.speedup_scale = 1.1

        #score settings
        self.alien_points=10
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """game settings changing in game initialization"""
        self.ship_speed = 0.9
        self.bullet_speed=1.0
        self.alien_speed=0.5

    def increase_speed(self):
        """changing game settings"""
        self.ship_speed*=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.alien_speed*=self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)