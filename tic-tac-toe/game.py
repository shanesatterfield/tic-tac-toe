from __future__ import print_function, division
import pyglet, random
from ai import *

class Game( pyglet.window.Window ):
    def __init__( self ):
        self.restart()
        super(Game, self).__init__( self.grid_height, self.grid_height )
        self.images = [ pyglet.image.load('res/cross_big.png'), pyglet.image.load('res/circle_big.png') ]

    def on_draw( self ):
        pyglet.window.Window.flip( self )
        self.clear()
        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                if self.grid[row][column] != 0:
                    self.images[self.grid[row][column]-1].blit( column*self.tile_height, (2-row)*self.tile_width )

    def on_mouse_release( self, x, y, button, modifiers ):
        if button == pyglet.window.mouse.LEFT:
            try:
                self.make_move( (self.grid_height-y) // self.tile_height, x // self.tile_width, self.grid, self.first_player )
                winner = self.check_win( self.grid )
                self.first_player = not self.first_player

                if winner == 0:
                    r, c = self.ai.make_move( self.grid )
                    self.make_move(r, c, self.grid, self.first_player)
                    self.first_player = not self.first_player

            except Exception as e:
                print(e)

            winner = self.check_win( self.grid )
            if winner != 0:
                if winner == -1:
                    print("Tie! It's a cat's eye.")
                else:
                    print('Player {} won!'.format(winner))
                super(Game, self).close()

    def restart( self ):
        self.first_player = True
        self.tile_width, self.tile_height = 128, 128
        self.grid_width, self.grid_height = self.tile_width * 3, self.tile_height * 3
        self.grid = [ [ 0 for _ in range(3) ] for _ in range(3) ]
        self.ai = RandomAI()

    def make_move( self, row, column, grid, first_player ):
        grid = grid[:]
        if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]):
            raise IndexError('The row or column you specified is not within the correct range.')

        if grid[row][column] is not 0:
            raise ValueError('The space you selected is already occupied.')

        grid[row][column] = 1 if first_player else 2
        # self.first_player = not self.first_player

        return grid

    def check_win( self, grid ):
        grid = list(grid)

        for _ in range(2):
            for i in range(3):
                if grid[i][0] == grid[i][1] and grid[i][1] == grid[i][2]:
                    return grid[i][0]
            grid = list(zip(*grid))
            grid = list(map(list, grid))

        if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] or \
           grid[2][0] == grid[1][1] and grid[1][1] == grid[0][2]:
            return grid[1][1]

        if '\n'.join([ ''.join(map(str,columns)) for columns in grid ]).find('0') < 0:
            return -1

        return 0

    def render( self ):
        print(self)

    def __str__( self ):
        return '\n--+---+--\n'.join(self.decode_keys(self.grid))

    def decode_keys( self, grid ):
        return [ ' | '.join([self.decode_key(x[i]) for i in range(len(x))]) for x in self.grid ]

    def decode_key( self, key ):
        if key == 1:
            return 'x'
        elif key == 2:
            return 'o'
        else:
            return ' '

    def is_first_player( x ):
        return True if x == 1 else False
