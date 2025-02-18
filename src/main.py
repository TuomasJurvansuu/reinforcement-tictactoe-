from game import TicTacToe

game = TicTacToe()
game.print_board()

while True:
    move = int(input("Valitse ruutu (0-8): "))
    print(f"Siirto: {move}, Pelaaja: X")
    if game.make_move(move, "X"):
        game.print_board()
    else:
        print("Virheellinen siirto, yritä uudelleen.")