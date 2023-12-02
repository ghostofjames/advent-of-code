from collections import defaultdict

with open("input.txt") as f:
    data = f.read()


# data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

data = data.splitlines()


# Part 1

red_cubes = 12
green_cubes = 13
blue_cubes = 14

sum = 0
for line in data:
    valid = True

    game, bags = line.split(": ")
    _, gameid = game.split(" ")

    for bag in bags.split("; "):
        counts = defaultdict(lambda: 0)

        for cubes in bag.split(", "):
            count, color = cubes.split(" ")
            counts[color] = int(count)

        if (
            (counts["red"] > red_cubes)
            or (counts["green"] > green_cubes)
            or (counts["blue"] > blue_cubes)
        ):
            valid = False

    if valid:
        sum += int(gameid)

print(f"Part 1: {sum}")


# Part 2

sum = 0
for line in data:
    shows = []

    game, bags = line.split(": ")
    _, gameid = game.split(" ")

    for bag in bags.split("; "):
        counts = defaultdict(lambda: 0)

        for cubes in bag.split(", "):
            count, color = cubes.split(" ")
            counts[color] = int(count)

        shows.append(counts)

    max_red = max(x["red"] for x in shows)
    max_green = max(x["green"] for x in shows)
    max_blue = max(x["blue"] for x in shows)

    sum += max_red * max_green * max_blue

print(f"Part 2: {sum}")
