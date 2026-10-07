from copy import deepcopy
import random


def think2_agent(env):
    # 1. Nếu chỉ còn 1 nước hợp lệ
    if len(env.valid_moves) == 1:
        return env.valid_moves[0]

    # 2. Nếu AI có thể thắng ngay -> thắng luôn
    for move in env.valid_moves:
        env_copy = deepcopy(env)

        _, reward, done, _ = env_copy.step(move)

        if done and reward == 1:
            return move

    # 3. Kiểm tra nước cần block
    #
    # Ý tưởng:
    # AI thử một nước m1.
    # Sau đó giả sử opponent đánh m2.
    # Nếu opponent thắng sau m2,
    # thì m2 là cột cần block ngay từ bây giờ.
    for m1 in env.valid_moves:
        for m2 in env.valid_moves:
            if m1 == m2:
                continue

            env_copy = deepcopy(env)

            _, _, done1, _ = env_copy.step(m1)

            # Nếu AI đã kết thúc game thì bỏ qua
            if done1:
                continue

            if m2 not in env_copy.valid_moves:
                continue

            _, reward2, done2, _ = env_copy.step(m2)

            if done2 and reward2 == 1:
                # opponent thắng bằng m2
                # nên ta block m2 ngay
                if m2 in env.valid_moves:
                    return m2

    # 4. Tìm những nước cần tránh
    to_avoid = []

    for move in env.valid_moves:
        env_copy = deepcopy(env)

        # AI đánh move
        _, _, done, _ = env_copy.step(move)

        if done:
            continue

        # Sau nước này tới lượt opponent.
        # Kiểm tra opponent có thắng ngay không.
        for opponent_move in env_copy.valid_moves:
            env_copy2 = deepcopy(env_copy)

            _, reward, done, _ = env_copy2.step(opponent_move)

            if done and reward == 1:
                to_avoid.append(move)
                break

    # 5. Chọn trong các nước an toàn
    safe_moves = [
        move
        for move in env.valid_moves
        if move not in to_avoid
    ]

    if safe_moves:
        return random.choice(safe_moves)

    # 6. Nếu tất cả đều nguy hiểm thì random
    return env.sample()
    