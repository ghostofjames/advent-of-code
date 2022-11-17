from collections import defaultdict

with open("input.txt") as f:
    data = list(f.read())


# Part 1
presents = defaultdict(int)
santa = (0, 0)
presents[santa] = 1

for move in data:
    match move:
        case '>':
            santa = (santa[0] + 1, santa[1])
        case '<':
            santa = (santa[0] - 1, santa[1])
        case '^':
            santa = (santa[0], santa[1] - 1)
        case 'v':
            santa = (santa[0], santa[1] + 1)

    presents[santa] += 1

at_least_one_present = len(presents)
print(f"Part 1: {at_least_one_present}")


# Part 2
presents = defaultdict(int)
santa, robot = (0, 0), (0, 0)
presents[santa] += 1
presents[robot] += 1
santa_turn = True

for move in data:
    if santa_turn:
        match move:
            case '>':
                santa = (santa[0] + 1, santa[1])
            case '<':
                santa = (santa[0] - 1, santa[1])
            case '^':
                santa = (santa[0], santa[1] - 1)
            case 'v':
                santa = (santa[0], santa[1] + 1)

        presents[santa] += 1

    else:
        match move:
            case '>':
                robot = (robot[0] + 1, robot[1])
            case '<':
                robot = (robot[0] - 1, robot[1])
            case '^':
                robot = (robot[0], robot[1] - 1)
            case 'v':
                robot = (robot[0], robot[1] + 1)

        presents[robot] += 1

    santa_turn = not santa_turn

at_least_one_present = len(presents)
print(f"Part 2: {at_least_one_present}")
