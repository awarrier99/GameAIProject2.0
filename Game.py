import pygame
import settings

from World import World
from random import seed, randint


__running = False
screen = None
background = None
clock = None
world = None


def run():
    global __running

    __running = True
    setup()
    mainloop()
    cleanup()


def setup():
    global screen, background, clock, world

    pygame.init()
    screen = pygame.display.set_mode(settings.size)
    pygame.display.set_caption('James and Ashvin\'s Game AI')

    clock = pygame.time.Clock()
    world = World()

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    seed()
    star_background()

    screen.blit(background, (0, 0))


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
