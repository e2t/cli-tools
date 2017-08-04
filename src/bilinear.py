"""
Нахождение коэффициентов уравнений вида Axy + Bx + Cy = z по трем точкам.

Задаются три набора координат (x, y, z), вычисляются A, B, C.
"""
from typing import Tuple
from cli import FloatParameter, print_error, mainloop


def main() -> None:
    """Выполняется при запуске модуля."""
    x1 = FloatParameter('x1')
    y1 = FloatParameter('y1')
    z1 = FloatParameter('z1')
    x2 = FloatParameter('x2')
    y2 = FloatParameter('y2')
    z2 = FloatParameter('z2')
    x3 = FloatParameter('x3')
    y3 = FloatParameter('y3')
    z3 = FloatParameter('z3')
    print('\tA * xy + B * x + C * y = z\n')

    def coeff(coords: Tuple[FloatParameter, ...]) -> float:
        return (coords[0].value * coords[1].value * coords[2].value -
                coords[3].value * coords[4].value * coords[5].value)

    def compute_and_print() -> None:
        k1 = coeff((z1, x2, y2, z2, x1, y1))
        k2 = coeff((y1, x2, y2, y2, x1, y1))
        k3 = coeff((x1, x2, y2, x2, x1, y1))
        k4 = coeff((z3, x2, y2, z2, x3, y3))
        k5 = coeff((y3, x2, y2, y2, x3, y3))
        k6 = coeff((x3, x2, y2, x2, x3, y3))
        try:
            kc = (k4 * k3 - k1 * k6) / (k5 * k3 - k2 * k6)
            if k3 == 0:
                kb = (k4 - k5 * kc) / k6
            else:
                kb = (k1 - k2 * kc) / k3
            ka = (z1.value - x1.value * kb - y1.value * kc) / x1.value /\
                y1.value
            print('A = {0}\nB = {1}\nC = {2}'.format(ka, kb, kc))
        except ZeroDivisionError:
            print_error('Деление на ноль!')

    mainloop((x1, y1, z1, x2, y2, z2, x3, y3, z3), compute_and_print)


if __name__ == '__main__':
    main()
