"""Вычисляет "золотые" пропорции цилиндра при заданном объеме."""
from math import pi
from cli import FloatParameter, is_positive, from_l, mainloop


PHI = (5**0.5 + 1) / 2  # Золотое сечение


def _cylinder_height(volume: float, diameter: float) -> float:
    return 4 * volume / pi / diameter**2


def main() -> None:
    volume = FloatParameter('Объем цилиндра, л', is_positive, from_l)

    def compute_and_print() -> None:
        diam1 = (4 * volume.value / pi * PHI)**(1 / 3)
        diam2 = (4 * volume.value / pi / PHI)**(1 / 3)
        height1 = _cylinder_height(volume.value, diam1)
        height2 = _cylinder_height(volume.value, diam2)
        print(f'D1 = {diam1 * 1e3:.0f} мм, H1 = {height1 * 1e3:.0f} мм\n'
              f'D2 = {diam2 * 1e3:.0f} мм, H2 = {height2 * 1e3:.0f} мм')

    mainloop((volume,), compute_and_print)


if __name__ == '__main__':
    main()
