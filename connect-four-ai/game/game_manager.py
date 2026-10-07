from game.environment import ConnectFourEnv


def play_game(player1, player2, render=True):
    env = ConnectFourEnv()
    env.reset()

    players = {
        1: player1,
        -1: player2
    }

    if render:
        env.render()

    while not env.done:
        current_player = env.current_player
        agent = players[current_player]

        move = agent(env)

        _, reward, done, _ = env.step(move)

        if render:
            env.render()

    winner = env.current_player if reward == 1 else 0

    return winner