with open("input.txt") as f:
    data = f.read()

# Part 1
x = 1
cycle = 0
interesting_cycles = [20, 60, 100, 140, 180, 220]
signals = []
for instruction in data.splitlines():
    # clock cycle 1
    cycle += 1

    if cycle in interesting_cycles:
        signals.append(cycle * x)

    if instruction == "noop":
        continue

    # clock cycle 2
    cycle += 1

    if cycle in interesting_cycles:
        signals.append(cycle * x)

    x += int(instruction[5:])

print(f"Part 1: {sum(signals)}")


# Part 2
x = 1
cycle = 0
crt = [['.' for _ in range(40)] for _ in range(6)]

for instruction in data.splitlines():
    # clock cycle 1
    cycle += 1

    row = (cycle - 1) // 40
    col = (cycle - 1) % 40
    if col in [x-1, x, x+1]:
        crt[row][col] = '█'

    if instruction == "noop":
        continue

    # clock cycle 2
    cycle += 1

    row = (cycle - 1) // 40
    col = (cycle - 1) % 40
    if col in [x-1, x, x+1]:
        crt[row][col] = '█'

    x += int(instruction[5:])

print("Part 2:")
print('\n'.join(''.join(row) for row in crt))
