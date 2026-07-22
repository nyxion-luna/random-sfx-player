import rsp.utils.timings_store as timings
from rsp.players._play import _play
from time import sleep
import random


class Type:
    @staticmethod
    def instant_double(blocking: bool = False):
        print('instant double')
        _play(blocking)
        sleep(timings.values['idt'])
        _play(blocking)

    @staticmethod
    def fast_double(blocking: bool = False):
        fastdoublewait = random.randrange(*timings.values['fdr'])
        print(f'fast double, wait {fastdoublewait}')
        _play(blocking)
        sleep(fastdoublewait)
        _play(blocking)

    @staticmethod
    def single(blocking: bool = False):
        print('single')
        _play(blocking)
