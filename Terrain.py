import pygame
import settings


class Terrain(pygame.Rect):
    def __init__(self):
        super().__init__(0, settings.height * 0.9, settings.width, 2)
        print(settings.size)