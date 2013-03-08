import sys
from zilla.utils import run_cmd

def run(args):
    if len(args) > 1:
        help()
        sys.exit(1)
    elif len(args) == 1:
        clone_dir = args[0]
    else:
        clone_dir = "mozilla-central"
    run_cmd("git clone git://github.com/mozilla/mozilla-central.git %s" % clone_dir)

def help():
    print """usage: zilla clone [DIRECTORY]

Clone the mozilla-central repository into DIRECTORY. By default, this creates a
'mozilla-central' directory."""
