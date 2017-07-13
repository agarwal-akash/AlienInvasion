import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ A class to represent an alien"""

    def __init__(self, ai_settings, screen):
        """ Initialise the alien and set the starting position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the image of the alien
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien at top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """ Draw the alien on the board"""
        self.screen.blit(self.image, self.rect)

    def update(self, ):
        """ Move the aliens to the right"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """ Return True if alien is at edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
