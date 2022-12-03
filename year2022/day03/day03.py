with open("input.txt") as f:
    data = f.read().splitlines()


def priority(c):
    p = ord(c)
    p -= 96 if (97 <= p <= 122) else 38
    return p


# Part 1
priorities = 0
for rucksack in data:
    a, b = set(rucksack[:len(rucksack)//2]), set(rucksack[len(rucksack)//2:])
    common = set.intersection(a, b).pop()
    priorities += priority(common)

print(f"Part 1: {priorities}")


# Part 2
priorities = 0
for i in range(0, len(data), 3):
    a, b, c = set(data[i]), set(data[i + 1]), set(data[i + 2])
    common = set.intersection(a, b, c).pop()
    priorities += priority(common)

print(f"Part 2: {priorities}")
