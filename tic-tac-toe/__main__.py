from __future__ import print_function, division
from game import Game

def main():
    game = Game()

    first_player = True
    for n in range(9):
        game.render()
        row, column = int(input()), int(input())
        game.make_move( row, column, first_player )

        winner = game.check_win()
        if winner != 0:
            print('Player {} won!'.format(winner))

        first_player = not first_player

if __name__ == '__main__':
    main()
