from cli import FloatParameter, IntParameter, mainloop, ispositive


def main() -> None:
    length = FloatParameter('Общая длина дистанции', ispositive)
    count = IntParameter('Количество отрезков', ispositive)
    coef = FloatParameter('Коэффициент пропорции соседних отрезков',
                          ispositive)

    def calc_and_print() -> None:
        first = length.value / sum(coef.value**i for i in range(count.value))
        print(f'{first:.0f}', end='')
        for i in range(1, count.value):
            print(f', {first * coef.value**i:.0f}', end='')
        print()

    mainloop(calc_and_print, length, count, coef)


if __name__ == '__main__':
    main()
