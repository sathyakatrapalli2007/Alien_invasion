import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien"""
    def __init__(self,ai_game):
        """Create a single Alien object"""
        super().__init__()
        #Assign the game window to a attribute so that it can be used
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.settings=ai_game.settings

        #Load the image
        self.image=pygame.image.load('images/alien.bmp')
        self.image=pygame.transform.smoothscale(self.image,(60,58))
        self.rect=self.image.get_rect()

        #Set the coordinates of the alien
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        #Assign x coordinate to a variable
        self.x=float(self.rect.x)

    def check_edges(self):
        """Return True if the fleet hits the edge"""
        return (self.rect.right>=self.screen_rect.right) or (self.rect.left<=0)

    def update(self):
        """Update the position of the aliens"""
        self.x+=self.settings.alien_speed*self.settings.fleet_direction
        self.rect.x=self.x
        
