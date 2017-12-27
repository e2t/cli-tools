"""Бегущие линии в консоли."""
import random
import time


MIN_POS = 0
MAX_POS = 78
LINES_QTY = 5


def main() -> None:
    positions = [random.randint(MIN_POS, MAX_POS) for i in range(LINES_QTY)]
    line = [' '] * (MAX_POS + 1)
    for i in positions:
        line[i] = '*'
    try:
        while True:
            print(''.join(line))
            for i in range(LINES_QTY):
                delta = random.randint(
                    0 if positions[i] == MIN_POS else -1,
                    0 if positions[i] == MAX_POS else 1)
                if delta:
                    line[positions[i]] = ' '
                    positions[i] += delta
                    line[positions[i]] = '*'
            time.sleep(0.05)
    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    main()
