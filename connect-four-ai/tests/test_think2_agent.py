from game.environment import ConnectFourEnv
from agents.think2_agent import think2_agent


def test_think2_blocks_vertical_win():
    env = ConnectFourEnv()

    # Red tạo 3 quân ở cột 1
    env.step(0)  # Red
    env.step(1)  # Yellow

    env.step(0)  # Red
    env.step(1)  # Yellow

    env.step(0)  # Red

    # Bây giờ tới Yellow.
    # Nếu Yellow không chặn cột 0,
    # Red sẽ thắng ở lượt sau.
    move = think2_agent(env)

    assert move == 0