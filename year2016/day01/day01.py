with open("input.txt") as f:
    data = f.read()

data = [(x[0], int(x[1:])) for x in data.split(", ")]


def distance(p):
    print(p)
    return abs(p[0]) + abs(p[1])


def part1():
    dir = 0
    pos = [0, 0]

    for rot, num in data:
        match rot:
            case 'R':
                dir = (dir + 90) % 360
            case 'L':
                dir = (dir - 90) % 360

        match dir:
            case 0:
                pos[1] += num
            case 90:
                pos[0] += num
            case 180:
                pos[1] -= num
            case 270:
                pos[0] -= num

    return distance(pos)


def part2():
    dir = 0
    pos = [0, 0]
    positions = set()

    for rot, num in data:
        match rot:
            case 'R':
                dir = (dir + 90) % 360
            case 'L':
                dir = (dir - 90) % 360

        match dir:
            case 0:
                for i in range(num):
                    tmp_pos = (pos[0], pos[1] + i)
                    if tmp_pos in positions:
                        return distance(tmp_pos)
                    positions.add(tmp_pos)
                pos[1] += num
            case 90:
                for i in range(num):
                    tmp_pos = (pos[0] + i, pos[1])
                    if tmp_pos in positions:
                        return distance(tmp_pos)
                    positions.add(tmp_pos)
                pos[0] += num
            case 180:
                for i in range(num):
                    tmp_pos = (pos[0], pos[1] - i)
                    if tmp_pos in positions:
                        return distance(tmp_pos)
                    positions.add(tmp_pos)
                pos[1] -= num
            case 270:
                for i in range(num):
                    tmp_pos = (pos[0] + 1, pos[1])
                    if tmp_pos in positions:
                        return distance(tmp_pos)
                    positions.add(tmp_pos)
                pos[0] -= num


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
