with open("input.txt") as f:
    data = f.read()

groups = [group.splitlines() for group in data.split('\n\n')]

# Part 1
count = 0
for group in groups:
    anyone = set.union(*[set(person) for person in group])
    count += len(anyone)

print(f"Part 1: {count}")


# Part 2
count = 0
for group in groups:
    everyone = set.intersection(*[set(person) for person in group])
    count += len(everyone)

print(f"Part 2: {count}")
