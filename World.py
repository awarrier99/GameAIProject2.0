import pygame
import settings
import game


class World:
    def __init__(self):
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
        return dirty_sprites, []
