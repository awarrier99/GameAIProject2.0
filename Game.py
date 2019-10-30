import pygame
import settings

from os.path import join


class Game:
    def __init__(self):
        self.__running = True
        self.screen = None
        self.background = None
        self.clock = pygame.time.Clock()
        self.visual_sensors = []

    def run(self):
        self.setup()
        self.mainloop()
        self.cleanup()

    def setup(self):
        pygame.init()
        self.screen = pygame.display.set_mode(settings.size)
        # self.visual_sensors.append([VisualSensors(self.player, *settings.size)])
        pygame.display.set_caption('James and Ashvin\'s Game \'AI\'')

        background = pygame.image.load(join('images', 'background.jpg'))
        background = pygame.transform.scale(background, settings.size)
        self.background = background.convert()

        self.screen.blit(self.background, (0, 0))

    def mainloop(self):
        while self.__running:
            self.clock.tick(settings.FPS)

            caption = 'James and Ashvin\'s Game \'AI\'  FPS: {}'.format(round(self.clock.get_fps(), 1))
            pygame.display.set_caption(caption)

            self.handle_events()

            if settings.visuals:
                for vs in self.visual_sensors:
                    vs.update()
            # self.world.update()
            self.redraw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__running = False

    def redraw(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()


    def cleanup(self):
        pygame.quit()
