from game.game_manager import play_game

from agents.human_agent import human_agent
from agents.think2_agent import think2_agent


def main():
    print("=" * 40)
    print("CONNECT FOUR AI")
    print("Human vs Think-2 AI")
    print("=" * 40)

    winner = play_game(
        human_agent,
        think2_agent,
        render=True
    )

    if winner == 1:
        print("Red wins!")
    elif winner == -1:
        print("Yellow Think-2 AI wins!")
    else:
        print("Draw!")


if __name__ == "__main__":
    main()