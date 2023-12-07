from collections import Counter

with open("input.txt") as f:
    data = f.read()

hands = []
for line in data.splitlines():
    hand, bid = line.split()
    hands.append({"hand": hand, "bid": int(bid)})


types = [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5,)]


# Part 1
def handvalue(hand):
    handtype = types.index(tuple(sorted(Counter(hand).values())))
    return (handtype, ["23456789TJQKA".index(i) for i in hand])


part1 = sum(
    (i + 1) * int(hand["bid"])
    for i, hand in enumerate(sorted(hands, key=lambda hand: handvalue(hand["hand"])))
)

print(f"Part 1: {part1}")


# Part 2
def handvalue2(hand):
    jokerhandtypes = [
        types.index(tuple(sorted(Counter(hand.replace("J", r)).values())))
        for r in "23456789TQKA"
    ]
    return (max(jokerhandtypes), ["J23456789TXQKA".index(i) for i in hand])


part2 = sum(
    (i + 1) * int(hand["bid"])
    for i, hand in enumerate(sorted(hands, key=lambda hand: handvalue2(hand["hand"])))
)

print(f"Part 2: {part2}")
