import itertools

data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

with open("input.txt") as f:
    data = f.read()

# Parse maps
seeds, *rawmaps = data.split("\n\n")

seeds = [int(x) for x in seeds.split()[1:]]

maps = []
for xmap in rawmaps:
    ranges = []
    for line in xmap.splitlines()[1:]:
        destination, source, length = map(int, line.split())
        m = {"destination": destination, "source": source, "length": length}
        ranges.append(m)

    maps.append(ranges)


# Part 1

locations = []
for seed in seeds:
    for m in maps:
        for r in m:
            if r["source"] <= seed <= r["source"] + r["length"]:
                seed = seed - r["source"] + r["destination"]
                break

    locations.append(seed)

print(f"Part 1: {min(locations)}")


# Part 2

for location in itertools.count(start=1):
    seed = location
    for m in maps[::-1]:
        for r in m:
            # if r["source"] <= seed <= r["source"] + r["length"]:
            #     seed = seed - r["source"] + r["destination"]
            #     break
            if r["destination"] <= seed <= r["destination"] + r["length"]:
                seed = seed - r["destination"] + r["source"]
                break

    print(seed)
    for start, length in zip(seeds[::2], seeds[1::2]):
        if start <= seed <= start + length:
            break
    else:
        continue
    break
print(f"Part 2: {location}")
