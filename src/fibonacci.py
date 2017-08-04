"""Вычисление ряда Фибоначчи."""


def main() -> None:
    """Выполняется при запуске модуля."""
    i, j = 0, 1
    for _ in range(20):
        print(i)
        i, j = j, i + j


if __name__ == '__main__':
    main()
