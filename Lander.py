import pygame
import game
import math
from pygame.math import Vector2
import random

from util import add


class Lander(pygame.sprite.DirtySprite):

    def __init__(self, location, velocity, angle):
        super().__init__()
        self.location = location
        self.velocity = velocity
        self.heading = angle
        self.accelMagnitude = 0.0

        self.image = pygame.image.load('images/small_lander.png')
        # self.image = pygame.transform.scale(self.image, (15, 10))
        self.rect = self.image.get_rect()
        self.rect.center = self.location

        self.thrust_count = 0
        self.scale = 1.0
        self.engine_height = 0
        self.engine_heights = [0, 5, 10, 20, 25, 28, 30]
        self.engine_increasing = True
        self.engine_left_anchor_offset = 10
        self.engine_right_anchor_offset = 50

    def thrust(self):
        self.thrust_count += 1

    def update(self):

        if self.engine_increasing:
            if self.engine_height < len(self.engine_heights) - 1:
                self.engine_height += 1
            else:
                self.engine_increasing = False
        else:
            if self.engine_height > 3:
                self.engine_height -= 1
            else:
                self.engine_increasing = True


        self.compute_velocity()
        self.translate_velocity()

        if not self.rect.center == self.location:
            self.dirty = 1
            self.rect.center = self.location
        else:
            self.dirty = 0

    def compute_velocity(self):
        pass
        # if not game.frame_counter % 50:
            # self.velocity = add(self.velocity, game.world.gravity)

    def translate_velocity(self):
        if not (game.world.terrain.colliderect(self.rect) or game.frame_counter % 2):
            self.location = add(self.location, self.velocity)
            self.normalize_location()

    def normalize_location(self):
        if (self.location[1] + (self.rect.height / 2)) > game.world.terrain.top:
            self.location = (self.location[0], game.world.terrain.top - (self.rect.height / 2) + 1)

    def draw(self, screen):
        pygame.draw.aaline(screen, (255,255,255), (self.location[0] - 3, self.location[1]+7), (self.location[0], self.location[1] + self.engine_heights[self.engine_height]), 1)
        pygame.draw.aaline(screen, (255,255,255), (self.location[0] + 3, self.location[1]+7), (self.location[0], self.location[1] + self.engine_heights[self.engine_height]), 1)
