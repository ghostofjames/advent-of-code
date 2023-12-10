from itertools import pairwise

with open("input.txt") as f:
    data = [[int(x) for x in line.split()] for line in f.read().splitlines()]


# Part 1


def predict(numbers):
    if all(x == 0 for x in numbers):
        return 0

    return numbers[-1] + predict([y - x for x, y in pairwise(numbers)])


print(f"Part 1: {sum(predict(history) for history in data)}")


# Part 2

print(f"Part 2: {sum(predict(history[::-1]) for history in data)}")
