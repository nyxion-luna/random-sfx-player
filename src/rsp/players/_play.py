import rsp.utils.process_store as procs
import rsp.players.cmd_store as cmd
import subprocess as sub


def _nonblocking():
    p = sub.Popen(
        cmd.command,
        stdout=sub.DEVNULL,
        stderr=sub.DEVNULL,
        start_new_session=True,
    )
    return p


def _blocking():
    p = sub.run(
        cmd.command,
        stdout=sub.DEVNULL,
        stderr=sub.DEVNULL,
    )
    return p


def _play(blocking: bool = False):
    if not blocking:
        p = _nonblocking()

        procs.procs.append(p)
    elif blocking:
        _blocking()
