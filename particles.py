import pygame
from pygame import sprite
import random


class Particles(sprite.Sprite):
    """Creates each of the particles"""

    def __init__(self, pe_game):
        super().__init__()
        self.settings = pe_game.settings
        self.screen = pe_game.screen
        self.screen_rect = pe_game.screen_rect

        self.width = self.settings.p_w
        self.height = self.settings.p_h
        self.color = (0, 0, 0)

        # initialize particle
        self.rect = pygame.Rect(self.settings.WIDTH/2,
                                self.settings.HEIGHT/2, self.width, self.height)

    def draw_particle(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def move_particle(self):
        pass
