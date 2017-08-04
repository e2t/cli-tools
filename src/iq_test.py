"""Решение перебором задачи из теста IQ  <https://toster.ru/q/419897>."""
from sys import stderr
from time import time
from typing import Dict, Callable, Set


def replace_letters_by_digits(
        possible_values: Dict[str, Set[int]],
        test_condition: Callable[[Dict[str, int]], bool],
        print_answer: Callable[[Dict[str, int]], None]) -> None:
    """
    Решает перебором задачи по подстановке цифр вместо букв.

    Результаты выводит на экран.
    Предполагается, что все цифры-буквы разные (А != В и т.д.).

    Принимает следующие аргументы:
    * possible_values - словарь из букв и соответствующих множеств чисел;
    * test_condition  - условие проверки значений;
    * print_answer    - способ вывода результатов на экран.
    """
    digits: Dict[str, int] = {}
    letters = tuple(possible_values)
    qty_letters = len(letters)
    start_time = time()

    def print_ellapsed_time() -> None:
        print('Прошло {0:.3f} сек'.format(time() - start_time), file=stderr)

    def compute(index: int) -> None:
        if index < qty_letters:
            key = letters[index]
            digits_values = digits.values()
            for i in possible_values[key]:
                if i not in digits_values:
                    digits[key] = i
                    compute(index + 1)
                    del digits[key]
        elif test_condition(digits):
            print_ellapsed_time()
            print_answer(digits)

    compute(0)
    print_ellapsed_time()


def _test_condition(digits: Dict[str, int]) -> bool:
    dgj  = digits['D'] * 100  + digits['G'] * 10 + digits['J']
    jae  = digits['J'] * 100  + digits['A'] * 10 + digits['E']
    bhf  = digits['B'] * 100  + digits['H'] * 10 + digits['F']
    ddab = digits['D'] * 1100 + digits['A'] * 10 + digits['B']
    ga   = digits['G'] * 10   + digits['A']
    return dgj + jae + bhf == ddab and \
        digits['F'] * digits['C'] / digits['J'] == ga


def _print_answer(digits: Dict[str, int]) -> None:
    values = ', '.join('{0} = {1}'.format(i, digits[i])
                       for i in sorted(digits))
    print('{0}\nA / G = {1}\n'.format(values, digits['A'] / digits['G']))


def main() -> None:
    """
    Задача: DGJ + JAE + BHF = DDAB и F * C / J = GA, найти A / G.

    Предварительный анализ данных:
    * B, G, J из 1..9, иначе числа утратят свою значность;
    * F, C    из 1..9, иначе F * C / J == 0;
    * D       из 1..2, т.к. сумма трёх цифр + 0..2 <= 26;
    * A, E, H из 0..9, всё остальное.
    """
    replace_letters_by_digits({'A': set(range(0, 10)),
                               'B': set(range(1, 10)),
                               'C': set(range(1, 10)),
                               'D': {1, 2},
                               'E': set(range(0, 10)),
                               'F': set(range(1, 10)),
                               'G': set(range(1, 10)),
                               'H': set(range(0, 10)),
                               'J': set(range(1, 10))},
                              _test_condition, _print_answer)


if __name__ == '__main__':
    import cProfile
    cProfile.run('for i in range(1): main()')
