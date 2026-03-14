import pygame

class Ship:
    """Class that manages mthe ship element"""
    def __init__(self,ai_game):
        """Initializes the ship"""
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()

        #Load the image and get its rect attribut
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()

        #Start the new ship at the midbottom of screen

        self.rect.midbottom=self.screen_rect.midbottom
        self.rect.y-=40
    
    def blitme(self):
        #Using blit function to draw 
        self.screen.blit(self.image,self.rect)

