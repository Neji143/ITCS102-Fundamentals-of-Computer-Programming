# ============================================================
# SNAKE GAME 
# Arrow keys or WASD to move. Eat red food, avoid purple poison & rocks
# P = pause, R = play again, Q = quit
# ============================================================
import random
import pygame

# ============================================================
# PART 1: GAME SETTINGS  (safe to change: start here!)
# ============================================================
GAME_TITLE = "Neill's Snake"
CELL_SIZE = 25          # size of one square, in pixels
GRID_WIDTH = 20        # how many squares across
GRID_HEIGHT = 20        # how many squares down
INITIAL_SPEED = 10      # starting speed
START_LENGTH = 3        # how long the snake is at the start
POINTS_PER_FOOD = 1     # score for each food eaten
GROW_PER_FOOD = 1       # how many squares the snake grows per food
WALLS_KILL = False      # False = snake goes through walls to the other side

# Colors are (red, green, blue), each from 0 to 255
BACKGROUND_COLOR = (154, 205, 50)
GRID_COLOR = (32, 38, 56)
SNAKE_COLOR = (255, 204, 203)
HEAD_COLOR = (165, 42, 42)
FOOD_COLOR = (255, 140, 0)
POISON_COLOR = (180, 70, 255)
TEXT_COLOR = (240, 240, 240)
ROCK_COLOR = (130, 130, 140)
BASE_ROCKS = [(6, 5), (7, 5), (8, 5), (15, 12), (16, 12), (17, 12)]

# ============================================================
# PART 2: SETUP
# ============================================================
pygame.init()
WIDTH = CELL_SIZE * GRID_WIDTH
HEIGHT = CELL_SIZE * GRID_HEIGHT
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_TITLE)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# ============================================================
# PART 3: FUNCTIONS
# ============================================================
def get_empty_spot(blocked_spots):
    """Pick a random empty square not in blocked_spots."""
    while True:
        spot = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if spot not in blocked_spots:
            return spot


def new_game():
    """Return a fresh game state."""
    start_x = GRID_WIDTH // 2
    start_y = GRID_HEIGHT // 2
    snake = []
    for i in range(START_LENGTH):
        snake.append((start_x - i, start_y))    # head is snake[0]
    direction = (1, 0)                          # moving right
    rocks = list(BASE_ROCKS)
    food = get_empty_spot(snake + rocks)
    poison = get_empty_spot(snake + rocks + [food])
    return snake, direction, rocks, food, poison, 0, 0, INITIAL_SPEED, 1


def draw_square(position, color):
    """Draw one grid square at (x, y) grid position."""
    x, y = position
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect, border_radius=5)


def draw_circle_item(position, color):
    """Draw a circular item at (x, y) grid position."""
    center = (position[0] * CELL_SIZE + CELL_SIZE // 2, position[1] * CELL_SIZE + CELL_SIZE // 2)
    pygame.draw.circle(screen, color, center, CELL_SIZE // 2)


def draw_text(text, y):
    """Draw text centered across the screen at height y."""
    image = font.render(text, True, TEXT_COLOR)
    screen.blit(image, (WIDTH // 2 - image.get_width() // 2, y))


def draw_game(snake, rocks, food, poison, score, high_score, level):
    """Draw the background, grid, rocks, items, snake, and HUD."""
    screen.fill(BACKGROUND_COLOR)
    for x in range(0, WIDTH, CELL_SIZE):        # grid lines
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))

    for rock in rocks:
        draw_square(rock, ROCK_COLOR)

    draw_circle_item(food, FOOD_COLOR)
    draw_circle_item(poison, POISON_COLOR)

    for part in snake[1:]:
        draw_square(part, SNAKE_COLOR)
    draw_square(snake[0], HEAD_COLOR)

    draw_text(f"Score: {score}   |   Level: {level}", 10)
    draw_text(f"Best: {high_score}", 40)


# ============================================================
# PART 4: THE GAME LOOP  (events -> update -> draw)
# ============================================================
snake, direction, rocks, food, poison, score, grow, speed, level = new_game()
high_score = 0
game_over = False
paused = False
running = True

while running:
    # ---- 1. EVENTS: read the keyboard ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_r:             # R = play again
                    snake, direction, rocks, food, poison, score, grow, speed, level = new_game()
                    game_over = False
                    paused = False
                elif event.key == pygame.K_q:           # Q = quit
                    running = False
            elif event.key == pygame.K_p:               # P = toggle pause
                paused = not paused
            elif not paused:
                # The "!=" checks stop the snake from turning back into itself
                if event.key in (pygame.K_UP, pygame.K_w) and direction != (0, 1):
                    direction = (0, -1)
                elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != (0, -1):
                    direction = (0, 1)
                elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != (-1, 0):
                    direction = (1, 0)

    # ---- 2. UPDATE: move the snake and check what happened ----
    if not game_over and not paused:
        head_x, head_y = snake[0]
        new_head = (head_x + direction[0], head_y + direction[1])

        if WALLS_KILL:
            if new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT:
                game_over = True
        else:                                           # wrap around
            new_head = (new_head[0] % GRID_WIDTH, new_head[1] % GRID_HEIGHT)

        if new_head in snake or new_head in rocks:      # hit itself or a rock
            game_over = True

        if not game_over:
            snake.insert(0, new_head)                   # add the new head

            if new_head == food:                        # ate regular red food
                score = score + POINTS_PER_FOOD
                grow = grow + GROW_PER_FOOD
                speed = speed + 1

                # Level up every 5 points and spawn a new rock
                new_level = (score // 5) + 1
                if new_level > level:
                    level = new_level
                    rocks.append(get_empty_spot(snake + rocks + [food, poison]))

                food = get_empty_spot(snake + rocks + [poison])
                poison = get_empty_spot(snake + rocks + [food])

            elif new_head == poison:                    
                score = max(0, score - 2)
                poison = get_empty_spot(snake + rocks + [food])
                if len(snake) > 2:
                    snake.pop()                         
                else:
                    game_over = True                    

            if grow > 0:
                grow = grow - 1                         
            else:
                if len(snake) > 1:
                    snake.pop()                         

    if score > high_score:
        high_score = score

    draw_game(snake, rocks, food, poison, score, high_score, level)

    if paused and not game_over:
        draw_text("PAUSED (Press P to resume)", HEIGHT // 2 - 20)

    if game_over:
        draw_text("GAME OVER", HEIGHT // 2 - 40)
        draw_text("Score: " + str(score) + "   R = play again   Q = quit", HEIGHT // 2)

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()