import random
from math import floor, log10


def main() -> None:
    minv, maxv = 0, 2
    size = 25

    poscount = floor(log10(size)) + 2
    space = ' ' * poscount
    horbar = '─' * poscount

    def cell(num: int) -> str:
        return f'{num:{poscount}d}'

    random.seed()
    range_size = range(size)
    matrix = [[space] * size for _ in range_size]

    for i in range_size:
        for j in range_size[i + 1:]:
            num = random.randint(minv, maxv)
            matrix[i][j] = cell(num)
            matrix[j][i] = cell(maxv - num + minv)

    headings = [cell(i + 1) for i in range_size]
    lines = []
    lines.append([space, '│'] + headings)
    lines.append([horbar, '┼'] + [horbar] * size)
    for i in range_size:
        lines.append([headings[i], '│'] + matrix[i])
    print(*(''.join(i) for i in lines), sep='\n')


if __name__ == '__main__':
    main()
