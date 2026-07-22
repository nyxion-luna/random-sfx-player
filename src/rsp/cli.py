from time import sleep
import argparse
import random
import sys

from rsp.__init__ import __version__, __description__
from rsp.utils.sigint_handler import setup
from rsp.utils.killprocs import clearPlays
import rsp.utils.timings_store as timings
import rsp.players.cmd_store as cmd
from rsp.players.types import Type

setup()

parser = argparse.ArgumentParser(prog='random-sfx-player', description=__description__)
pexcl = parser.add_mutually_exclusive_group(required=True)
pexcl.add_argument(
    'filename',
    nargs='?',
    help='the path of the audio you want to use. the length should be under the minimum time between events to avoid a sharp cutoff.',
)
parser.add_argument(
    '-v',
    '--volume',
    nargs=1,
    type=int,
    help='the volume you want to play the sound at in percentage form. min = 0, max = 800, both inclusive.',
)
parser.add_argument(
    '-b',
    '--blocking',
    action='store_true',
    help='passing this flag will cause all events to be blocking rather than asynchronous.',
)
parser.add_argument(
    '-t',
    '--test',
    help='this flag will play one single event and exit.',
    action='store_true',
)
pexcl.add_argument(
    '-V',
    '--version',
    help='prints the version and exits.',
    action='store_true',
)
parser.add_argument(
    '-f',
    '--force',
    help='this flag will allow volumes over 800.',
    action='store_true',
)
args = parser.parse_args()

if args.version:
    print(f'\033[32;1mrsp\033[0m, version \033[36;1m{__version__}\033[0m')
    sys.exit(0)


cmd.init(['ffplay', args.filename, '-nodisp', '-autoexit'])

if args.force and args.volume is None:
    print('\033[31;1merror: \033[33m--force \033[0mrequires \033[33;1m--volume\033[0m')
    sys.exit(1)

if args.volume is not None:
    args.volume = args.volume[0]
    if args.volume < 0:
        print(
            f'\033[31;1merror: \033[35mvolume {args.volume} is under 0.\033[0m pass a volume \033[33;1mover or equal to 0.\033[0m'
        )
        sys.exit(1)
    elif 0 <= args.volume <= 100:
        cmd.command.append('-volume')
        cmd.command.append(str(args.volume))
    elif 100 < args.volume <= 800 or args.force:
        cmd.command.append('-af')
        cmd.command.append(f'volume={args.volume / 100}')
    else:
        print(
            f'\033[31;1merror: \033[35mvolume {args.volume} is over 800.\033[0m use the \033[33;1m--force flag.\033[0m'
        )
        sys.exit(1)


def main():
    while not args.test:
        playtype = random.randrange(101)

        is_idc = 0 <= playtype < (timings.values['idc'] + 1)
        is_fdc = (
            (timings.values['idc'] + 1)
            <= playtype
            < (timings.values['fdc'] + timings.values['idc'] + 1)
        )

        clearPlays()

        if is_idc:
            Type.instant_double(args.blocking)
        elif is_fdc:
            Type.fast_double(args.blocking)
        else:
            Type.single(args.blocking)

        randwait = random.randrange(*timings.values['rot'])
        print(f'\033[32;1mmain: \033[0mwaiting for \033[36;1m{randwait} seconds\033[0m')
        sleep(randwait)
    else:
        Type.single(args.blocking)
