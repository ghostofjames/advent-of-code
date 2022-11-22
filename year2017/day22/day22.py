from collections import defaultdict
from copy import copy

turn_right = {'UP': 'RIGHT', 'RIGHT': 'DOWN', 'DOWN': 'LEFT', 'LEFT': 'UP'}
turn_left = {'UP': 'LEFT', 'LEFT': 'DOWN', 'DOWN': 'RIGHT', 'RIGHT': 'UP'}
reverse = {'UP': 'DOWN', 'LEFT': 'RIGHT', 'DOWN': 'UP', 'RIGHT': 'LEFT'}
move_dir = {'UP': (0, -1), 'RIGHT': (1, 0), 'DOWN': (0, 1), 'LEFT': (-1, 0)}


with open("input.txt") as f:
    data = f.read()

start_nodes = defaultdict(lambda: '.')
for i, y in enumerate(data.splitlines()):
    for j, x in enumerate(y):
        if x == '#':
            start_nodes[(j, i)] = x


# Part 1
nodes = copy(start_nodes)
position = (len(data.splitlines()) // 2, len(data.splitlines()) // 2)
direction = 'UP'

infect_bursts = 0
for _ in range(10_000):
    if nodes[position] == '#':
        direction = turn_right[direction]
        nodes[position] = '.'
    else:
        direction = turn_left[direction]
        nodes[position] = '#'
        infect_bursts += 1

    d = move_dir[direction]
    position = (position[0] + d[0], position[1] + d[1])

print(f"Part 1: {infect_bursts}")


# Part 2
nodes = copy(start_nodes)
position = (len(data.splitlines()) // 2, len(data.splitlines()) // 2)
direction = 'UP'

infect_bursts = 0
for _ in range(10_000_000):
    if nodes[position] == '.':
        direction = turn_left[direction]
        nodes[position] = 'W'

    elif nodes[position] == 'W':
        nodes[position] = '#'
        infect_bursts += 1

    elif nodes[position] == '#':
        direction = turn_right[direction]
        nodes[position] = 'F'

    elif nodes[position] == 'F':
        direction = reverse[direction]
        nodes[position] = '.'

    d = move_dir[direction]
    position = (position[0] + d[0], position[1] + d[1])

print(f"Part 2: {infect_bursts}")
