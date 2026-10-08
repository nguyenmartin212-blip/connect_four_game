from copy import deepcopy
from collections import Counter
import random


def find_immediate_win(env):
    """
    Tìm nước giúp người chơi hiện tại thắng ngay.
    """
    for move in env.valid_moves:
        env_copy = deepcopy(env)

        _, reward, done, _ = env_copy.step(move)

        if done and reward == 1:
            return move

    return None


def find_block_move(env):
    """
    Tìm nước mà đối thủ có thể dùng để thắng ngay,
    sau đó chặn nước đó.
    """
    current_player = env.current_player

    for move in env.valid_moves:
        env_copy = deepcopy(env)

        # Giả lập đổi sang lượt đối thủ
        env_copy.current_player = -current_player

        _, reward, done, _ = env_copy.step(move)

        if done and reward == 1:
            return move

    return None


def find_safe_moves(env):
    """
    Tìm các nước mà sau khi AI đánh,
    đối thủ không thể thắng ngay ở lượt kế tiếp.
    """
    safe_moves = []

    for move in env.valid_moves:
        env_copy = deepcopy(env)

        _, _, done, _ = env_copy.step(move)

        if done:
            safe_moves.append(move)
            continue

        opponent_can_win = False

        for opponent_move in env_copy.valid_moves:
            opponent_env = deepcopy(env_copy)

            _, reward, finished, _ = opponent_env.step(opponent_move)

            if finished and reward == 1:
                opponent_can_win = True
                break

        if not opponent_can_win:
            safe_moves.append(move)

    return safe_moves


def think3_agent(env):

    # ----------------------------------
    # 1. Chỉ còn một nước
    # ----------------------------------

    if len(env.valid_moves) == 1:
        return env.valid_moves[0]

    # ----------------------------------
    # 2. Có thể thắng ngay -> thắng
    # ----------------------------------

    winning_move = find_immediate_win(env)

    if winning_move is not None:
        return winning_move

    # ----------------------------------
    # 3. Opponent sắp thắng -> block
    # ----------------------------------

    block_move = find_block_move(env)

    if block_move is not None:
        return block_move

    # ----------------------------------
    # 4. Tìm các nước an toàn
    # ----------------------------------

    safe_moves = find_safe_moves(env)

    if not safe_moves:
        safe_moves = list(env.valid_moves)

    # ----------------------------------
    # 5. Ưu tiên cột giữa
    #
    # Trong code của chúng ta:
    # index 3 = cột số 4
    # ----------------------------------

    CENTER_COLUMN = 3

    if (
        CENTER_COLUMN in safe_moves
        and all(env.state[row][CENTER_COLUMN] == 0
                for row in range(6))
    ):
        return CENTER_COLUMN

    # ----------------------------------
    # 6. Look ahead 3 bước
    #
    # m1 = AI
    # m2 = opponent
    # m3 = AI
    # ----------------------------------

    winning_first_moves = []

    for m1 in safe_moves:

        env1 = deepcopy(env)

        _, _, done1, _ = env1.step(m1)

        if done1:
            continue

        # Opponent move
        for m2 in env1.valid_moves:

            env2 = deepcopy(env1)

            _, _, done2, _ = env2.step(m2)

            # Nếu opponent đã thắng thì đường này không tốt
            if done2:
                continue

            # AI move lần thứ hai
            for m3 in env2.valid_moves:

                env3 = deepcopy(env2)

                _, reward3, done3, _ = env3.step(m3)

                if done3 and reward3 == 1:
                    winning_first_moves.append(m1)

    # ----------------------------------
    # 7. Chọn m1 xuất hiện nhiều nhất
    # ----------------------------------

    if winning_first_moves:

        counter = Counter(winning_first_moves)

        best_score = max(counter.values())

        best_moves = [
            move
            for move, score in counter.items()
            if score == best_score
        ]

        # nếu hòa thì ưu tiên gần trung tâm
        best_moves.sort(
            key=lambda move: abs(move - CENTER_COLUMN)
        )

        return best_moves[0]

    # ----------------------------------
    # 8. Không tìm được chiến thuật
    # ----------------------------------

    return random.choice(safe_moves)