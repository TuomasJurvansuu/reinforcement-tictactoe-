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

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Vaakasuorat
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Pystysuorat
            (0, 4, 8), (2, 4, 6)  # Vinot
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                print(f"Voittoruudut: {combo}")  # Näyttää voittoruudut
                return self.board[combo[0]]
        return None

    def is_draw(self):
        return " " not in self.board
