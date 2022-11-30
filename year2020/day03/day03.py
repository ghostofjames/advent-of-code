from math import prod

with open("input.txt") as f:
    data = f.read()


data = [list(line) for line in data.splitlines()]


def traverse(slope):
    trees = 0
    position = [0, 0]
    while position[1] < len(data) - 1:
        position[0] = (position[0] + slope[0]) % len(data[0])
        position[1] += slope[1]
        if data[position[1]][position[0]] == '#':
            trees += 1

    return trees


# Part 1
s = [3, 1]
trees = traverse(s)
print(f"Part 1: {trees}")


# Part 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
tree_counts = [traverse(slope) for slope in slopes]
print(f"Part 2: {prod(tree_counts)}")
