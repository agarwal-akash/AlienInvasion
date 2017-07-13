import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ A class to manage bullets fired fom the ship"""

    def __init__(self, ai_settings, screen, ship):
        """ Create a bullet object at ships current position"""
        super().__init__()
        self.screen = screen

        # Create a bullet rect at (0,0) and set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullets position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """ Move the bullet up no the screen"""

        # Update teh decimal position of thw bullet
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw the bullets to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
