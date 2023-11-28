import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions and settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Color definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 128)

# Font settings
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 70)

# Application states
START_SCREEN, FILE_SELECT_SCREEN, GAME_SCREEN, LEVEL_SELECT_SCREEN = 0, 1, 2, 3
state = START_SCREEN  # Initial state

# File and Level selection properties
file_options = ["File 1", "File 2", "File 3"]
selected_file = 0
level_options = ["Level 1", "Level 2", "Level 3"]
selected_level = 0

# Start screen text and positioning
title_text = title_font.render('Reality2D Engine', True, RED, WHITE)
title_text_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
start_text = font.render('Press Z to Start', True, WHITE)
start_text_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))

# Function to render file or level selection options
def render_options(options, selected):
    y = SCREEN_HEIGHT // 2 - 50
    for i, option in enumerate(options):
        text_color = WHITE if i == selected else BLUE
        text = font.render(option, True, text_color)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, y))
        y += 50

# CD drawing function
def draw_cd(surface, position, radius, angle):
    pygame.draw.circle(surface, WHITE, position, radius)
    end_pos = (position[0] + radius * math.cos(angle), position[1] + radius * math.sin(angle))
    pygame.draw.line(surface, BLACK, position, end_pos)

# CD properties for animation
cd_pos = (400, 300)
cd_radius = 50
cd_angle = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Start Screen: Press 'Z' to proceed to File Select Screen
        if state == START_SCREEN and event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            state = FILE_SELECT_SCREEN

        # File Select Screen: Navigate and select a file
        elif state == FILE_SELECT_SCREEN and event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                selected_file = (selected_file + (-1 if event.key == pygame.K_UP else 1)) % len(file_options)
            elif event.key == pygame.K_RETURN:
                print(f"File {selected_file + 1} selected")  # Placeholder for file selection logic
                state = LEVEL_SELECT_SCREEN

        # Level Select Screen: Navigate and select a level
        elif state == LEVEL_SELECT_SCREEN and event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                selected_level = (selected_level + (-1 if event.key == pygame.K_UP else 1)) % len(level_options)
            elif event.key == pygame.K_RETURN:
                print(f"Level {selected_level + 1} selected")  # Placeholder for level selection logic
                state = GAME_SCREEN

    # Rendering based on current state
    screen.fill(BLACK)
    if state == START_SCREEN:
        screen.blit(title_text, title_text_rect)
        screen.blit(start_text, start_text_rect)
    elif state in [FILE_SELECT_SCREEN, LEVEL_SELECT_SCREEN]:
        options = file_options if state == FILE_SELECT_SCREEN else level_options
        selected = selected_file if state == FILE_SELECT_SCREEN else selected_level
        render_options(options, selected)
    elif state == GAME_SCREEN:
        # Game screen content (e.g., CD animation)
        cd_angle += 0.05
        draw_cd(screen, cd_pos, cd_radius, cd_angle)

    # Update the display
    pygame.display.update()

# Clean up and exit
pygame.quit()
sys.exit()
