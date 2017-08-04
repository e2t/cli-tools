"""Расчет скорости перебора паролей."""
from collections import OrderedDict
from math import log
from cli import FloatParameter, is_positive, mainloop


UNITS = OrderedDict({60 * 60 * 24 * 30 * 12: 'year',
                     60 * 60 * 24 * 30: 'month',
                     60 * 60 * 24: 'day',
                     60 * 60: 'hour',
                     60: 'minute',
                     1: 'second'})


def _optimal_size_units(time: float) -> int:
    i = 0
    for i in UNITS:
        if time >= i:
            break
    return i


def _qty_units(time: float, size_units: int) -> str:
    qty = round(time / size_units)
    return '%7.0f %s%s' % (qty, UNITS[size_units], 's' if qty > 1 else '')


def main() -> None:
    """Выполняется при запуске модуля."""
    symbols_number = 36
    max_len_passwd = 12
    speed = FloatParameter('Brut-force speed, paswd/sec', is_positive, None,
                           1e6)

    def compute_and_print() -> None:
        for i in range(1, max_len_passwd + 2):
            variants_number = symbols_number**i
            time = variants_number / speed.value
            if time < 1:
                text_time = 'less than one second'
            else:
                text_time = _qty_units(time, _optimal_size_units(time))
            entropy = log(variants_number) / log(2)
            print('%2d symb. %21d variants, %2.0f bits, %s' %
                  (i, variants_number, entropy, text_time))

    mainloop((speed,), compute_and_print)


if __name__ == '__main__':
    main()
