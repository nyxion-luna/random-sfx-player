import os
import sys
import signal
import random
import argparse
from time import sleep
import subprocess as sub


def onExit(code, stack):
    print(f'\n\033[31;1mexiting with code {code}\033[0m')
    sys.exit(0)


signal.signal(signal.SIGINT, handler=onExit)

parser = argparse.ArgumentParser(
    prog='random-sfx-player',
    description="you know those '1 hour of random sfx' videos? now with modular design, load your own sound for infinite random sounds!",
)

parser.add_argument(
    'filename',
    help='the path of the audio you want to use. the length should be under the minimum time between events to avoid a sharp cutoff.',
)
args = parser.parse_args()

procs = []
values = {
    'rot': [99, 218, 2],  # range of time between each event in seconds [min, max, step]
    'idc': 20,  # instant double chance in %
    'idt': 0.5,  # time between each event of a fast double in seconds
    'fdc': 20,  # fast double chance in %
    'fdr': [8, 16],  # range of time between each event of a fast double [min, max]
}


def play(blocking: bool = False):
    def _nonblocking(command):
        p = sub.Popen(
            command,
            stdout=sub.DEVNULL,
            stderr=sub.DEVNULL,
            start_new_session=True,
        )
        return p

    def _blocking(command):
        p = sub.run(
            command,
            stdout=sub.DEVNULL,
            stderr=sub.DEVNULL,
        )
        return p

    command = ['ffplay', args.filename, '-nodisp', '-autoexit']
    if not blocking:
        p = _nonblocking(command)

        procs.append(p)
    elif blocking:
        _blocking(command)


def clearPlays():
    for p in procs:
        try:
            os.killpg(p.pid, signal.SIGTERM)
            p = []
        except ProcessLookupError:
            pass


def main():
    while True:
        playtype = random.randrange(101)

        if 0 <= playtype < (values['idc'] + 1):
            print('instant double')
            play()
            sleep(values['idt'])
            play()
        elif (values['idc'] + 1) <= playtype < (values['fdc'] + values['idc'] + 1):
            fastdoublewait = random.randrange(*values['fdr'])
            print(f'fast double, wait {fastdoublewait}')
            play()
            sleep(fastdoublewait)
            play()
        else:
            print('single')
            play()

        randwait = random.randrange(*values['rot'])
        print(f'waiting for {randwait} seconds')
        sleep(randwait)

        clearPlays()
