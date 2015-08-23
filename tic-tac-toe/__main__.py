from __future__ import print_function, division
import pyglet, time
from game import Game
from ai import *
from grid import Grid

def main():
    game = Game()
    pyglet.app.run()

if __name__ == '__main__':
    main()
