"""Сортировка пузырьком."""
import random
from typing import List


def _bsort(array: List[int]) -> None:
    len_array = len(array)
    for i in range(len_array - 1):
        for j in range(i + 1, len_array):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]


def main() -> None:
    ary = [random.randint(1, 100) for i in range(20)]
    print(ary)
    _bsort(ary)
    print(ary)


if __name__ == '__main__':
    main()
