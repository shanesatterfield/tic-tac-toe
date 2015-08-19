from __future__ import print_function, division
import pyglet, random

class Game( pyglet.window.Window ):
    def __init__( self ):
        self.restart()
        super(Game, self).__init__( self.grid_height, self.grid_height )
        self.images = [ pyglet.image.load('res/cross.png'), pyglet.image.load('res/circle.png') ]

    def on_draw( self ):
        pyglet.window.Window.flip( self )
        self.clear()
        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                if self.grid[row][column] != 0:
                    self.images[self.grid[row][column]-1].blit( column*self.tile_height, (2-row)*self.tile_width )

    def on_mouse_release( self, x, y, button, modifiers ):
        if button == pyglet.window.mouse.LEFT:
            self.make_move( (self.grid_height-y) // self.tile_height, x // self.tile_width )

            winner = self.check_win()
            if winner != 0:
                print('Player {} won!'.format(winner))
                super(Game, self).close()

    def restart( self ):
        self.first_player = True
        self.tile_width, self.tile_height = 32, 32
        self.grid_width, self.grid_height = self.tile_width * 3, self.tile_height * 3
        self.grid = [ [ 0 for _ in range(3) ] for _ in range(3) ]

    def make_move( self, row, column ):
        if row < 0 or row >= len(self.grid) or column < 0 or column >= len(self.grid[0]):
            raise IndexError('The row or column you specified is not within the correct range.')

        if self.grid[row][column] is not 0:
            raise ValueError('The space you selected is already occupied.')

        self.grid[row][column] = 1 if self.first_player else 2
        self.first_player = not self.first_player

    def check_win( self ):
        grid = list(self.grid)
        for _ in range(2):
            for i in range(3):
                if grid[i][0] == grid[i][1] and grid[i][1] == grid[i][2]:
                    return grid[i][0]
            grid = list(zip(*grid))
            grid = list(map(list, grid))

        if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] or \
           grid[2][0] == grid[1][1] and grid[1][1] == grid[0][2]:
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
