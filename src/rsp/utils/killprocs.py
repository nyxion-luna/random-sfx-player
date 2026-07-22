import rsp.utils.process_store as procs
from signal import SIGTERM
import os


def clearPlays():
    for p in procs.procs:
        try:
            os.killpg(p.pid, SIGTERM)
            procs.reset()
        except ProcessLookupError:
            pass
