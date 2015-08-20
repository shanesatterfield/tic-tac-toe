from __future__ import print_function, division
import random

class AI():
    def make_move( self, grid ):
        """Returns the row and column of where to place their next move."""
        return (0, 0)

class RandomAI( AI ):
    def make_move( self, grid ):
        width, height = len(grid[0])-1, len(grid)-1

        for _ in range(30):
            r, c = random.randint(0, width), random.randint(0, height)
            if grid[r][c] == 0:
                return (r, c)
        return 0,0


class SolvedStrategies( AI ):
    def make_move( self, grid ):
        return super(Minimax, self).make_move( grid )


class Minimax( AI ):
    def make_move( self, grid ):
        return super(Minimax, self).make_move( grid )


class CounterPlay( AI ):
    def make_move( self, grid ):
        return super(Minimax, self).make_move( grid )
