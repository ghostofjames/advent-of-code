def part1(data):
    region = [list(r) for r in data]

    # step_history = [region]

    change = True
    steps = 0
    while change:
        change = False
        steps += 1

        # > herd
        new_region = [['.' for _ in range(len(region[0]))] for _ in range(len(region))]
        for i in range(len(region)):
            for j in range(len(region[0])):
                if region[i][j] == '>':
                    if region[i][(j+1) % len(region[0])] == '.':
                        new_region[i][(j+1) % len(region[0])] = '>'
                        change = True
                    else:
                        new_region[i][j] = '>'
                elif region[i][j] == 'v':
                    new_region[i][j] = 'v'
        region = new_region

        # v herd
        new_region = [['.' for _ in range(len(region[0]))] for _ in range(len(region))]
        for i in range(len(region)):
            for j in range(len(region[0])):
                if region[i][j] == 'v':
                    if region[(i+1) % len(region)][j] == '.':
                        new_region[(i+1) % len(region)][j] = 'v'
                        change = True
                    else:
                        new_region[i][j] = 'v'
                elif region[i][j] == '>':
                    new_region[i][j] = '>'
        region = new_region

        # step_history.append(region)

    return steps


with open("example.txt") as f:
    example_data = f.read().splitlines()

with open("input.txt") as f:
    data = f.read().splitlines()

res = part1(example_data)
print(f"Part 1 Example: {res}")

res = part1(data)
print(f"Part 1: {res}")


# visualisation attempt
# TODO create nice visualisation

# import curses
# import time

# stdscr = curses.initscr()

# for step in step_history:
#     stdscr.addstr(0, 0, '\n'.join(
#         [''.join([item for item in row[:20]]) for row in step[:20]]))
#     stdscr.refresh()
#     time.sleep(0.1)
