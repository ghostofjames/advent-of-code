with open("input.txt") as f:
    data = f.read()

diagram = [list(line) for line in data.splitlines()]


# Part 1
visited_letters = []
steps = 0

position = (list(diagram[0]).index('|'), 0)
direction = (0, 1)
while True:
    current = diagram[position[1]][position[0]]

    if current == ' ':
        break

    if current == '+':
        if direction in [(0, -1), (0, 1)]:
            if diagram[position[1]][position[0] + 1] != ' ':
                direction = (1, 0)
            else:
                direction = (-1, 0)
        else:
            if diagram[position[1] + 1][position[0]] != ' ':
                direction = (0, 1)
            else:
                direction = (0, -1)
        position = (position[0] + direction[0], position[1] + direction[1])

    else:
        if current in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            visited_letters.append(current)

        position = (position[0] + direction[0], position[1] + direction[1])

    steps += 1

print(f"Part 1: {''.join(visited_letters)}")


# Part 2
print(f"Part 2: {steps}")
