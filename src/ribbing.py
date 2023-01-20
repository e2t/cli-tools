from cli import FloatParameter, IntParameter, mainloop, ispositive, isthis


def arseq_step(sum1: float, count1: int, sum2: float, count2: int) -> float:
    return (sum1 / count1 - sum2 / count2) * 2 / (count1 - count2)


def arseq_first(summa: float, count: int, step: float) -> float:
    return summa / count - (count - 1) * step / 2


def arseq_summa(count: int, first: float, step: float) -> float:
    return count * (first + (count - 1) * step / 2)


def main() -> None:
    sum1 = FloatParameter('Сумма N1 элементов', ispositive)
    count1 = IntParameter('N1', ispositive)
    sum2 = FloatParameter('Сумма N2 элементов', ispositive)

    def check_count2(value: int) -> bool:
        return ispositive(value) and isthis(value != count1.value,
                                            'Не может быть равным N1')
    count2 = IntParameter('N2', check_count2)

    def calc_and_print() -> None:
        step = arseq_step(sum1.value, count1.value, sum2.value, count2.value)
        first = arseq_first(sum1.value, count1.value, step)
        sums = []
        for i in range(max(count1.value, count2.value) + 1, 0, -1):
            sums.append(round(arseq_summa(i, first, step)))
        print(*sums, sep=', ', end=' ')
        print(f'[{step:+.0f}]')
    mainloop(calc_and_print, sum1, count1, sum2, count2)


if __name__ == '__main__':
    main()
