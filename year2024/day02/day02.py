from itertools import pairwise

with open("input.txt") as f:
    data = f.read()


reports = [[int(i) for i in line.split(" ")] for line in data.splitlines()]

# Part 1


def is_safe(report):
    return all((a < b) and (b - a <= 3) for a, b in pairwise(report)) or all(
        (a > b) and (a - b <= 3) for a, b in pairwise(report)
    )


safe = sum(is_safe(report) for report in reports)

print(f"Part 1: {safe}")


# Part 2


def is_safe_minus_element(report):
    return any(
        is_safe(r)
        for r in [report[: x - 1] + report[x:] for x in range(1, len(report) + 1)]
    )


safe2 = sum(is_safe(report) or is_safe_minus_element(report) for report in reports)


print(f"Part 2: {safe2}")
