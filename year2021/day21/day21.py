from dataclasses import dataclass
from functools import lru_cache
from itertools import cycle, islice, product

with open("input.txt") as f:
    data = f.read().splitlines()


@dataclass(frozen=True)
class Player():
    position: int
    score: int = 0

    def turn(self, roll):
        position = ((self.position - 1 + roll) % 10) + 1
        score = self.score + position
        return Player(position, score)


# Part 1
p1 = Player(int(data[0][-1]))
p2 = Player(int(data[1][-1]))

die = cycle(range(1, 101))
die_rolled = 0

while True:
    p1_roll = sum(islice(die, 3))
    die_rolled += 3

    p1 = p1.turn(p1_roll)
    if p1.score >= 1000:
        break

    p2_roll = sum(islice(die, 3))
    die_rolled += 3

    p2 = p2.turn(p2_roll)
    if p2.score >= 1000:
        break

print(f"Part 1: {min(p1.score, p2.score) * die_rolled}")
assert min(p1.score, p2.score) * die_rolled == 903630

# Part 2
dirac_die = [1, 2, 3]


@lru_cache(maxsize=None)
def count_wins(player: int, p1: Player, p2: Player):
    if p1.score >= 21:
        return 1, 0
    elif p2.score >= 21:
        return 0, 1

    wins = [0, 0]
    for rolls in product(dirac_die, repeat=3):
        if player == 1:
            new_p1 = p1.turn(sum(rolls))
            wins0, wins1 = count_wins(2, new_p1, Player(p2.position, p2.score))
        else:
            new_p2 = p2.turn(sum(rolls))
            wins0, wins1 = count_wins(1, Player(p1.position, p1.score), new_p2)

        wins[0] += wins0
        wins[1] += wins1

    return wins


p1 = Player(int(data[0][-1]))
p2 = Player(int(data[1][-1]))
wins = count_wins(1, p1, p2)
print(f"Part 2: {max(wins)}")
assert max(wins) == 303121579983974
