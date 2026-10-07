from game.game_manager import play_game

from agents.human_agent import human_agent
from agents.think1_agent import think1_agent


def main():
    print("=" * 40)
    print("CONNECT FOUR AI")
    print("Human vs Think-1 AI")
    print("=" * 40)

    winner = play_game(
        human_agent,
        think1_agent,
        render=True
    )

    if winner == 1:
        print("Red wins!")

    elif winner == -1:
        print("Yellow AI wins!")

    else:
        print("Draw!")


if __name__ == "__main__":
    main()