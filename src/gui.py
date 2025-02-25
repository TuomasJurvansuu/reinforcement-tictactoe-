import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500

WHITE = (255, 255, 255)

GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE
LINE_WIDTH = 10
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ristinolla")

def draw_grid():
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)

running = True
while running:
    screen.fill(WHITE)
    draw_grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
