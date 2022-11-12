data = []
with open("day04_input.txt") as f:
    data = f.read().split("\n\n")

numbers = [int(x) for x in data[0].split(",")]
boards = [[[int(z) for z in y.split()]
           for y in x.splitlines()]
          for x in data[1:]]

# Part 1
win_number = None
win_board = None
for number in numbers:
    for board in boards:
        # mark number on board
        for y, row in enumerate(board):
            for x, value in enumerate(row):
                if value == number:
                    board[y][x] = -1

        # check board for win
        hori = any([all([x == -1 for x in y]) for y in board])
        vert = any(all([y[x] == -1 for y in board]) for x in range(5))
        if hori or vert:
            win_number = number
            win_board = board
            break
    else:
        continue
    break

final_score = sum([x for y in win_board for x in y if x != -1]) * win_number
print(f"Part 1: {final_score}")

# Part 2
last_number = None
last_board = None
wins = [False] * len(boards)
for number in numbers:
    for board in boards:
        # mark number on board
        for y, row in enumerate(board):
            for x, value in enumerate(row):
                if value == number:
                    board[y][x] = -1

        # check board for win
        hori = any([all([x == -1 for x in y]) for y in board])
        vert = any(all([y[x] == -1 for y in board]) for x in range(5))
        if hori or vert:
            wins[boards.index(board)] = True

            # check if all boards have now won
            if all(wins):
                last_number = number
                last_board = board
                break
    else:
        continue
    break

final_score = sum([x for y in last_board for x in y if x != -1]) * last_number
print(f"Part 2: {final_score}")
