"""
Решение кубическиз уравнений вида x^3 + Ax^2 + Bx + C = 0.

https://ru.wikipedia.org/wiki/Тригонометрическая_формула_Виета
"""
from math import acos, pi, cos, acosh, copysign, cosh, asinh, sinh
from typing import Tuple, Union
from cli import FloatParameter, mainloop


def compute_q(a: float, b: float) -> float:
    return (a**2 - 3 * b) / 9


def compute_r(a: float, b: float, c: float) -> float:
    return (2 * a**3 - 9 * a * b + 27 * c) / 54


def copmute_s(q: float, r: float) -> float:
    return q**3 - r**2


TupleFloats = Union[Tuple[float],
                    Tuple[float, float],
                    Tuple[float, float, float]]


def roots(a: float, c: float, q: float, r: float, s: float) -> TupleFloats:
    result: TupleFloats
    if s > 0:
        phi = acos(r / q**1.5) / 3
        root1 = -2 * q**0.5 * cos(phi) - a / 3
        root2 = -2 * q**0.5 * cos(phi + 2 / 3 * pi) - a / 3
        root3 = -2 * q**0.5 * cos(phi - 2 / 3 * pi) - a / 3
        result = (root1, root2, root3)

    elif s < 0:
        if q > 0:
            phi = acosh(abs(r) / q**1.5) / 3
            root1 = -2 * copysign(1, r) * q**0.5 * cosh(phi) - a / 3
            result = (root1, )

        elif q < 0:
            phi = asinh(abs(r) / abs(q)**1.5) / 3
            root1 = -2 * copysign(1, r) * abs(q)**0.5 * sinh(phi) - a / 3
            result = (root1, )
        else:
            root1 = -(c - a**3 / 27)**(1 / 3) - a / 3
            result = (root1, )
    else:
        root1 = -2 * r**(1 / 3) - a / 3
        root2 = r**(1 / 3) - a / 3
        result = (root1, root2)
    return result


def main() -> None:
    print('\tx^3 + A * x^2 + B * x + C = 0\n')

    a = FloatParameter('A')
    b = FloatParameter('B')
    c = FloatParameter('C')

    def compute_and_print() -> None:
        q = compute_q(a.value, b.value)
        r = compute_r(a.value, b.value, c.value)
        s = copmute_s(q, r)

        print(f'Q = {q}, R = {r}, S = {s}')

        for i, root in enumerate(roots(a.value, c.value, q, r, s)):
            res = round(root**3 + a.value * root**2 +
                        b.value * root + c.value, 6)
            print(f'X_{i} = {root}, result = {res}')

    mainloop((a, b, c), compute_and_print)


if __name__ == '__main__':
    main()
