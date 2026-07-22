from time import sleep
import argparse
import random
import sys

from rsp.__init__ import __version__, __description__
from rsp.players.types import Type
from rsp.utils.sigint_handler import setup
import rsp.utils.timings_store as timings
import rsp.players.cmd_store as cmd

setup()

parser = argparse.ArgumentParser(prog='random-sfx-player', description=__description__)
pexclusive = parser.add_mutually_exclusive_group(required=True)
pexclusive.add_argument(
    'filename',
    nargs='?',
    help='the path of the audio you want to use. the length should be under the minimum time between events to avoid a sharp cutoff.',
)
parser.add_argument(
    '-v',
    '--volume',
    nargs=1,
    help='the volume you want to play the sound at in percentage form. min = 0, max = 800.',
)
parser.add_argument(
    '-b',
    '--blocking',
    action='store_true',
    help='passing this flag will cause all events to be blocking rather than asynchronous.',
)
parser.add_argument(
    '-t', '--test', help='this flag will play one single event and exit.'
)
pexclusive.add_argument(
    '--version',
    help='prints the version and exits.',
    action='store_true',
)
args = parser.parse_args()

if args.version:
    print(f'rsp, version {__version__}')
    sys.exit(0)


cmd.init(['ffplay', args.filename, '-nodisp', '-autoexit'])


def main():
    while True:
        playtype = random.randrange(101)

        is_idc = 0 <= playtype < (timings.values['idc'] + 1)
        is_fdc = (
            (timings.values['idc'] + 1)
            <= playtype
            < (timings.values['fdc'] + timings.values['idc'] + 1)
        )

        if is_idc:
            Type.instant_double(args.blocking)
        elif is_fdc:
            Type.fast_double(args.blocking)
        else:
            Type.single(args.blocking)

        randwait = random.randrange(*timings.values['rot'])
        print(f'waiting for {randwait} seconds')
        sleep(randwait)
