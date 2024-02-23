import pygame
import numpy as np

# Constants
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Set the dimensions of each cell and the size of the grid
CELL_SIZE = 10
GRID_WIDTH = 80
GRID_HEIGHT = 60

# Initialize the pygame module
pygame.init()

# Set the size of the screen
SCREEN_SIZE = (GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Conway's Game of Life")

# Function to initialize the grid randomly
def initialize_grid():
    grid = np.random.choice([0, 1], size=(GRID_WIDTH, GRID_HEIGHT), p=[0.5, 0.5])
    return grid

# Function to draw the grid
def draw_grid(grid, view_x, view_y):
    screen.fill(BLACK)
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if grid[x, y] == 1:
                pygame.draw.rect(screen, GREEN, (x * CELL_SIZE - view_x, y * CELL_SIZE - view_y, CELL_SIZE, CELL_SIZE))
    pygame.display.update()

# Function to update the grid based on Conway's rules
def update_grid(grid):
    new_grid = grid.copy()
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            # Count neighbors
            neighbors = sum(grid[(x+i)%GRID_WIDTH, (y+j)%GRID_HEIGHT] for i in [-1, 0, 1] for j in [-1, 0, 1] if (i != 0 or j != 0))
            # Apply Conway's rules
            if grid[x, y] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[x, y] = 0
            elif grid[x, y] == 0 and neighbors == 3:
                new_grid[x, y] = 1
    return new_grid

# Main function to run the game
def main():
    # Initialize grid
    grid = initialize_grid()
    view_x = 0
    view_y = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:  # Check if left mouse button is pressed
                    print("Mouse moved while left button pressed")
                    mouse_rel = pygame.mouse.get_rel()
                    view_x += mouse_rel[0]
                    view_y += mouse_rel[1]

                    # Clamp view position to grid bounds
                    view_x = max(0, min(view_x, GRID_WIDTH * CELL_SIZE - SCREEN_SIZE[0]))
                    view_y = max(0, min(view_y, GRID_HEIGHT * CELL_SIZE - SCREEN_SIZE[1]))

        # Update grid and draw
        grid = update_grid(grid)
        draw_grid(grid, view_x, view_y)

        pygame.time.delay(100)  # Delay to control speed
    pygame.quit()

if __name__ == "__main__":
    main()