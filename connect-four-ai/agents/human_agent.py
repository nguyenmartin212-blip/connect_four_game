def human_agent(env):
    while True:
        try:
            move = int(input("Choose column 1-7: ")) - 1

            if move in env.valid_moves:
                return move

            print("Invalid move or column is full.")

        except ValueError:
            print("Please enter a number from 1 to 7.")