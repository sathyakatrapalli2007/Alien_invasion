import pygame.font

class Button:
    """A class to bulid buttons for the game"""
    def __init__(self,ai_game,msg):
        """Initialize button elements"""
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()

        #Set the settings for button
        self.width=250
        self.height=70
        self.button_color=(180,0,100)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont("consolas",48)

        #Build the button
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self,msg):
        """Render the font image"""
        self.font_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.font_image_rect=self.font_image.get_rect()
        self.font_image_rect.center=self.rect.center

    def blitme(self):
        """Draw the button and text image"""
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.font_image,self.font_image_rect)