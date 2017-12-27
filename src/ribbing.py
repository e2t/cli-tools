"""Модуль вычисляет суммы арифметической прогрессии."""
from cli import mainloop, FloatParameter, IntParameter, is_this, is_positive


def _arith_seq_step(sum_a: float, qty_a: int, sum_b: float, qty_b: int) \
        -> float:
    """
    Шаг арифметической прогрессии.

    Принимает пару сумм и количество элементов.
    """
    return (sum_a / qty_a - sum_b / qty_b) * 2 / (qty_a - qty_b)


def _arith_seq_first(summa: float, qty: int, step: float) -> float:
    """Первый элемент арифметической прогрессии."""
    return summa / qty - (qty - 1) * step / 2


def _arith_seq_summa(qty: int, first: float, step: float) -> float:
    """Сумма элементов арифметической прогрессии."""
    return qty * (first + (qty - 1) * step / 2)


def main() -> None:
    sum_a = FloatParameter('Сумма N1 элементов', is_positive)
    qty_a = IntParameter('N1', is_positive)
    sum_b = FloatParameter('Сумма N2 элементов', is_positive)

    def test_qty_b(value: float) -> bool:
        return is_positive(value) and \
            is_this(value != qty_a.value, 'Не может быть равным N1')

    qty_b = IntParameter('N2', test_qty_b)

    def compute_and_print() -> None:
        step = _arith_seq_step(sum_a.value, qty_a.value,
                               sum_b.value, qty_b.value)
        first = _arith_seq_first(sum_a.value, qty_a.value, step)
        for i in reversed(range(1, max(qty_a.value, qty_b.value) + 2)):
            print(round(_arith_seq_summa(i, first, step)), end='  ')
        print('[{0}{1}]'.format('+' if step > 0 else '', round(step)))

    mainloop((sum_a, qty_a, sum_b, qty_b), compute_and_print)


if __name__ == '__main__':
    main()
