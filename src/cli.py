"""CLI for wrangler"""
import argparse
import glob
import pathlib
import sys


parser = argparse.ArgumentParser(
    prog="wrangler",
    description="Parses and transcribes yaml files to lua scripts",
    epilog="Example: wrangler --output-path ./temp file.yaml path",
)

parser.add_argument("paths", nargs="*", type=pathlib.Path)
parser.add_argument("--output-path", type=pathlib.Path)


def files_from_path(_path):
    """returns generator of files from path"""
    if _path.is_dir():
        for _file in glob.glob(_path, recursive=True):
            yield _file


def get_queue(_paths):
    """creates generator of files for parsing"""
    for _path in _paths:
        if _path.is_dir():
            yield files_from_path(_path)
        yield _path


def get_cli_data():
    """returns an object of user inputted data"""
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()
    return {"output_path": args.output_path, "queue": get_queue(args.paths)}
