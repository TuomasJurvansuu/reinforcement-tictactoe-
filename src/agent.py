import random

class SmartAgent:
    def __init__(self, symbol, game):
        self.symbol = symbol
        self.game = game
        self.opponent = "X" if symbol == "O" else "O"

    def choose_move(self, board):
        available_moves = [i for i, square in enumerate(board) if square == " "]
        # Voittosiirto jos mahdollista
        for move in available_moves:
            board[move] = self.symbol
            if self.game.check_winner() == self.symbol:
                board[move] = " "
                return move
            board[move] = " "
        # Pelaajan blokkaus
        for move in available_moves:
            board[move] = self.opponent
            if self.game.check_winner() == self.opponent:
                board[move] = " "
                return move
            board[move] = " "
        # keskelle siirto jos mahdollista
        if 4 in available_moves:
            return 4

        
        return random.choice(available_moves) if available_moves else None