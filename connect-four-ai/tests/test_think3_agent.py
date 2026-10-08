from game.environment import ConnectFourEnv
from agents.think3_agent import think3_agent


def test_think3_takes_immediate_win():
    env = ConnectFourEnv()

    # Red
    env.step(0)

    # Yellow
    env.step(1)

    # Red
    env.step(0)

    # Yellow
    env.step(1)

    # Red
    env.step(0)

    # Yellow
    env.step(2)

    # Red có thể thắng ở cột 0
    move = think3_agent(env)

    assert move == 0


def test_think3_blocks_opponent():
    env = ConnectFourEnv()

    # Red tạo 3 quân dọc ở cột 0
    env.step(0)
    env.step(1)

    env.step(0)
    env.step(1)

    env.step(0)

    # tới lượt Yellow
    # Yellow phải block cột 0
    move = think3_agent(env)

    assert move == 0


def test_think3_prefers_center_on_empty_board():
    env = ConnectFourEnv()

    move = think3_agent(env)

    # index 3 = cột số 4
    assert move == 3