from __future__ import print_function, division
import pyglet, random
from ai import *
from grid import Grid

class Game( pyglet.window.Window ):
    def __init__( self ):
        self.restart()
        super(Game, self).__init__( self.grid_height, self.grid_height )
        self.images = [ pyglet.image.load('res/cross_big.png'), pyglet.image.load('res/circle_big.png') ]

    def restart( self ):
        self.first_player = True
        self.tile_width, self.tile_height = 128, 128
        self.grid_width, self.grid_height = self.tile_width * 3, self.tile_height * 3
        self.grid = [ [ 0 for _ in range(3) ] for _ in range(3) ]
        # self.ai = Minimax()
        self.ai = RandomAI()


    def on_draw( self ):
        pyglet.window.Window.flip( self )
        self.clear()
        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                if self.grid[row][column] != 0:
                    self.images[self.grid[row][column]-1].blit( column*self.tile_height, (2-row)*self.tile_width )

    def on_mouse_release( self, x, y, button, modifiers ):
        if button == pyglet.window.mouse.LEFT:
            # try:

            Grid.make_move( (self.grid_height-y) // self.tile_height, x // self.tile_width, self.grid, self.first_player )
            winner = Grid.check_win( self.grid )
            self.first_player = not self.first_player

            if winner == 0:
                r, c = self.ai.make_move( self.grid, self.first_player )
                Grid.make_move(r, c, self.grid, self.first_player)
                self.first_player = not self.first_player

            # print(Grid.open_spaces(self.grid))

            # except Exception as e:
            #     print(e)

            winner = Grid.check_win( self.grid )
            if winner != 0:
                if winner == -1:
                    print("Tie! It's a cat's eye.")
                else:
                    print('Player {} won!'.format(winner))
                super(Game, self).close()



    

    def is_first_player( x ):
        return True if x == 1 else False
