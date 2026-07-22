import rsp.utils.timings_store as timings
from rsp.players._play import _play
from time import sleep
import random


class Type:
    @staticmethod
    def instant_double(blocking: bool = False):
        print('\033[34;1minfo: \033[0mplaying \033[36;1minstant double\033[0m')
        _play(blocking)
        sleep(timings.values['idt'])
        _play(blocking)

    @staticmethod
    def fast_double(blocking: bool = False):
        fastdoublewait = random.randrange(*timings.values['fdr'])
        print(
            f'\033[34;1minfo: \033[0mplaying \033[36;1mfast double\033[0m, waiting \033[36;1m{fastdoublewait} seconds\033[0m'
        )
        _play(blocking)
        sleep(fastdoublewait)
        _play(blocking)

    @staticmethod
    def single(blocking: bool = False):
        print('\033[34;1minfo: \033[0mplaying \033[36;1msimple\033[0m')
        _play(blocking)
