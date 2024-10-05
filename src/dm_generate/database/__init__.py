from textwrap import dedent

from docopt import docopt


def cli():
    """
    DM Generate dbase

    Copyright © 2024 Dragon Mobile

    Usage:
        dm-gen dbase (-h | --help)
        dm-gen dbase [options] [PATH ...]

    Arguments:
        DB            Schema (database) name which meets platform requires.
        MISS          One of ("skip", "warn", "raise").
        PATH          One or more file path(s) to search for cvs file(s).
        PLATFORM      One of ("SQLite", "MySQL", "PostgreSQL").

    Options:
        -h, --help           Show this help message.
        -s DB, --schema=DB   Database name to use.[default: component]
        --init               Create database if it does not exit.
        --on-missing=MISS    How any missing cvs files should be handled.[default: warn]
        --platform=PLATFORM  Database connection type.[default: SQLite]
    """
    # print(argv)
    if cli.__doc__ is None:
        raise ValueError("Required Docstring is missing on function")
    args = docopt(dedent(cli.__doc__), options_first=False)
    print(args)


if __name__ == "__main__":
    cli()
