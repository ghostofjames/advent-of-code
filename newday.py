import sys
from pathlib import Path

template = """with open("input.txt") as f:
    data = f.read()

print(data)


# Part 1

print(f"Part 1: {0}")


# Part 2

print(f"Part 2: {0}")
"""

# Get day and year from args
day = f"day{int(sys.argv[1]):02}"
year = f"year{sys.argv[2]}"

print(f"Creating files for {year} {day}")

# Create directories
Path(f"{year}/{day}").mkdir(parents=True)

# Create solution file and write template
Path(f"{year}/{day}/{day}.py").touch()
with open(f"{year}/{day}/{day}.py", "w") as f:
    f.write(template)

# Create input file
Path(f"{year}/{day}/input.txt").touch()
# TODO: fetch input from website and write
