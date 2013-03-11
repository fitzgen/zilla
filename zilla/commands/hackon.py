import sys
import subprocess
from argparse import ArgumentParser
from zilla import utils

parser = ArgumentParser(prog="zilla hackon")
parser.add_argument("-n", "--new",
                    dest="new",
                    action="store_true",
                    help="Create a new branch")
parser.add_argument("-o", "--off",
                    dest="off",
                    default="master",
                    help="""The name of the branch we want to branch off from. Defaults to
mozilla-central. Used in conjuciton with --new.""")
parser.add_argument("branch",
                    help="The name of the branch")

def run(args):
    args = parser.parse_args(args)
    if args.off and not args.new:
        help()
        sys.exit(1)

    cmd = "git checkout "
    if args.new:
        cmd += "-b "
    cmd += args.branch
    if args.off:
        cmd += " %s" % args.off
    # utils.run_cmd(cmd)

    if args.new:
        store = utils.get_zilla_data_store()
        result = utils.run_cmd("git rev-parse --show-toplevel",
                               stdout=subprocess.PIPE)
        repo_dir = result.stdout.read().strip()
        print repo_dir
        store[repo_dir]["branches"][args.branch] = {
            "off": args.off
        }
        store.save()


def help():
    parser.print_help()
