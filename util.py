from pygame.math import Vector2


def copy(vec):
    return Vector2(vec)


def scale(vec, scalar):
    v = copy(vec)
    v.scale_to_length(scalar)
    return v


def position(obj, timestep):
    a = scale(obj.acceleration, timestep)
    obj.velocity += a
    a = scale(obj.acceleration, timestep / 2)
    delta = scale(obj.velocity + a, timestep)
    obj.position += delta
