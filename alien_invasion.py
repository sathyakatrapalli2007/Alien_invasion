#importing modules required
import sys

import pygame

from settings import Settings

from ship import Ship

from bullets import Bullet

from alien import Alien

class AlienInvasion:
    """Creating a class that would manage all game attributes"""
    def __init__(self):
        """Creating a game object"""
        pygame.init()
        #Create a Settings instance
        self.settings=Settings()

        #Creating overall game window
        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width=self.screen.get_rect().width
        self.settings.screen_height=self.screen.get_rect().height

        #Creating text to be displayed
        pygame.display.set_caption("Alien Invasion")

        #Creating a class Clock object
        self.clock=pygame.time.Clock()

        #Creating the Ship instance
        self.ship=Ship(self)

        #Creating the bullet group
        self.bullets=pygame.sprite.Group()

        #creating an alien fleet
        self.aliens=pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Creating a loop that will update the screen"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            #Keeps consistent framerate by ticking once through a loop
            self.clock.tick(60)



    def _check_events(self):
        """Checks for user input and responds accordingly"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """Deal with Key presses"""
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key==pygame.K_LEFT:
             self.ship.moving_left=True
        elif event.key==pygame.K_ESCAPE:
            sys.exit()
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()
        
    def _check_keyup_events(self,event):
        """Deal with key releases"""
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=False


    def _update_screen(self):
        """Updates the screen after every loop"""
        #Redraw the screen with the appropriate filling
        self.screen.fill(self.settings.bg_color)
        #Draws the bullet
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #Draws the ship
        self.ship.blitme()
        #Draws the alien
        self.aliens.draw(self.screen)
        #Draws new screen
        pygame.display.flip()

    def _fire_bullet(self):
        """Create the bullet instance"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        """Update the location of the bullet and get rid of old bullets"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)

        #check for any bullets that hit the alien and get rid of them
        collisions=pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)

    def _create_fleet(self):
        """Creates alien fleets"""
        #spacing between aliens is one alien width and one alien height
        alien=Alien(self)
        alien_width=alien.rect.width
        alien_height=alien.rect.height

        current_x=alien_width
        current_y=alien_height
        while (current_y < self.settings.screen_height-3*alien_height):
            while (current_x<=self.settings.screen_width - 2*alien_width):
                self._create_alien(current_x,current_y)
                current_x+=2*alien_width
            #finished row
            current_y+=2*alien_height
            current_x=alien_width

    def _create_alien(self,x_pos,y_pos):
        """Create aliens and add its to the group"""
        new_alien=Alien(self)
        new_alien.x=x_pos
        new_alien.rect.x=x_pos
        new_alien.rect.y=y_pos
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y+=self.settings.fleet_dropdown_speed
        self.settings.fleet_direction*=-1

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

    
if __name__=='__main__':

    ai=AlienInvasion()
    ai.run_game()

