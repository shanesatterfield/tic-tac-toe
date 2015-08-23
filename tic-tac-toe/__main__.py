from __future__ import print_function, division
import pyglet, time
from game import Game
from ai import *
from grid import Grid

def main():
    # game = Game()
    # pyglet.app.run()

    ai = Minimax()
    ai2 = Minimax()
    grid = Grid()

    grid.grid = [[0,1,0],[0,0,0],[2,0,0]]
    # grid.grid = [[1,0,0],[0,2,0],[0,0,0]]
    # print(ai.make_move(grid.grid, False))

    winner = Grid.check_win( grid.grid )

    while winner == 0:
        # r, c = int(input()), int(input())

        # grid.grid = Grid.make_move( r, c, grid.grid, True )
        ai_move   = ai2.make_move(grid.grid, True)
        grid.grid = Grid.make_move( ai_move[0], ai_move[1], grid.grid, True )
        print(grid, '\n')

        winner = Grid.check_win( grid.grid )
        if winner == 0:
            ai_move   = ai.make_move(grid.grid, False)
            grid.grid = Grid.make_move( ai_move[0], ai_move[1], grid.grid, False )
            # print(ai.make_move(grid, False))
            print(grid, '\n')

        winner = Grid.check_win( grid.grid )
        if winner != 0:
            if winner == -1:
                print("Tie! It's a cat's eye.")
            else:
                print('Player {} won!'.format(winner))

    # grid.grid = Grid.make_move( 1, 1, grid.grid, True )
    # start = time.time()
    # print(ai.make_move(grid.grid, False))
    # print("{:0.3f}".format((time.time()-start)))

if __name__ == '__main__':
    main()
