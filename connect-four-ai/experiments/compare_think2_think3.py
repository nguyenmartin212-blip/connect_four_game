from game.game_manager import play_game

from agents.think2_agent import think2_agent
from agents.think3_agent import think3_agent


TOTAL_GAMES = 1000


def run_benchmark():
    think3_wins = 0
    think2_wins = 0
    draws = 0

    print("=" * 50)
    print("THINK-3 vs THINK-2 BENCHMARK")
    print(f"Total games: {TOTAL_GAMES}")
    print("=" * 50)

    for game_number in range(TOTAL_GAMES):

        # Game chẵn:
        # Think-3 = Red = đi trước
        if game_number % 2 == 0:

            winner = play_game(
                think3_agent,
                think2_agent,
                render=False
            )

            if winner == 1:
                think3_wins += 1

            elif winner == -1:
                think2_wins += 1

            else:
                draws += 1

        # Game lẻ:
        # Think-2 = Red = đi trước
        # Think-3 = Yellow = đi sau
        else:

            winner = play_game(
                think2_agent,
                think3_agent,
                render=False
            )

            if winner == 1:
                think2_wins += 1

            elif winner == -1:
                think3_wins += 1

            else:
                draws += 1

        # Hiển thị tiến độ mỗi 100 game
        if (game_number + 1) % 100 == 0:
            print(
                f"Completed {game_number + 1}/{TOTAL_GAMES} games..."
            )

    print_results(
        think3_wins,
        think2_wins,
        draws
    )


def print_results(think3_wins, think2_wins, draws):

    print()
    print("=" * 50)
    print("RESULTS")
    print("=" * 50)

    print(f"Think-3 wins : {think3_wins}")
    print(f"Think-2 wins : {think2_wins}")
    print(f"Draws        : {draws}")

    print()

    think3_rate = think3_wins / TOTAL_GAMES * 100
    think2_rate = think2_wins / TOTAL_GAMES * 100
    draw_rate = draws / TOTAL_GAMES * 100

    print(f"Think-3 win rate : {think3_rate:.2f}%")
    print(f"Think-2 win rate : {think2_rate:.2f}%")
    print(f"Draw rate        : {draw_rate:.2f}%")

    print("=" * 50)


if __name__ == "__main__":
    run_benchmark()