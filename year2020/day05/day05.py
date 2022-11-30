with open("input.txt") as f:
    data = f.read().splitlines()


def bsp(string, upper, lower_char):
    lower = 0
    for letter in string:
        if letter == lower_char:
            upper = (upper + lower) // 2
        else:
            lower = (upper + lower) // 2 + 1
    return lower


# Part 1
seatids = []
for bp in data:
    brow, bcol = bp[:7], bp[7:]
    row = bsp(brow, 127, 'F')
    col = bsp(bcol, 7, 'L')
    seatids.append(row * 8 + col)

print(f"Part 1: {max(seatids)}")


# Part 2
possible_seatids = set(i * 8 + j for i in range(1, 127) for j in range(0, 8))
missing = possible_seatids - set(seatids)

seat = 0
for id in missing:
    if (id - 1 in seatids) and (id + 1 in seatids):
        seat = id

print(f"Part 2: {seat}")
