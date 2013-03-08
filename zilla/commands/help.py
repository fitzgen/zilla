import sys
from zilla.utils import usage, command_importer

def run(args):
    if len(args) == 0:
        usage()
    else:
        subcmd = command_importer(args[0])
        subcmd.help()
        sys.exit(1)

def help():
    usage()
