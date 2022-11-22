with open("input.txt") as f:
    data = f.read()

data = [line.split() for line in data.splitlines()]
print(data)


# Part 1
count = 0
for passphrase in data:
    if len(passphrase) == len(set(passphrase)):
        count += 1

print(f"Part 1: {count}")


# Part 2
count = 0
for passphrase in data:
    sorted_words = [''.join(sorted(word)) for word in passphrase]

    if len(passphrase) == len(set(sorted_words)):
        count += 1

print(f"Part 2: {count}")
