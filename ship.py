import pygame

class Ship:
    """Class that manages mthe ship element"""
    def __init__(self,ai_game):
        """Initializes the ship"""
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.settings=ai_game.settings

        #Load the image and get its rect attribut
        self.image=pygame.image.load('images/ship1.bmp')
        self.image= pygame.transform.smoothscale(self.image, (60, 48))
        self.rect=self.image.get_rect()

        #Start the new ship at the midbottom of screen
        self.rect.midbottom=self.screen_rect.midbottom

        #Store a float for the ship's exact horizontal position.
        self.x=float(self.rect.x)

        #Set the movement flag to not move
        self.moving_right=False
        self.moving_left=False
    
    def blitme(self):
        """Draw the ship image at the given location"""
        #Using blit function to draw 
        self.screen.blit(self.image,self.rect)

    def update(self):
        """Update the location of the ship based on kew pressed"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.ship_speed

        #Update rect object from x
        self.rect.x=self.x

    def center_ship(self):
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)


