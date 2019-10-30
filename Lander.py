import pygame
import game

from pygame.math import Vector2


class Lander(pygame.sprite.DirtySprite):

    def __init__(self, position, velocity, angle):
        super().__init__()
        self.dirty = 1
        self.position = position
        self.i_velocity = velocity
        self.velocity = velocity
        self.angle = angle
        self.thrust = Vector2(0, -0.003)
        self.thrusting = False

        self.image = pygame.image.load('images/small_lander.png')
        # self.image = pygame.transform.scale(self.image, (15, 10))
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        self.thrust_count = 0
        self.scale = 1.0
        self.engine_height = 0
        self.engine_heights = [0, 5, 10, 20, 25, 28, 30]
        self.engine_increasing = True
        self.engine_left_anchor_offset = 10
        self.engine_right_anchor_offset = 50

    def apply_thrust(self):
        self.thrust_count += 1
        self.thrusting = True

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

        self.compute_position()
        self.rect.center = self.position
        self.dirty = 1

    def compute_position(self):
        if not game.world.terrain.colliderect(self.rect):
            self.position += self.velocity
            if self.thrusting:
                self.thrusting = False
                self.velocity += self.thrust
            self.velocity += game.world.gravity

    def normalize_location(self):
        if (self.position.y + (self.rect.height / 2)) > game.world.terrain.top:
            self.position = Vector2(self.position.x, game.world.terrain.top - (self.rect.height / 2) + 1)

    def draw(self, screen):
        pygame.draw.aaline(screen, (255,255,255), (self.position[0] - 3, self.position[1]+7), (self.position[0], self.position[1] + self.engine_heights[self.engine_height]), 1)
        pygame.draw.aaline(screen, (255,255,255), (self.position[0] + 3, self.position[1]+7), (self.position[0], self.position[1] + self.engine_heights[self.engine_height]), 1)
