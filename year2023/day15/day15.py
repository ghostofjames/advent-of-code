from collections import defaultdict

with open("input.txt") as f:
    data = f.read()
    # data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

steps = data.split(",")

# Part 1


def hash(string):
    value = 0
    for char in string:
        value += ord(char)
        value *= 17
        value %= 256

    return value


part1 = sum(hash(step) for step in steps)

print(f"Part 1: {part1}")


# Part 2

boxes = defaultdict(dict)

for step in steps:
    if step.endswith("-"):
        label = step.strip("-")
        boxes[hash(label)].pop(label, None)

    else:
        label, focal = step.split("=")
        boxes[hash(label)][label] = int(focal)


part2 = sum(
    (box_num + 1) * slot * focal
    for box_num, box in boxes.items()
    for slot, focal in enumerate(box.values(), start=1)
)

print(f"Part 2: {part2}")
