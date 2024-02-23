Conway's Game of Life

This is a Python implementation of Conway's Game of Life using the Pygame library.

Description
Conway's Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

In this implementation, the game is displayed on a grid with each cell being either alive or dead. The game follows the rules:

1. Underpopulation: A live cell with fewer than two live neighbors dies.
2. Survival: A live cell with two or three live neighbors survives to the next generation.
3. Overpopulation: A live cell with more than three live neighbors dies.
4. Reproduction: A dead cell with exactly three live neighbors becomes alive.

Controls (Currently Inoperative)
Left Mouse Button: Hold and drag to pan across the grid. (Currently not functional)
Note: Although the script detects left mouse button movements and prints "Mouse moved while left button pressed" in the terminal, the functionality to pan across the grid is currently not operational.

I might return to add the user interaction later.
