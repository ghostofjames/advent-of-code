import numpy as np

with open("input.txt") as f:
    data = f.read()

adjacent = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


# Part 1
seats = np.pad(np.array([[x for x in y] for y in data.splitlines()]),
               1, constant_values=('.'))

change = True
while change:
    change = False
    new_seats = np.copy(seats)
    for i in range(1, seats.shape[0]-1):
        for j in range(1, seats.shape[1]-1):
            if seats[i, j] == '.':
                continue

            neighbours = [n for n in [(i + a[0], j + a[1]) for a in adjacent]]
            occupied = sum(1 for n in neighbours if seats[n] == '#')

            if seats[i, j] == 'L' and occupied == 0:
                new_seats[i, j] = '#'
                change = True
            elif seats[i, j] == '#' and occupied >= 4:
                new_seats[i, j] = 'L'
                change = True

    seats = new_seats

occupied_seats = sum(1 for y in seats for x in y if x == '#')
print(f"Part 1: {occupied_seats}")


# Part 2
seats = np.pad(np.array([[x for x in y] for y in data.splitlines()]),
               1, constant_values=('.'))

change = True
while change:
    change = False
    new_seats = np.copy(seats)
    for i in range(1, seats.shape[0]-1):
        for j in range(1, seats.shape[1]-1):
            if seats[i, j] == '.':
                continue

            neighbours = []
            for direction in adjacent:
                temp = (i + direction[0], j + direction[1])
                while 1 <= temp[0] < seats.shape[0] and 1 <= temp[1] < seats.shape[1]:
                    if seats[temp] == 'L' or seats[temp] == '#':
                        neighbours.append(temp)
                        break
                    temp = (temp[0] + direction[0], temp[1] + direction[1])
            occupied = sum(1 for n in neighbours if seats[n] == '#')

            if seats[i, j] == 'L' and occupied == 0:
                new_seats[i, j] = '#'
                change = True
            elif seats[i, j] == '#' and occupied >= 5:
                new_seats[i, j] = 'L'
                change = True

    seats = new_seats

occupied_seats = sum(1 for y in seats for x in y if x == '#')
print(f"Part 2: {occupied_seats}")
