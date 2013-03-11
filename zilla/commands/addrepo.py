from zilla import utils
from argparse import ArgumentParser

parser = ArgumentParser(prog="zilla addrepo")
parser.add_argument("repository",
                    nargs="?",
                    default=".",
                    help="The path to the repository to add to zilla.")

def run(args):
    args = parser.parse_args(args)
    store = utils.get_zilla_data_store()

def help():
    parser.print_help()
