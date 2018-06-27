#!/usr/bin/python
# -- Content-Encoding: UTF-8 --

from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
    Validate, Invalidate, Instantiate

@ComponentFactory("game_tictactoe_factory")
@Provides("game_tictactoe_service")
@Instantiate("game_tictactoe_instance")

class Game(object):

    def __init__(self):
        self.board = []
        self.players = ['X', 'O']
        self.turn = 0;
        
    @Validate
    def validate(self, context):
        for x in range(3):
            self.board.append(['_']*3)

    @Invalidate
    def invalidate(self,context):
        self.board = None

    def setPos(self, r, c):
        if(self.board[r][c] == '_'):
            self.board[r][c] = self.players[self.turn]
            self.turn += 1;
            self.turn %= 2;

    def checkWinner(self):
        for r in range(len(self.board)):
            if self.board[r][0] == self.board[r][1] \
                and self.board[r][0] == self.board[r][2] \
                and self.board[r][0] != '_':
                return True
        for c in range(len(self.board[0])):
            if self.board[0][c] == self.board[1][c] \
                and self.board[0][c] == self.board[2][c] \
                and self.board[r][0] != '_':
                return True
        if self.board[0][0] == self.board[1][1] \
           and self.board[0][0] == self.board[2][2] \
           and self.board[r][0] != '_':
            return True
        if self.board[0][2] == self.board[1][1] \
           and self.board[0][2] == self.board[2][0] \
           and self.board[r][0] != '_':
            return True

        return False

    def getPos(self, r, c):
        return self.board[r][c];








    

