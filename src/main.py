from game import TicTacToe

game = TicTacToe()
game.print_board()

current_player = "X"

while True:
    move = int(input(f"Pelaaja {current_player}, valitse ruutu (0-8): "))
    
    if game.make_move(move, current_player):
        game.print_board()
        current_player = "O" if current_player == "X" else "X"
        winner = game.check_winner()
        if winner:
            print(f"Pelaaja {winner} voitti!")
            break
    else:
        print("Virheellinen siirto, yritä uudelleen.")