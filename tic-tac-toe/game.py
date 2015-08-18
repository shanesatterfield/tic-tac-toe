from __future__ import print_function
import random

class Game:
    def __init__( self ):
        self.restart()

    def restart( self ):
        self.grid = [ [ 0 for _ in range(3) ] for _ in range(3) ]

    def make_move( self, row, column, first_player ):
        if row < 0 or row >= len(self.grid) or column < 0 or column >= len(self.grid[0]):
            raise IndexError('The row or column you specified is not within the correct range.')

        if self.grid[row][column] is not 0:
            raise ValueError('The space you selected is already occupied.')

        self.grid[row][column] = 1 if first_player else 2

    def check_win( self ):
        grid = list(self.grid)
        for _ in range(2):
            for i in range(3):
                if grid[i][0] == grid[i][1] == grid[i][2]:
                    return grid[i][0]
            grid = list(zip(*grid))
            grid = list(map(list, grid))

        if grid[0][0] == grid[1][1] == grid[2][2] or \
           grid[2][0] == grid[1][1] == grid[0][2]:
            return grid[1][1]

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
