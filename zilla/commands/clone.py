import sys
import os
from zilla.utils import run_cmd, get_zilla_data_store
from argparse import ArgumentParser

parser = ArgumentParser(prog="zilla clone")
parser.add_argument("directory",
                    nargs="?",
                    default="mozilla-central",
                    help="Directory to clone the repository into.")

def run(args):
    args = parser.parse_args(args)
    run_cmd("git clone git://github.com/mozilla/mozilla-central.git %s" % args.directory)

    # TODO: check for failure of command here

    store = get_zilla_data_store()
    store[os.path.abspath(clone_dir)] = {
        "branches": {}
    }
    store.save()

def help():
    parser.print_help()
