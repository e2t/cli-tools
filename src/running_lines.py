"""Бегущие линии в консоли."""
import random
import time


def main() -> None:
    """Выполняется при запуске модуля."""
    min_pos = 0
    max_pos = 78
    lines_qty = 5
    positions = [random.randint(min_pos, max_pos) for i in range(lines_qty)]
    line = [' '] * (max_pos + 1)
    for i in positions:
        line[i] = '*'
    try:
        while True:
            print(''.join(line))
            for i in range(lines_qty):
                delta = random.randint(
                    0 if positions[i] == min_pos else -1,
                    0 if positions[i] == max_pos else 1)
                if delta:
                    line[positions[i]] = ' '
                    positions[i] += delta
                    line[positions[i]] = '*'
            time.sleep(0.05)
    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    main()
