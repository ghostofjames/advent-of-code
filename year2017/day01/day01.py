from itertools import pairwise

with open("input.txt") as f:
    data = f.read()

print(data)


# Part 1
count = 0
for i, j in pairwise(list(data + data[0])):
    if i == j:
        count += int(i)

print(f"Part 1: {count}")


# Part 2
count = 0
n = len(data) // 2
for i, j in zip(data, data[n:] + data[:n]):
    if i == j:
        count += int(i)

print(f"Part 2: {count}")
