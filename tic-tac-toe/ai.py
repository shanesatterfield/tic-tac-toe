from __future__ import print_function, division
from grid import Grid
import random, copy

class AI():
    def make_move( self, grid, this_player ):
        """Returns the row and column of where to place their next move."""
        return (0, 0)

class RandomAI( AI ):
    def make_move( self, grid, this_player ):
        width, height = len(grid[0])-1, len(grid)-1

        for _ in range(30):
            r, c = random.randint(0, width), random.randint(0, height)
            if grid[r][c] == 0:
                return (r, c)
        return 0,0

# TODO Something wrong with functions. Ignore the alpha beta pruning, it's not
# even doing the minimax right. Doesn't want to win when it can just go for it.
# Maybe something about the sorting.
class Minimax( AI ):
    def make_move( self, grid, this_player ):
        # grid = grid[:]
        grid        = copy.deepcopy(grid)
        alpha, beta = float('-inf'), float('inf')
        spaces      = sorted(Grid.open_spaces( grid ), key=lambda x: abs(x[0] - x[1])%2)

        lst = [ (x, Minimax.minimax(Grid.make_move(x[0], x[1], grid[:], this_player), 1, alpha, beta, this_player, this_player)) for x in spaces ]
        # return sorted(lst, key=lambda x: x[1])[0][0]
        # return sorted(lst, key=lambda x: x[1])[-1][0]
        lst = sorted(lst, key=lambda x: x[1])
        print(lst)
        return lst[-1][0]

        # result = None
        # stuff = float('-inf')
        # for x in spaces:
        #     temp = Minimax.minimax(Grid.make_move(x[0], x[1], grid[:], this_player), 1, alpha, beta, this_player, this_player)
        #     if temp > stuff:
        #         stuff = temp
        #         result = x
        #
        #     print(x)
        # return result

        # return super(Minimax, self).make_move( grid )

        # Copy the grid.
    def minimax( grid, depth, alpha, beta, this_player, curr_player ):
        # Check if the game is over and return the value.
        winner = Grid.check_win( grid )
        if winner != 0:
            if winner == -1:
                return 0
            elif winner == int(not this_player)+1:
                # return 100 - depth
                return 100
            else:
                # return -100 + depth
                return -100

        grid = copy.deepcopy(grid)

        # Maximizing
        if curr_player is this_player:
            v = float('-inf')
            for n in Grid.open_spaces(grid):
                temp  = Minimax.minimax(Grid.make_move(n[0], n[1], grid, not curr_player), depth+1, alpha, beta, this_player, not curr_player)
                v     = max(v, temp)
                alpha = max(alpha, v)

                # print('\t'*depth, 'Depth: {:d} V: {:03d} Player: {:d}'.format(depth, v, int(not curr_player)+1))
                # if alpha >= beta:
                #     break
            return v

        # Minimizing
        else:
            v = float('inf')
            for n in Grid.open_spaces(grid):
                temp = Minimax.minimax(Grid.make_move(n[0], n[1], grid, not curr_player), depth+1, alpha, beta, this_player, not curr_player)
                v    = min(v, temp)
                beta = min(beta, v)

                # print('\t'*depth, 'Depth: {:d} V: {:03d} Player: {:d} \t{} {}'.format(depth, v, int(not curr_player)+1, n[0], n[1]))
                # if beta >= alpha:
                #     break
            print('\t'*depth, v, n)
            return v

        # Returns 0 if result is still None.
        # return 0

        # lst = [ Minimax.minimax(Grid.make_move(n[0], n[1], grid[:], not curr_player), this_player, not curr_player) for n in Grid.open_spaces(grid) ]
        # # print('Minimax List: ', lst)
        # if len(lst) <= 0:
        #     return 0
        #
        # if curr_player is this_player:
        #     return max(lst)
        # else:
        #     return min(lst)


class SolvedStrategies( AI ):
    def make_move( self, grid, this_player ):
        return super(Minimax, self).make_move( grid )


class CounterPlay( AI ):
    def make_move( self, grid, this_player ):
        return super(Minimax, self).make_move( grid )
