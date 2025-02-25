import pygame
from game import TicTacToe
from agent import SmartAgent

pygame.init()

# Ikkunan asetukset
WIDTH, HEIGHT = 500, 500
WHITE = (255, 255, 255)
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE
LINE_WIDTH = 10
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
FONT = pygame.font.Font(None, 120)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ristinolla")

game = TicTacToe()
current_player = "X"
agent = SmartAgent("O",game)

def draw_grid():
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)

def draw_marks():
    for i, mark in enumerate(game.board):
        if mark != " ":
            row, col = divmod(i, GRID_SIZE)
            x = col * CELL_SIZE + CELL_SIZE // 3
            y = row * CELL_SIZE + CELL_SIZE // 6
            text = FONT.render(mark, True, BLACK)
            screen.blit(text, (x, y))
                
def cell_from_mouse(pos):
    x, y = pos
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    return row * GRID_SIZE + col

running = True
while running:
    screen.fill(WHITE)
    draw_grid()
    draw_marks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cell = cell_from_mouse(event.pos)
            if game.board[cell] == " ":
                game.board[cell] = current_player
                winner = game.check_winner()
                if winner:
                    print(f"Pelaaja {winner} voitti!")
                    running = False
                elif game.is_draw():
                    print("Peli päättyi tasapeliin!")
                    running = False
                if running:
                    current_player = "O"
    if running and current_player == "O":
        pygame.time.delay(500)
        ai_move = agent.choose_move(game.board)
        if ai_move is not None:
            game.board[ai_move] = "O"
            winner = game.check_winner()
            if winner:
                print(f"Pelaaja {winner} voitti!")
                running = False
            elif game.is_draw():
                print("Peli päättyi tasapeliin!")
                running = False
            if running:
                current_player = "X"
    

    pygame.display.flip()

pygame.quit()
