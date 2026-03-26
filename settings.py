class Settings:
    """ A class that stores all the game object settings"""
    def __init__(self):
        """Initialises different settings as attributes"""
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(231,196,213)
        self.ship_limit=3

        #Bullet Settings
        self.bullet_width=3 
        self.bullet_height=15
        self.bullet_color=(237,18,132)
        self.bullets_allowed=5

        #Alien Settings
        self.fleet_dropdown_speed=10
        
        self.increase_speed=1.1
        self.score_scale=1.5

    def initialize_dynamic_settings(self):
        """Reset these values whenever the player restarts the game"""
        self.ship_speed=2.0
        self.bullet_speed=3.0
        self.alien_speed=1.0
        #right=1, left=-1
        self.fleet_direction=1

        #alien settings
        self.alien_points=50

    def speed_up(self):
        """Increase the dynamic settings each time player levels up"""
        self.ship_speed*=self.increase_speed
        self.bullet_speed*=self.increase_speed
        self.alien_speed*=self.increase_speed
        #right=1, left=-1
        self.fleet_direction*=self.increase_speed
        self.alien_points=int(self.alien_points*self.score_scale)
        