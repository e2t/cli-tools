"""Вычисление пропорционального среднего диаметра вала."""
from cli import FloatParameter, mainloop, is_positive, is_this
from mean import geom_mean


def main() -> None:
    """Выполняется при запуске модуля."""
    diam1 = FloatParameter('Diameter #1, mm', is_positive)

    def test_diam2(val: float) -> bool:
        return is_positive(val) and \
            is_this(val != diam1.value, "Can't be equal to #1")

    diam2 = FloatParameter('Diameter #2, mm', test_diam2)

    def compute_and_print() -> None:
        dmin = min(diam1.value, diam2.value)
        dmax = max(diam1.value, diam2.value)
        mid = geom_mean([dmin, dmax])
        rmin = (geom_mean([dmin, mid]) - dmin) / 2
        rmax = (dmax - geom_mean([dmax, mid])) / 2
        print('Middle diameter is %.2f\nRadius near %g is %.2f\n'
              'Radius near %g is %.2f' % (mid, dmin, rmin, dmax, rmax))

    mainloop((diam1, diam2), compute_and_print)


if __name__ == '__main__':
    main()
