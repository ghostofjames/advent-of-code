import re
from dataclasses import dataclass


@dataclass
class Vec():
    x: int
    y: int
    z: int

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __radd__(self, other):
        return self.__add__(self, other)

    def distance(self):
        return abs(self.x) + abs(self.y) + abs(self.z)


@dataclass
class Particle():
    p: Vec
    v: Vec
    a: Vec

    def simulate(self):
        self.v += self.a
        self.p += self.v

    def distance_origin(self):
        return self.p.distance()


with open("input.txt") as f:
    # with open("example.txt") as f:
    data = f.read()


# Part 1
particles = {}
for i, x in enumerate(data.splitlines()):
    x = [int(s) for s in re.findall(r'-?\d+', x)]
    particles[i] = Particle(Vec(*x[0:3]), Vec(*x[3:6]), Vec(*x[6:9]))

for _ in range(500):
    for i, p in particles.items():
        p.simulate()

    print(min(particles.keys(), key=lambda x: particles[x].distance_origin()))

id = min(particles.keys(), key=lambda x: particles[x].distance_origin())
print(f"Part 1: {id}")


# Part 2
particles = []
for i, x in enumerate(data.splitlines()):
    x = [int(s) for s in re.findall(r'-?\d+', x)]
    particles.append(Particle(Vec(*x[0:3]), Vec(*x[3:6]), Vec(*x[6:9])))

for _ in range(100):
    for p in particles:
        p.simulate()

    positions = [p.p for p in particles]
    particles = [part for part in particles if positions.count(part.p) == 1]

    print(len(particles))
print(f"Part 2: {len(particles)}")
