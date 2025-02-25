import random

class SmartAgent:
    def __init__(self, symbol, game):
        self.symbol = symbol
        self.game = game

    def choose_move(self, board):
        available_moves = [i for i, square in enumerate(board) if square == " "]
        
        for move in available_moves:
            board[move] = self.symbol
            if self.game.check_winner() == self.symbol:
                board[move] = " "
                return move
            board[move] = " "
        
        return random.choice(available_moves) if available_moves else None