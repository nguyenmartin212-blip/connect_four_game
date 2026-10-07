import numpy as np

ROWS = 6
COLS = 7

EMPTY = 0
RED = 1
YELLOW = -1


class Board:
    def __init__(self):
        self.grid = np.zeros((ROWS, COLS), dtype=int)

    def reset(self):
        self.grid.fill(EMPTY)

    def is_valid_move(self, column):
        return 0 <= column < COLS and self.grid[0][column] == EMPTY

    def get_valid_moves(self):
        return [
            col
            for col in range(COLS)
            if self.is_valid_move(col)
        ]

    def drop_piece(self, column, player):
        if not self.is_valid_move(column):
            return False

        for row in range(ROWS - 1, -1, -1):
            if self.grid[row][column] == EMPTY:
                self.grid[row][column] = player
                return True

        return False

    def is_full(self):
        return len(self.get_valid_moves()) == 0

    def check_winner(self, player):
        # Horizontal
        for row in range(ROWS):
            for col in range(COLS - 3):
                if all(self.grid[row][col + i] == player for i in range(4)):
                    return True

        # Vertical
        for row in range(ROWS - 3):
            for col in range(COLS):
                if all(self.grid[row + i][col] == player for i in range(4)):
                    return True

        # Diagonal \
        for row in range(ROWS - 3):
            for col in range(COLS - 3):
                if all(self.grid[row + i][col + i] == player for i in range(4)):
                    return True

        # Diagonal /
        for row in range(3, ROWS):
            for col in range(COLS - 3):
                if all(self.grid[row - i][col + i] == player for i in range(4)):
                    return True

        return False

    def __str__(self):
        return str(self.grid)