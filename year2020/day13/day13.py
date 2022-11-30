from math import gcd

with open("input.txt") as f:
    data = f.read().splitlines()
    # data = ["939", "7,13,x,x,59,x,31,19"]

# Part 1
time = int(data[0])
buses = [int(b) for b in data[1].split(',') if b != 'x']

wait_times = [(bus, ((time // bus) * bus) + bus - time) for bus in buses]
next_bus = min(wait_times, key=lambda x: x[1])

print(f"Part 1: {next_bus[0] * next_bus[1]}")


# Part 2
buses = [int(b) if b != 'x' else 'x' for b in data[1].split(',')]

timestamp = 0
matched_buses = [buses[0]]
while not len(matched_buses) == len(buses) - buses.count('x'):
    lcm = matched_buses[0]
    for i in matched_buses[1:]:
        lcm = lcm * i // gcd(lcm, i)
    timestamp += lcm

    for i, bus in enumerate(buses):
        if bus != 'x':
            if (timestamp + i) % bus == 0:
                if bus not in matched_buses:
                    matched_buses.append(bus)

print(f"Part 2: {timestamp}")
