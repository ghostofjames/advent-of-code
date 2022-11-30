with open("input.txt") as f:
    data = f.read().splitlines()

turn_left = {'NORTH': 'WEST', 'WEST': 'SOUTH', 'SOUTH': 'EAST', 'EAST': 'NORTH'}
turn_right = {'NORTH': 'EAST', 'EAST': 'SOUTH', 'SOUTH': 'WEST', 'WEST': 'NORTH'}
move_dir = {'NORTH': (0, 1), 'EAST': (1, 0), 'SOUTH': (0, -1), 'WEST': (-1, 0)}

# Part 1
position = [0, 0]
rot = 'EAST'

for ins in data:
    action, value = ins[0], int(ins[1:])

    match action:
        case 'N':
            position[1] += value
        case 'S':
            position[1] -= value
        case 'E':
            position[0] += value
        case 'W':
            position[0] -= value
        case 'L':
            for i in range(value // 90):
                rot = turn_left[rot]
        case 'R':
            for i in range(value // 90):
                rot = turn_right[rot]
        case 'F':
            dir = move_dir[rot]
            position[0] += dir[0] * value
            position[1] += dir[1] * value

distance = abs(position[0]) + abs(position[1])
print(f"Part 1: {distance}")


# Part 2
position = [0, 0]
waypoint = [10, 1]

for ins in data:
    action, value = ins[0], int(ins[1:])

    match action:
        case 'N':
            waypoint[1] += value
        case 'S':
            waypoint[1] -= value
        case 'E':
            waypoint[0] += value
        case 'W':
            waypoint[0] -= value

        case 'L':
            for i in range(value // 90):
                waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]

        case 'R':
            for i in range(value // 90):
                waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]

        case 'F':
            position[0] += waypoint[0] * value
            position[1] += waypoint[1] * value

distance = abs(position[0]) + abs(position[1])
print(f"Part 2: {distance}")
