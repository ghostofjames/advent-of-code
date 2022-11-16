import os
import sys

day = f"day{int(sys.argv[1]):02}"

print(f"Creating files for {day}")

os.mkdir(day)
os.mknod(f"{day}/{day}.py")
os.mknod(f"{day}/input.txt")
