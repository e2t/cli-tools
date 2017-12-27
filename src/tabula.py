"""Генерация таблицы случайных ответов для одного корпоративного теста."""
from random import randint
from math import log10


SIZE = 26
MAXNUM = 2


def main() -> None:
    pos_number = int(log10(SIZE)) + 2

    def cell_s(value: str) -> str:
        return value * pos_number

    def cell_i(value: int) -> str:
        return '%*d' % (pos_number, value)

    matrix = [[randint(0, MAXNUM) for i in range(SIZE)] for i in range(SIZE)]
    for row in range(SIZE):
        for col in range(row + 1, SIZE):
            matrix[row][col] = MAXNUM - matrix[col][row]
    table = [[cell_s(' '), '|'] + [cell_i(i + 1) for i in range(SIZE)],
             [cell_s('-')] * (SIZE + 2)]
    for row in range(SIZE):
        table.append([cell_i(row + 1), '|'] +
                     [cell_s(' ') if row == col else cell_i(matrix[row][col])
                      for col in range(SIZE)])
    print('\n'.join([''.join(i) for i in table]))


if __name__ == '__main__':
    main()
