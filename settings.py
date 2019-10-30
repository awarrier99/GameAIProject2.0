width, height = 1680, 1050
# width, height = 0, 0
size = width, height
FPS = 60
visuals = False
__config = None


def init(config):
    global size, __config
    __config = config
    _set('width')
    _set('height')
    size = width, height
    _set('FPS', 'fps')
    _set('visuals', 'no_visuals', True)


def _set(prop, alias=None, reverse=False):
    cprop = alias or prop
    val = __config[cprop]
    if type(val) is bool:
        if reverse:
            globals()[prop] = not val
        else:
            globals()[prop] = __config[cprop]
    elif __config[cprop]:
        globals()[prop] = __config[cprop]


def toggle(prop):
    val = globals()[prop]
    if type(val) is bool:
        globals()[prop] = not val
