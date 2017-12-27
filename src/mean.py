"""Вычисление среднего ариметического и геометрического ряда чисел."""
from typing import List
from cli import mainloop, ArrayFloatParameter


def arith_mean(array: List[float]) -> float:
    """Среднее арифметическое ряда чисел."""
    return sum(array) / len(array)


def geom_mean(array: List[float]) -> float:
    """Среднее геометрическое ряда чисел."""
    mult = 1.0
    for i in array:
        mult *= i
    return mult**(1 / len(array))


def main() -> None:
    number = ArrayFloatParameter('Число')

    def compute_and_print() -> None:
        print(f'Среднее арифметическое: {arith_mean(number.value)}')
        print(f'Среднее геометрическое: {geom_mean(number.value)}')

    mainloop((number,), compute_and_print)


if __name__ == '__main__':
    main()
