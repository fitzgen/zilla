import sys
import os
import subprocess
import json

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
    pipe = subprocess.Popen(command_string, **opts)
    pipe.wait()
    return pipe

_zilla_data_store = None

def get_zilla_data_store():
    global _zilla_data_store
    if not _zilla_data_store:
        _zilla_data_store = _ZillaDataStore()
    return _zilla_data_store

class _ZillaDataStore(object):
    DATA_STORE_PATH = os.path.join(os.path.expanduser("~"),
                                   ".zilla/store.json")
    DATA_STORE_DEFAULTS = {}

    def __init__(self):
        zilla_dir = os.path.dirname(self.DATA_STORE_PATH)
        if not os.path.isdir(zilla_dir):
            os.mkdir(zilla_dir)
        if not os.path.isfile(self.DATA_STORE_PATH):
            with open(self.DATA_STORE_PATH, "w") as f:
                f.write(json.dumps(self.DATA_STORE_DEFAULTS))
        with open(self.DATA_STORE_PATH, "r") as f:
            self._data = json.loads(f.read())

    def __getitem__(self, attr):
        return self._data[attr]

    def __setitem__(self, attr, val):
        self._data[attr] = val

    def save():
        with open(self.DATA_STORE_PATH, "w") as f:
            f.write(json.dumps(self._data))
