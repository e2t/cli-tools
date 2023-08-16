import random


def _ssort(items: list[int]) -> None:
    size = len(items)
    d = size // 2
    while d >= 1:
        for i in range(d, size):
            for j in range(i, d - 1, -d):
                if items[j] < items[j - d]:
                    items[j], items[j - d] = items[j - d], items[j]
        d //= 2


def main() -> None:
    random.seed()
    items = [random.randint(0, 100) for _ in range(19)]
    print(items)
    _ssort(items)
    print(items)


if __name__ == "__main__":
    main()
