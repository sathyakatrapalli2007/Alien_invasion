class Settings:
    """ A class that stores all the game object settings"""
    def __init__(self):
        """Initialises different settings as attributes"""
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(231,196,213)
        self.ship_speed=1.5
        self.ship_limit=3

        #Bullet Settings
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_speed=2.5
        self.bullet_color=(237,18,132)
        self.bullets_allowed=5

        #Alien Settings
        self.alien_speed=1.0
        self.fleet_dropdown_speed=10
        #right=1, left=-1
        self.fleet_direction=1