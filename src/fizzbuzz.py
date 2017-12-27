"""
Решение популярной задачи FizzBuzz.

Перебирая числа от 1 до 100, если число кратно 3, напечатать Fizz, если число
кратно 5, напечатать Buzz, если число кратно и 3 и 5, напечатать FizzBuzz, если
число не кратно ни 3, ни 5, напечатать само число.
"""


def main() -> None:
    for i in range(1, 101):
        is_multiple_by_3 = (i % 3) == 0
        is_multiple_by_5 = (i % 5) == 0
        if is_multiple_by_3:
            print('Fizz', end='')
        if is_multiple_by_5:
            print('Buzz', end='')
        if not is_multiple_by_3 and not is_multiple_by_5:
            print(i, end='')
        print()


if __name__ == '__main__':
    main()
