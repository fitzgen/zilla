import pkg_resources

def run(args):
    print pkg_resources.require("zilla")[0].version

def help():
    print "usage: zilla --version"
