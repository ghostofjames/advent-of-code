from itertools import cycle, islice, product

data = []
with open("example.txt") as f:
    data = f.read().splitlines()


class Player():
    def __init__(self, start):
        self.position = start
        self.score = 0

    def __repr__(self):
        return f"Position: {self.position:2} Score: {self.score:4} Win: {self.score >= 1000}"

    def turn(self, roll):
        self.position = (self.position - 1 + roll) % 10 + 1
        self.score += self.position


# Part 1
p1 = Player(int(data[0][-1]))
p2 = Player(int(data[1][-1]))

die = cycle(range(1, 101))
die_rolled = 0

while True:
    p1_roll = sum(islice(die, 3))
    die_rolled += 3

    p1.turn(p1_roll)
    if p1.score >= 1000:
        break

    p2_roll = sum(islice(die, 3))
    die_rolled += 3

    p2.turn(p2_roll)
    if p2.score >= 1000:
        break

print(f"Part 1: {min(p1.score, p2.score) * die_rolled}")


# Part 2
# p1 = Player(int(data[0][-1]))
# p2 = Player(int(data[1][-1]))
# print(f"Player 1: {p1}")
# print(f"Player 2: {p2}")


# dirac_die = [1, 2, 3]
# rolls = [sum(roll) for roll in product(dirac_die, dirac_die, dirac_die)]
# print(rolls)


# print(f"Part 2: {2}")
