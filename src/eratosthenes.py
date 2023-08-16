import gc
import os
import time
from typing import Generic, TypeVar

import psutil
from bitarray import bitarray

_T = TypeVar("_T", bound=list[bool] | bitarray)


class _Sieve(Generic[_T]):
    # False - простое, True - не простое
    def __init__(self, maxnum: int) -> None:
        self._maxnum = maxnum
        self._size = (maxnum + 1) // 2
        self._storage: _T

    def calc(self) -> None:
        if self._maxnum < 2:
            return
        self._storage[0] = True  # 1 не является простым числом

        for i in range(3, int(self._maxnum**0.5) + 1, 2):
            if not self._storage[i // 2]:
                for j in range(i**2, self._maxnum + 1, 2 * i):
                    self._storage[j // 2] = True

    def isprime(self, index: int) -> bool:
        if index == 2:
            return True
        if index % 2 == 0:
            return False
        return not self._storage[index // 2]

    def clear(self) -> None:
        self._storage.clear()


class _SimpleSieve(_Sieve[list[bool]]):
    def __init__(self, maxnum: int) -> None:
        super().__init__(maxnum)

        self._storage = [False] * self._size


class _BitarraySieve(_Sieve[bitarray]):
    def __init__(self, maxnum: int) -> None:
        super().__init__(maxnum)

        self._storage = bitarray(self._size)
        self._storage.setall(False)


def _print_time(sec: float) -> None:
    print(f'\t[{time.strftime("%H:%M:%S", time.gmtime(sec))}]', flush=True)


def _test_sieve(sieve_t: type, maxnum: int) -> None:
    print(f"{sieve_t}, MaxNumber = {maxnum}")
    sieve = sieve_t(maxnum)

    print("Memory = ", end="")
    start = time.time()
    ram = psutil.Process(os.getpid()).memory_info().rss
    elapsed = time.time() - start
    print(f"{ram}", end="")
    _print_time(elapsed)

    print("Calculation...\t", end="")
    start = time.time()
    sieve.calc()
    elapsed = time.time() - start
    _print_time(elapsed)

    if maxnum < 1000:
        for i in range(2, maxnum + 1):
            if sieve.isprime(i):
                print(i, end=", ")
    sieve.clear()
    print("\n")


def main() -> None:
    _test_sieve(_SimpleSieve, 103)
    _test_sieve(_BitarraySieve, 103)

    _test_sieve(_SimpleSieve, 750000000)  # 1.5 min, 1.5 GB
    gc.collect()
    _test_sieve(_BitarraySieve, 750000000)  # 1.5 min, 50 MB
    gc.collect()
    _test_sieve(_BitarraySieve, 2**32 - 16)  # almost int32, 21 min


if __name__ == "__main__":
    main()
