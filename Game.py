import pygame
import settings
from Lander import Lander

from World import World
from random import seed, randint


<<<<<<< HEAD
class Game:
    def __init__(self):
        self.__running = True
        self.screen = None
        self.background = None
        self.clock = pygame.time.Clock()
        self.visual_sensors = []
        self.lander = Lander((300, 200), 0, 0)
        self.all_sprites = None

__running = False
screen = None
background = None
clock = None
world = None
>>>>>>> 853899a1d9809c9fc7073625aff8b5e5f847b784


def run():
    global __running

<<<<<<< HEAD
        # background = pygame.image.load(join('images', 'background.jpg'))
        # background = pygame.transform.scale(background, settings.size)
        # self.background = background.convert()
        self.all_sprites = pygame.sprite.Group(self.lander)
        # self.screen.blit(self.background, (0, 0))
=======
    __running = True
    setup()
    mainloop()
    cleanup()

>>>>>>> 853899a1d9809c9fc7073625aff8b5e5f847b784

def setup():
    global screen, background, clock, world

    pygame.init()
    screen = pygame.display.set_mode(settings.size)
    pygame.display.set_caption('James and Ashvin\'s Game AI')

<<<<<<< HEAD
            self.handle_events()
            self.lander.update()
            if settings.visuals:
                for vs in self.visual_sensors:
                    vs.update()
            # self.world.update()
            self.all_sprites.update()
            self.redraw()
=======
    clock = pygame.time.Clock()
    world = World()

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    seed()
    star_background()
>>>>>>> 853899a1d9809c9fc7073625aff8b5e5f847b784

    screen.blit(background, (0, 0))

<<<<<<< HEAD
    def redraw(self):
        # self.screen.blit(self.background, (0, 0))
        pygame.display.update(self.lander)
        self.all_sprites.draw(self.screen)
        self.lander.draw(self.screen)

        pygame.display.flip()
=======
>>>>>>> 853899a1d9809c9fc7073625aff8b5e5f847b784

def star_background():
    x_bound = settings.width - 1
    y_bound = world.terrain.top - 1
    for i in range(25):
        x = randint(0, x_bound)
        y = randint(0, y_bound)
        pygame.draw.circle(background, (255, 255, 255), (x, y), 0)


def mainloop():
    global __running, clock, world

    while __running:
        clock.tick(settings.FPS)

        caption = 'Lunar Landing AI | FPS: {}'.format(round(clock.get_fps(), 1))
        pygame.display.set_caption(caption)

        handle_events()
        world.update()
        draw()


def handle_events():
    global __running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            __running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                __running = False


def draw():
    global world

    dirty_sprites, dirty_rects = world.draw()
    pygame.display.update(dirty_sprites + dirty_rects)


def cleanup():
    global screen, background, clock, world

    screen = background = clock = world = None
    pygame.quit()
