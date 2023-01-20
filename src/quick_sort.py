import random


def qsort(items: list[int], lowerb: int, upperb: int) -> None:
    if upperb <= lowerb:
        return
    pivot = items[lowerb // 2 + upperb // 2]
    lb, ub = lowerb, upperb
    while lb <= ub:
        while items[lb] < pivot and lb < upperb:
            lb += 1
        while pivot < items[ub] and ub > lowerb:
            ub -= 1
        if lb <= ub:
            items[lb], items[ub] = items[ub], items[lb]
            lb += 1
            ub -= 1
    qsort(items, lowerb, ub)
    qsort(items, lb, upperb)


def main() -> None:
    random.seed()
    items = [random.randint(0, 100) for _ in range(20)]
    print(items)
    qsort(items, 0, len(items) - 1)
    print(items)


if __name__ == '__main__':
    main()
