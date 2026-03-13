#importing modules required
import sys

import pygame

class AlienInvasion:
    """Creating a class that would manage all game attributes"""
    def __init__(self):
        """Creating a game object"""
        pygame.init()

        #Creating overall game window
        self.screen=pygame.display.set_mode((1200,800))
        #Creating text to be displayed
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Creating a loop that will update the screen"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            """Draws new screen"""
            pygame.display.flip()
    
if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()