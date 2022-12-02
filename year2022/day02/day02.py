with open("input.txt") as f:
    data = f.read()

data = [line.split(' ') for line in data.splitlines()]


# Part 1
moves = {'A': 'R', 'B': 'P', 'C': 'S', 'X': 'R', 'Y': 'P', 'Z': 'S'}
shape_score = {'R': 1, 'P': 2, 'S': 3}
outcome_score = {'L': 0, 'D': 3, 'W': 6}

score = 0
for opponent, player in data:
    move = moves[player]
    match moves[opponent]:
        case 'R':
            match move:
                case 'R':
                    outcome = 'D'
                case 'P':
                    outcome = 'W'
                case 'S':
                    outcome = 'L'
        case 'P':
            match move:
                case 'R':
                    outcome = 'L'
                case 'P':
                    outcome = 'D'
                case 'S':
                    outcome = 'W'
        case 'S':
            match move:
                case 'R':
                    outcome = 'W'
                case 'P':
                    outcome = 'L'
                case 'S':
                    outcome = 'D'

    score += shape_score[move] + outcome_score[outcome]

print(f"Part 1: {score}")


# Part 2
outcomes = {'X': 'L', 'Y': 'D', 'Z': 'W'}

score = 0
for opponent, outcome in data:
    outcome = outcomes[outcome]
    match moves[opponent]:
        case 'R':
            match outcome:
                case 'L':
                    move = 'S'
                case 'D':
                    move = 'R'
                case 'W':
                    move = 'P'
        case 'P':
            match outcome:
                case 'L':
                    move = 'R'
                case 'D':
                    move = 'P'
                case 'W':
                    move = 'S'
        case 'S':
            match outcome:
                case 'L':
                    move = 'P'
                case 'D':
                    move = 'S'
                case 'W':
                    move = 'R'

    score += shape_score[move] + outcome_score[outcome]

print(f"Part 2: {score}")
