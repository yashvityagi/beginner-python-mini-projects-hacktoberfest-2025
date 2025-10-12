import pygame
import random

pygame.init()
CELL_SIZE = 30
ROWS, COLS = 15, 20
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape the Maze")
clock = pygame.time.Clock()
DIRS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def generate_maze(rows, cols):
    maze = [[1 for _ in range(cols)] for _ in range(rows)]
    stack = [(0, 0)]
    visited = set([(0, 0)])
    maze[0][0] = 0
    while stack:
        x, y = stack[-1]
        neighbors = []
        for dx, dy in DIRS:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                neighbors.append((nx, ny))
        if neighbors:
            nx, ny = random.choice(neighbors)
            maze[x + (nx - x) // 2][y + (ny - y) // 2] = 0
            maze[nx][ny] = 0
            visited.add((nx, ny))
            stack.append((nx, ny))
        else:
            stack.pop()
    return maze

def draw_maze(maze, player_pos, exit_pos):
    for i in range(ROWS):
        for j in range(COLS):
            color = WHITE if maze[i][j] == 0 else BLACK
            pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (exit_pos[1]*CELL_SIZE, exit_pos[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, BLUE, (player_pos[1]*CELL_SIZE, player_pos[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
    maze = generate_maze(ROWS, COLS)
    player_pos = [0, 0]
    exit_pos = [ROWS - 1, COLS - 1]
    running = True
    while running:
        screen.fill(WHITE)
        draw_maze(maze, player_pos, exit_pos)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_UP]: dx, dy = -1, 0
        elif keys[pygame.K_DOWN]: dx, dy = 1, 0
        elif keys[pygame.K_LEFT]: dx, dy = 0, -1
        elif keys[pygame.K_RIGHT]: dx, dy = 0, 1
        new_x, new_y = player_pos[0] + dx, player_pos[1] + dy
        if 0 <= new_x < ROWS and 0 <= new_y < COLS and maze[new_x][new_y] == 0:
            player_pos = [new_x, new_y]
        if player_pos == exit_pos:
            print("🎉 You Escaped the Maze!")
            running = False
        clock.tick(10)
    pygame.quit()

if __name__ == "__main__":
    main()