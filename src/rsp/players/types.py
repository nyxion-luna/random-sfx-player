import rsp.utils.timings_store as timings
from rsp.players._play import _play
from time import sleep
import random


class Type:
    def instant_double(self):
        print('instant double')
        _play()
        sleep(timings.values['idt'])
        _play()

    def fast_double(self):
        fastdoublewait = random.randrange(*timings.values['fdr'])
        print(f'fast double, wait {fastdoublewait}')
        _play()
        sleep(fastdoublewait)
        _play()

    def single(self):
        print('single')
        _play()
