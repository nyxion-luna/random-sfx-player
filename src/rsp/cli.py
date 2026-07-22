from time import sleep
import argparse
import random
import sys

from rsp.__init__ import __version__, __description__
from rsp.utils.sigint_handler import setup
import rsp.players.cmd_store as cmd
from rsp.players._play import _play

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
values = {
    'rot': [99, 218, 2],  # range of time between each event in seconds [min, max, step]
    'idc': 20,  # instant double chance in %
    'idt': 0.5,  # time between each event of a fast double in seconds
    'fdc': 20,  # fast double chance in %
    'fdr': [8, 16],  # range of time between each event of a fast double [min, max]
}


def main():
    while True:
        playtype = random.randrange(101)

        if 0 <= playtype < (values['idc'] + 1):
            print('instant double')
            _play()
            sleep(values['idt'])
            _play()
        elif (values['idc'] + 1) <= playtype < (values['fdc'] + values['idc'] + 1):
            fastdoublewait = random.randrange(*values['fdr'])
            print(f'fast double, wait {fastdoublewait}')
            _play()
            sleep(fastdoublewait)
            _play()
        else:
            print('single')
            _play()

        randwait = random.randrange(*values['rot'])
        print(f'waiting for {randwait} seconds')
        sleep(randwait)
