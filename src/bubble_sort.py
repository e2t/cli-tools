import random


def _bsort(items: list[int]) -> None:
    size = len(items)
    for i in range(size - 1):
        need_sort = False
        for j in range(size - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                need_sort = True
        if not need_sort:
            break


def main() -> None:
    random.seed()
    items = [random.randint(0, 100) for _ in range(19)]
    print(items)
    _bsort(items)
    print(items)


if __name__ == "__main__":
    main()
