data = []
with open("day08_input.txt") as f:
    data = f.read().splitlines()

entries = [[y.split() for y in x.split(" | ")] for x in data]
print(entries[0])


# Part 1
count = {1: 0, 4: 0, 7: 0, 8: 0}
for entry in entries:
    for value in entry[1]:
        match len(value):
            case 2: count[1] += 1  # len(seg) = 2 -> digit 1
            case 4: count[4] += 1  # len(seg) = 4 -> digit 4
            case 3: count[7] += 1  # len(seg) = 3 -> digit 7
            case 7: count[8] += 1  # len(seg) = 7 -> digit 8
print(count)
print(f"Part 1: {sum(count.values())}")


# Part 2
total = 0
for entry in entries:
    usp, output = entry
    print(usp, output)