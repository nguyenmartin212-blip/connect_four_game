from game.environment import ConnectFourEnv
from game.board import RED, YELLOW


def test_initial_state():
    env = ConnectFourEnv()

    assert len(env.valid_moves) == 7
    assert env.current_player == RED
    assert env.done is False


def test_turn_switch():
    env = ConnectFourEnv()

    env.step(3)

    assert env.current_player == YELLOW


def test_vertical_win():
    env = ConnectFourEnv()

    env.step(0)
    env.step(1)

    env.step(0)
    env.step(1)

    env.step(0)
    env.step(1)

    _, reward, done, _ = env.step(0)

    assert done is True
    assert reward == 1