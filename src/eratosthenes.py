"""Поиск простых чисел методом Решето Эратосфена."""
import sys
from typing import List


def _sieve(max_number: int) -> List[bool]:
    sieve = [False, False, True] + \
            [i % 2 != 0 for i in range(3, max_number + 1)]
    for i in range(3, max_number, 2):
        if sieve[i]:
            for j in range(i * i, max_number + 1, i):
                sieve[j] = False
    return sieve


def _extract_prime_numbers(sieve: List[bool]) -> List[int]:
    return [index for index, is_prime_number in enumerate(sieve)
            if is_prime_number]


def compute_prime_numbers(max_number: int) -> List[int]:
    """Функция возвращает список простых чисел меньше указанного."""
    return _extract_prime_numbers(_sieve(max_number))


def main() -> None:
    """Выполняется при запуске модуля."""
    max_num = int(sys.argv[1]) if len(sys.argv) > 1 else 1000009
    prime_numbers = compute_prime_numbers(max_num)
    for i in prime_numbers:
        print('{0} '.format(i), end='')


if __name__ == '__main__':
    import cProfile
    cProfile.run('print(sys.getsizeof(_sieve(4000000000)))')


# Писал своего Эратосфена году эдак в 2002.
# На машине было то ли 128, то ли 256 мб памяти (не помню точно, до апгрейда это всё происходило или после), а хотелось проверять 4 миллиарда чисел — ну то есть максимум, что в int32 влезает.
# Я поступил просто: флажок для каждого нечетного числа соответствовал одному биту, четные пропускались вообще. 4 млрд чисел / 16 = 256 мб памяти.
# Внутри цикла индекс преобразовывался в битовую маску, проставлялись флажки тоже битовыми операциями.
# Писалось всё на C++.
# Время работы, если склероз не подводит, было что-то в районе 5 минут на Celeron-667.
# Код за давностью лет, к сожалению, утерян.
