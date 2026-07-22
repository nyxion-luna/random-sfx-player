import rsp.utils.timings_store as timings
from rsp.players._play import _play
from time import sleep
import random


def fast_double():
    fastdoublewait = random.randrange(*timings.values['fdr'])
    print(f'fast double, wait {fastdoublewait}')
    _play()
    sleep(fastdoublewait)
    _play()
