import pygame
import settings

from World import World
from random import seed, randint


__running = False
frame_counter = 0
frame_counter_limit = 1000
screen = None
background = None
clock = None
world = None
stars = []


def run():
    global __running

    __running = True
    setup()
    mainloop()
    cleanup()


def setup():
    global screen, background, clock, world

    screen = pygame.display.set_mode(settings.size)
    pygame.display.set_caption('Lunar Landing AI')

    clock = pygame.time.Clock()

    world = World()
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    seed()
    get_star_positions()
    star_background()
    draw_background()


def get_star_positions():
    global stars

    x_bound = settings.width - 1
    y_bound = world.terrain.top - 1
    for i in range(50):
        x = randint(0, x_bound)
        y = randint(0, y_bound)
        stars.append((x, y))


def star_background():
    global background, stars

    for star in stars:
        pygame.draw.circle(background, (255, 255, 255), star, 0)


def draw_background():
    global screen, background

    star_background()
    screen.blit(background, (0, 0))


def mainloop():
    global __running, clock, world, frame_counter, frame_counter_limit

    while __running:
        clock.tick(settings.FPS)

        caption = 'Lunar Landing AI | FPS: {}'.format(round(clock.get_fps(), 1))
        pygame.display.set_caption(caption)

        handle_events()
        handle_keys()
        world.update()
        draw()

        frame_counter = (frame_counter + 1) % frame_counter_limit


def handle_events():
    global __running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            __running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                __running = False


def handle_keys():
    global world

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        world.lander.apply_thrust()


def draw():
    global world, screen

    # draw_background()
    dirty = world.draw()
    pygame.display.update(dirty)


def cleanup():
    global screen, background, clock, world

    screen = background = clock = world = None
    pygame.quit()
