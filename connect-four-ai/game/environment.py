import random

from game.board import Board, RED


class ConnectFourEnv:
    def __init__(self):
        self.board = Board()

        self.current_player = RED
        self.reward = 0
        self.done = False
        self.info = ""

    @property
    def state(self):
        return self.board.grid

    @property
    def valid_moves(self):
        return self.board.get_valid_moves()

    def reset(self):
        self.board.reset()

        self.current_player = RED
        self.reward = 0
        self.done = False
        self.info = ""

        return self.state.copy()

    def sample(self):
        if not self.valid_moves:
            return None

        return random.choice(self.valid_moves)

    def step(self, action):
        if self.done:
            raise ValueError("Game is already finished.")

        if action not in self.valid_moves:
            raise ValueError("Invalid move.")

        player = self.current_player

        self.board.drop_piece(action, player)

        if self.board.check_winner(player):
            self.reward = 1
            self.done = True

        elif self.board.is_full():
            self.reward = 0
            self.done = True

        else:
            self.reward = 0
            self.current_player *= -1

        return (
            self.state.copy(),
            self.reward,
            self.done,
            self.info
        )

    def render(self):
        symbols = {
            0: ".",
            1: "R",
            -1: "Y"
        }

        print()

        for row in self.state:
            print(
                " ".join(
                    symbols[cell]
                    for cell in row
                )
            )

        print("1 2 3 4 5 6 7")
        print()

    def close(self):
        pass