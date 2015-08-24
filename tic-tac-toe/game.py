from __future__ import print_function, division
import pyglet, random
from ai import *
from grid import Grid

class Game( pyglet.window.Window ):
    def __init__( self ):
        self.restart()
        super(Game, self).__init__( self.grid_height, self.grid_height )
        self.images = [
            pyglet.image.load('res/cross.png'),
            pyglet.image.load('res/circle.png'),
            pyglet.image.load('res/line_horizontal.png'),
            pyglet.image.load('res/line_vertical.png'),
            pyglet.image.load('res/text_background.png')
        ]
        self.game_over = False

        pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
        pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
        pyglet.gl.glClearColor(255,255,255,0)

    def restart( self ):
        self.first_player = True
        self.tile_width, self.tile_height = 128, 128
        self.grid_width, self.grid_height = self.tile_width * 3, self.tile_height * 3
        self.grid = [ [ 0 for _ in range(3) ] for _ in range(3) ]

        self.ai = Minimax()


    def on_draw( self ):
        pyglet.window.Window.flip( self )
        self.clear()

        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                if self.grid[row][column] != 0:
                    self.images[self.grid[row][column]-1].blit( column*self.tile_height, (2-row)*self.tile_width )

        self.images[2].blit(10,127)
        self.images[2].blit(10,255)

        self.images[3].blit(127,10)
        self.images[3].blit(255,10)

        if self.game_over is True:
            self.images[4].blit(0,0)
            self.label.draw()

    def on_mouse_release( self, x, y, button, modifiers ):
        if button == pyglet.window.mouse.LEFT and not self.game_over:
            try:

                self.grid = Grid.make_move( (self.grid_height-y) // self.tile_height, x // self.tile_width, self.grid, self.first_player )
                winner = Grid.check_win( self.grid )
                self.first_player = not self.first_player
                self.dispatch_event('on_draw')
                self.flip()

                if winner == 0:
                    r, c = self.ai.make_move( self.grid, self.first_player )
                    self.grid = Grid.make_move(r, c, self.grid, self.first_player)
                    self.first_player = not self.first_player
                    self.dispatch_event('on_draw')
                    self.flip()

            except Exception as e:
                print(e)

            winner = Grid.check_win( self.grid )
            if winner != 0:
                label_text = None
                if winner == -1:
                    label_text = "Tie!"
                else:
                    label_text = 'Player {} won!'.format(winner)

                self.game_over = True
                self.label = pyglet.text.Label(
                    label_text,
                    font_name='Arial',
                    font_size=45,
                    x=self.width//2,
                    y=self.height//2,
                    anchor_x='center',
                    anchor_y='center',
                    color=(0,0,0,255),
                    bold=True
                )
                # super(Game, self).close()
