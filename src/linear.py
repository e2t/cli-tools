"""Вычисляет уравнение линейной функции по двум координатам."""
from cli import FloatParameter, mainloop, is_this


def _eq1_coeficient_k(x1_coor: float, y1_coor: float,
                      x2_coor: float, y2_coor: float) -> float:
    return (y1_coor - y2_coor) / (x1_coor - x2_coor)


def _eq1_coeficient_b(x1_coor: float, y1_coor: float, coef_k: float) -> float:
    return y1_coor - coef_k * x1_coor


def main() -> None:
    """Выполняется при запуске модуля."""
    x1_coor = FloatParameter('X1')
    y1_coor = FloatParameter('Y1')
    x2_coor = FloatParameter('X2')

    def test_y2(value: float) -> bool:
        return is_this(
            x1_coor.value != x2_coor.value or y1_coor.value != value,
            'Введите координаты двух разных точек.')

    y2_coor = FloatParameter('Y2', test_y2)
    print('\tY = k*X + b\n')

    def compute_and_print() -> None:
        if x1_coor.value == x2_coor.value:
            print('X = %g' % x1_coor.value)
        elif y1_coor.value == y2_coor.value:
            print('Y = %g' % y1_coor.value)
        else:
            coef_k = _eq1_coeficient_k(x1_coor.value, y1_coor.value,
                                       x2_coor.value, y2_coor.value)
            coef_b = _eq1_coeficient_b(x1_coor.value, y1_coor.value, coef_k)
            print('Y = %g * X + (%g)' % (coef_k, coef_b))
            print('Y2 = %g' % (coef_k * x2_coor.value + coef_b))

    mainloop((x1_coor, y1_coor, x2_coor, y2_coor), compute_and_print)


if __name__ == '__main__':
    main()
