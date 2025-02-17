class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9  # 3x3 pelilauta yksinkertaisena listana

    def print_board(self):
        for i in range(0, 9, 3):
            print(self.board[i], "|", self.board[i + 1], "|", self.board[i + 2])