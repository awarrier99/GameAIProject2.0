"""
Authors: Ashvin Warrier and James Lowe
"""
import settings
import game

from argparse import ArgumentParser


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-nv', '--no-visuals', action='store_true', help='whether to show visual sensors for debugging')
    parser.add_argument('-w', '--width', type=int, help='width of the game screen')
    parser.add_argument('-he', '--height', type=int, help='height of the game screen')
    parser.add_argument('-f', '--fps', type=int, help='frames per second')
    config = vars(parser.parse_args())
    settings.init(config)
    game.run()
