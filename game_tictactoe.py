#!/usr/bin/python
# -- Content-Encoding: UTF-8 --

from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
    Validate, Invalidate, Instantiate

@ComponentFactory("game_tictactoe_factory")
@Provides("game_service")
@Insantiate("game_tictactoe_instance")

class Game(object):

    def __init__(self):
        self.board = []
        self.players = ['X', 'O']
        self.turn = 0;
        
    @Validate
    def validate(self, context):
        for x in range(3):
            self.board.append([' ']*3)
        print('TicTacToe Game has been loaded')

    @Invalidate
    def invalidate(self,context):
        self.board = None

    def setPos(self, r, c)
        if(self.board[r][c] == ' '):
            self.board[r][c] = self.players[turn]
            self.turn += 1;
            self.turn %= 2;

    def checkWinner():
        for r in range(len(self.board)):
            if self.board[r][0] == self.board[r][1] \
                and self.board[r][0] == self.board[r][2]:
                return True
        for c in range(len(self.board[0])):
            if self.board[0][c] == self.board[1][c] \
                and self.board[0][0] == self.board[2][c]:
                return True
        if self.board[0][0] == self.board[1][1] \
           and self.board[0][0] == self.board[2][2]:
            return True
        if self.board[0][2] == self.board[1][1] \
           and self.board[0][2] == self.board[2][0]:
            return True

        return False

    def getPos(self, r, c):
        return self.board[r][c];






    

