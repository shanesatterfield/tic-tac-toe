from __future__ import print_function, division
from functools import reduce
import copy

class Grid:
    def __init__( self, width=3, height=3 ):
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def make_move( row, column, grid, first_player ):
        grid = copy.deepcopy(grid)
        if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]):
            raise IndexError('The row or column you specified is not within the correct range.')

        if grid[row][column] is not 0:
            raise ValueError('The space you selected is already occupied.')

        grid[row][column] = 1 if first_player else 2

        return grid

    def open_spaces( grid ):
        lst = []
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 0:
                    lst.append((row, column))
        return lst

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

    def check_win( grid ):
        grid = copy.deepcopy(grid)
        # Check for win conditions.
        for x in win_list:
            if grid[x[0][0]][x[0][1]] == grid[x[1][0]][x[1][1]] and grid[x[1][0]][x[1][1]] == grid[x[2][0]][x[2][1]] and grid[x[0][0]][x[0][1]] != 0:
                return grid[x[0][0]][x[0][1]]

        # Check if it's a tie.
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 0:
                    return 0
        return -1

win_list = [[(0,0),(0,1),(0,2)], [(1,0),(1,1),(1,2)], [(2,0),(2,1),(2,2)],
            [(0,0),(1,0),(2,0)], [(0,1),(1,1),(2,1)], [(0,2),(1,2),(2,2)],
            [(0,0),(1,1),(2,2)], [(0,2),(1,1),(2,0)]]
