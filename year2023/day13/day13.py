with open("input.txt") as f:
    data = f.read()

patterns = [pattern.splitlines() for pattern in data.split("\n\n")]


# Part 1


def findreflection(pattern):
    for i in range(1, len(pattern)):
        for n, row in enumerate(pattern):
            if n == i:
                return i
            mirrored = i * 2 - 1 - n
            if mirrored < len(pattern) and row != pattern[mirrored]:
                break


part1 = 0
for pattern in patterns:
    if horizontal := findreflection(pattern):
        part1 += horizontal * 100
    else:
        part1 += findreflection([*zip(*pattern)])


print(f"Part 1: {part1}")


# Part 2


def findreflectionwithsmudge(pattern):
    for i in range(1, len(pattern)):
        diff = 0
        for n, row in enumerate(pattern):
            if n == i and diff == 1:
                return i
            mirrored = i * 2 - 1 - n
            if mirrored < len(pattern):
                diff += sum(c1 != c2 for c1, c2 in zip(row, pattern[mirrored]))
                if diff > 1:
                    break


part2 = 0
for pattern in patterns:
    if horizontal := findreflectionwithsmudge(pattern):
        part2 += horizontal * 100
    else:
        part2 += findreflectionwithsmudge([*zip(*pattern)])

print(f"Part 2: {part2}")
