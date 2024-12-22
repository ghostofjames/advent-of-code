from collections import defaultdict
from itertools import islice, pairwise

with open("input.txt") as f:
    data = f.read()

buyers = list(map(int, data.splitlines()))

# Part 1


def mix(n, x):
    return n ^ x


def prune(n):
    return n % 16777216


def secrets(n):
    s = n
    while True:
        s = prune(mix(s, s * 64))
        s = prune(mix(s, s // 32))
        s = prune(mix(s, s * 2048))
        yield s


assert mix(42, 15) == 37
assert prune(100000000) == 16113920
assert list(islice(secrets(123), 10)) == [
    15887950,
    16495136,
    527345,
    704524,
    1553684,
    12683156,
    11100544,
    12249484,
    7753432,
    5908254,
]

total = sum(list(islice(secrets(b), 2000))[-1] for b in buyers)

print(f"Part 1: {total}")


# Part 2

totals_for_sequence = defaultdict(int)
for b in buyers:
    prices = [b % 10] + [s % 10 for s in islice(secrets(b), 2000)]
    changes = [b - a for a, b in pairwise(prices)]

    seen = set()
    for i in range(len(prices) - 4):
        pat = tuple(changes[i : i + 4])
        if pat not in seen:
            totals_for_sequence[pat] += prices[i + 4]
            seen.add(pat)

best = max(totals_for_sequence.values())

print(f"Part 2: {best}")
