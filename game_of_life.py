from typing import List

class GameOfLife:
    def __init__(self, board: List[List[int]]):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

    def update(self) -> None:
        copy_board = [[self.board[row][col] for col in range(self.cols)] for row in range(self.rows)]

        for row in range(self.rows):
            for col in range(self.cols):
                live_neighbors = 0
                for dr, dc in self.neighbors:
                    r, c = row + dr, col + dc
                    if 0 <= r < self.rows and 0 <= c < self.cols and copy_board[r][c] == 1:
                        live_neighbors += 1

                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    self.board[row][col] = 0
                elif copy_board[row][col] == 0 and live_neighbors == 3:
                    self.board[row][col] = 1

    def print_board(self, label="Board"):
        print(f"\n{label}:")
        for row in self.board:
            print(" ".join(str(cell) for cell in row))
        print()

    def plot_board(self):
        try:
            import matplotlib.pyplot as plt
            import numpy as np
            plt.imshow(self.board, cmap='binary')
            plt.title("Conway's Game of Life")
            plt.axis('off')
            plt.show()
        except ImportError:
            self.print_board("Matplotlib not found, falling back to console output")

    def animate_board(self, generations=5, delay=500):
        try:
            import pygame
            import time

            pygame.init()
            size = 20
            screen = pygame.display.set_mode((self.cols * size, self.rows * size))
            pygame.display.set_caption("Conway's Game of Life")

            for _ in range(generations):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

                screen.fill((255, 255, 255))
                for r in range(self.rows):
                    for c in range(self.cols):
                        color = (0, 0, 0) if self.board[r][c] == 1 else (255, 255, 255)
                        pygame.draw.rect(screen, color, (c * size, r * size, size, size))
                pygame.display.flip()
                time.sleep(delay / 1000.0)
                self.update()

            pygame.quit()

        except ImportError:
            print("Pygame not found, falling back to static preview.")
            self.plot_board()


if __name__ == "__main__":
    initial_board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]

    game = GameOfLife(initial_board)
    game.print_board("Initial Board")
    game.update()
    game.print_board("Next Generation")
    game.plot_board()
    # game.animate_board(generations=10)
