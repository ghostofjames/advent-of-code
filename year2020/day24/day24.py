with open("input.txt") as f:
    data = f.read()
#     data = """sesenwnenenewseeswwswswwnenewsewsw
# neeenesenwnwwswnenewnwwsewnenwseswesw
# seswneswswsenwwnwse
# nwnwneseeswswnenewneswwnewseswneseene
# swweswneswnenwsewnwneneseenw
# eesenwseswswnenwswnwnwsewwnwsene
# sewnenenenesenwsewnenwwwse
# wenwwweseeeweswwwnwwe
# wsweesenenewnwwnwsenewsenwwsesesenwne
# neeswseenwwswnwswswnw
# nenwswwsewswnenenewsenwsenwnesesenew
# enewnwewneswsewnwswenweswnenwsenwsw
# sweneswneswneneenwnewenewwneswswnese
# swwesenesewenwneswnwwneseswwne
# enesenwswwswneneswsenwnewswseenwsese
# wnwnesenesenenwwnenwsewesewsesesew
# nenewswnwewswnenesenwnesewesw
# eneswnwswnwsenenwnwnwwseeswneewsenese
# neswnwewnwnwseenwseesewsenwsweewe
# wseweeenwnesenwwwswnew"""


directions = {
    #     ( q,  r,  s)
    "nw": (00, -1, +1),
    "ne": (+1, -1,  0),
    "e":  (+1,  0, -1),
    "se": (00, +1, -1),
    "sw": (-1, +1,  0),
    "w":  (-1,  0, +1),
}


def cube_add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


# Part 1
black_tiles = set()

for line in data.splitlines():
    position = (0, 0, 0)
    while line:
        if line.startswith(('ne', 'se', 'sw', 'nw')):
            dir, line = line[:2], line[2:]
        else:
            dir, line = line[:1], line[1:]

        position = cube_add(position, directions[dir])
    if position not in black_tiles:
        black_tiles.add(position)
    else:
        black_tiles.remove(position)

print(f"Part 1: {len(black_tiles)}")


# Part 2
for _ in range(100):
    new_tiles = set()
    to_check = set()
    for coord in black_tiles:
        to_check.add(coord)
        for diff in directions.values():
            to_check.add(cube_add(coord, diff))

    for coord in to_check:
        count = sum([cube_add(coord, d) in black_tiles for d in directions.values()])

        if (coord in black_tiles and 0 < count <= 2) or (
                coord not in black_tiles and count == 2):
            new_tiles.add(coord)

    black_tiles = new_tiles

print(f"Part 2: {len(black_tiles)}")
