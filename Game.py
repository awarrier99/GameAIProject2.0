import pygame
import settings

from os.path import join
from World import World


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
    pygame.display.set_caption('James and Ashvin\'s Game \'AI\'')

    background = pygame.image.load(join('images', 'background.jpg'))
    background = pygame.transform.scale(background, settings.size)
    background = background.convert()

    screen.blit(background, (0, 0))

    clock = pygame.time.Clock()
    world = World()


def mainloop():
    global __running, clock, world

    while __running:
        clock.tick(settings.FPS)

        caption = 'Lunar Landing \'AI\'  FPS: {}'.format(round(clock.get_fps(), 1))
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
