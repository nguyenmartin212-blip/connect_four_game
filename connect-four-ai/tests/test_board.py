from game.board import Board, RED


def test_empty_board():
    board = Board()
    assert len(board.get_valid_moves()) == 7


def test_drop_piece():
    board = Board()
    board.drop_piece(3, RED)
    assert board.grid[5][3] == RED


def test_vertical_win():
    board = Board()

    for _ in range(4):
        board.drop_piece(3, RED)

    assert board.check_winner(RED)


def test_horizontal_win():
    board = Board()

    for col in range(4):
        board.drop_piece(col, RED)

    assert board.check_winner(RED)
    