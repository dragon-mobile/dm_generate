import os
import sys
from importlib.metadata import EntryPoints, entry_points, version
from textwrap import dedent

from docopt import docopt

from .errors import PluginError


# cspell:ignore licence
def cli():
    """
    DM Generate

    Copyright © 2024 Dragon Mobile

    Usage:
        dm-gen [options]
        dm-gen <command> [<args>...]

    Arguments:
        <command>      CLI command to be ran.
        <args>         Per command additional arguments.

        Common commands are:
            dbase      Managing database(s) and their tables, data, etc.
            footprint  Creating and updating KiCAD component footprint(s).
            model      Adding and updating KiCAD component 3D Model(s).
            symbol     Management of KiCAD symbol libraries.

    Options:
        -h, --help     Show this help message.
        --license      Show license text.
        --licence      Show license text for those who can't remember spelling.
        --version      Show version.
    """
    if cli.__doc__ is None:
        raise ValueError("Required Docstring is missing on function")
    args = docopt(
        dedent(cli.__doc__), options_first=True, version=version(__name__)
    )
    # print(args)
    if args["--license"] or args["--licence"]:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = f"{script_dir}/../../LICENSE"
        with open(file_path, "r") as file:
            contents = file.read()
            print("\n", contents)
            sys.exit()
    if args["<command>"]:
        cname: str = args["<command>"]
        eps: EntryPoints = entry_points(group="cli")
        if len(eps) == 0:
            raise PluginError(msg=f"Command '{cname}' not found in group 'cli'")
        elif len(eps) > 1:
            raise PluginError(msg=f"More than one {cname} found in group 'cli'")
        if cname not in eps.names:
            raise PluginError(msg=f"Unknown command: '{cname}'")
        command = eps[cname].load()
        # argv = args["<args>"]
        # print(argv)
        sys.exit(command.cli())


if __name__ == "__main__":
    cli()
