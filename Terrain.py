import pygame
import settings


class Terrain(pygame.Rect):
    def __init__(self):
        super().__init__(0, settings.height * 0.8, settings.width, 2)