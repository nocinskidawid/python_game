class Settings:
    def __init__(self):
        """game settings initialization"""

        #screen settings
        self.screen_width = 1600
        self.screen_height = 989
        self.bg_color = (120,120,120)

        #ship movement settings
        self.ship_speed = 0.9
        self.ship_limit=3

        #bullets settings
        self.bullet_speed=1.0
        self.bullet_width=3
        self.bullet_height=15
        self.bullets_allowed=3
        self.bullet_color=(60,60,60)

        #aliens settings
        self.alien_speed=0.5
        self.fleet_drop_speed=5
        #fleet direction 1=right -1=left
        self.fleet_direction=1
