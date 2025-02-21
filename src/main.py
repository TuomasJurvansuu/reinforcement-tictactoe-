from game import TicTacToe
from agent import RandomAgent  # Tuo AI-agentti

game = TicTacToe()
agent = RandomAgent("O")  # AI pelaa "O":na

game.print_board()
current_player = "X"

while True:
    if current_player == "X":
        move = int(input(f"Pelaaja {current_player}, valitse ruutu (0-8): "))
    else:
        move = agent.choose_move(game.board)  # AI valitsee siirron
        print(f"AI valitsi ruudun {move}")

    if game.make_move(move, current_player):
        game.print_board()
        
        winner = game.check_winner()
        if winner:
            print(f"Pelaaja {winner} voitti!")
            break

        if game.is_draw():
            print("Peli päättyi tasapeliin!")
            break

        current_player = "O" if current_player == "X" else "X"
    else:
        print("Virheellinen siirto, yritä uudelleen.")
