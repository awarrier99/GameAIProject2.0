import pygame
import settings
import game

from Terrain import Terrain


class World:
    def __init__(self):
        self.terrain = Terrain()
        self.__init_terrain = True
        self.all_sprites = pygame.sprite.LayeredDirty()
        self.all_sprites.clear(game.screen, game.background)
        self.visual_sensors = []

    def update(self):
        self.all_sprites.update()
        if settings.visuals:
            for vs in self.visual_sensors:
                vs.update()

    def draw(self):
        dirty_sprites = self.all_sprites.draw(game.screen)
        dirty_rects = []
        if self.__init_terrain:
            self.__init_terrain = False
            pygame.draw.rect(game.screen, (150, 150, 150), self.terrain)
            dirty_rects.append(self.terrain)

        return dirty_sprites, dirty_rects

