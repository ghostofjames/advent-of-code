import numpy as np

with open("input.txt") as f:
    data = f.read()

adjacent = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


# Part 1
lights = np.pad(np.array([[x for x in y] for y in data.splitlines()]),
                1, constant_values=('.'))

for step in range(1, 101):
    new_lights = np.full_like(lights, '.')
    for i in range(1, 101):
        for j in range(1, 101):
            neighbours = [n for n in [(i + a[0], j + a[1]) for a in adjacent]]
            on = sum(1 for n in neighbours if lights[n] == '#')

            if lights[i, j] == '#':
                if (2 <= on <= 3):
                    new_lights[i, j] = '#'
                else:
                    new_lights[i, j] = '.'
            else:
                if on == 3:
                    new_lights[i, j] = '#'
                else:
                    new_lights[i, j] = '.'

    lights = new_lights

light_count = sum(1 for y in lights for x in y if x == '#')
print(f"Part 1: {light_count}")


# Part 2
lights = np.pad(np.array([[x for x in y] for y in data.splitlines()]),
                1, constant_values=('.'))
for corner in [(1, 1), (1, 100), (100, 1), (100, 100)]:
    lights[corner] = '#'

for step in range(1, 101):
    new_lights = np.full_like(lights, '.')
    for i in range(1, 101):
        for j in range(1, 101):
            neighbours = [n for n in [(i + a[0], j + a[1]) for a in adjacent]]
            on = sum(1 for n in neighbours if lights[n] == '#')

            if lights[i, j] == '#':
                if (2 <= on <= 3):
                    new_lights[i, j] = '#'
                else:
                    new_lights[i, j] = '.'
            else:
                if on == 3:
                    new_lights[i, j] = '#'
                else:
                    new_lights[i, j] = '.'

    lights = new_lights

    for corner in [(1, 1), (1, 100), (100, 1), (100, 100)]:
        lights[corner] = '#'

light_count = sum(1 for y in lights for x in y if x == '#')
print(f"Part 2: {light_count}")
