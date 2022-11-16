from itertools import product

data = []
with open("input.txt") as f:
    data = f.read()


def update_position(pos, vel):
    x, y, = pos
    vx, vy = vel
    x += vx
    y += vy
    vx -= 1 if vx > 0 else 0
    vy -= 1
    return (x, y), (vx, vy)


def hits(velocity, target):
    position = (0, 0)
    max_y = 0

    while (position[0] <= target[0][1]) and (position[1] >= target[1][0]):
        position, velocity = update_position(position, velocity)

        if position[1] >= max_y:
            max_y = position[1]

        if (target[0][0] <= position[0] <= target[0][1]) and (
                target[1][0] <= position[1] <= target[1][1]):
            return True, max_y

    return False, max_y


# Part 1
target_area = [list(map(int, x[3:].split(".."))) for x in data[12:].split(",")]
search_x = range(0, target_area[0][1] + 1)
search_y = range(-abs(target_area[1][0]), abs(target_area[1][0]))

velocity_results = {}

for starting_velocity in product(search_x, search_y):
    hit, max_y = hits(starting_velocity, target_area)

    if hit:
        velocity_results[starting_velocity] = max_y

print(f"Part 1: {max(velocity_results.values())}")


# Part 2
print(f"Part 2: {len(velocity_results.keys())}")

print(max(velocity_results.keys()))
