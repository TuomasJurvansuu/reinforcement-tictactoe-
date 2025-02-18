class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9  # 3x3 pelilauta listana

    def print_board(self):
        print("\n")
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("---|---|---")  # Erotusviivat riveille

    def make_move(self, square, player):
        if 0 <= square < 9 and self.board[square] == " ":
            self.board[square] = player  # Asetetaan X tai O laudalle
            print("Päivitetty lauta:", self.board)
            return True
        return False  # Estetään siirto, jos ruutu on jo varattu
