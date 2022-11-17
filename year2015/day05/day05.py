import re

# I can't regex so thank you to inokichi for the regex
# https://www.reddit.com/r/adventofcode/comments/3viazx/day_5_solutions/cxnt6bp/

with open("input.txt") as f:
    data = f.read().splitlines()


# Part 1
count = 0
for string in data:
    # It does not contain the strings ab, cd, pq, or xy, even if they are part of one of
    # the other requirements.
    if any(x in string for x in ("ab", "cd", "pq", "xy")):
        continue

    # It contains at least one letter that appears twice in a row, like xx, abcdde (dd),
    # or aabbccdd (aa, bb, cc, or dd).
    if not re.search(r"([a-z])\1", string):
        continue

    # It contains at least three vowels (aeiou only), like aei, xazegov,
    # or aeiouaeiouaeiou.
    if not len([x for x in string if x in "aeiou"]) > 2:
        continue

    count += 1

print(f"Part 1: {count}")


# Part 2
count = 0
for string in data:
    # It contains a pair of any two letters that appears at least twice in the string
    # without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but
    # it overlaps).
    if not len(re.findall(r"([a-z]{2}).*\1", string)):
        continue

    # It contains at least one letter which repeats with exactly one letter between them,
    # like xyx, abcdefeghi (efe), or even aaa.
    if not re.findall(r"([a-z]).\1", string):
        continue

    count += 1

print(f"Part 2: {count}")
