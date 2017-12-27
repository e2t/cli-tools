"""Разложение числа на множители."""
from cli import mainloop, IntParameter, is_this
from eratosthenes import compute_prime_numbers


def main() -> None:
    def test_number(number: int) -> bool:
        return is_this(number > 1, 'Введите число больше единицы.')

    number = IntParameter('Число', test_number)

    def compute_and_print() -> None:
        prime_numbers = compute_prime_numbers(number.value)
        if number.value in prime_numbers:
            print('Простое число.')
        else:
            quotient: float = number.value
            multipliers = []
            while quotient > 1:
                iterator = filter(lambda x: quotient % x == 0, prime_numbers)
                try:
                    prime_number = next(iterator)
                except StopIteration:
                    break
                else:
                    multipliers.append(prime_number)
                    quotient /= prime_number
            print(', '.join([str(i) for i in multipliers]), '.', sep='')

    mainloop((number,), compute_and_print)


if __name__ == '__main__':
    main()
