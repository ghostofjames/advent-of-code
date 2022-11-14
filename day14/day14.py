from collections import Counter

data = []
# with open("day14_input.txt") as f:
#     data = f.read().splitlines()
with open("example.txt") as f:
    data = f.read().splitlines()


polymer = data[0]
rules = {r[0]: r[1] for r in [r.split(" -> ") for r in data[2:]]}

print(polymer)
print(rules)

for step in range(1, 11):
    print(f"Step {step}")

    # Apply each rule

count = Counter(polymer)
most_common = count.most_common()[0]
least_common = count.most_common()[-1]
print(f"Part 1: {most_common[1] - least_common[1]}")
