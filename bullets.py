import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class that manages the bullets"""
    def __init__(self,ai_game):
        """Initializes and creates a bullet"""
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=self.settings.bullet_color

        #Let's create the bullet rect object
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,
                              self.settings.bullet_height)
        self.rect.midtop=ai_game.ship.rect.midtop

        #Let's assign the y coordinate to another variable
        self.y=float(self.rect.y)

    def update(self):
        """Update the location of bullet"""
        #We need to update the location of the bullet
        self.y-=self.settings.bullet_speed

        #assign it back to the the y coordinate
        self.rect.y=self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        #we need to draw the bullet 
        pygame.draw.rect(self.screen,self.color,self.rect)