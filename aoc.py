import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

TEMPLATE_FILE = Path("newtemplate.py")


def create_directories(year: str, day: str):
    path = Path(f"year{year}/day{day}")
    path.mkdir(parents=True)


def create_solution(year: str, day: str):
    path = Path(f"year{year}/day{day}/day{day}.py")
    path.touch()

    with TEMPLATE_FILE.open() as fsrc:
        with path.open('w') as fdst:
            fdst.write(fsrc.read())


def create_input(year: str, day: str):
    path = Path(f"year{year}/day{day}/input.txt")
    path.touch()

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = dict(session=AOC_SESSION)
    r = requests.get(url, cookies=cookies)

    with path.open('w') as f:
        f.write(r.text.rstrip('\n'))


if __name__ == "__main__":
    load_dotenv()
    AOC_SESSION = os.getenv("AOC_SESSION")

    # Get day and year from args
    try:
        YEAR = f"{sys.argv[1]}"
        DAY = f"{int(sys.argv[2]):02}"
    except IndexError:
        print(f"Invalid args {sys.argv}")
        exit()

    print(f"Creating files for year{YEAR} day{DAY}")

    try:
        create_directories(YEAR, DAY)
        create_solution(YEAR, DAY)
        create_input(YEAR, DAY)

    except FileExistsError:
        print(f"Files for year{YEAR} day{DAY} already exist")
