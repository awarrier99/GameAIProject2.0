import pygame
from pygame import gfxdraw


class Lander(pygame.sprite.DirtySprite):

    def __init__(self, location, velocity, angle):
        pygame.sprite.Sprite.__init__(self)
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
        pass

    def draw(self, screen):
        pass
