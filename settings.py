import random
import math


class Settings:
    def __init__(self):

        # Define the window
        self.WIDTH = 800
        self.HEIGHT = 800
        self.bg_color = (255, 255, 255)

        # define some particle parameters
        self.p_w = 20
        self.p_h = 20
        self.p_speed = 1
        self.p_acc = 1
        self.n_particles = 1
