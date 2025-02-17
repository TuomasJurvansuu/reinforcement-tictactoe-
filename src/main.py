from game import TicTacToe

game = TicTacToe()
game.print_board()

while True:
    move = int(input("Valitse ruutu (0-8): "))