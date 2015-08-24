from __future__ import print_function, division
from grid import Grid
import random, copy

class AI():
    def make_move( self, grid, this_player ):
        """Returns the row and column of where to place their next move."""
        return (0, 0)


class RandomAI( AI ):
    """Picks a random open space on the board each turn."""
    def make_move( self, grid, this_player ):
        width, height = len(grid[0])-1, len(grid)-1

        for _ in range(30):
            r, c = random.randint(0, width), random.randint(0, height)
            if grid[r][c] == 0:
                return (r, c)
        return 0,0


class Minimax( AI ):
    """Runs the minimax algorithm with alpha beta pruning to not lose the game"""
    def make_move( self, grid, this_player ):
        grid        = copy.deepcopy(grid)
        alpha, beta = float('-inf'), float('inf')
        spaces      = sorted(Grid.open_spaces( grid ), key=lambda x: abs(x[0] - x[1])%2)

        lst = [ (x, Minimax.minimax(Grid.make_move(x[0], x[1], grid[:], this_player), 0, alpha, beta, this_player, not this_player)) for x in spaces ]
        return sorted(lst, key=lambda x: x[1])[-1][0]


    def minimax( grid, depth, alpha, beta, this_player, curr_player ):
        # Check if the game is over and return the value.
        winner = Grid.check_win( grid )
        if winner != 0:
            if winner == -1:
                return depth
            elif winner == int(not this_player)+1:
                return 100 - depth
            else:
                return -100 + depth

        grid = copy.deepcopy(grid)

        # Maximizing
        if curr_player is this_player:
            v = float('-inf')
            for n in Grid.open_spaces(grid):
                temp  = Minimax.minimax(Grid.make_move(n[0], n[1], grid, curr_player), depth+1, alpha, beta, this_player, not curr_player)
                v     = max(v, temp)
                alpha = max(alpha, v)

                if alpha >= beta:
                    break
            return v

        # Minimizing
        else:
            v = float('inf')
            for n in Grid.open_spaces(grid):
                temp = Minimax.minimax(Grid.make_move(n[0], n[1], grid, curr_player), depth+1, alpha, beta, this_player, not curr_player)
                v    = min(v, temp)
                beta = min(beta, v)

                if beta <= alpha:
                    break
            return v
