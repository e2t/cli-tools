"""Расчет скорости перебора паролей."""
from collections import OrderedDict
from math import log
from cli import FloatParameter, is_positive, mainloop


SYMBOLS_NUMBER = 36
MAX_LEN_PASSWD = 12

UNITS = OrderedDict({60 * 60 * 24 * 30 * 12: 'year',
                     60 * 60 * 24 * 30: 'month',
                     60 * 60 * 24: 'day',
                     60 * 60: 'hour',
                     60: 'minute',
                     1: 'second'})


def _optimal_size_units(time: float) -> int:
    iterator = filter(lambda x: time >= x, UNITS)
    return next(iterator)


def _qty_units(time: float, size_units: int) -> str:
    qty = round(time / size_units)
    if qty > 1:
        ending = 's'
    else:
        ending = ''
    return f'{qty:7.0f} {UNITS[size_units]}{ending}'


def main() -> None:
    speed = FloatParameter('Brut-force speed, paswd/sec', is_positive, None,
                           1e6)

    def compute_and_print() -> None:
        for i in range(1, MAX_LEN_PASSWD + 2):
            variants_number = SYMBOLS_NUMBER**i
            time = variants_number / speed.value
            try:
                units = _optimal_size_units(time)
            except StopIteration:
                text_time = 'less than one second'
            else:
                text_time = _qty_units(time, units)
            entropy = log(variants_number) / log(2)
            print(f'{i:2d} symb. {variants_number:21d} variants, '
                  f'{entropy:2.0f} bits, {text_time}')

    mainloop((speed,), compute_and_print)


if __name__ == '__main__':
    main()
