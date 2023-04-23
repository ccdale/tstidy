import json
import os
import sys

__appname__ = "tstidy"
__version__ = "0.1.2"
tvhuser = "unset"
tvhpass = "unset"
tvhipaddr = "druidmedia"
radiooutputdir = "~/radio"
sshhost = "druidmedia"
sshuser = "chris"


def errorNotify(exci, e, fname=None):
    lineno = exci.tb_lineno
    if fname is None:
        fname = exci.tb_frame.f_code.co_name
    ename = type(e).__name__
    msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
    print(msg)


def errorRaise(exci, e, fname=None):
    errorNotify(exci, e, fname)
    raise


def errorExit(exci, e, fname=None):
    errorNotify(exci, e, fname)
    sys.exit(1)


def absPath(usrpath):
    try:
        return os.path.abspath(os.path.expanduser(usrpath))
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def setConfig():
    try:
        global tvhuser, tvhpass, tvhipaddr
        fn = absPath(f"~/.config/{__appname__}.cfg")
        if os.path.exists(fn):
            with open(fn, "r") as ifn:
                cfg = json.load(ifn)
            tvhuser = cfg["tvhuser"]
            tvhpass = cfg["tvhpass"]
            tvhipaddr = cfg["tvhipaddr"]
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def getConfig():
    try:
        fn = absPath(f"~/.config/{__appname__}.cfg")
        # print(fn)
        if os.path.exists(fn):
            # print(f"reporting existence of {fn}")
            with open(fn, "r") as ifn:
                cfg = json.load(ifn)
            # print(f"loaded config: {cfg}")
            return cfg
        return {}
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)
