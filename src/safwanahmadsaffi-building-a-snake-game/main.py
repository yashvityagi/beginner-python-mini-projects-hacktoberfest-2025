import pygame
import sys
import random

# ---------- Config ----------
CELL_SIZE = 20
CELL_NUMBER = 30  # grid will be CELL_NUMBER x CELL_NUMBER
WIDTH = CELL_SIZE * CELL_NUMBER
HEIGHT = CELL_SIZE * CELL_NUMBER
FPS_START = 10
FPS_ACCEL = 0.5  # increase FPS as snake grows
# ----------------------------

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (40, 40, 40)
YELLOW = (230, 230, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

def random_cell(exclude):
    while True:
        x = random.randint(0, CELL_NUMBER - 1)
        y = random.randint(0, CELL_NUMBER - 1)
        if (x, y) not in exclude:
            return (x, y)

def draw_rect_cell(pos, color):
    rect = pygame.Rect(pos[0]*CELL_SIZE, pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)

def show_text(text, pos, color=WHITE):
    surf = font.render(text, True, color)
    screen.blit(surf, pos)

def main():
    direction = (1, 0)  # start moving to the right
    snake = [(CELL_NUMBER//2 - i, CELL_NUMBER//2) for i in range(3)]  # head is snake[0]
    food = random_cell(set(snake))
    score = 0
    fps = FPS_START
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_w, pygame.K_UP) and direction != (0, 1):
                    direction = (0, -1)
                elif event.key in (pygame.K_s, pygame.K_DOWN) and direction != (0, -1):
                    direction = (0, 1)
                elif event.key in (pygame.K_a, pygame.K_LEFT) and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key in (pygame.K_d, pygame.K_RIGHT) and direction != (-1, 0):
                    direction = (1, 0)
                elif event.key == pygame.K_r and game_over:
                    # restart
                    return main()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        if not game_over:
            # move snake
            new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

            # wrap-around behavior (optional). To disable wrapping and make walls deadly,
            # change below to set game_over True if head is outside grid.
            new_head = (new_head[0] % CELL_NUMBER, new_head[1] % CELL_NUMBER)

            # check collisions
            if new_head in snake:
                game_over = True
            else:
                snake.insert(0, new_head)
                if new_head == food:
                    score += 1
                    # speed up slightly each time food eaten
                    fps = FPS_START + FPS_ACCEL * score
                    food = random_cell(set(snake))
                else:
                    snake.pop()

        # draw
        screen.fill(BLACK)
        draw_grid()
        # food
        draw_rect_cell(food, RED)
        # snake
        for i, segment in enumerate(snake):
            color = YELLOW if i == 0 else GREEN
            draw_rect_cell(segment, color)

        # HUD
        show_text(f"Score: {score}", (10, 10))
        if game_over:
            # overlay
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))
            screen.blit(overlay, (0, 0))
            show_text("Game Over", (WIDTH//2 - 90, HEIGHT//2 - 40), color=WHITE)
            show_text("Press R to restart or ESC to quit", (WIDTH//2 - 200, HEIGHT//2 + 5), color=WHITE)

        pygame.display.flip()
        clock.tick(max(1, int(fps)))

if __name__ == "__main__":
    main()
