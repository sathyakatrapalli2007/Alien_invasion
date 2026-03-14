#importing modules required
import sys

import pygame

from settings import Settings

class AlienInvasion:
    """Creating a class that would manage all game attributes"""
    def __init__(self):
        """Creating a game object"""
        pygame.init()
        self.settings=Settings()

        #Creating overall game window
        self.screen=pygame.display.set_mode((self.settings.screen_width,
                                             self.settings.screen_height))
        #Creating text to be displayed
        pygame.display.set_caption("Alien Invasion")
        #Creating a class Clock object
        self.clock=pygame.time.Clock()
        #Setting background colour

    def run_game(self):
        """Creating a loop that will update the screen"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Redraw the screen with the appropriate filling
            self.screen.fill(self.settings.bg_color)
            #Draws new screen
            pygame.display.flip()
            #Keeps consistent framerate by ticking once through a loop
            self.clock.tick(60)
            
    
if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()