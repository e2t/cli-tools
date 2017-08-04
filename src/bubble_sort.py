"""Сортировка пузырьком."""
import random
from typing import List


def _bsort(array: List[int]) -> None:
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]


def main() -> None:
    """Выполняется при запуске модуля."""
    ary = [random.randint(1, 100) for i in range(20)]
    print(ary)
    _bsort(ary)
    print(ary)


if __name__ == '__main__':
    main()
