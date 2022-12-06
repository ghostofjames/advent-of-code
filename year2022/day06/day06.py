with open("input.txt") as f:
    data = f.read()


def find_marker(data, n):
    for pos in range(n, len(data)):
        if len(set(data[pos - n:pos])) == n:
            return pos


# Part 1
print(f"Part 1: {find_marker(data, 4)}")


# Part 2
print(f"Part 2: {find_marker(data, 14)}")
