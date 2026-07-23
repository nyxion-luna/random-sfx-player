from rsp.utils.killprocs import clearPlays
import signal
import sys


def setup():
    def onExit(code, stack):
        clearPlays()
        print('\033[31;1mend: \033[33mexiting\033[0m')
        sys.exit(0)

    signal.signal(signal.SIGINT, handler=onExit)
