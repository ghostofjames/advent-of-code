with open("input.txt") as f:
    data = f.read()


# Part 1
elfs = [[int(item) for item in elf.split('\n')]
        for elf in data.split('\n\n')]
calories = [sum(items for items in elf) for elf in elfs]

print(f"Part 1: {max(calories)}")


# Part 2
print(f"Part 2: {sum(sorted(calories)[-3:])}")
