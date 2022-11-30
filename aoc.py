from datetime import datetime
from pathlib import Path

import click
import requests
from dateutil.tz import gettz
from dotenv import load_dotenv

TEMPLATE_FILE = Path("newtemplate.py")
AOC_TZ = gettz("America/New_York")


def get_input(year: int, day: int, session: str):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = dict(session=session)
    r = requests.get(url, cookies=cookies)
    return r.text.rstrip('\n')


def most_recent_year():
    now = datetime.now(AOC_TZ)
    if int(now.month) == 12:
        return int(now.year)
    else:
        return int(now.year) - 1


def get_day():
    now = datetime.now(AOC_TZ)
    if int(now.month) != 12:
        return 25
    return int(now.day)


@click.group()
def cli():
    pass


@cli.command()
@click.argument('day',
                default=get_day(),
                type=click.IntRange(1, 25))
@click.argument('year',
                default=most_recent_year(),
                type=click.IntRange(2015, most_recent_year()))
@click.option('--download/--no-download', '-d/ ',
              default=True,
              help="Download input from AOC")
@click.option('--session', envvar='AOC_SESSION',
              help="Session cookie")
def new(day, year, download, session):
    """Create files for new advent of code day, optionally fetching input"""

    # Create directories and files
    click.echo(f"Creating files for day {day} {year}")
    try:
        Path(f"year{year}/day{day:02}").mkdir(parents=True)
        Path(f"year{year}/day{day:02}/day{day:02}.py").touch()
        Path(f"year{year}/day{day:02}/input.txt").touch()
    except FileExistsError:
        click.echo(f"Files for year{year} day{day} already exist")
        exit()

    # Copy content of template file to new solution file
    click.echo("Copying template to solution file")
    with TEMPLATE_FILE.open() as fsrc:
        with Path(f"year{year}/day{day:02}/day{day:02}.py").open('w') as fdst:
            fdst.write(fsrc.read())

    # Download input and save to input file
    if download:
        click.echo(f"Downloading input for day {day:02}")
        input_ = get_input(year, day, session)

        with Path(f"year{year}/day{day:02}/input.txt").open('w') as f:
            f.write(input_)


if __name__ == "__main__":
    load_dotenv()
    cli()
