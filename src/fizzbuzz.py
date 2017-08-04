"""Решение популярной задачи FizzBuzz."""


def main() -> None:
    """Выполняется при запуске модуля."""
    i = 0

    def fizz() -> None:
        print('Fizz')

    def buzz() -> None:
        print('Buzz')

    def fizzbuzz() -> None:
        print('FizzBuzz')

    def number() -> None:
        print(i)

    to_print = {0: number, 1: fizz, 2: buzz, 3: fizzbuzz}
    for i in range(1, 101):
        key = 0
        if not i % 3:
            key += 1
        if not i % 5:
            key += 2
        to_print[key]()


if __name__ == '__main__':
    main()
