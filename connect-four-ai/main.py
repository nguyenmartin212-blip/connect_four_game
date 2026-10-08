from game.game_manager import play_game

from agents.human_agent import human_agent
from agents.think3_agent import think3_agent


def main():
    print("=" * 40)
    print("CONNECT FOUR AI")
    print("Human vs Think-3 AI")
    print("=" * 40)

    winner = play_game(
        human_agent,
        think3_agent,
        render=True
    )

    if winner == 1:
        print("Red wins!")

    elif winner == -1:
        print("Yellow Think-3 AI wins!")

    else:
        print("Draw!")


if __name__ == "__main__":
    main()