import pygame
import sys
import settings
import time
import particles
import random
import math


class ParticleExplosion:
    def __init__(self):
        # initialize parameters
        self.settings = settings.Settings()
        self.width = self.settings.WIDTH
        self.height = self.settings.HEIGHT
        self.bg_color = self.settings.bg_color
        self.p_red = 0
        self.p_green = 0
        self.p_blue = 0

        # initialize the screen
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Particle Explosion")
        self.screen_rect = self.screen.get_rect()

        # initialize the particles
        self.particle_group = particles.sprite.Group()
        self.create_particles()

        # initialize run speed
        self.FPS = 60
        self.clock = pygame.time.Clock()

    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def on_loop(self):
        self.color_change()

    def on_render(self):
        self.screen.fill(self.bg_color)
        # draw particles
        for particle in self.particle_group.sprites():
            particle.draw_particle()
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):

        while True:
            # self.clock.tick(self.FPS)
            self.on_event()
            self.on_loop()
            self.on_render()
        self.on_cleanup()

# --------------------------------------------------------------
    def create_particles(self):
        while len(self.particle_group) < self.settings.n_particles:
            particle = particles.Particles(self)
            self.particle_group.add(particle)

# ----------------------------------------------------------------
    def color_change(self):
        self.p_red = abs(math.sin(time.time()*.5))*255
        self.p_green = abs(math.sin(time.time()*.3))*255
        self.p_blue = abs(math.sin(time.time()*.1))*255
        for particle in self.particle_group.sprites():
            particle.change_color(self.p_red, self.p_green, self.p_blue)


if __name__ == "__main__":
    pe = ParticleExplosion()
    pe.on_execute()
