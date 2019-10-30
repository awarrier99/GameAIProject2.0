import pygame
import game

from util import add


class Lander(pygame.sprite.DirtySprite):

    def __init__(self, location, velocity, angle):
        super().__init__()
        self.location = location
        self.velocity = velocity
        self.angle = angle

        self.image = pygame.image.load('images/lander.png')
        # self.image = pygame.transform.scale(self.image, (15, 10))
        self.rect = self.image.get_rect()
        self.rect.center = self.location

        self.scale = 1.0
        self.engine_height = 0
        self.engine_left_anchor_offset = 10
        self.engine_right_anchor_offset = 50

    def update(self):
        self.compute_velocity()
        self.translate_velocity()

        if not self.rect.center == self.location:
            self.dirty = 1
            self.rect.center = self.location
        else:
            self.dirty = 0

    def compute_velocity(self):
        if not game.frame_counter % 50:
            self.velocity = add(self.velocity, game.world.gravity)

    def translate_velocity(self):
        if not (game.world.terrain.colliderect(self.rect) or game.frame_counter % 2):
            self.location = add(self.location, self.velocity)
            self.normalize_location()

    def normalize_location(self):
        if (self.location[1] + (self.rect.height / 2)) > game.world.terrain.top:
            self.location = (self.location[0], game.world.terrain.top - (self.rect.height / 2) + 1)

    def draw(self, screen):
        pass
