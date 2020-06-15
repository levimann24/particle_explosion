import pygame
from pygame import sprite
import random
import math


class Particles(sprite.Sprite):
    """Creates each of the particles"""

    def __init__(self, pe_game):
        super().__init__()
        self.settings = pe_game.settings
        self.screen = pe_game.screen
        self.screen_rect = pe_game.screen_rect

        # initialize the particle
        self.width = self.settings.p_w
        self.height = self.settings.p_h
        self.color = (0, 0, 0)
        self.x = self.settings.WIDTH/2
        self.y = self.settings.HEIGHT/2

        # create random radian directions between 1 and 2 PI
        self.direction = 2*math.pi*random.uniform(0, 1)
        # create different speed of particle
        self.speed = 4 * random.uniform(0.1, 1)

        # initialize particle
        self.rect = pygame.Rect(self.x,
                                self.y, self.width, self.height)

    def draw_particle(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def move_particle(self):
        x_speed = self.speed * math.cos(self.direction)
        y_speed = self.speed * math.sin(self.direction)

        self.x += x_speed
        self.y += y_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def change_color(self, r, g, b):
        self.color = (r, g, b)

    def check_delete(self):
        if self.x < 0 or self.x > self.settings.WIDTH:
            return True
        if self.y < 0 or self.y > self.settings.HEIGHT:
            return True
        else:
            return False
