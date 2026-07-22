import signal
import sys


def setup():
    def onExit(code, stack):
        print(f'\n\033[31;1mexiting with code {code}\033[0m')
        sys.exit(0)

    signal.signal(signal.SIGINT, handler=onExit)
