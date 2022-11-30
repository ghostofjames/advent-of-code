with open("input.txt") as f:
    data = f.read()
    # data = "3,1,2"
    data = [int(n) for n in data.split(',')]

print(data)


# Part 1
last_spoken = {}
for i, p in enumerate(data):
    last_spoken[int(p)] = i + 1

turn = len(last_spoken) + 1
last = 0

while turn < 2020:
    if last in last_spoken:
        diff = turn - last_spoken[last]
        last_spoken[last] = turn
    else:
        diff = 0
        last_spoken[last] = turn
    last = diff
    turn += 1

print(f"Part 1: {last}")


# Part 2
last_spoken = {}
for i, p in enumerate(data):
    last_spoken[int(p)] = i + 1

turn = len(last_spoken) + 1
last = 0

while turn < 30000000:
    if last in last_spoken:
        diff = turn - last_spoken[last]
        last_spoken[last] = turn
    else:
        diff = 0
        last_spoken[last] = turn
    last = diff
    turn += 1

print(f"Part 2: {last}")
