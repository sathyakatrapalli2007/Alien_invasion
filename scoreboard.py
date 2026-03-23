import pygame.font
from ship import Ship
from pygame.sprite import Group

class ScoreBoard:
    """A class to report scores"""
    def __init__(self,ai_game):
        """Initialize score related attributes"""
        self.ai_game=ai_game
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.stats=ai_game.stats
        self.settings=ai_game.settings

        self.font=pygame.font.SysFont("consolas",48)
        self.text_colour=(180,0,100)

        self.prep_score()
        self.prep_highscore()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the rounded score into an image"""
        rounded_score=round(self.stats.score,-1)
        self.score_str=f"{rounded_score:,}"
        self.score_image=self.font.render(self.score_str,True,self.text_colour,
                                          self.settings.bg_color)

        self.rect=self.score_image.get_rect()
        self.rect.right=self.screen_rect.right-20
        self.rect.top=20

    def prep_highscore(self):
        """Turn the highscore into an image"""
        rounded_highscore=round(self.stats.high_score,-1)
        self.highscore_str=f"{rounded_highscore:,}"

        self.high_score_image=self.font.render(self.highscore_str,True,self.text_colour,
                                          self.settings.bg_color)

        self.highrect=self.score_image.get_rect()
        self.highrect.midtop=self.screen_rect.midtop

    def prep_level(self):
        """Turn the level into an image"""
        level_str=str(self.stats.level)
        self.level_image=self.font.render(level_str,True,self.text_colour,
                                            self.settings.bg_color)
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.rect.right
        self.level_rect.top=self.rect.bottom-10

    def check_high_score(self):
        """Checks if the highscore needs to be updated"""
        if self.stats.score>self.stats.high_score:
            self.stats.high_score=self.stats.score
            self.prep_highscore()

    def prep_ships(self):
        self.ships=Group()
        for ship_count in range(self.stats.ships_left):
            new_ship=Ship(self.ai_game)
            new_ship.rect.x=10+ship_count*new_ship.rect.width
            new_ship.rect.y=10
            self.ships.add(new_ship)

    def show_score(self):
        """Draw score to screen"""
        self.screen.blit(self.score_image,self.rect)
        self.screen.blit(self.high_score_image,self.highrect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)


