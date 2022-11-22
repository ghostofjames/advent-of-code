with open("input.txt") as f:
    data = f.read()

data = [int(line) for line in data.splitlines()]

# Part 1
list_ = data[:]
steps = 0
position = 0
while 0 <= position < len(list_):
    steps += 1

    jump = list_[position]
    list_[position] += 1

    position += jump

print(f"Part 1: {steps}")


# Part 2
list_ = data[:]
steps = 0
position = 0
while 0 <= position < len(list_):
    steps += 1

    jump = list_[position]
    list_[position] += -1 if list_[position] >= 3 else 1

    position += jump

print(f"Part 2: {steps}")
