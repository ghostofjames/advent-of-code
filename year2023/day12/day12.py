from functools import cache

with open("input.txt") as f:
    data = [line.split() for line in f.read().splitlines()]


# Part 1


@cache
def count_arrangements(record, groups, groupsize=0):
    if not record:
        return not groups and not groupsize

    count = 0
    for char in [".", "#"] if record[0] == "?" else record[0]:
        if char == "#":
            count += count_arrangements(record[1:], groups, groupsize + 1)
        else:
            if groupsize:
                if groups and groups[0] == groupsize:
                    count += count_arrangements(record[1:], groups[1:])
            else:
                count += count_arrangements(record[1:], groups)
    return count


part1 = sum(
    count_arrangements(record + ".", tuple(int(x) for x in groups.split(",")))
    for record, groups in data
)

print(f"Part 1: {part1}")


# Part 2

unfolded = [
    ["?".join(record for _ in range(5)), ",".join(groups for _ in range(5))]
    for record, groups in data
]

part2 = sum(
    count_arrangements(record + ".", tuple(int(x) for x in groups.split(",")))
    for record, groups in unfolded
)

print(f"Part 2: {part2}")
