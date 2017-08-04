"""Программма генерирует случайную таблицу для одного корпоративного теста."""
from random import randint
from math import log10
from typing import List


def main() -> None:
    """Выполняется при запуске модуля."""
    size = 26
    maxnum = 2
    pos_number = int(log10(size)) + 2

    def create_matrix(size: int) -> List[List[int]]:
        matrix = [[randint(0, maxnum) for i in range(size)]
                  for i in range(size)]
        for row in range(size):
            for col in range(row + 1, size):
                matrix[row][col] = maxnum - matrix[col][row]
        return matrix

    def cells(value: str) -> str:
        return value * pos_number

    def celli(value: int) -> str:
        return '%*d' % (pos_number, value)

    def create_table(matrix: List[List[int]]) -> str:
        table = [[cells(' '), '|'] + [celli(i + 1) for i in range(size)],
                 [cells('-')] * (size + 2)]
        for row in range(size):
            table.append([celli(row + 1), '|'] +
                         [cells(' ') if row == col else celli(matrix[row][col])
                          for col in range(size)])
        return '\n'.join([''.join(i) for i in table])

    print(create_table(create_matrix(size)))


if __name__ == '__main__':
    main()
