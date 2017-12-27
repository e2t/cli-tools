"""Вычисление ряда Фибоначчи."""


def main() -> None:
    i = 0
    j = 1
    for _ in range(20):
        print(i)
        i, j = j, i + j


if __name__ == '__main__':
    main()
