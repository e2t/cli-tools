"""Решение кубическиз уравнений вида x^3 + Ax^2 + Bx + C = 0."""
from math import acos, pi, cos, acosh, copysign, cosh, asinh, sinh
from typing import Tuple, Union
from cli import FloatParameter, mainloop


def _coef_q(coef_a: float, coef_b: float) -> float:
    return (coef_a**2 - 3 * coef_b) / 9


def _coef_r(coef_a: float, coef_b: float, coef_c: float) -> float:
    return (2 * coef_a**3 - 9 * coef_a * coef_b + 27 * coef_c) / 54


def _coef_s(coef_q: float, coef_r: float) -> float:
    return coef_q**3 - coef_r**2


def _roots(coef_a: float, coef_c: float, coef_q: float, coef_r: float,
           coef_s: float) -> Union[Tuple[float],
                                   Tuple[float, float],
                                   Tuple[float, float, float]]:
    if coef_s > 0:
        phi = acos(coef_r / coef_q**(1 / 3)) / 3
        return (-2 * coef_q**0.5 * cos(phi) - coef_a / 3,
                -2 * coef_q**0.5 * cos(phi + 2 / 3 * pi) - coef_a / 3,
                -2 * coef_q**0.5 * cos(phi - 2 / 3 * pi) - coef_a / 3)

    if coef_s < 0:
        if coef_q > 0:
            phi = acosh(abs(coef_r) / coef_q**1.5) / 3
            return (-2 * copysign(1, coef_r) * coef_q**0.5 * cosh(phi) -
                    coef_a / 3, )

        if coef_q < 0:
            phi = asinh(abs(coef_r) / abs(coef_q)**1.5) / 3
            return (-2 * copysign(1, coef_r) * abs(coef_q)**0.5 *
                    sinh(phi) - coef_a / 3, )

        return (-(coef_c - coef_a**3 / 27)**(1 / 3) - coef_a / 3, )

    return (-2 * coef_r**(1 / 3) - coef_a / 3,
            coef_r**(1 / 3) - coef_a / 3)


def main() -> None:
    """Выполняется при запуске модуля."""
    print('\tx^3 + A * x^2 + B * x + C = 0\n')

    coef_a = FloatParameter('A')
    coef_b = FloatParameter('B')
    coef_c = FloatParameter('C')

    def compute_and_print() -> None:
        coef_q = _coef_q(coef_a.value, coef_b.value)
        coef_r = _coef_r(coef_a.value, coef_b.value, coef_c.value)
        coef_s = _coef_s(coef_q, coef_r)

        print('S = {0}, Q = {1}'.format(coef_s, coef_q))

        for i, root in enumerate(_roots(coef_a.value, coef_c.value,
                                        coef_q, coef_r, coef_s)):
            print('X_{0} = {1}, result = {2}'.format(i, root, (
                round(root**3 + coef_a.value * root**2 +
                      coef_b.value * root + coef_c.value, 6))))

    mainloop((coef_a, coef_b, coef_c), compute_and_print)


if __name__ == '__main__':
    main()
