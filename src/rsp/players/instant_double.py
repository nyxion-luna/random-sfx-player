import rsp.utils.timings_store as timings
from rsp.players._play import _play
from time import sleep


def instant_double():
    print('instant double')
    _play()
    sleep(timings.values['idt'])
    _play()
