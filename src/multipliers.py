"""Разложение числа на множители."""
from cli import mainloop, IntParameter, is_this
from eratosthenes import compute_prime_numbers


def main() -> None:
    """Выполняется при запуске модуля."""
    def test_number(number: int) -> bool:
        return is_this(number > 1, 'Введите число больше единицы.')

    number = IntParameter('Число', test_number)

    def compute_and_print() -> None:
        prime_numbers = compute_prime_numbers(number.value)
        if number.value in prime_numbers:
            print('Простое число.')
            return
        quotient: float = number.value
        multipliers = []
        while quotient > 1:
            for i in prime_numbers:
                if quotient % i == 0:
                    multipliers.append(i)
                    quotient /= i
                    break
        print('{0}.'.format(', '.join([str(i) for i in multipliers])))

    mainloop((number,), compute_and_print)


if __name__ == '__main__':
    main()
