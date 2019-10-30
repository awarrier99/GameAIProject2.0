import pygame
import settings
import game

from pygame.math import Vector2
from Terrain import Terrain
from Lander import Lander
from pygame import Vector2


class World:
    def __init__(self):
        self.terrain = Terrain()
        self.gravity = Vector2(0, 0.001)
        self.lander = Lander(Vector2(300, 100), Vector2(0, 0), 0)
        self.all_sprites = pygame.sprite.LayeredDirty(self.lander)
        self.visual_sensors = []

    def update(self):
        self.all_sprites.update()
        if settings.visuals:
            for vs in self.visual_sensors:
                vs.update()

    def draw(self):
        pygame.draw.rect(game.screen, (150, 150, 150), self.terrain)
        self.lander.draw(game.screen)
        return self.all_sprites.draw(game.screen)
