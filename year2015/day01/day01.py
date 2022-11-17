with open("input.txt") as f:
    data = f.read()


# Part 1

up = data.count('(')
down = data.count(')')

floor = up - down

print(f"Part 1: {floor}")


# Part 2
position = 1
floor = 0
for p, i in enumerate(list(data)):
    if i == '(':
        floor += 1
    else:
        floor -= 1
    if floor < 0:
        position = p + 1
        break

print(f"Part 2: {position}")
