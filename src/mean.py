from typing import Any

import sympy

from cli import ListFloatParameter, mainloop


def _armean(values: tuple[float, ...]) -> float:
    return sum(values) / len(values)


def _geomean(values: tuple[float, ...]) -> Any:
    mult = 1.0
    for i in values:
        mult *= i
    return sympy.root(mult, len(values))


def main() -> None:
    numbers = ListFloatParameter("Число")

    def calc_and_print() -> None:
        print(f"Среднее арифметическое: {_armean(numbers.value)}")
        print(f"Среднее геометрическое: {_geomean(numbers.value)}")

    mainloop(calc_and_print, (numbers,))


if __name__ == "__main__":
    main()
