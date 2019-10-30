import pygame
import settings
import game

from Terrain import Terrain
from Lander import Lander
from pygame import Vector2
from pygame import gfxdraw


class World:
    def __init__(self):
        self.terrain = Terrain()
        self.__init_terrain = True
        self.gravity = (0, 0.1)
        self.lander = Lander(Vector2(300, 50), Vector2(0.0, .1), 0)
        self.all_sprites = pygame.sprite.LayeredDirty(self.lander)
        self.visual_sensors = []

    def set_background(self):
        self.all_sprites.clear(game.screen, game.background)
        game.screen.blit(game.background, (0, 0))

    def update(self):
        self.all_sprites.update()
        if settings.visuals:
            for vs in self.visual_sensors:
                vs.update()

    def draw(self):
        game.screen.fill((0, 0, 0))
        self.lander.draw(game.screen)
        dirty_sprites = self.all_sprites.draw(game.screen)
        dirty_rects = []
        if self.__init_terrain:
            self.__init_terrain = False
            pygame.draw.rect(game.screen, (150, 150, 150), self.terrain)
            dirty_rects.append(self.terrain)
        pygame.gfxdraw.aacircle(game.screen, 200, 200, 4, (255,255,255))
        pygame.gfxdraw.rectangle(game.screen, (500, 500, 20, 20), (255, 255, 255))
        return dirty_sprites, dirty_rects

