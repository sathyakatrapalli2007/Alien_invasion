import pygame.font

class ScoreBoard:
    """A class to report scores"""
    def __init__(self,ai_game):
        """Initialize score related attributes"""
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.stats=ai_game.stats
        self.settings=ai_game.settings

        self.font=pygame.font.SysFont("consolas",48)
        self.text_colour=(180,0,100)

        self.prep_score()

    def prep_score(self):
        """Turn the rounded score into an image"""
        rounded_score=round(self.stats.score,-1)
        self.score_str=f"{rounded_score:,}"
        self.score_image=self.font.render(self.score_str,True,self.text_colour,
                                          self.settings.bg_color)

        self.rect=self.score_image.get_rect()
        self.rect.right=self.screen_rect.right-20
        self.rect.top=20

    def show_score(self):
        """Draw score to screen"""
        self.screen.blit(self.score_image,self.rect)