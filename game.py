import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors and Fonts
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 128)
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 70)

# States
START_SCREEN, FILE_SELECT_SCREEN, GAME_SCREEN, LEVEL_SELECT_SCREEN = 0, 1, 2, 3

# Initialize state
state = START_SCREEN

# File and Level Select Properties
file_options = ["File 1", "File 2", "File 3"]
selected_file = 0
level_options = ["Level 1", "Level 2", "Level 3"]
selected_level = 0

# Start Screen Text
title_text = title_font.render('Reality2D Engine', True, RED, WHITE)
title_text_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
start_text = font.render('Press Z to Start', True, WHITE)
start_text_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))

# Function to render file or level options
def render_options(options, selected):
    y = SCREEN_HEIGHT // 2 - 50
    for i, option in enumerate(options):
        text = font.render(option, True, WHITE if i == selected else BLUE)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, y))
        y += 50

# CD Drawing Function
def draw_cd(surface, position, radius, angle):
    pygame.draw.circle(surface, WHITE, position, radius)
    pygame.draw.line(surface, BLACK, position, (position[0] + radius * math.cos(angle), position[1] + radius * math.sin(angle)))

# CD Properties
cd_pos = (400, 300)
cd_radius = 50
cd_angle = 0

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == START_SCREEN:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                state = FILE_SELECT_SCREEN

        elif state == FILE_SELECT_SCREEN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_file = (selected_file - 1) % len(file_options)
                elif event.key == pygame.K_DOWN:
                    selected_file = (selected_file + 1) % len(file_options)
                elif event.key == pygame.K_RETURN:
                    print(f"File {selected_file + 1} selected")  # Placeholder for file selection logic
                    state = LEVEL_SELECT_SCREEN

        elif state == LEVEL_SELECT_SCREEN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_level = (selected_level - 1) % len(level_options)
                elif event.key == pygame.K_DOWN:
                    selected_level = (selected_level + 1) % len(level_options)
                elif event.key == pygame.K_RETURN:
                    print(f"Level {selected_level + 1} selected")  # Placeholder for level selection logic
                    state = GAME_SCREEN

    # Clear screen
    screen.fill(BLACK)

    if state == START_SCREEN:
        screen.blit(title_text, title_text_rect)
        screen.blit(start_text, start_text_rect)

    elif state == FILE_SELECT_SCREEN or state == LEVEL_SELECT_SCREEN:
        render_options(file_options if state == FILE_SELECT_SCREEN else level_options, 
                       selected_file if state == FILE_SELECT_SCREEN else selected_level)

    elif state == GAME_SCREEN:
        # Update and draw CD
        cd_angle += 0.05
        draw_cd(screen, cd_pos, cd_radius, cd_angle)
        # Main game logic goes here

    # Update screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
