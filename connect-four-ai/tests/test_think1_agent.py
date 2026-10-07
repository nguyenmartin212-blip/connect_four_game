from game.environment import ConnectFourEnv
from agents.think1_agent import think1_agent


def test_think1_takes_winning_move():
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
    env.step(2)

    # Yellow
    env.step(1)

    # Bây giờ Red đánh tạm để chuyển lượt sang Yellow
    env.step(3)

    # Yellow đang có 3 quân ở cột 2
    # nên cột index 1 là nước thắng ngay
    move = think1_agent(env)

    assert move == 1