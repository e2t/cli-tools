import sympy

from cli import IntParameter, isthis, mainloop


def _check_number(value: int) -> bool:
    return isthis(value > 1, "Ожидается целое число больше единицы")


def main() -> None:
    number = IntParameter("Число", _check_number)
    primes: list[int] = []
    max_size = 0

    def calc_and_print() -> None:
        nonlocal max_size
        size = number.value // 2
        if size > max_size:
            max_size = size
            primes.clear()
            primes.extend(sympy.primerange(size + 1))
        mults = []
        num = number.value
        for i in primes:
            while True:
                if num % i != 0:
                    break
                mults.append(i)
                num //= i
        if len(mults) > 1:
            print(mults)
        else:
            print("Простое число")

    mainloop(calc_and_print, (number,))


if __name__ == "__main__":
    main()
