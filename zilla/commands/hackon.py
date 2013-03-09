import sys
from zilla.utils import run_cmd

def run(args):
    if len(args) != 1:
        help()
        sys.exit(1)
    else:
        run_cmd("git checkout %s" % args[0])

def help():
    print """usage: zilla hackon BRANCH

Checkout the given branch so that you can hack on it"""
