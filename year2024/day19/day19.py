from functools import cache

with open("input.txt") as f:
    data = f.read()

patterns, designs = data.split("\n\n")
patterns = patterns.split(", ")
designs = designs.splitlines()


# Part 1


@cache
def check(d):
    if d == "":
        return True
    return any(check(d.removeprefix(p)) for p in patterns if d.startswith(p))


print(f"Part 1: {sum(check(design) for design in designs)}")


# Part 2


@cache
def count(d):
    if d == "":
        return 1
    return sum(count(d.removeprefix(p)) for p in patterns if d.startswith(p))


print(f"Part 2: {sum(count(design) for design in designs)}")
