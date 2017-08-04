"""Вычисляет "золотые" пропорции цилиндра при заданном объеме."""
from math import pi
from cli import FloatParameter, is_positive, from_l, mainloop


PHI = (5**0.5 + 1) / 2  # Золотое сечение


def _cylinder_height(volume: float, diameter: float) -> float:
    return 4 * volume / pi / diameter**2


def main() -> None:
    """Выполняется при запуске модуля."""
    volume = FloatParameter('Объем цилиндра, л', is_positive, from_l)

    def compute_and_print() -> None:
        diam1 = (4 * volume.value / pi * PHI)**(1 / 3)
        diam2 = (4 * volume.value / pi / PHI)**(1 / 3)
        height1 = _cylinder_height(volume.value, diam1)
        height2 = _cylinder_height(volume.value, diam2)
        print('D1 = %.0f мм, H1 = %.0f мм\nD2 = %.0f мм, H2 = %.0f мм' %
              (diam1 * 1e3, height1 * 1e3, diam2 * 1e3, height2 * 1e3))

    mainloop((volume,), compute_and_print)


if __name__ == '__main__':
    main()
