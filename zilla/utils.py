import sys
import os
import subprocess

IGNORED_COMMAND_FILES = [
    "__init__.py",
    "help.py",
    "version.py"
]

def usage():
    print "usage: zilla COMMAND [OPTIONS]"
    print
    print "Commands:"
    for f in os.listdir(os.path.abspath(os.path.join(__file__, "../commands"))):
        if f.endswith(".py") and not f in IGNORED_COMMAND_FILES:
            print "    %s" % f.replace(".py", "")
    print
    print "To learn more about a specific command, run"
    print "    zilla help COMMAND"
    sys.exit(1)

def command_importer(subcmd):
    try:
        mod = __import__("zilla.commands.%s" % subcmd)
        subcmd = "zilla.commands." + subcmd
    except ImportError:
        try:
            mod = __import__("zilla_%s" %subcmd)
        except ImportError:
            print "Unknown command '%s'" % subcmd
            print
            usage()

    components = subcmd.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)

    return mod

def run_cmd(command_string, **kwargs):
    opts = {
        "shell": True
    }
    opts.update(kwargs)
    return subprocess.call(command_string, **opts)
