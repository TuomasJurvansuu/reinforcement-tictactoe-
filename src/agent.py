import random

class RandomAgent:
    def __init__(self, symbol):
        self.symbol = symbol

    def choose_move(self, board):
        available_moves = [i for i, square in enumerate(board) if square == " "]
        return random.choice(available_moves) if available_moves else None