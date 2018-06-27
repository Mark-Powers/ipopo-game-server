#!/usr/bin/python
# -- Content-Encoding: UTF-8 --

from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
    Validate, Invalidate, Instantiate

@ComponentFactory("game_tictactoe_factory")
@Provides("game_service")
@Instantiate("game_tictactoe_instance")

class Game(object):

    def __init__(self):
        self.board = []
        
    @Validate
    def validate(self, context):
        for x in range(3):
            self.board.append([' ']*3)
        print('TicTacToe Game has been loaded')


    @Invalidate
    def invalidate(self,context):
        self.board = None
        

    def getBoard(self, x, y):
        return self.board[x][y];

