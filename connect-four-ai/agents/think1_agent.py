from copy import deepcopy


def think1_agent(env):
    # thử từng nước đi hợp lệ
    for move in env.valid_moves:
        env_copy = deepcopy(env)

        _, reward, done, _ = env_copy.step(move)

        # nếu nước đi này thắng ngay thì chọn
        if done and reward == 1:
            return move

    # nếu không có nước thắng ngay thì random
    return env.sample()