"""Решение квадратных уравнений вида Ax^2 + Bx + C = 0."""
from cli import FloatParameter, mainloop, is_this


def _discriminant(coef_a: float, coef_b: float, coef_c: float) -> float:
    return coef_b**2 - 4 * coef_a * coef_c


def _first_root(discr: float, coef_a: float, coef_b: float) -> float:
    return (-coef_b + discr**0.5) / 2 / coef_a


def _second_root(discr: float, coef_a: float, coef_b: float) -> float:
    return (-coef_b - discr**0.5) / 2 / coef_a


def _test_roots(root: float, coef_a: float, coef_b: float, coef_c: float) \
        -> None:
    zero = coef_a * root**2 + coef_b * root + coef_c
    print('{0} * {3}^2 + {1} * {3} + {2} = {4}'.format(
        coef_a, coef_b, coef_c, root, zero))


def main() -> None:
    """Выполняется при запуске модуля."""
    print('\tA * x^2 + B * x + C = 0\n')

    def is_nozero(number: float) -> bool:
        return is_this(number != 0, 'Не может быть нулём')

    coef_a = FloatParameter('A', is_nozero)
    coef_b = FloatParameter('B')
    coef_c = FloatParameter('C')

    def compute_and_print() -> None:
        discr = _discriminant(coef_a.value, coef_b.value, coef_c.value)
        print('Дискриминант = {0}'.format(discr))
        if discr < 0:
            print('Нет корней')
            return
        root1 = _first_root(discr, coef_a.value, coef_b.value)
        print('1-й корень = {0}'.format(root1))
        if discr > 0:
            root2 = _second_root(discr, coef_a.value, coef_b.value)
            print('2-й корень = {0}'.format(root2))
        print()
        _test_roots(root1, coef_a.value, coef_b.value, coef_c.value)
        if discr > 0:
            _test_roots(root2, coef_a.value, coef_b.value, coef_c.value)

    mainloop((coef_a, coef_b, coef_c), compute_and_print)


if __name__ == '__main__':
    main()
