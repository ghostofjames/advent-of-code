from collections import Counter

with open("input.txt") as f:
    data = [int(line) for line in f.read().splitlines()]

print(data)


# Part 1
adapters = sorted(data + [0, max(data) + 3])

diffs = [adapters[i] - adapters[i - 1] for i in range(1, len(adapters))]
count = Counter(diffs)

print(f"Part 1: {count[1] * count[3]}")


# Part 2

print(f"Part 2: {0}")
