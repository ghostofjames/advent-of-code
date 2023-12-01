with open("input.txt") as f:
    data = f.read()

data = data.splitlines()
print(data)


# Part 1

sum = 0
for line in data:
    digits = list(filter(str.isdigit, line))
    sum += int(digits[0] + digits[-1])

print(f"Part 1: {sum}")


# Part 2

lettermap = {
    letters: str(number + 1)
    for number, letters in enumerate(
        ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    )
}

sum = 0
for line in data:
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(c)

        for letters, number in lettermap.items():
            if line[i:].startswith(letters):
                digits.append(number)

    sum += int(digits[0] + digits[-1])


print(f"Part 2: {sum}")
